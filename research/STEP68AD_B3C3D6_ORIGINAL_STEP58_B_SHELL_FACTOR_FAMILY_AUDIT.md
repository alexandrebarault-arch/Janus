# JANUS b3c3d6 — original Step58: structural B-factor candidates on exact algebraic shells (2026-10-31)

**Status: PARTIAL. GATE_2B OPEN; JANUS_R NOT_VALIDATED.** This is **not** an interval enclosure of the six physical Step58 coefficients and **not** a universal symbolic factorization.

## Original sources and exact work

The original Step45 (`66aa43841dccfe4a5d586a49be9c10af3a67a10e`) and Step58 (`802c23aebd41780d8c462f1aa1711707fe4ee88f`) Python source bytes were authenticated locally as Git blobs. Step58's **actual** `physical_operator()` and `highest_lapse_certificate()` were executed with a **minimal Step57 import shim**, not the complete Step57 implementation. The original Step46/55 and DOP853 were **not** run. The Step58 identity `E_N=E_M=0` on `Fz=Hg=0` was rerun (existing result).

A new structural candidate emerged from exact substitutions into the **original** first-lapse-jet coefficients: on a shell satisfying `Fz=0`, `d_r Fz=0`, `Hg=0`, `d_r Hg=0`, one finds `B_M=0` and `B_N=(z/Lg)*C` in two nontrivial symbolic families. Family A has **six** independent symbolic canonical/jet variables and the rationalized shift `z=2*tau/(1+tau^2)`, `0<tau<1`. Family B has **twenty** independent symbolic variables (including `Lg,Lf,Sg,Sf`) at `z=3/5`. Both fix `tgr=3*Lg/4`, `tfr=0` and some other parameters. `C` is **not identically zero** in either family, so the observed `B_N` relation is not a trivial `0=0`. All four shell residuals and both candidate factor residuals simplify to **exact zero** on each family.

The shell construction solves sequentially for `pg`, `pLg_r`, `pLg_rr`, `Sg_rrr`; it does not impose `Hf=0`, `C=0`, the Step55 radial ODE, or physical boundary data. Exact derivative negative controls show `B_M` genuinely depends on `pLg_rr` and `B_N-z*C/Lg` on `Sg_rrr` off the shell. The family identities are **exact on their stated slices**, not a theorem for arbitrary six-pair fields, arbitrary dust slopes or the physical Step55 profile. In particular, do **not** replace physical `B_N,B_M` by zero yet.

## Executed checks and evidence

`PYTHONHASHSEED=0 PYTHONPATH=. python -m unittest discover -s tests -p 'test_hr_b3c3d6_step58_B_shell_family_probe.py' -q`: **6 PASS, 0 FAIL, 0 SKIP**. `python -m compileall -q numerics/hr_b3c3d6_step58_B_shell_family_probe.py tests/test_hr_b3c3d6_step58_B_shell_family_probe.py`: **PASS**. CLI module report also executed with `PYTHONHASHSEED=0` and saved as JSON. The original two sources were SHA-identical to GitHub; the new code and tests were tested locally before publication. The symbolic family tests share the original Step58 implementation and are **not independent physics validations**.

## Highest-value next step

Prove or refute **universally** the proposed on-shell ideal memberships `B_M in <Fz,Fz',Hg,Hg',...>` and `B_N-z*C/Lg in <Fz,Fz',Hg,Hg',...>`, retaining all shift derivatives and valid positive-K chart assumptions. A proof should exhibit explicit coefficients and verify it on the complete original Step58 expression; otherwise find a counterexample on a valid shell. Only then apply `C=0` and the authenticated Step55 geometry to establish exact B cancellations. Subsequently certify **all six** `A_N,A_M,B_N,B_M,E_N,E_M` at exact `r=1/4,1/2,7/10,17/20` with interval control, solve the **positive two-boundary lapse BVP**, and proceed to Dirac six-pair rank/charges/temporal gauge, 4D dynamics, stability and observables. **No physical BVP or JANUS validation is claimed.**
