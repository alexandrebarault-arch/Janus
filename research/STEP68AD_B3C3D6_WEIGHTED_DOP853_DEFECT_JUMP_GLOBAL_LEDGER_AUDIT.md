# JANUS b3c3d6 — Weighted continuous-defect and DOP853 jump ledger (2026-10-30)

**GATE_2B OPEN ; JANUS_R NOT_VALIDATED.** This is an exact conditional error-propagation result and a tested adapter to the previous DOP853 rational dense-output infrastructure, **not** a new physical Step55 residual certificate.

## Proven theorem and boundary bookkeeping

On every interval [a_i,b_i] with a_i>0, let the exact Step55 solution satisfy 2s U_s=G(s,U)-2U and let P_i(s) be a differentiable candidate. Put H_i=2s P_i'-G(s,P_i)+2P_i. Assume U and P_i lie in a common tube where G_U<=0 and that an outward inclusion proof establishes |H_i|<=R_i **continuously**. Then for e=U-P_i,

d(s|e|)/ds <= |H_i|/2,

in the Dini-derivative sense, since 2s e_s=(G(s,U)-G(s,P_i))-2e-H_i and G_U<=0. At an internal endpoint b_i=a_(i+1), define the **exact mathematical dense-polynomial jump** J_i=P_(i+1)(b_i+)-P_i(b_i-). Thus |e(b_i+)|<=|e(b_i-)|+|J_i|. Telescoping yields

**s_R |e(s_R-)| <= s_0 E_0 + (1/2) SUM_i R_i (b_i-a_i) + SUM_internal_i b_i |J_i|.**

The right-hand side is a **rational number** if E0 and R_i are rational. Even if E0 is unknown, the affine inequality |e(s_R)| <= (s0/sR) E0 + additive_error is exact under the stated hypotheses; it must not be advertised as a certified final error.

The proof remains valid when the DOP853 true binary64 domain has xmax=(t-t_old)/h != 1. The adapter uses the preceding module's exact rational domain, exact dense-polynomial jump, and physical Step55 outward-integer interval residual on every piece. It rejects non-contiguous domains, negative residual bounds, and a final spurious jump. The endpoint is the actual binary64 solver s_R, **not** automatically the exact decimal r² needed by Step58.

## Sharp exact rational tests and counterexample

For G=0, U=0, P=c(1-a/s) on [a,b], the defect H=2c and the inequality is an equality. For a two-piece example a=1/4, b=1/2, R=1, P1=2(1-a/s), jump J=1, P2=2(b/s)+3(1-b/s), defects 4 and 6, the ledger yields integrated defect numerator 2, jump numerator 1/2 and exact terminal error 5/2: **sharp**. A separate example with zero continuous defect on both pieces but a jump J=1 at 1/2 has exact final error 1/2; ignoring jumps would incorrectly give zero. These are mathematical **toy** examples, not JANUS physics.

Ten local unittest cases PASS, zero FAIL, including equality cases, missing-jump negative control, non-contiguous true domains, strict start, invalid defect, exact binary64 conversion, and absent E0. Command: `cd /mnt/data/janus_piecewise && PYTHONPATH=. python -m unittest discover -s tests -v`; `python -m compileall -q numerics tests` PASS. Tested local source Git blob SHA: module `74dc0bcf1cf77d90be4f840464b66c72c5b30648`, tests `6edbe05a8430072fa16964065a895d39cb9a7287`. Both were uploaded via authenticated GitHub create_file and read back at those exact SHAs.

## Physical scope and next executable action

The previous SHA-authenticated physical four-radius Step58 replay and Step55 256-cell barrier remain historical evidence; the original five physical modules were **read**, not executed in this session. The new `physical_step55_dense_ledger(sol, subcells=256)` adapter is published but **has not been run on the original Step55 DOP853 interpolants**. It is deliberately fail-closed if any physical interval residual/tube guard fails. A proof of G_U<=0 on the common physical tube must be explicitly linked to the original Step63 certificate, not inferred from this code.

Next: rerun original Step55 DOP853 with dense_output=True and all SHA-verified originals; execute the adapter on every piece and record all R_i and J_i; certify the center Taylor C, binary64 initial value and true solver start s0, and the decimal Step58 endpoint transport. Only then turn the affine error bound into a physical bound, propagate into U_s/U_ss and six original Step58 coefficients, attempt exact B/E factorization and positive N,M BVP at two true boundaries. Dirac six couples/rank/tertiaries, K=0/J=0, charges/time gauge, 4D/stability/observables remain open. No modifications to main, research/v2-flrw, or disabled workflows.
