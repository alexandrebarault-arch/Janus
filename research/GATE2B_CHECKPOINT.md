# Gate 2B — persistent checkpoint

Date: 2026-10-12
Canonical branch: `research/v2-flrw`
Global first restart file: `research/RESTART_TASKS.md`

## Verdict

**Gate 2B remains OPEN / NOT VALIDATED.**

The direct Comelli closure is a closed negative route: it does not recover the physical helicity-0 gradient. The active route is an independent scalar quadratic-action reconstruction checked against De Felice et al. 1404.0008 and Lagos & Ferreira 1610.00553.

## Closed facts

### Convention bridge

- JANUS -> De Felice/Comelli: `beta_n=n! a_n`, `xi=y`, `kappa=alpha^2`, `c=ctilde`, `f2=xi*J`, `f1=Gamma`.
- Lagos massive bigravity: `r=xi`, `Nbar=xi*c`, `Z=m^2 f2/xi=m^2 J`, `Z_tilde=m^2 f1/xi=m^2 Gamma/xi`.
- massive bigravity has `alpha_L=0`; the helicity-0 gradient appears only after lapse/shift elimination together with the Einstein-Hilbert/background structure.
- use `Phi_DF = Phi_L`; do not introduce a factor-of-two patch.

### Independent De Felice principal action

- `numerics/de_felice_action_principal.py` independently implements the relevant high-k coefficients;
- Candidate-C checks exist at `a=1,0.5,0.2`;
- at `a=0.5`: `c_s^2 ~= 0.6920799927`, `c_s ~= 0.83191345`.

### Lagos pure-metric/action work already established

- interaction potential and EH scalar self-actions independently reconstructed;
- two proven Lagos coefficient errors corrected;
- lapse/shift auxiliaries eliminated algebraically;
- proportional-control post-auxiliary kinetic rank identified;
- two P(X) matter characteristics are independently recovered by the current pencil, including f-lapse rescaling.

### Direct Comelli route — closed negative result

- radiation mode is recovered at `1/sqrt(3)`;
- the supposed gravity pair fails the independent De Felice benchmark;
- the bad high-k gravity frequency saturates instead of scaling with `k`;
- changing matter mixture, closure rows, selected signs/minors, or making `B1` nondynamical does not repair it.

## Current hard failure

The coupled Lagos/P(X) assembly has three kinetic directions and correctly tracks the two matter sound characteristics, but its third scalar branch still lacks the required `omega ~ k` gravity propagation.

Therefore the current action bridge is still incomplete or incorrectly background-reduced. The quadratic pencil is **not** the leading suspect because the two independent matter characteristics move correctly when their sound speeds are changed.

## Current leading hypothesis

`numerics/lagos_two_matter_action.py` subtracts the complete zero-matter-perturbation part of De Felice Eq. (54), on the assumption that all those metric-only matter terms are already present in the Lagos metric block, and then restores only

`(rho+P) Phi^2 / (2 c_s^2)`

in each sector.

But `numerics/lagos_scalar_action.py` builds `pure_metric_lagrangian_healthy()` from EH + interaction terms and explicitly documents that at least the matter-background lapse correction is not included. This creates a concrete risk of over-subtraction.

For De Felice Eq. (54), setting the matter perturbation variable to zero gives the bracket-level metric-only structure

`C_Phi Phi^2 - (rho/2) k^2 B_DF^2 + P[3 psi_DF^2/2 - k^4 E_DF^2/6] - 3 rho Phi psi_DF`,

where

`C_Phi = rho/2 + (rho+P)/(2 c_s^2)`.

The next task is to map this entire expression into Lagos variables and establish, term by term, which pieces are genuinely already absorbed by the one-matter background reduction and which must be retained in a two-matter action.

This is a **diagnostic target**, not permission to add the terms blindly.

## Active task list

- [x] convention bridge / exact Candidate-C and Case-C backgrounds;
- [x] reject direct Comelli closure for Gate-2B physics;
- [x] independent De Felice principal-action regression;
- [x] one-sector P(X) scalar matter action;
- [x] g/f lapse, scale-factor and volume normalization;
- [x] first two-matter assembly and auxiliary elimination;
- [x] Lagos interaction coefficient audit and corrections;
- [ ] **T1c.6o.5c-R — ACTIVE:** independently reconstruct the two-matter background-reduced metric+matter action rather than assuming the one-matter Lagos reduction generalizes;
  - [ ] map full De Felice metric-only Eq. (54) remainder into Lagos variables for g and f sectors;
  - [ ] add RED diagnostics for the shift, spatial metric, `Phi*psi`, and remaining lapse structures;
  - [ ] classify every difference against the Lagos block as background-equation equivalent or genuinely missing;
  - [ ] correct only proven missing structures, RED->GREEN;
  - [ ] re-run auxiliary rank and exchange controls;
  - [ ] re-run high-k matter speeds and Candidate-C gravity speed;
- [ ] recover exactly three physical high-k scalar modes with healthy kinetic/gradient signs;
- [ ] only then build the non-homothetic transfer solver and mode tracking.

## Immediate restart instruction

**Resume at T1c.6o.5c-R.**

1. Do not modify the frozen quadratic pencil to force the benchmark.
2. Do not return to the direct Comelli closure.
3. Use the exact De Felice Eq. (54) zero-matter-perturbation remainder as the first independent audit object.
4. Check the g-sector mapping first, then obtain the f-sector by its own lapse/scale/volume normalization rather than by visual symmetry.
5. First production change must be preceded by a RED test that fails for the current `full - metric_only + background_lapse` construction.
6. Acceptance after correction: matter speeds unchanged and gravity branch approaches the independent Candidate-C `omega^2/k^2` benchmark at `a=1,0.5,0.2`.
7. Update `research/RESTART_TASKS.md`, this file and `LATEST.md` at the next hard result.