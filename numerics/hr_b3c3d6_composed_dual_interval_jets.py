"""Candidate physical Step55 G_s/G_U enclosure by forward interval AD.

Requires the original authenticated Step45/46/55 sources at runtime.
No claim of a physical certificate until run() is executed with those sources,
and the Step55 barrier, signs, and resulting enclosures pass.
"""
from fractions import Fraction as Q
from types import FunctionType

class Dual:
    """Forward-mode first derivative, using outward arithmetic of value type.

    For interval values this is a set enclosure, not a point estimate.
    Nonsmooth abs crossing zero is rejected, never silently differentiated.
    """
    def __init__(self, value, derivative):
        self.v, self.d = value, derivative

    def as_dual(self, other):
        return other if isinstance(other, Dual) else Dual(other, self.d * 0)

    def __add__(self, other):
        other = self.as_dual(other)
        return Dual(self.v + other.v, self.d + other.d)
    __radd__ = __add__

    def __neg__(self):
        return Dual(-self.v, -self.d)
    def __sub__(self, other):
        return self + -self.as_dual(other)
    def __rsub__(self, other):
        return self.as_dual(other) + -self

    def __mul__(self, other):
        other = self.as_dual(other)
        return Dual(self.v * other.v, self.d * other.v + self.v * other.d)
    __rmul__ = __mul__

    def inv(self):
        return Dual(1 / self.v, -self.d / (self.v * self.v))
    def __truediv__(self, other):
        return self * self.as_dual(other).inv()
    def __rtruediv__(self, other):
        return self.as_dual(other) * self.inv()

    def sqrt(self):
        root = self.v.sqrt() if hasattr(self.v, 'sqrt') else self.v ** Q(1, 2)
        return Dual(root, self.d / (2 * root))

    def __pow__(self, exponent):
        if exponent == Q(1, 2):
            return self.sqrt()
        if exponent == Q(-1, 2):
            return self.sqrt().inv()
        if int(exponent) != exponent:
            raise ValueError('unsupported noninteger exponent')
        exponent = int(exponent)
        if exponent == 0:
            return Dual(self.v * 0 + 1, self.d * 0)
        return Dual(self.v ** exponent,
                    exponent * (self.v ** (exponent - 1)) * self.d)

    def __abs__(self):
        lo = self.v.lo if hasattr(self.v, 'lo') else self.v
        hi = self.v.hi if hasattr(self.v, 'hi') else self.v
        if lo > 0:
            return self
        if hi < 0:
            return -self
        raise ValueError('abs not differentiable on interval containing zero')


def lift_global_constants(function, interval_class):
    """Clone geometry with interval globals promoted to zero-derivative Duals.

    The original geometry() evaluates constants on the LEFT, e.g. A*ug**2.
    Its interval class does not return NotImplemented for Dual operands, so
    merely passing a Dual argument is invalid. Clone globals, do not mutate
    the authenticated original module or monkeypatch its interval class.
    """
    env = function.__globals__.copy()
    zero = interval_class.c(0)
    for key, val in list(env.items()):
        if isinstance(val, interval_class):
            env[key] = Dual(val, zero)
    return FunctionType(function.__code__, env, function.__name__,
                        function.__defaults__, function.__closure__)


def evaluate_composed(compiled_symbols, compiled_fn, geometry_fn,
                      interval_class, s_box, u_box, seed_s, seed_u):
    """Physical partial derivative: every prescribed geometry(s) participates."""
    z, o = interval_class.c(0), interval_class.c(1)
    ds = Dual(s_box, o if seed_s else z)
    du = Dual(u_box, o if seed_u else z)
    geo = lift_global_constants(geometry_fn, interval_class)(ds)
    geo['s'], geo['U'] = ds, du
    missing = [str(x) for x in compiled_symbols if str(x) not in geo]
    if missing:
        raise KeyError(f'missing original physical geometry variables: {missing}')
    result = compiled_fn(*[geo[str(x)] for x in compiled_symbols])
    if not isinstance(result, Dual):
        raise TypeError('AD dependency lost in original symbolic expression')
    return result


def original_physical_boxes_at_four_radii():
    """Execution candidate; NO result without authentic originals and barrier.

    Uses the existing certified Step55 global barrier (not a DOP853
    refinement) to obtain U intervals. Every radius is exact rational.
    The output boxes can be wide; downstream Step58 is NOT certified.
    """
    from . import hr_step55_global_barrier as b
    from .hr_b3c3d6_physical_correlated_replay import authenticate_originals
    from .hr_b3c3d6_direct_first_partial_jet_enclosure import (
        RInterval, enclose_second_jet)
    authenticate_originals()
    barrier = b.certify_global_barrier(cells=256)
    symbols, compiled_fn = b.compiled()
    out = []
    for r in (Q(1, 4), Q(1, 2), Q(7, 10), Q(17, 20)):
        s = r * r
        si = b.I.c(s)
        star = b.stars(si)[0]
        delta = b.I.c(Q(1, 10000))
        ui = b.I(star.lo - delta.hi, star.hi + delta.hi)
        gs = evaluate_composed(symbols, compiled_fn, b.geometry, b.I,
                               si, ui, True, False)
        gu = evaluate_composed(symbols, compiled_fn, b.geometry, b.I,
                               si, ui, False, True)
        # Separate passes are independently outward; their G boxes must overlap.
        if gs.v.hi < gu.v.lo or gu.v.hi < gs.v.lo:
            raise ArithmeticError('inconsistent interval evaluation of G')
        def interval_record(x):
            return [str(Q(x.lo, b.S)), str(Q(x.hi, b.S))]
        def rational_box(x):
            return RInterval(Q(x.lo, b.S), Q(x.hi, b.S))
        jets = enclose_second_jet(s, rational_box(ui), rational_box(gs.v),
                                  rational_box(gs.d), rational_box(gu.d))
        out.append({'r': str(r), 's': str(s), 'U': interval_record(ui),
                    'G': interval_record(gs.v), 'G_s_composed': interval_record(gs.d),
                    'G_U': interval_record(gu.d),
                    'direct_jets': {k: [str(v.lo), str(v.hi)]
                                    for k, v in jets.items()}})
    return {'original_barrier_cells': barrier['cells'], 'boxes': out,
            'scope': 'PHYSICAL_STEP55_DIRECT_SECOND_JET_BOXES_ONLY_IF_EXECUTED',
            'Step58': 'NOT_CERTIFIED', 'GATE_2B': 'OPEN',
            'JANUS_R': 'NOT_VALIDATED'}
