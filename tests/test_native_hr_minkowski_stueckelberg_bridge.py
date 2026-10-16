import math
import numpy as np


def _quadratic_hessian(action, n, step):
    zero = np.zeros(n, dtype=float)
    f0 = action(zero)
    H = np.zeros((n, n), dtype=float)
    for i in range(n):
        ei = np.zeros(n, dtype=float)
        ei[i] = step
        H[i, i] = (action(ei) - 2.0*f0 + action(-ei))/(step*step)
        for j in range(i + 1, n):
            ej = np.zeros(n, dtype=float)
            ej[j] = step
            value = (
                action(ei + ej) - action(ei - ej)
                - action(-ei + ej) + action(-ei - ej)
            )/(4.0*step*step)
            H[i, j] = H[j, i] = value
    return H


def _control(beta1, beta2, beta3, k):
    from numerics.hr_scalar_potential import hr_scalar_quadratic_action_density_de_felice
    from numerics.nonhomothetic_hr_native_action import native_hr_potential_density

    # K=1 proportional Minkowski.  Tune beta0,beta4 so the interaction itself
    # has vanishing first metric variation; this removes any quadratic-field-
    # redefinition ambiguity from the bridge test.
    beta0 = -3.0*beta1 - 3.0*beta2 - beta3
    beta4 = -3.0*beta3 - 3.0*beta2 - beta1
    betas = (beta0, beta1, beta2, beta3, beta4)

    # x=(L,T,Ldot,Tdot,Phi_g,Phi_f_native,B_g,B_f_native)
    def de_felice_action(x):
        L, T, Ldot, Tdot, Phi_g, Phi_f_native, B_g, B_f_native = x
        return hr_scalar_quadratic_action_density_de_felice(
            lapse_g=1.0, scale_g=1.0,
            lapse_f=1.0, scale_f=1.0,
            m2=1.0, betas=betas, k=k,
            Phi_g=Phi_g, B_g=B_g, psi_g=0.0, E_g=0.0,
            Phi_f=Phi_f_native - Tdot,
            B_f=B_f_native + T - Ldot,
            psi_f=k*k*L/3.0,
            E_f=-2.0*L,
        )

    def exact_native_action(x):
        L, T, Ldot, Tdot, Phi_g, Phi_f_native, B_g, B_f_native = x
        count = 96
        total = 0.0
        for j in range(count):
            coordinate = (j + 0.5)*2.0*math.pi/(k*count)
            cosine = math.cos(k*coordinate)
            sine = math.sin(k*coordinate)

            g_native = np.array([
                [-(1.0 + 2.0*Phi_g*cosine), -k*B_g*sine],
                [-k*B_g*sine, 1.0],
            ])
            f_native = np.array([
                [-(1.0 + 2.0*Phi_f_native*cosine), -k*B_f_native*sine],
                [-k*B_f_native*sine, 1.0],
            ])
            # Native relative map: T_coord=t-T and X=x-partial_x L.
            Jf = np.array([
                [1.0 - Tdot*cosine, k*T*sine],
                [k*Ldot*sine, 1.0 + k*k*L*cosine],
            ])
            total += native_hr_potential_density(
                g_radial_native=g_native,
                f_radial_native=f_native,
                g_angular_native=1.0,
                f_angular_native=1.0,
                jacobian_g=np.eye(2), jacobian_f=Jf,
                betas=betas, m2=1.0, Mg2=1.0,
            )
        return total/count

    old = _quadratic_hessian(de_felice_action, 8, 1.0e-5)
    exact = _quadratic_hessian(exact_native_action, 8, 6.0e-5)
    # A real cosine mode averages a quadratic Fourier amplitude by 1/2; the
    # standard-beta native action has the opposite interaction sign convention
    # from the De Felice quadratic helper.  Hence exact = -old/2.
    scale = max(1.0, float(np.linalg.norm(exact, ord=np.inf)))
    return float(np.linalg.norm(exact + 0.5*old, ord=np.inf)/scale)


def test_exact_native_hr_pullback_reproduces_de_felice_stueckelberg_hessian():
    controls = (
        (1.0, -0.7, 0.25, 2.3),
        (0.8, -0.2, 0.05, 4.1),
        (1.3, -1.1, 0.4, 1.4),
    )
    for args in controls:
        assert _control(*args) < 2.0e-5
