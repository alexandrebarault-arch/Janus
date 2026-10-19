"""Smeared spherical EH_g+EH_f+HR+two-dust primary diagonal spatial Ward.

Extends Step33c's exact momentum-constraint functional bracket without
modifying its verified implementation. This is NOT the mixed H_g/H_f
Poisson bracket or the local BD secondary constraint.
"""
from __future__ import annotations
import math
import numpy as np
from numpy.polynomial import Polynomial as Poly
from numerics.hr_spherical_radial_diffeo_ward import (
    densities,default_fields,transformed,spatial_generator,
)


def smeared_primary_hamiltonians(fields,lapse,order=72):
    """Integrate both exact spherical HR+EH+two-dust primary coefficients."""
    if not isinstance(lapse,Poly):raise ValueError('polynomial lapse test required')
    if abs(lapse(0))>1e-14 or abs(lapse(1))>1e-14:
        raise ValueError('test lapse must vanish at both radial boundaries')
    if type(order) is not int or order<12:raise ValueError('order >=12 required')
    x,w=np.polynomial.legendre.leggauss(order);r=(x+1)/2
    values=np.asarray([densities(fields,float(t))[0][:2] for t in r])
    return np.dot(.5*w*lapse(r),values)


def smeared_primary_diagonal_ward(*,epsilon=2.e-5,order=72,fields=None):
    """Direct finite field variation vs exact weight-one transport with IBP."""
    if not math.isfinite(epsilon) or epsilon<=0:
        raise ValueError('finite positive chart perturbation required')
    initial=default_fields() if fields is None else fields
    eta=spatial_generator()
    N=Poly([0.,0.,1.])*Poly([1.,-1.])**2*Poly([1.,.3])
    plus=smeared_primary_hamiltonians(transformed(initial,eta,epsilon),N,order)
    minus=smeared_primary_hamiltonians(transformed(initial,eta,-epsilon),N,order)
    actual=(plus-minus)/(2*epsilon)
    x,w=np.polynomial.legendre.leggauss(order);r=(x+1)/2
    base=np.asarray([densities(initial,float(t))[0][:2] for t in r])
    expected=np.dot(-.5*w*eta(r)*N.deriv()(r),base)
    return actual,expected
