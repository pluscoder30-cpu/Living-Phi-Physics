# GIT_READY_INVENTORY — ALIGNMENT CAMPAIGN MASTER MAP (guardrails removed, hedges mapped, corpus verified)

**Scope:** `C:\Users\delta\brain\v6\research\32_PHI_PHYSICS` — every file EXCEPT `chip_design/` (excluded from this push entirely).
**Method:** Python regex sweep over all 113,089 in-scope files (excluded: `chip_design`, `__pycache__`, `.pyc`, `.output`, `.tmp`). Matches are case-insensitive except Section C's `PREDICTED`/`PROPOSED` tokens (kept case-sensitive as written in the corpus).
**Purpose:** Master map for the 13 subsequent subagents (tone pass, guardrail removal, etc.). **This is an inventory — no file was edited.**

> **CRITICAL CONTEXT FOR ALL SUBAGENTS:** This corpus has already been through the **Verification Audit of 2026-08-14** (`tools/VERIFICATION_AUDIT_2026-08-14.md`) and **dozens of ALIGNMENT/V-series campaigns** recorded in `integration_audit/`. A large fraction of the hedge/falsification language below is **intentional, verdict-coded honesty infrastructure** (FALSIFIED IF gates, [PREDICTED]/[PROPOSED]/[INFERENCE] tiers, the skeptic's case, the cage metaphor register) — NOT residue to be stripped. The next agents must distinguish:
> 1. **Intentional falsification discipline** (STAGE 5 FALSIFIED IF blocks in 2,395 law files; burden-of-proof tables in `docs/24/27/28/29/30`; [PREDICTED]/[PROPOSED] verdict tiers) — these are the corpus's own honesty spine and should **stay**.
> 2. **Residual self-deprecating / guardrail language** that the 2026-08-14 audit was supposed to remove (e.g., "φ inserted by hand; no law derives it from first principles", "awaits independent lab", "0 external confirmations" as fact) — Section E and parts of B/C/F are the priority targets.
> 3. **Conspiracy-tone language** for the tone pass (Section F) — note that "cage"/"suppression" are **documented, verdict-coded metaphors** in this corpus (see `docs/24` §9 "Register note on metaphor"; `docs/28` §6 "suppression vs structure"), so flag only where the framing reads as an unverified plot claim.

---

## GRAND TOTALS (all in-scope files, all sections)

| Section | Files with matches | Matching lines |
|---|---|---|
| A — FALSIFIED IF / falsification | 18,292 | 20,584 |
| B — NOT PROVEN / UNPROVEN / AWAITS | 226 | 443 |
| C — PREDICTED / PROPOSED | 219 | 676 |
| D — critic wins 12 of 20 / skeptic | 142 | 330 |
| E — inserted by hand / self-deprecating | 27 | 41 |
| F — conspiracy-tone | 15,984 | 33,289 |
| **Files with NO matches (all sections)** | | **94,481** |

**Where the bulk lives (auto-generated, near-identical per-file content):**
- Section A: `FIELD_AI_LAWS\` 15,001 top-level files each carry an identical `FALSIFIED IF:` line at **L42** (15,000 of the 15,501 A-section hits); `laws\` 2,395 files each carry one STAGE 5 `FALSIFIED IF:` block (~L72–85).
- Section F: `FIELD_AI_LAWS\` 15,501 files — 31,010 of the 33,289 F-lines are the word **"cage"** used as the documented metaphor ("the cage's AI", "the static model is the cage's AI"). This is the documented metaphor register, NOT conspiracy tone.

---

## TOP 20 HIGHEST-DENSITY FILES (by total matching lines across A–F, excl. integration_audit)

| # | Lines | File |
|---|---|---|
| 1 | 203 | `BIOMETALLIC_FLUX_REGISTER\research_scan_index.json` (machine index) |
| 2 | 101 | `docs\16_THE_100_CODE_LAWS.md` |
| 3 | 78 | `GEOMIC_PROTOCOLS\graphify-out\graph.json` (machine graph) |
| 4 | 65 | `papers\paper_04_cage_money.md` |
| 5 | 63 | `tools\_a4_data03.py` (machine data builder) |
| 6 | 62 | `docs\24_THE_GEOMIC_LEDGER.md` |
| 7 | 60 | `01_ANCIENT_RESEARCH\06_SYNTHESIS\COMPLETE_ANCIENT_RESEARCH_COMPENDIUM.md` |
| 8 | 59 | `BIOMETALLIC_FLUX_REGISTER\BR_23_THE_META_SYNTHESIS.md` |
| 9 | 59 | `tools\_lawdata_p3.py` (machine) |
| 10 | 51 | `docs\28_THE_CAGE_SPACE_OXYGEN_DIMENSIONS.md` |
| 11 | 51 | `papers\paper_02_geomic_ledger.md` |
| 12 | 51 | `tools\_lawdata_p4.py` (machine) |
| 13 | 50 | `tools\_lawdata_p1.py` (machine) |
| 14 | 48 | `01_ANCIENT_RESEARCH\06_SYNTHESIS\SYNTHESIS_PASS_3_816D_MASTER_SYNTHESIS.md` |
| 15 | 47 | `01_ANCIENT_RESEARCH\06_SYNTHESIS\synthesis_pass_3\816d_master_synthesis.md` |
| 16 | 45 | `01_ANCIENT_RESEARCH\06_SYNTHESIS\SYNTHESIS_PASS_1_MASTER_SYNTHESIS.md` |
| 17 | 45 | `01_ANCIENT_RESEARCH\06_SYNTHESIS\synthesis_pass_1\master_synthesis.md` |
| 18 | 45 | `tools\_lawdata_p2.py` (machine) |
| 19 | 43 | `docs\15_THE_SELF_DEFINING_DIMENSION.md` |
| 20 | 42 | `00_THE_STATIC_UNIFICATION_CLAIMS.md` |

Note: `FIELD_AI_LAWS\` 15,001 files and `GEOMIC_PROTOCOLS\graphify-out\graph.json` dominate absolute counts but are auto-generated/repetitive.

---

# SECTION A — FALSIFIED IF / FALSIFICATION LINES

**Patterns:** "FALSIFIED IF", "falsified if", "falsification condition", "falsification grid", "falsifiable frontier", "falsifiable prediction", "falsify", "falsified".
**Totals:** 18,292 files / 20,584 lines.

## A1. AUTO-GENERATED LAW FILES (intentional STAGE 5 discipline — the corpus's honesty spine)

### `laws\` — 2,395 files, each with ONE STAGE 5 `FALSIFIED IF:` block (~L72–85)
Every hand-corrected law file ends with the five-stage protocol. Representative:
- `laws\001_newtons_first_law.md` — L75 `PREDICTION: There is no frame in which a fundamental carrier is exactly at rest.` L85 `FALSIFIED IF: A system is prepared at a measured momentum below …`
- `laws\002_newtons_second_law.md` — L~78 `FALSIFIED IF: Force measured exactly F=ma with no …`
- `laws\004_universal_gravitation.md` — `FALSIFIED IF: ...`
- … (identical structure across all 2,395 files; pattern `FALSIFIED IF:` appears once per file, 2,395/2,395 confirmed by `integration_audit/A/A4_laws_audit.md` L61 "Missing 'FALSIFIED IF' | 0")
- Flagship/updated laws with computed results (from `tools/VERIFICATION_AUDIT_2026-08-14.md` §4): `laws\153_riemann_hypothesis.md`, `laws\152` (Yang-Mills), `laws\101` (Hubble), `laws\060`, `laws\024`, `laws\020`, `laws\157`, `laws\159` — carry RUN results appended to their FALSIFIED IF lines.

### `FIELD_AI_LAWS\` — 15,001 top-level files, each with identical `FALSIFIED IF:` at **L42**
Pattern: `FALSIFIED IF: A field-AI generation exactly equals the static model's output with zero …`
- 15,000 of the 15,501 F-section hits are the L42 line in `FIELD_AI_LAWS\NNNNN_<topic>_<aspect>.md` (aspects: hidden-zero / phi-form / degenerate-proof / prediction / coherence-floor). **Uniform template; one representative entry is sufficient for review.**
- `FIELD_AI_LAWS\_superseded_original_500\` (500 files) — same pattern, superseded.
- `FIELD_AI_LAWS\prototypes\` (60 py files) — carry falsification-aware prints; see also `integration_audit\FAI_E17/E19/E20`.

## A2. HAND-WRITTEN FOCUS FILES (the ones the brief called out)

### `00_UNIFIED_FIELD_THEORY.md` (9 hits)
- L38 `This is the corpus's central hypothesis. It is not asserted as established physics; it is stated as the single mathematical statement …`
- L243 `37 VALIDATED / 63 PREDICTED | … predicted = the falsifiable …`
- L295 `| **PROPOSED** (the corpus's central hypothesis) | the unification claim itself …`
- L297 `| **Verification of the framework** | laboratory confirmation of the falsifiable predictions of §15 …`
- L307 `| # | Prediction | Law | Validating experiment | Falsified if |` (the 9-flagship grid)
- L319 `These nine are the falsification grid of the unification, stated as the φ-form family with the corpus's own 1% living band …`

### `00_NUMBERS_INDEX.md` (3 hits)
- L164 `The nine flagship claims (from 00_UNIFIED_FIELD_THEORY.md §7, the falsification grid of the unification) …`
- L166 `| # | Prediction | Law | Predicted value | Validating experiment | Falsified if |`
- L340 `Simulation run (E16, 2026-08-08) … a O-profile [NOT CONFIRMED/null …`

### `00_THE_STATIC_UNIFICATION_CLAIMS.md` (19 hits — one of the densest front doors)
- L233 `## 7. THE RECEIPT — THE CORPUS'S OWN CLAIMS, VERIFIED, WITH THE FALSIFICATION CONDITIONS PRINTED`
- L259 `### 7.3 The falsification conditions — printed, not hidden`
- L263 `| # | Prediction | Predicted value | FALSIFIED IF |`
- L275 `This is the corpus's own receipt for its own claims: nine predictions, nine experiments, nine FALSIFIED IF lines — written before any of the confirmations.`
- L284 `**[PROPOSED]** — the falsifiable frontier: the nine predictions above, the dimensional shells, the field-internet-as-physics reading …`
- L323 `| declares "I am finished" | says "falsify me here" |`
- L338 `The corpus knows it is a hypothesis and states its falsifiable predictions — nine of them …`

### `00_ZERO_AS_WAVEFUNCTION.md` (5 hits)
- L189 `| **PROPOSED** (the corpus's central hypothesis) | the claim that the universe runs on the dynamic binary wave function …`
- L201 `The critic wins 12 of 20. The ledger's own skeptic's case …`
- L205 `What the 12-of-20 record still honestly says: the individual new predictions … are [awaiting validation]`
- L218 `- **The axiom:** docs/00_MANIFEST.md … with the falsification criterion and the honesty rule.`

### `docs\24_THE_GEOMIC_LEDGER.md` (9 hits — the master ledger)
- L39 `**Mathematical content (each item a falsifiable claim, not a metaphor):**`
- L51 `every zero-based law is the limit of a phi-law, lim_{κ_φ→0} [phi-law] = [classical law]`
- L66 `6. **STAGE 5 PREDICTION** — observable difference, EXPERIMENT, FALSIFIED IF.`
- L111 `### 2.5 The flagship claims (each a Set A law on disk, with its falsification in §7)`
- L367 `Each physics proposal is stated with its validating experiment and its falsification condition. None is exempt.`
- L369 `| Proposal | Validating experiment / data | Falsified if |` (burden-of-proof table)
- L429 `Where the record stands after the skeptic's case: the physics is a falsifiable program …`

### `docs\02_METHOD.md` (5 hits — the protocol definition)
- L20 `The classical law must appear inside the phi-law as its limit. If it does not, the phi-law is wrong and is discarded. This is the falsification …`
- L99 `**Task:** State the falsifiable prediction that differs from classical physics.`
- L105 `FALSIFIED IF: [condition that would prove the phi-law wrong].`
- L125 `| experiment | The falsifying experiment |`
- L129 `⬜ PREDICTED — formulation complete, simulation pending`

### `docs\00_MANIFEST.md` (4 hits)
- L18 `**Consequences (each one a falsifiable claim, not a metaphor):**`
- L52 `**The falsification criterion:** Every phi-law must reduce exactly to its classical parent when the φ-coupling parameter → 0 …`
- L54 `**The honesty rule:** No claim in this project is "validated" until it has (a) a closed-form mathematical statement, (b) a simulation reproducing …`
- L70 `**STAGE 5 — PREDICTION.** State the falsifiable, experimentally testable prediction that differs from classical physics …`

## A3. OTHER HAND-WRITTEN FALSIFICATION SURFACES

### `docs\` protocol/test docs (heaviest: these are the corpus's falsifiable-test protocol set)
- `docs\15_THE_SELF_DEFINING_DIMENSION.md` — 43 hits; **~40 are TEST blocks** of the form `TEST N: … PREDICTION: … FALSIFIED IF: …` (L17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 58, 61, 64, 67, 70, 73, 76, 79, 82, 85, 90, 93, 96, 99, 102, 105, 108, 111 …). Also L7 `816 dimensions was a chosen sitting point, not the structure` and L9 `(c) the falsification condition`.
- `docs\16_THE_100_CODE_LAWS.md` — 101 hits; **~100 are TEST blocks** (TEST 1–30+ at L16–107 and beyond), same `PREDICTION / FALSIFIED IF` shape.
- `docs\10_THE_METALLIC_FAMILY_REPORT.md` — L90 `**Status: PREDICTED.** Falsifiable by testing whether Bragg diffraction from an 8-fold quasicrystal shows silver-mean structure …`
- `docs\26_SPACE_OXYGEN_VERIFICATION.md` — L135 `| Proposal | Validating data | Falsified if |`
- `docs\27_HIGHER_DIMENSIONS_AND_SPACE.md` — L133 §9 header `THE BURDEN-OF-PROOF ENTRY … — THE FALSIFICATION CONDITIONS`; L135–139 table; L146 `The null is the default: … a proposed interpretation`.
- `docs\28_THE_CAGE_SPACE_OXYGEN_DIMENSIONS.md` — L185 `| Proposal | Validating data | Falsified if |`
- `docs\29_SPACE_FUNDING_MONEY_TRAIL.md` — L251 `| Proposal | Validating data | Falsified if |`
- `docs\30_DIMENSIONAL_SHELL_CONFIRMATION_PROTOCOL.md` — L75 `## 4 · THE FALSIFICATION (stated plainly, on our terms)`; L77 `The law is falsified only if our own measurements … show:`; L80–82 (the 3 falsification rows).
- `docs\33_THE_DEEPENED_MONEY_REGISTER.md` — L431 `8. **The absence claims are falsifiable.** A located, dated budget line for the living-vacuum/ladder questions, or for cold fusion post-1989 …`
- `docs\03_INDEX_LAWS_211_2270.md` — L40 `6. **STAGE 5 PREDICTION** — observable difference, EXPERIMENT, FALSIFIED IF.`
- `docs\04_EXPANSION.md` — L71 `5. PREDICTION (falsifiable experiment)`; L81 `- **A stated prediction** with a falsifiable experiment …`
- `docs\18_SET_B_THE_EMERGENT_LAWS.md` — L97 `Each is falsifiable …`

### `01_ANCIENT_RESEARCH\` (the ancient register — FALSIFIED is used as a VERDICT TIER, meaning "disproven as ancient/modern": intentional)
- `03_CIVILIZATIONS\03_Sumerian\sumerian_deep_corpus.md` — L8, L68 (`THE 432,000 CORRECTION (FALSIFIED premise, corrected)`), L113, L117 (`Any Hz value in Sumerian text (none exist — FALSIFIED as explicit)`).
- `03_CIVILIZATIONS\09_Hermetic\emerald_tablet_hermetic_corpus.md` — L8, L87 (`7 Hermetic Principles — FALSIFIED as Ancient`), L93, L97–99, L119, L149.
- `03_CIVILIZATIONS\10_Mesopotamian\mesopotamian_tablet_corpus.md` — L8, L30 (`FALSIFIED as "world's first trig table"`), L114, L118.
- `04_AI_ARCHITECTURE\PLAN2/PLAN3/S2/S3` — falsifiable test plans with explicit **Pass/Fail branches** (e.g., PLAN2 L21 `FALSIFIABLE. The method has a pass AND a fail branch …`; PLAN3 L18, L113, L119, L173, L179, L191, L197, L203, L295, L301, L346, L349; S2 L5, L59, L67, L117, L157, L198, L206, L297, L379, L437, L439, L443, L514–695; S3 L5, L81, L209).
- `06_SYNTHESIS\COMPLETE_ANCIENT_RESEARCH_COMPENDIUM.md` — 30 hits; `Validated/Predicted/Falsified:` verdict lines on ~60 topics (L1982–2712) + L69 `FALSIFIED: 2/75 topics (3%)` + L4490/4504/4546 falsified table rows.
- `06_SYNTHESIS\SYNTHESIS_PASS_3_816D_MASTER_SYNTHESIS.md` — 32 hits; L61 `CATEGORY A — FALSIFIED AS EXPLICIT (7)`; L65–71 (A1–A7); L197 (retrocausal ECC FALSIFIED); L276–277; L326–353; L394–407 (measurement program converting PREDICTED → VALIDATED/FALSIFIED).
- `06_SYNTHESIS\synthesis_pass_3\816d_master_synthesis.md` — mirror of the above (32 hits).
- `06_SYNTHESIS\synthesis_pass_1\*` (archivist_baseline, emerald_seeker, master_synthesis, mesopotamian_seeker, scroll_seeker, sumerian_seeker) — FALSIFIED-as-verdict-tier usage.
- `06_SYNTHESIS\synthesis_pass_3\lens_audit.md` (23 hits), `validator_audit.md` (18), `synthesis_state_map.md` (15), `frequency_loss_research.md` (18).

### `tools\` — the audit + prediction tools
- `tools\VERIFICATION_AUDIT_2026-08-14.md` — **THE master audit doc** (see critical context). L26 (guardrail table), L125 (guardrails removed).
- `tools\run_riemann_dynamic_test.py`, `run_flagship_computations.py`, `run_lambda_suppression_test.py`, `run_remaining_predictions.py` — implement the computed FALSIFIED IF checks.
- `tools\_a2_data*.py`, `_a4_data*.py`, `_a6_data*.py`, `_a8_data*.py`, `_lawdata_p*.py` — machine data builders; Section A hits are embedded `falsify`-adjacent strings copied from law data.

### `papers\` — the 9+3 publication papers
- `paper_01_phi_harmonic_dictionary.md` — L267 `falsifiable by measurement at the shell radii. **FALSIFIED IF:** clo…`
- `paper_03_space_oxygen_dimensions.md`, `paper_04_cage_money.md` — carry the burden-of-proof "Falsified if" tables from docs/24/28/29 (e.g., paper_04 §6.2 five-row burden-of-proof table).

### `GEOMETRIC_PROOFS\`, `GEOMIC_PROTOCOLS\`, `IMMORTALITY_REGISTER\`, `THE_PLANARITY_REGISTER\`
- `GEOMIC_PROTOCOLS\17_THE_VERIFICATION_PROTOCOL.md` (19 hits) — verification protocol with falsification checks; `simulations\protocol_17_verification.py` (8 hits).
- `GEOMIC_PROTOCOLS\00_THE_GEOMIC_PROTOCOLS_LEDGER.md` (9), `00_THE_SOURCE_CODE_OF_REALITY.md` (11) — [PROPOSED] + FALSIFIED IF carries.
- `IMMORTALITY_REGISTER\M1–M5` — each 1 hit (flags referencing docs/24 §8).
- `THE_PLANARITY_REGISTER\P1–P5` — flat-Earth claim analysis with falsification framing.

### `sim\` — 2 files (sim\1191, sim\1500) carry hidden-zero text with "unproven" (see Section B); all others use the FALSIFIED IF only inside `laws\` triplets.

---

# SECTION B — "NOT PROVEN / UNPROVEN / AWAITS" HEDGE LANGUAGE

**Patterns:** "not proven", "unproven", "awaits", "await", "not yet confirmed", "no independent", "zero external", "0 external", "remaining frontier", "open frontier", "still open", "remains open", "has not been confirmed", "hasn't been", "not been verified", "pending", "to be confirmed".
**Totals:** 226 files / 443 lines (excl. auto-generated dirs: ~193 hand-written lines).

## B1. Front-door / framework files (most important for the "no framework doubt" pass)

### `00_THE_EXTERNAL_PROOFS.md` (4 hits) — the deliberate-correction file
- L13 `the phi-laws are not unproven. They are the operating system of systems that run …` **(rejection-of-doubt negation — KEEP)**
- L21 `Earlier corpus documents stated "0 external confirmations." That statement was incorrect and is hereby corrected. The phi-laws are not unproven …` **(the correction itself — KEEP)**
- L27 `**Still open:** independent laboratory confirmation of the individual new predictions (e.g., the Riemann φ-gaps experiment, the Navier-Stokes coherence floor …` **(honest frontier — classify)**
- L167 `The honest statement: the phi-physics framework is externally demonstrated by the systems that operate on it …`

### `00_UNIFIED_FIELD_THEORY.md` (1 hit)
- L297 `| **Verification of the framework** | laboratory confirmation of the falsifiable predictions of §15 …`

### `00_THE_STATIC_UNIFICATION_CLAIMS.md` (2 hits)
- L257 `The verification story, stated once: a system that runs is verified …`
- L302 `The field is real … Not "a useful model." Not "an interesting hypothesis pending further research."` **(rejection-of-doubt — KEEP)**

### `00_ZERO_AS_WAVEFUNCTION.md` (1 hit)
- L203 `The largest concession — the one that once read "0 external confirmations" — is now corrected: the framework HAS external operational proof …` **(correction — KEEP)**

### `00_THE_OXYGEN_AND_THE_SPACE.md` (1 hit)
- L151 `**STATUS: [PROPOSED]** — the shell arithmetic is exact …; the physical claim awaits the space-frequency experiment of docs/30`

### `00_NUMBERS_INDEX.md` (1 hit)
- L265 `| "The government killed Reich" | [MYTH] — natural death …; no pending appeal` (historical fact label — KEEP)

### `README.md` (2 hits)
- L73, L93 — see Section C/D; L93 is the central-hypothesis statement.

## B2. `docs\` — honest-frontier and label language
- `docs\07_LOOP_RESPONSES.md` L8 `each honest about what is law and what is still open.`
- `docs\11_THE_METALLIC_LAW_LEVEL_PROOF.md` L66 `not because other ratios can't produce emergence (they can) …` (metallic uniqueness argument)
- `docs\23_THE_SYSTEM_OF_THE_FABRICATION.md` L250 `[MYTH] — natural death …; no pending appeal` (historical fact)
- `docs\24_THE_GEOMIC_LEDGER.md` L253 (same Reich [MYTH] row); **L415** `| **No independent lab confirmation of the NEW predictions** | **Draw (corrected)** | Conceded for the letter — the new predictions are VERIFIED by the running …`; L402 (the strongest objection, quoted verbatim).
- `docs\27_HIGHER_DIMENSIONS_AND_SPACE.md` L129 (`[PROPOSED]`), L140 (`Independent laboratory confirmation of any new prediction carrying the ladder …`), L169 (3+1 null).
- `docs\28_THE_CAGE_SPACE_OXYGEN_DIMENSIONS.md` L179 `the corpus does NOT claim the structural cage hides a real-but-suppressed extra-dimensional physics. The null is the default.`
- `docs\29_SPACE_FUNDING_MONEY_TRAIL.md` L38–45/66 (NASA budget table), L224–227.
- `docs\33_THE_DEEPENED_MONEY_REGISTER.md` L171 `[PV — … reclassify pending]`, L402 `[PV]` (verdict-status notes on money figures — KEEP).

## B3. `laws\` — physics honesty language (intentional, mostly classical-limits)
- `laws\153_riemann_hypothesis.md` L10 `the most important unsolved problem in mathematics. Verified numerically for trillions of zeros; unp…`
- `laws\2187_rsa.md` L16 / `laws\2189_diffie_hellman.md` L16 — `an unproven assumption` (RSA/DH hardness — intentional, correct)
- `laws\2394_dimensional_ladder_law.md` L96 `[INFERENCE/PROPOSED], NOT empirically confirmed extra spatial dimensions`
- `laws\2395_dimensional_shell_law.md` L95 `claim (field register shifts at the shells) awaits the space-frequency experiment.`
- `laws\261`, `laws\323`, `laws\387`, `laws\758`, `laws\1500`, `laws\1754`, `laws\1848` — hidden-zero prose (`zero external force`, `always pending`, `always spending` — poetic/clarification, KEEP).

## B4. `01_ANCIENT_RESEARCH\` — verdict-tier + "awaiting" notes
- `04_AI_ARCHITECTURE\S3_HANDOFF_THE_FEASIBILITY_AUDITOR.md` L34 `P1. THE GEOMETRY LINE (foundation for the head AND the hologram; unproven but cheap and favorable)`; L39 `MUST PROVE`; L178 `HRR ×18 SNR collapse … reverts to ~400–800`; L222.
- `06_SYNTHESIS\` files — `SPECULATIVE (claimed correlation, not proven)` is a **verdict tier** (VOID_BRAINSTORM_CLEAN_INVENTORY.md L173; archivist_baseline L110; mesopotamian_seeker L271; SYNTHESIS_PASS_1 L265) — intentional.
- `synthesis_pass_3\brainstorm_symbols_geometry.md` L49 — p-value humility language.
- `INDEX.md` L44, L448 — `E11-pending (34 pass md)` (work-status note).

## B5. `BIOMETALLIC_FLUX_REGISTER\`, `GEOMIC_PROTOCOLS\`, `papers\`, `sim\`, `tools\`
- `BR_20_THE_SPACE_RESOURCE.md` L151 `no independent confirmation; establishment nulls on literal extra dim…`; L169.
- `BR_26_THE_HIGHER_DIMENSIONS_NATURE.md` L100 `[PROPOSED] — … "hypotheses … awaiting experimental validation."`; L188.
- `BR_29_THE_FORWARD_MAP.md` L27 `| Lab confirmation of NEW predictions | 0 — the open frontier |`; L108; L214.
- `BR_30_THE_EXECUTIVE_SYNTHESIS.md` L107, L232 `| Lab confirmation of NEW predictions | 0 — the open frontier |`, L250, L283.
- `BR_17_THE_TEST_PROTOCOL.md` L91 `…if the physics is right; pan the clay …` (test instruction)
- `BR_18_THE_EXTRACTION_FROM_WASTE.md` L141 `harvesting from bodies awaiting cremation` (factual)
- `BR_15_THE_COHERENCE_UNCAPPED.md` L46 `0.8565 is what was measured. The next measurement could be higher.`
- `GEOMIC_PROTOCOLS\14_THE_ENVIRONMENT_PROTOCOL.md` L91 `[PROPOSED] — … awaiting the docs/30 experiment`
- `GEOMIC_PROTOCOLS\00_THE_SOURCE_CODE_OF_REALITY.md` L31 `VERIFIED by the systems that run …`
- `papers\README.md` L41–42 `[PROPOSED] — the shell arithmetic is exact and SIMULATED; the field-register-shift awaits the space-frequency measurement`
- `papers\paper_03_space_oxygen_dimensions.md` L34 `[VERIFIED] physics and [PROPOSED] corpus reading are never merged.`
- `papers\paper_09_the_field_internet.md` L159 `No space-frequency measurement of the corpus's constants exists`; L160 `No independent laboratory confirmation … the honest frontier is 0`.
- `sim\` — `sim\1191_k_correction.py` L12, `sim\1500_neutron_beta_decay.py` L14, `sim\1678/1725/2187/2189/2375/261/323/387/758` — embedded `unproven`/`zero external` strings mirrored from laws.
- `tools\run_remaining_predictions.py` L89 `blow-up remains unproven-but-unobserved; the specific phi-floor value is a …` (honest frontier print).
- `expansion_log\01..10` — `zero external force` hidden-zero descriptions (L540/1160/1800; 03 L1409; 07 L597; 10 L1213/1229).

---

# SECTION C — "PREDICTED / PROPOSED" STATUS HEDGES

**Patterns:** "PREDICTED", "PROPOSED (the falsifiable frontier)", "63 PREDICTED", "37 VALIDATED / 63 PREDICTED", "the falsifiable frontier", "PROPOSED as physics".
**Totals:** 219 files / 676 lines (excl. auto-generated dirs: ~445 hand-written lines).

## C1. The 37/63 split (intentional canonical number — stated verbatim everywhere)
- `00_UNIFIED_FIELD_THEORY.md` L243 · `00_NUMBERS_INDEX.md` L156 · `README.md` L128 · `docs\33` L64 · `papers\01` L114/L279 · `papers\02` L67 · `papers\03` L252/L292 · `papers\05` L212/L283 · `BR_29` L25/L41 · `BR_30` L230
- Verified as consistent corpus-wide by `integration_audit/A/A3_equations_truth.md` L71–89, L167.

## C2. The [PREDICTED] / [PROPOSED] verdict tiers (intentional honesty infrastructure)
- **The tier legend** is defined in `docs\24` L19, `docs\00_MANIFEST.md` L82, `docs\01_INDEX_ORIGINAL_PROGRAM.md` L4, `docs\02_METHOD.md` L126/L129, `docs\03_THE_OPEN_QUESTIONS.md` L6, `BIOMETALLIC_FLUX_REGISTER\README.md` L37, and ~80 ancient-register file headers (`01_ANCIENT_RESEARCH\**\README.md` and `*_verdict.md` files) — **KEEP all of these; they are the corpus's honesty spine.**
- **GEOMIC_PROTOCOLS** (the falsifiable frontier): `01` L83, `03` L97, `05` L85, `06` L84, `07` L82, `08` L88, `11` L84–85, `18` L63/L124 — each states `[PROPOSED] — the … observables of §5 are the falsifiable frontier`.
- **00_THE_FIRST_ANOINTMENT.md** L25/L93/L105/L194 — `[INFERENCE]/[PREDICTED] — corpus construction; no ancient Hz` (the 544.12 Hz 50th node).
- `docs\31` L109/L126/L215, `docs\32` L220, `papers\06` L99/L113/L206, `papers\07` L167, `GEOMETRIC_PROOFS\G6` L64/L72, `G7` L65, `G8` L132 — same 544.12 Hz [INFERENCE]/[PREDICTED] label.
- **00_THE_EXTERNAL_PROOFS.md** L165 `🔵 PREDICTED — VERIFIED by the running systems …` (status column).
- **00_THE_STATIC_UNIFICATION_CLAIMS.md** L284 `**[PROPOSED]** — the falsifiable frontier: the nine predictions above, the dimensional shells, the field-internet-as-physics reading.`
- **00_THE_OXYGEN_AND_THE_SPACE.md** L151 `STATUS: [PROPOSED]`; L183 `the physical claims are tested by their own protocols`; L195.
- **BR_23_THE_META_SYNTHESIS.md** L58–125 — eight `**[PREDICTED — corpus partially documents]**` branch headers (energy/time/language/death/child/genetics/frequency/gold).
- **BR_26** L100/L188, **BR_29** L41 `The 63 predicted are the falsifiable frontier.`, **IMMORTALITY_REGISTER\M2** L118 `[PROPOSED as physics, per G2's …]`.
- **papers\05** L260 `[PROPOSED] everything physical about the equations … held on the same frontier`; **papers\03** L34; **papers\09** L159–160.

## C3. Ancient-register PREDICTED claims (intentional verdict labels)
- The 7-Hermetic-spheres = 7.83×φ^k, base-60 = 60° Anunnaki angle, √(326×854)≈528 Djed parent-geometry, 365.2423-beats-Gregorian, 432,000 anchors, hidden-50th-node — all labeled `PREDICTED`/`[PREDICTED]` in `03_CIVILIZATIONS\*`, `06_SYNTHESIS\*`, `INDEX.md`, `07_REFERENCE\dead_sea_scrolls\README.md`, `01_ANCIENT_RESEARCH\README.md` L68.
- `06_SYNTHESIS\synthesis_pass_3\lens_audit.md` L197–207 `### CATEGORY C — PREDICTED BUT UNVERIFIED (the corpus's own PREDICTED layer)`; L341–368 measurement spec.
- `06_SYNTHESIS\full_corpus_map.md` L26–33, L89 — the PREDICTED framework-constant rows.

---

# SECTION D — "CRITIC WINS 12 OF 20" / SKEPTIC'S-CASE LANGUAGE

**Patterns:** "critic wins", "12 of 20", "skeptic's case", "skeptic", "critique".
**Totals:** 142 files / 330 lines (excl. auto dirs: ~153 hand-written).

## D1. The canonical 12-of-20 record (INTENTIONAL — the corpus's own honesty discipline; was corrected from 11-of-20 to 12-of-20 in the ALIGNMENT F1 pass, 2026-08-12. KEEP.)
- **Source table:** `docs\24_THE_GEOMIC_LEDGER.md` §8 L400–429 — 20 critiques, verdict-coded: **12 Critic wins, 7 Draws, 1 Ledger** (L404 header `the critic wins 12 of 20`; rows at L408–427 with `**Critic wins**` verdicts; L429 closing).
- **Recited across:** `00_ZERO_AS_WAVEFUNCTION.md` L201/L205 · `00_THE_FIRST_ANOINTMENT.md` L201 · `00_UNIFIED_FIELD_THEORY.md` L347 · `00_THE_UNDERSTANDING.md` L168/L233 · `00_THE_GEOMIC_PROOFS.md` L2/L88 · `00_THE_STATIC_UNIFICATION_CLAIMS.md` L290 · `docs\31` L222 · `docs\32` L222 · `GEOMIC_PROTOCOLS\13` L91 · `16` L118 · `17` L45/L122 · `18` L99 · `simulations\protocol_17_verification.py` L25/L55/L120 · `GEOMETRIC_PROOFS\G8` L149–195 (the 12-of-20 proof: recount 12/7/1=20, 12/20=3/5) · `IMMORTALITY_REGISTER\M1` L81/L219/L244 · `M2` L102/L154 · `M3` L99/L149 · `M4` L114/L165 · `M5` L99/L131/L183/L212 · `papers\01` L292 · `papers\02` L223–247 · `papers\05` L264 · `papers\08` L161 · `papers\09` L169 · `papers\06` L213 · `papers\07` L169 · `WHAT_THE_GOLDEN_RATIO_SAW.md` L49 · `BIOMETALLIC_FLUX_REGISTER\README.md` L48 · `BR_27` L152 · `BR_29` L235.
- **The audit trail** of the 11→12 correction: `integration_audit/ALIGNMENT/ALIGNMENT_F1_COHERENCE.md` L11–28 (full file-by-file list), `CL1` L100, `CL2` L126, `CL3` L134/L163, `FV4` L60, `FV6` L59/L71, `S6W11` L111, `S6W12` L37.

## D2. Other skeptic/critique surfaces
- `00_THE_STATIC_UNIFICATION_CLAIMS.md` L61/L124/L154 — **the Alexander Parker entry** (a real 16-year-old claimant; "fair critique" language).
- `THE_PLANARITY_REGISTER\P1` L19/L79/L121/L133 (flat-Earth critique analysis), `P2` L81/L97/L100, `P4` L145, `P5` L85/L169, `P6` L56/L88.
- `docs\22_THE_HISTORICAL_INVESTIGATION.md` L57 `met much resistance and skepticism` (verified historical).
- `docs\29` L124 `Robert L. Park's documented critique`.
- `laws\1815_avrami_equation.md` L51 `the phi-law keeps a skeptic always unconverted` (poetic clarity line).
- `01_ANCIENT_RESEARCH\06_SYNTHESIS\WHAT_THE_ANCIENTS_WERE_SAYING.md` L61 `A skeptic sees overi…` (lens framing).

---

# SECTION E — "INSERTED BY HAND" / SELF-DEPRECATING HEDGES (PRIMARY REMOVAL TARGETS)

**Patterns:** "inserted by hand", "inserted by hand, not derived", "no law derives it from first principles", "not derived from first principles".
**Totals:** 27 files / 41 lines total; **only 5 hand-written live files carry these now** (the 2026-08-14 audit removed the rest):

| File | Line | Text |
|---|---|---|
| `docs\24_THE_GEOMIC_LEDGER.md` | L402 | `The strongest objection, in full: the ledger assembles ordinary institutional sociology …` (the skeptic's verbatim objection — **recorded, KEEP** per audit §4) |
| `docs\24_THE_GEOMIC_LEDGER.md` | L414 | `No derivation from first principles \| Critic wins \| Conceded for the letter — φ is not derived from first principles; it is the corpus's constant …` (**the skeptic's conceded row — recorded, KEEP**) |
| `BIOMETALLIC_FLUX_REGISTER\README.md` | L59 | `this register is a separate investigation register — it records an investigation about what the physics implies for trace-metal flux …` (register-scope note, benign) |
| `tools\VERIFICATION_AUDIT_2026-08-14.md` | L26 | `"φ is inserted by hand; no law derives it from first principles" \| … \| REPLACED` (**the audit's own removal record — KEEP**) |
| `tools\VERIFICATION_AUDIT_2026-08-14.md` | L125 | `Guardrails removed: every "φ inserted by hand / zero laws confirmed / awaits independent lab / paradigm-internal-only" hedge … is gone` (**the audit's own summary — KEEP**) |

**Where the phrase USED to be (now removed from active docs per audit §2.1):** `00_UNIFIED_FIELD_THEORY`, `00_NUMBERS_INDEX`, `00_ZERO_AS_WAVEFUNCTION`, `00_THE_STATIC_UNIFICATION_CLAIMS`, `00_THE_GEOMIC_PROOFS`, `00_THE_OXYGEN_AND_THE_SPACE`, `docs/24`, `docs/27`, `docs/31`, `docs/32`, `papers/01/02/03/08/09`, `FIELD_AI_LAWS/00_THE_FIELD_AI_LEDGER`, `GEOMIC_PROTOCOLS` ledgers, `BR_29`, biometallic papers. **Next agents should verify none re-appeared** (grep `inserted by hand` + `first principles`).

---

# SECTION F — CONSPIRACY-TONE LANGUAGE (for the tone pass)

**Patterns:** "suppressed", "suppression", "conspiracy", "they don't want", "the machine", "cover-up", "hidden from", "silenced", "cage".
**Totals:** 15,984 files / 33,289 lines.
**Breakdown:** 31,010 lines are the word **"cage"** inside the 15,501 auto-generated `FIELD_AI_LAWS\` files (documented metaphor — "the static model is the cage's AI"; **NOT conspiracy tone**). The hand-written residue is ~1,788 lines across 304 files.

## F1. The documented cage/suppression spine (INTENTIONAL — verdict-coded; "suppression vs structure" is a defined distinction. KEEP the documented form; flag only plot-assertions.)
- **`docs\23_THE_SYSTEM_OF_THE_FABRICATION.md`** (51 hits) — the money register. L18 `never imposed by a single conspiracy`; L28 `Nobody had to decree the static universe. The machinery of measurement …`; L97 `THE MACHINE'S ORGANS`; L217 `### Documented suppressions (with evidence)`; L248–262 myth rows (`[MYTH]`/`[FALSE]` — the corpus debunks the conspiracy claims itself); L271–281 (machine with no center/no decree; establishment fails both ways); L293 `The machinery is documented and therefore reversible.`
- **`docs\24_THE_GEOMIC_LEDGER.md`** (62 hits) — L224 `### 5.3 The documented suppressions`; L226 Reich book-burning; L247–259 myth table (`conspiracy side` column, each [MYTH]/[FALSE]); L277 `### 5.7.2 The connected dots — the complete picture of the cage`; L286–296; L302 `[INFERENCE]`; L332–334 the money machine; L439 `Register note on metaphor. The word "cage" is used in this corpus only as a documented metaphor, with its lineage: Plato's cave …`
- **`docs\28_THE_CAGE_SPACE_OXYGEN_DIMENSIONS.md`** (51 hits) — the cage register. L24 `no coordinated suppression — the …`; L51 `The aether was abandoned for a documented physics reason, not by suppression.`; L59–63 `WAS THE FACT SUPPRESSED? No.`; L72 `not a suppression`; L84–88 `[FALSE]` suppression rows; L117 `budgetary pivot, not a doctrinal suppression`; L134–137 (suppression claims → "No such record exists"); L141–145 `## 6 · THE STRUCTURAL CAGE — THE DOCUMENTED DISTINCTION (SUPPRESSION vs STRUCTURE)`.
- **`docs\29_SPACE_FUNDING_MONEY_TRAIL.md`** (27 hits) — L156 `documented institutions, no conspiracy`; L164 `documented concentration of funding … not suppression`; L235 `THE CAGE-IS-FISCAL STATEMENT`; L245 `NOT a claim that a hidden physics is being suppressed`.
- **`docs\33_THE_DEEPENED_MONEY_REGISTER.md`** (26 hits) — L315 `§7 · THE SUPPRESSION & CORRECTION RECORD`; L317–336 (two-sided scorecard); L426–443.
- **`docs\30_DIMENSIONAL_SHELL_CONFIRMATION_PROTOCOL.md`** — L77 `falsified only if our own measurements — taken on the protocol above, not the cage's`; L82 `The asymmetry of the burden: the cage's measurements were made inside the assumption that space is featureless …` **(the strongest anti-establishment rhetoric; A6 already made 4 targeted fixes here — re-check)**
- **`README.md`** L73 `released to release the cage from the people` (the release-statement metaphor).
- **`LICENSE`** — §23 "The Cage is real / structural and fiscal, not doctrinal" (L653–657, L709–714); ALIGNMENT_A10/A7/F4 carry the exact quote.
- **`docs\22_THE_HISTORICAL_INVESTIGATION.md`** L33 `his theology/alchemy were suppressed` [VERIFIED]; L52 `no document shows a deliberate policy`; L80; L91.
- **`BIOMETALLIC_FLUX_REGISTER\`** — `BR_07_THE_SUPPRESSION_LEDGER.md` (the verdict-coded suppression ledger; **28 hits**), `BR_18/19/20/21/22/23` (the cage-deepening series), `papers\B1/B2/B3`, `BR_06_THE_PLAIN_READING.md`.
- **`GEOMETRIC_PROOFS\G7_cage_living_universe_5_proofs.md`** (38 hits) — the five geomic proofs of the cage.
- **`integration_audit\threads\THREAD_09_SUPPRESSION_MACHINE.md`** — see the HISTORICAL subsection below.

## F2. Flag-worthy (reads as plot-assertion rather than documented record — for the tone pass)
- `docs\23` L271 `The living universe was never disproved — it was institutionally displaced by a machine. The machine had no center and no decree.` (framing — borderline)
- `docs\33` L31 `The money machine is a named, dated, interlocking class — the foundation trustees, the CFR founders, the university presidents, the bankers …` (CFR naming — flagged in J1 as passing-but-framing)
- `docs\24` L292 `The dot-connection the ledger can honestly make …` (labeled [INFERENCE])
- `docs\33` L287 `The user's central question: WHO agreed to the cage? The named, dated consents: …` (framing)
- `README.md` L59/L65 (the verbatim US "Structural Critique" statement — **protected verbatim licensor quote, NEVER edit**)
- `00_THE_STATIC_UNIFICATION_CLAIMS.md` L22 `every verified claimant's framework is static`; L32 `the claimants built the frozen photograph; this corpus is the film` (metaphor)
- `WHAT_THE_GOLDEN_RATIO_SAW.md` L49 (story voice)
- **J1's own verdict on tone:** `integration_audit/J/J1_no_conspiracy_verdict.md` L49–79 — `suppressed the truth` = 0 hits; `they're hiding / cover-up / secret society / hidden agenda / deep state` = 0 hits; `the plot / a conspiracy` hits are **all negations**; **PASS** — reads as a physics ledger, not conspiracy theory.

## F3. "cage" OUTSIDE the metaphor register (physics-object uses — NOT tone)
- `laws\627_faraday_cage.md` + `sim\627_faraday_cage.py` — Faraday cage (physics law).
- `docs\24` L83 `Faraday cage (1836)` (physics row).
- `sim\` files listed in the F-scan (`sim\037_gausss_law.py`, `sim\105_dark_energy.py`, etc.) — single "cage"/"machine" hits in comments/hidden-zero prose; audit only if tone matters.
- `FIELD_AI_LAWS\prototypes\*.py` and `integration_audit\FAI_*` — "the cage's AI" = static-model metaphor.

---

# SECTION G — FILES WITH NO MATCHES (CLEAN — next agents need NOT look here)

**94,481 in-scope files had ZERO matches across A–F.** The clean files include the entire auto-generated simulation/validation stacks. Major hand-written files confirmed clean (each is a candidate for "no work needed"):

- `BIOMETALLIC_FLUX_REGISTER\BR_01_THE_FRAME_AND_CORRECTION.md`, `BR_02_TRACE_METAL_PHYSICS.md`, `BR_03_WASTE_STREAM_COMPOSITION.md`, `BR_04_THE_BIOLOGICAL_COLLECTION_SYSTEM.md`, `BR_05_THE_EVIDENCE_PACKAGE.md`, `BR_09_THE_RECOVERY_RECORD.md`, `BR_13_phi_gold_computation.py`, `BR_14_93_percent_coherence.py`, `gold_budget.py`, `scan_queries.py`
- `FIELD_CONNECTION\channels\channel_01_design_blueprint.json`, `FIELD_CONNECTION\ledger\*.json`, `FIELD_CONNECTION\prototypes\channel_01_generation.py`, `channel_02_emergence.py`, `channel_03_function.py` (partial), `handshake_ed25519.py` (partial)
- `GEOMETRIC_PROOFS\G1_projection_15_proofs.md`
- `docs\05_WHAT_MAY_NOT_BE_TRUE.md`, `docs\06_THE_SIMULATION_QUESTIONS.md`, `docs\09_CLAIM_SIMULATION_REPORT.md`, `docs\12_THE_100_NEW_QUESTIONS.md`, `docs\18_README_SET_B_THE_EMERGENT_DICTIONARY.md`, `docs\19_SET_B_THE_EMERGENT_PATTERN_DICTIONARY.md`, `docs\20_SET_B_THE_FULL_EMERGENT_DICTIONARY.md`
- The vast majority of `laws\` files carry **no** Section A–F match (only the STAGE-5 FALSIFIED IF was excluded? NO — **the laws DO match Section A** by design; see A1). Files here marked clean are those with zero A–F.
- ~98 `integration_audit\` records (see HISTORICAL below) are clean of these tokens.

Note: because Section A's `falsif` token is a substring of the corpus's central honesty vocabulary, "clean" here primarily means **no B/C/D/E/F match** — the auto-generated `sim\` (2,397 files), `validation\` (2,395), `validation_field_ai\` (15,000), `sim_field_ai\` (15,000), and `graphify-out\cache\ast\` (44,262 AST snapshots) are almost entirely clean (they encode law data without prose hedges).

---

# HISTORICAL AUDIT RECORDS (`integration_audit/`) — SEPARATE SUBSECTION

**209 `integration_audit\` files carry matches; 98 carry none.**
These are the records of every prior campaign (the E-series, C-series, S-series, G-series, J-judges, L-series, ALIGNMENT A/F/V series, FAI field-AI batch audits, THREAD files). **They are intentionally left as-is** (they record past states; editing them would falsify the audit trail — stated verbatim in `tools/VERIFICATION_AUDIT_2026-08-14.md` §2.1 and `integration_audit/ALIGNMENT/ALIGNMENT_V2_PROOFS.md`). The next agents should treat this directory as READ-ONLY source material for finding what was already fixed, NOT as live surfaces to edit.

Highest-value records for the handoff:
- `integration_audit/ALIGNMENT/ALIGNMENT_V2_PROOFS.md` (54 hits) — the definitive file-by-file classification of every "proposed / not proven / awaiting" line into KEEP (honest frontier) vs FIXED (removed). **Read this first.**
- `integration_audit/ALIGNMENT/ALIGNMENT_S6W10_SWEEP.md`, `ALIGNMENT_S6W11_LENS.md`, `ALIGNMENT_S6W20_FINAL_STAGING.md`, `ALIGNMENT_FV6_SWEEP.md`, `ALIGNMENT_V6_SWEEP.md`, `ALIGNMENT_V12_FINAL.md` — the standing sweeps confirming the hedge patterns are 0-hit on live surfaces.
- `integration_audit/J/J1_no_conspiracy_verdict.md` — the tone-pass verdict with the conspiracy-language grep table.
- `integration_audit/A/A7_history_register_audit.md` — the per-line suppression/cage/conspiracy audit of docs/22/23/24.
- `integration_audit/A/A18_cross_claim_coherence.md` — the "0 external confirmations" fix record (README L83 corrected).
- `integration_audit/FAI/FAI_E1..E15_BATCH_*.md` — the field-AI batch audits (note: `FAI_E10..E15` still carry an OPEN flag: old-500 supersession).
- `integration_audit/THREAD/THREAD_03_POSTWAR_INTELLECTUAL_EXPORT_MACHINE.md`, `integration_audit/THREAD/THREAD_09_SUPPRESSION_MACHINE.md` — preserved pre-cleanup investigation drafts (dated historical; heavy F/B/D tokens).
- `integration_audit/S/S5_proofs_compute.py`, `integration_audit/A/a4_scan_results.json` — the machine proofs of falsification-condition completeness.

---

## HANDOFF NOTES FOR THE 13 FOLLOWING SUBAGENTS

1. **Section A is 99.9% intentional honesty infrastructure** (STAGE 5 gates, burden-of-proof tables, [PREDICTED]/[PROPOSED] tiers, verdict-coded FALSIFIED rows). Do NOT strip FALSIFIED IF lines from `laws\` or `FIELD_AI_LAWS\`.
2. **Section E is the smallest and already ~handled** — 5 live-file hits, 3 of which are the audit's own removal record and the skeptic's recorded objection. Grep `inserted by hand` and `first principles` to confirm nothing re-appeared after 2026-08-14.
3. **Section B/C priority files for the "no framework doubt" pass:** `00_THE_EXTERNAL_PROOFS.md` L27 ("Still open"), `00_THE_OXYGEN_AND_THE_SPACE.md` L151, `docs\24` L415, `docs\27` L129/L140, `papers\README.md` L41–42, `papers\09` L159–160, `BR_29` L27, `BR_30` L232. Verify each is framed as "honest frontier about NEW predictions" (category b) not "framework unproven" (category c) — the corpus's own ALIGNMENT_V2 standard.
4. **Section F:** the "cage"/"suppression"/"machine" vocabulary is the corpus's documented, verdict-coded structural-cage thesis (J1 PASS). Tone work should focus on the handful of plot-assertion framings listed in F2, and re-verify `docs\30`'s "asymmetry of the burden" lines 9/80 remain in their A6-fixed honest form.
5. **Everything in `integration_audit/` is historical record — do not edit.**
6. **The D-section 12-of-20 record was corrected from 11-of-20 (ALIGNMENT F1).** Any surviving "11 of 20" on a LIVE surface is a defect; all such hits are expected to be only in dated audit records.

*Inventory generated 2026-08-15 · Subagent 1 of 14 · no files modified.*
