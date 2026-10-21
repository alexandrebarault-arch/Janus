"""Step43 executable full 3x3 numerical Ward gates on actual HR Kij.

Runs with real Step33g/37 provider via kernel_fast(w,r), but a toy injected
kernel can test the instrumentation alone. The physical provider comparison
is NOT executed in this lightweight self-test environment. All numbers are
finite-resolution diagnostics; exact vanishing needs independent proof.
"""
from __future__ import annotations
import numpy as np
from numpy.polynomial.legendre import leggauss


def _kernel(kernel, witness, r):
    z=np.asarray(kernel(witness,float(r)),dtype=float)
    if z.shape!=(3,3) or not np.isfinite(z).all():
        raise ArithmeticError('physical six-pair kernel must be finite 3x3')
    return z


def _fivepoint_component(kernel,witness,r,h,i,j):
    values=[_kernel(kernel,witness,r+h*v)[i,j] for v in (-2,-1,1,2)]
    return (-values[3]+8*values[2]-8*values[1]+values[0])/(12*h)


def physical_ward_sample(witness, r=.43, h=.001, kernel=None):
    """Full local numerical C,W,D and all four excluded smearing jets.

    Compute exact operator obstruction quantitatively only at a finite
    difference step: W=K01-K10+(K20)', D=K20-K11,
    C=K00-(K01)'.  The full kernel is computed by all six canonical pairs.
    Do not interpret finite small W as a symbolic Ward proof.
    """
    if kernel is None:
        from .hr_step37_curved_solver import kernel_fast as kernel
    if not (np.isfinite(r) and np.isfinite(h) and h>0 and .025<r-2*h
            and r+2*h<.9):
        raise ValueError('stencil outside the spherical chart')
    k=_kernel(kernel,witness,r)
    dk01=_fivepoint_component(kernel,witness,r,h,0,1)
    dk20=_fivepoint_component(kernel,witness,r,h,2,0)
    bad={(0,2):k[0,2],(1,2):k[1,2],(2,1):k[2,1],(2,2):k[2,2]}
    return {'r':float(r),'h':float(h),
            'C':float(k[0,0]-dk01),
            'W':float(k[0,1]-k[1,0]+dk20),
            'D':float(k[2,0]-k[1,1]),
            'excluded':{f'K{i}{j}':float(v) for (i,j),v in bad.items()},
            'max_excluded_abs':float(max(map(abs,bad.values()))),
            'numerical_not_symbolic':True}


def full_jet_gauss_vs_C(witness,lo=.2,hi=.7,h=.001,points=48,
                        kernel=None,smears=None):
    """Numerically compare ALL nine mixed jets against just C.

    For physical witness, default smearing is original Step39 A pair and
    the kernel is genuine Step37 full six-pair kernel. Caller may inject
    independent polynomial kernels/smears for instrumentation tests.

    Returns a direct diagnostic, never a rigorous continuum equality.
    """
    if kernel is None:
        from .hr_step37_curved_solver import kernel_fast as kernel
    if smears is None:
        from .hr_step39_cross_oracle import lapse_jets as lapse_pair
        smears=lambda rad:lapse_pair(rad,'A')
    if not(isinstance(points,int) and 16<=points<=512 and .025<lo<hi<.9
           and np.isfinite(h) and h>0 and lo-2*h>.025 and hi+2*h<.9):
        raise ValueError('invalid support, quadrature or derivative stencil')
    xs,ws=leggauss(points)
    xs=lo+(xs+1)*(hi-lo)/2
    ws=ws*(hi-lo)/2
    original=reduced=0.
    max_w=max_d=max_high=0.
    for rad,wt in zip(xs,ws):
        sm_N,sm_M=smears(float(rad))
        n=np.asarray(sm_N,float).reshape(3)
        m=np.asarray(sm_M,float).reshape(3)
        k=_kernel(kernel,witness,rad)
        gates=physical_ward_sample(witness,float(rad),h,kernel)
        original+=float(wt*(n@k@m))
        reduced+=float(wt*n[0]*m[0]*gates['C'])
        max_w=max(max_w,abs(gates['W']))
        max_d=max(max_d,abs(gates['D']))
        max_high=max(max_high,gates['max_excluded_abs'])
    return {'full_jet_bracket':float(original),'C_only_bracket':float(reduced),
            'difference':float(original-reduced),
            'max_abs_W_samples':max_w,'max_abs_D_samples':max_d,
            'max_abs_excluded_samples':max_high,
            'n_gauss':points,'finite_resolution_only':True}


if __name__=='__main__':
    print('Use physical_ward_sample(witness) or full_jet_gauss_vs_C(witness) in a complete Janus checkout; no auto-fabricated physical witness.')
