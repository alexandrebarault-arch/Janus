"""Replay all 1006 newly certified Step68s inner temporal interval cells.

Reuses Step68r exact cell-by-cell replay with a pinned SHA256 additional proof.
This is NOT an independent non-IBP theoretical oracle.
"""
from fractions import Fraction as F
from . import hr_step68r_cell_replay as base
base.PROOFS['near'] = ('gate2b-step68s-inner-1over32-to-1over16-cover.json',
   '7491e166286279f8ac6423677fec069f7fc9d6bca7bfda4271cedd1c0addedd4',
   F(1,32), F(1,16), 1006)
prep=base.prep
replay=base.replay
if __name__=='__main__':base.cli()
