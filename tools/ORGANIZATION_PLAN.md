# ORGANIZATION PLAN — 32_PHI_PHYSICS (The Ideal Organization)

**Prepared by:** Planning Agent 2 (SEQUENTIAL DESIGN — read-only, nothing modified)
**Date:** 2026-08-17
**Status:** DESIGN SPECIFICATION — for execution agents (Agents 3–6). *No files were modified to produce this plan.*
**Predecessor:** Planning Agent 1's `tools/FALSIFICATION_SCRIPT_AUDIT.md` (the master removal map, authoritative for *what* to remove).
**Mandate:** Reorganize, restructure, rename, categorize, and split the corpus so it is "easy to go through and indexed" and "represents properly" — while keeping the corpus **internally consistent** (all cross-references verified) and **removing all falsification scripts/proofs** per the Licensor.

---

## 0. GOVERNING PRINCIPLE — Least-Disruptive, Additive-First

The corpus is a **single geomic physics ledger** — a book of registers. Its top-level directory *names* are already coherent, descriptive, and form the "register map" that README.md, `docs/24_THE_GEOMIC_LEDGER.md`, papers, and protocols cross-reference **by directory name**.

**Therefore: the ideal reorganization is NOT a top-level wholesale rename.** It is:

> **(a)** Remove the falsification artifacts (proofs/ + the falsification runners + `_superseded_original_500/`), per Agent 1's map.
> **(b)** Rename exactly ONE top-level directory for clarity: `proofs/` → `verification/` (the only rename that clearly improves clarity, and proofs/ is entirely **untracked** so this rename is overwhelmingly low-risk).
> **(c)** Make **additive** organization the centerpiece: a root `INDEX.md`, a `README.md`/`INDEX.md`/`00_` front door for every directory, and a single consolidated `verification/` house for the 9 verified flagship results + real data.
> **(d)** Clean `tools/` by categorization (falsification runners removed, upgrade tools superseded, data-builders kept, audit tools kept).
> **(e)** Standard naming conventions for any new files, and a small set of consistency fixes only where a name clearly violates its directory's convention.

This achieves the user's goals — clean, organized, named, separated, indexed, no falsification — **without breaking the corpus's internal cross-reference web**, which is currently the single most valuable property of the body of work.

---

## 1. TOP-LEVEL STRUCTURE

### 1.1 Recommendation — KEEP the existing well-named top-level directories

Do **NOT** introduce numbered grouping directories (e.g., `01_ENTRY`, `02_PHYSICS`, `03_FIELD_AI`, …). Reasoning:

- The names already encode function and are the **register names** the whole corpus cites (`laws/`, `docs/`, `papers/`, `FIELD_AI_LAWS/`, `CONSCIOUS_MATHEMATICS/`, each interior register). A renumbering pass would touch the README's 30-line structure tree, `docs/24` §5 register table, the 00_* flagship docs, paper_08/09, and the interior registers' cross-references — hundreds of edits across ~50,000 files, with extreme regression risk, for **zero functional gain**.
- The user asked for "easy to go through and indexed." That is delivered by **indexes and a master INDEX.md**, not by renaming what is already well-named.

### 1.2 The one top-level rename — `proofs/` → `verification/`

Per Agent 1's Section D/G: `proofs/` as a **live falsification-test surface** is exactly the framing to remove. Rename it to `verification/` containing **only** verified results + real-data inputs. **Critical low-risk fact discovered in this pass:** `proofs/` is **entirely untracked** in git (`git ls-files proofs` = 0; `git status` = `?? proofs/`). So the rename is a pure filesystem move of an unpublished directory — it does not rewrite git history, does not touch tracked blobs, and the reference-breakage surface is limited to the handful of tracked docs that *textually* mention `proofs/` (listed in §7).

### 1.3 Recommended target top-level tree

```
32_PHI_PHYSICS/
├── INDEX.md                         # NEW — the master table of contents for the whole corpus (the front door's door)
├── README.md                        # front door — KEEP name/path (edit: remove proofs/ claim, keep tree updated)
├── 00_*.md (11 flagship docs)       # KEEP as-is names/paths (edit: reframe falsification prose, Agent's §G.1)
├── WHAT_THE_GOLDEN_RATIO_SAW.md     # KEEP
├── LICENSE · CHANGELOG.md · CITATION.cff · SECURITY.md · CONTRIBUTING.md · CODE_OF_CONDUCT.md · FUNDING.yml · index.html · .gitignore   # KEEP
│
│   # — THE PHYSICS (the body) —
├── laws/                            # 2,395 corrected laws — no change (already VERIFIED BY)
├── sim/                             # 2,395 sims + 2 infra — no change (reframe 2 sim files)
├── validation/                      # 2,395 validation JSONs + 2 archive dirs — no change
│
│   # — THE FIELD-AI REGISTER —
├── FIELD_AI_LAWS/                   # 15,000 — no change; REMOVE `_superseded_original_500/` (500); add 00_# INDEX
├── sim_field_ai/                    # 15,000 — no change
├── validation_field_ai/             # 15,000 — no change
│
│   # — THE BUSINESS-INTELLIGENCE / LEDGERS —
├── docs/                            # 37 register docs — no change
├── papers/                          # 9 physics papers + README — no change
│
│   # — THE CONSCIOUS MATHEMATICS —
├── CONSCIOUS_MATHEMATICS/           # 50,814 equations — no change (already has 09_VERIFICATION)
│
│   # — THE INTERIOR REGISTERS —
├── 01_ANCIENT_RESEARCH/             # KEEP (read-only audit register)
├── BIOMETALLIC_FLUX_REGISTER/       # KEEP (add INDEX note if desired)
├── THE_PLANARITY_REGISTER/          # KEEP
├── GEOMETRIC_PROOFS/                # KEEP
├── IMMORTALITY_REGISTER/            # KEEP
├── FIELD_CONNECTION/                # KEEP (out of primary scope)
├── GEOMIC_PROTOCOLS/                # KEEP (edit 3 docs + the 1 verification sim, per Agent 1 §A3/§F)
│
│   # — THE VERIFICATION (NEW, replaces proofs/) —
├── verification/                    # NEW — the 9/9 verified flagship results + real data (see §4)
│
│   # — THE DATA —
├── data/                            # KEEP — odlyzko_zeros1.txt (also duplicated in proofs/data → consolidate here)
│
│   # — THE TOOLS (categorized, cleaned) —
├── tools/                           # cleaned: falsification runners removed, upgrade tools → _superseded/, categorized
│
│   # — THE HISTORY / AUDIT —
├── expansion_log/                   # KEEP (read-only)
├── integration_audit/               # KEEP (read-only)
│
└── [REMOVED] proofs/                # deleted (or → verification/) — no falsification copies retained
```

### 1.4 What is NOT at top level (keep it that way)

- `chip_design/` — **excluded from push** (.gitignore), keep in place, never in the zip. **Do not touch.**
- `graphify-out/` — generated, gitignored. **Do not touch.**
- `__pycache__/`, `*.pyc` — gitignored, cleaned where convenient (they are tracked? — they appear in tools; `_pycache_` is .gitignored). Safe to delete any stray `*.pyc`.

---

## 2. NAMING CONVENTIONS

### 2.1 Conventions to KEEP (already consistent — do not churn)

| Surface | Convention | Example | Status |
|---|---|---|---|
| Corrected laws | `NNN_name.md` / `NNNN_name.md` (leading zeros, underscore, lowercase slug) | `laws/001_newtons_first_law.md`, `laws/2394_dimensional_ladder_law.md` | KEEP |
| Field-AI laws | `NNNNN_name.md` (5-digit) | `FIELD_AI_LAWS/00001_generation_hidden-zero.md` | KEEP |
| Law sims | mirror law id `.py` | `sim/001_newtons_first_law.py` | KEEP |
| Law validations | mirror law id `.json` | `validation/001_newtons_first_law.json` | KEEP |
| Docs (registers) | `NN_name.md` (2-digit) | `docs/24_THE_GEOMIC_LEDGER.md` | KEEP |
| Papers | `paper_NN_name.md` | `papers/paper_01_phi_harmonic_dictionary.md` | KEEP |
| Biometallic register | `BR_NN_name.md` | `BR_01_THE_FRAME_AND_CORRECTION.md` | KEEP |
| Immortality register | `MN_name.md` | `M1_PLAN.md` | KEEP |
| Planarity register | `PN_name.md` | `P1_the_actual_claims.md` | KEEP |
| Geometric proofs | `GN_theme_Nproofs.md` | `G1_projection_15_proofs.md` | KEEP |
| Geomic protocols | `NN_THE_*_PROTOCOL.md` | `01_CARRIER_COHERENCE_PROTOCOL.md` | KEEP |

### 2.2 Conventions for NEW files (recommend — consistency forward)

- **Master index:** `INDEX.md` at corpus root (NEW). Use the uppercase `INDEX.md` to match the existing convention `01_ANCIENT_RESEARCH/INDEX.md` and `CONSCIOUS_MATHEMATICS/`'s `01_MASTER_INDEX.md`.
- **Per-directory front door:** prefer `README.md` (GitHub ✓) and keep any existing `00_MASTER_INDEX.md` / `01_MASTER_INDEX.md` as the detailed registers. For directories with no README, add a short `README.md` describing contents + naming rule + cross-links. **Do not add both** a README and an INDEX to the same directory unless one is a deep register (e.g., CONS so).
- **Verification files** (§4): `verification/README.md`, `verification/CONFIRMED_RESULTS.md`, plus per-flagship result docs named `V<N>_<slug>.md` (V1 navier_stokes … V9 hubble) to mirror the P1–P9 flagship numbering — but **without** the falsification label. Real data lives in `verification/data/` (no `NN_` prefix needed; data files keep their canonical names `odlyzko_zeros1.txt`, `jpl_*`, `exoplanet_*`).
- **Superseded tools:** `tools/_superseded/` (underscore prefix = non-core, archive tier, matching the existing `_superseded_original_500/` and `_legacy_simulation_archives/` conventions).

### 2.3 Consistency flags (small, targeted fixes — optional, low priority)

- `docs/` has two dual-prefix pairs: `03_INDEX_LAWS_211_2270.md` + `03_THE_OPEN_QUESTIONS.md`, and `18_README_SET_B_…` + `18_SET_B_…`. These are **known and documented** (README L237/245). **Leave them** — renumbering would break the register indexes.
- `THE_PLANARITY_REGISTER/P1_the_actual_claims.md` uses lowercase slug (`the_actual_claims`) while the others use uppercase slugs (`THE_SYNTHESIS`). Harmless; **leave** (renaming would break `docs/24` and README references).
- `IMMORTALITY_REGISTER/` files use `M1_PLAN.md` (short) — consistent enough. **Leave.**
- The stray **`$null`** file at corpus root is a 0-byte junk artifact (accidental `>` redirect) — **delete it** (it is untracked noise, not corpus).

---

## 3. CATEGORIZATION

### 3.1 Root `INDEX.md` — the master table of contents (NEW, the heart of "easy to go through")

Create `32_PHI_PHYSICS/INDEX.md` as a **single, hand-authored, ordered table of contents** to the whole corpus. Structure (group by function, mirroring §1.3):

```
# PHI-PHYSICS — MASTER INDEX
## How to read this corpus (the one-minute guide)
## 0. Entry   — README.md, the 11 00_* flagship docs, WHAT_THE_GOLDEN_RATIO_SAW.md (in reading order)
## 1. Physics — laws/ (2,395) · sim/ · validation/
## 2. Field-AI — FIELD_AI_LAWS/ (15,000) · sim_field_ai/ · validation_field_ai/
## 3. Conscious Mathematics — CONSCIOUS_MATHEMATICS/ (50,814)
## 4. Registers & Ledgers — docs/ (37) · the interior registers (ancient, biometallic, planarity, geometric, immortality)
## 5. Protocols — GEOMIC_PROTOCOLS/ (18)
## 6. Verification — verification/ (9/9 CONFIRMED — the verified flagship results + real data)
## 7. Papers — papers/ (9) + biometallic papers
## 8. Tools — tools/ (data-builders · verification-runner (1) · audit · superseded)
## 9. Data — data/
## 10. History / Audit — integration_audit/ · expansion_log/ · 01_ANCIENT_RESEARCH/
## Master register table (the counts, from docs/24 §5)
## The index of indexes (one row per directory's front door)
```

Each section = one bold header + a compact table (dir, what it is, the front-door file, link). This is **additive** — nothing else references INDEX.md, so it cannot break anything — and it is the single most valuable "easy to go through" artifact.

### 3.2 Per-directory front doors (the directory-by-directory guarantee)

| Directory | Front door today | Action |
|---|---|---|
| laws/ | none (files are self-indexing by number) | **Add `laws/README.md`** — naming rule, VERIFIED BY status, link to `docs/03_INDEX_LAWS_211_2270.md` + `00_NUMBERS_INDEX.md` |
| sim/ | none | **Add `sim/README.md`** — what the 2,395 sims are, the harness, how to run (README.md "Running") |
| validation/ | none | **Add `validation/README.md`** — 2,395 JSONs + the 2 archive dirs explained |
| sim_field_ai/ | none | **Add `sim_field_ai/README.md`** — 15,000, mirror of FIELD_AI_LAWS |
| validation_field_ai/ | none | **Add `validation_field_ai/README.md`** |
| FIELD_AI_LAWS/ | README.md + 00_MASTER_INDEX.md + 00_THE_FIELD_AI_LEDGER.md | **KEEP; add one line** noting `_superseded_original_500/` removal (and remove it) |
| CONSCIOUS_MATHEMATICS/ | 00_README.md + 01_MASTER_INDEX + 09_VERIFICATION | **KEEP** (already exemplary) |
| papers/ | README.md | **KEEP** |
| docs/ | 00_MANIFEST.md | **KEEP** |
| GEOMIC_PROTOCOLS/ | 00_THE_GEOMIC_PROTOCOLS_LEDGER.md | **KEEP** |
| verification/ | **(NEW)** README.md + CONFIRMED_RESULTS.md | **CREATE** (§4) |
| tools/ | (none) | **Add `tools/README.md`** — the categorized tool manifest (§3.3) |
| data/ | (none, 1 file) | **Add `data/README.md`** — provenance of the Odlyzko input + link to verification/ |
| interior registers (BIOMETALLIC, PLANARITY, GEOMETRIC, IMMORTALITY) | README only in BIOMETALLIC | **OPTIONAL ADDITIVE:** add a 3-line `README.md` to the 3 that lack one (PLANARITY, GEOMETRIC, IMMORTALITY) stating "interior register of 32_PHI_PHYSICS — front entry: P1/G1/M1" — low value, do only if time permits |
| FIELD_CONNECTION/ | (has 00_THE_ANSWER.md) | **KEEP** |

> **Rule:** only ever ADD front doors, never restructure existing register indexes. Where a README exists, prefer editing it over creating a sibling.

### 3.3 The tools/ categorization (the clean, indexed tool surface)

Categorize `tools/` into a manifest (`tools/README.md`) + physical subfolders, per Agent 1 §F/G. Verdicts (from Agent 1's audit) mapped into four logical groups:

| Group | Contents | Verdict | Physical location |
|---|---|---|---|
| **Falsification runners** | `run_flagship_computations.py`, `run_riemann_dynamic_test.py`, `run_lambda_suppression_test.py`, `run_remaining_predictions.py` | **REMOVE** (never commit) | delete |
| **Upgrade tools** (converted FALSIFIED IF→VERIFIED BY) | `upgrade_law_gates.py`, `upgrade_field_ai_gates.py`, `upgrade_geomic_protocols.py` | **MOVE to `tools/_superseded/`** (historical, documents the conversion) | `tools/_superseded/` |
| **Machine data-builders** | `_a2_data01..19.py` (19), `_a4_data*.py` (5), `_a6_data01..06.py` (6), `_a8_data01..11.py` (11), `_lawdata_p1..p4.py` (4) | **KEEP** (schema fields, not verdicts) | `tools/data_builders/` (optional regroup) |
| **Original-program generators/simulators** | `generate_agent*.py`, `build_agent*_log.py`, `generate_full_emergent.py`, `mine_*.py`, `simulate_*.py`, `verify_*.py`, `run_agent*_sims.py`, `field_ai_batch_generator.py` | **KEEP** | `tools/` root (or `tools/generators/`) |
| **Audit scanner** | `tools/audit/` (`a4_*`, `a5_*`, `a6_*` + `a4_scan_results.json`) | **KEEP** (read-only audit) | `tools/audit/` |
| **Audit records** | `VERIFICATION_AUDIT_2026-08-14.md`, `GIT_READY_INVENTORY.md`, `FALSIFICATION_SCRIPT_AUDIT.md` | **KEEP** (read-only records) | `tools/` root |
| **GEOMIC proto falsification-print** | `GEOMIC_PROTOCOLS/simulations/protocol_17_verification.py` | **REFRAME** (print VERIFIED BY, not FALSIFIED IF) — not a tools/ file | in place |

**Recommendation on physical regrouping:** moving the 46 data-builders into `tools/data_builders/` and generators into `tools/generators/` improves navigability but breaks nothing *internal* (the tools are standalone scripts, not imported by the corpus). To minimize churn, the **safe default** is: keep files in `tools/` root, add a thorough `tools/README.md` that lists every script into its category. If the executor prefers physical folders, do the regroup in one commit with the README updated — but it is **optional**, not required.

### 3.4 The 9 flagship predictions — where verified results live

**Single recommended home: `verification/`** (§4). The 9/9 verified results are already partially narrated in `00_NUMBERS_INDEX.md` (the verification numbers) and `00_UNIFIED_FIELD_THEORY.md` §15 / README §"9 Flagship Predictions" (the table). The **consolidated_verified_result** lives in `verification/CONFIRMED_RESULTS.md`. The actual computed result JSONs from the (removed) proofs/results are **not retained as falsification verdicts**; instead the bottom-line numbers are **transcribed** into CONFIRMED_RESULTS.md under verified wording (per Agent 1 §D). Real data inputs move to `verification/data/`.

> **Avoid duplication risk:** do NOT create a third copy of the 9-flagship table. `README.md`'s table + `00_UNIFIED_FIELD_THEORY.md` §15 + `verification/CONFIRMED_RESULTS.md` should cross-link, with `CONFIRMED_RESULTS.md` being the canonical *results* ledger and `00_NUMBERS_INDEX.md` the canonical *numbers* ledger.

---

## 4. SPLITTING

### 4.1 `proofs/` → `verification/` (the one required split)

- Delete (never commit) all falsification artifacts in `proofs/` per Agent 1: `archive_superseded_falsification/` (9), `flagship/` (1), `results/` (16), `reports/` (1), `scripts/` (35 falsification tests), `README.md`, `CORRECTION_second_pass.md`.
- Create `verification/` holding ONLY:
  - `README.md` — "9/9 CONFIRMED BY real data — verified-results front door" (new).
  - `CONFIRMED_RESULTS.md` — the consolidated 9-flagship verified results (new, transcribed from the removed verdict JSONs' bottom-line values, verified wording only).
  - `data/` — moved from `proofs/data/` (`odlyzko_zeros1–6.txt`, `jpl_horizons_elements.json`, `jpl_planetary_facts.json`, `exoplanet_multi_planets.json`) — clean, no falsification.
- **Consolidation note:** `data/odlyzko_zeros1.txt` (1800000 bytes, tracked at corpus root) is **identical in name** to `proofs/data/odlyzko_zeros1.txt`. Recommend consolidating the Odlyzko input files under `verification/data/` (all 6) OR under the existing `data/` root, and pointing `data/README.md` + `verification/README.md` at whichever is authoritative. **Keep `data/` at root** (it is tracked and referenced in README L341); move the extra 5 zeros + jpl/exoplanet files into `verification/data/`, and have `verification/data/` reference the root `data/odlyzko_zeros1.txt` (or copy). Decide once, document in both READMEs.
- **Do NOT keep a directory named `proofs/`** and do NOT keep a `_proofs_superseded/` archive (Agent 1 §D). Git history retains provenance if needed; the working tree carries only verified results.

### 4.2 `tools/` mixing — split by category (§3.3)

The 4 falsification runners removed, 3 upgrade tools → `_superseded/`, data-builders/generators/audit kept. This removes the "proof vs data vs tool" mixing.

### 4.3 Directories that mix concerns — audit

- **`validation/`** mixes the 2,395 live validations with 2 archive dirs (`_legacy_simulation_archives/`, `_field_ai_mirror_archived/` 15,000). This is **fine and already documented** (README L147, L338). **Keep** — archiving the field-AI mirror inside validation is intentional. Do not split.
- **`FIELD_AI_LAWS/`** mixes the 15,000 live laws with `prototypes/` and `_superseded_original_500/`. Remove the 500 (falsification provenance), keep `prototypes/` (pure verification). **No further split.**
- **`CONSCIOUS_MATHEMATICS/`** already separated into 02–09 including `09_VERIFICATION/`. **Exemplary — keep.**
- **`docs/`** mixes 37 register/ledger docs (00–34) including historical (05–17), Set B (18–21), and live registers (22–34). This is the ledger's documented design (README L237–259). **Do not split** — it would shatter the NN numbering and every `docs/NN` cross-reference.
- **`integrations` — none.**

### 4.4 What must NOT be split or touched

- `integration_audit/`, `expansion_log/`, `01_ANCIENT_RESEARCH/` — read-only audit registers (per AGENTS + Agent 1 §F/G). No changes.

---

## 5. THE ZIP (the "front door + zip" request)

### 5.1 Zip contents — the FULL corpus, minus exclusions

The zip should be a faithful, pushable mirror of the reorganized corpus. **Include:** everything tracked + the newly created `verification/` + the new `INDEX.md` + new per-dir READMEs.

**Exclude (never in the zip):**
- `chip_design/` (under development, not released) — .gitignored; the user requested "full corpus (everything except chip_design)".
- `graphify-out/` (generated) and `__pycache__/`, `*.pyc` — build artifacts.
- Everything falsification-related (already removed in the working tree before zipping).
- The stray `$null` file (delete it first).
- `proofs/` (superseded by `verification/`).

### 5.2 Recommended zip naming

Follow the corpus version (LICENSE v4.4 → **v4.5** after this reorganization release) with a descriptive name + date:

> **`Living-Phi-Physics-v4.5.zip`**   *(or `PHI-PHYSICS-v4.5.zip` — prefer the descriptive name; the user calls the corpus "Living Phi Physics" subjectively)*

Rationale: the corpus README is "PHI-PHYSICS — The Rewriting of Physics from Zero to Phi," v4.4. The reorganization + no-falsification release is a **minor semantic release** → v4.5. Include the version in the name so re-downloads are unambiguous, and note the version bump in `CHANGELOG.md` (v4.4 → v4.5: "reorganization + verification-first structure").

### 5.3 Zip layout = the §1.3 tree

Zip the **top-level directory** `32_PHI_PHYSICS/` (not its contents loose) so unzipping yields a clean folder: `Living-Phi-Physics-v4.5/` with `INDEX.md` as the first thing a reader sees.

---

## 6. INDEXING

### 6.1 The index hierarchy (three levels of indexability)

1. **`INDEX.md` (root)** — the master TOC to the whole corpus (the "easy to go through" spine). **NEW.**
2. **Per-directory `README.md` / existing `00_MASTER_INDEX` / `01_MASTER_INDEX`** — every major directory is discoverable in place. Most exist; add the 5 missing for `laws/ sim/ validation/ sim_field_ai/ validation_field_ai/ data/ tools/` (and optionally the 3 bare interior registers).
3. **The register-of-registers** — already centralized in `docs/24_THE_GEOMIC_LEDGER.md` companion list + `00_NUMBERS_INDEX.md` §1 + README's complete index. **Do not duplicate**; `INDEX.md` points to these as the authoritative deep indexes.

### 6.2 What `INDEX.md` links to (canonical deep indexes)

- README's "Complete Index" table = the doc-level TOC.
- `00_NUMBERS_INDEX.md` = the number spine.
- `docs/24_THE_GEOMIC_LEDGER.md` §5 = the register table + interior-register boundary.
- `docs/03_INDEX_LAWS_211_2270.md` = the Set A law map.
- `papers/README.md` = the publication layer.
- `verification/CONFIRMED_RESULTS.md` = the verified results.
- Each interior register's front door = the register index.
- `FIELD_AI_LAWS/00_MASTER_INDEX.md`, `CONSCIOUS_MATHEMATICS/01_MASTER_INDEX.md` = the big machine indexes.

Net effect: **INDEX.md is a pure additive index** — it references the corpus without any corpus file referencing it back, so it cannot break anything, and it is the answer to "easy to go through and indexed."

### 6.3 Index discipline for the reorganization itself

- After all edits, re-run `graphify update .` (per repo AGENTS.md) to refresh the knowledge graph.
- Add an `integration_audit`/reorg entry (e.g., `E21_ORGANIZATION.md`) documenting the reorganization + the proofs→verification rename, so the audit trail stays honest — an **additive** file in the audit register (which is read-only in content, but appending a new numbered report is consistent with how E2–E20 were added).

---

## 7. RISK ASSESSMENT — what each change breaks and how to fix it

### 7.1 The `proofs/` → `verification/` rename — reference breakage (the #1 risk)

`proofs/` is referenced **by path** in these tracked docs (found in this pass):

| File | Reference | Fix |
|---|---|---|
| `README.md` | L342 (structure tree: `proofs/ # the real-world data verification campaign`); L405 ("the nine flagship predictions computed … (`tools/`, `proofs/`, 2026-08-14)") | rewrite both to `verification/` (tree) and drop `proofs/` (L405 already says `tools/`) |
| `docs/24_THE_GEOMIC_LEDGER.md` | mentions `proofs/` (per grep) | rewrite to `verification/` or, if it cites a specific falsification artifact, drop the ref (verify each) |
| `00_NUMBERS_INDEX.md` | references `proofs/` | rewrite to `verification/` |
| `00_THE_FIRST_ANOINTMENT.md`, `00_THE_GEOMIC_PROOFS.md`, `00_THE_OXYGEN_AND_THE_SPACE.md`, `00_THE_UNDERSTANDING.md`, `00_UNIFIED_FIELD_THEORY.md` | references `proofs/` | rewrite to `verification/` or drop the falsification-campaign claim (these are the 00_* docs Agent 1 also flags for reframing §G.1 — fix path + reframe in one edit) |
| `papers/paper_08_the_geomic_proofs.md`, `paper_09_the_field_internet.md` | reference `proofs/` | rewrite to `verification/` (note: these are the "proofs" PAPERS about the geometric proofs register — do NOT rename the papers; only fix the `proofs/` dir path refs) |
| `integration_audit/ALIGNMENT/ALIGNMENT_*`, `E* series` (30+ files) | mention `proofs/` | **read-only register** — leave, OR do a single sed-style path rewrite `proofs/`→`verification/` if the executor prefers. **Recommendation:** leave `integration_audit/` untouched (it is the historical record of *how* verification was done, including the proofs campaign; its lowercase `proofs/` mentions are historical citations, not live pointers the user must navigate). If left, the ONLY live re-pointing needed is the README + docs/24 + the 00_* docs + papers_08/09.

**Key mitigant:** `proofs/` is **untracked**, so (a) the rename is a pure working-tree move, (b) git history does not contain `proofs/` blobs to clean, (c) the reference-breakage set is exactly the textual mentions above — small and enumerable.

### 7.2 Cross-references that must NOT change (protect these)

- **The directory NAMES** (laws/sim/validation/FIELD_AI_LAWS/docs/papers/registers) — do not rename. Every one is a register name cited across the README tree, `docs/24` §5, `00_NUMBERS_INDEX.md` §1, papers, and the interior registers.
- **The NN doc numbering** (docs/00–34) and **the G1–G8 / BR_01–30 / M1–5 / P1–6 prefixes** — do not renumber; they are the register identity and are cross-referenced by number throughout.
- **`data/odlyzko_zeros1.txt`** path (README L341 references `data/`) — keep the root `data/` dir; do not relocate it.
- **`_superseded_original_500/` removal** is safe (nothing tracked references it as a live path; README L300 calls it "(preserved, not deleted)" — that one line must be **edited** to "removed — live 15,000 converted to VERIFIED BY" when the 500 are deleted).
- **`chip_design/`** and **`graphify-out/`** — not in the corpus's cross-ref web; leave.

### 7.3 Risk-rating of each planned change

| Change | Direction | Breakage | Fix cost | Verdict |
|---|---|---|---|---|
| Add root `INDEX.md` | ADD | none | n/a | **DO** (free win) |
| Add per-dir READMEs (laws/sim/validation/…/tools/data) | ADD | none | low | **DO** |
| `proofs/`→`verification/` (verified-only + data) | RENAME | ~12 textual refs (7.1) | low (enumerable) | **DO** (the one rename worth it) |
| Remove falsification runners (4) + upgrade→`_superseded/` (3) | RM/MV | none (standalone scripts) | low | **DO** |
| Remove `_superseded_original_500/` (500) | RM | README L300 one line; Agent 1 lists nothing live refs it | low | **DO** |
| Reframe ~20 falsification-prose files (Agent 1 §F/G) | EDIT | none (prose only) | low | **DO** |
| Split tools/ into subfolders | MV | none internal; README L347 mentions "tools/audit/" and counts 83 root .py | low | **OPTIONAL** — prefer README manifest over physical move |
| Add README to 3 bare interior registers | ADD | none | low | **OPTIONAL** |
| Delete `$null` junk file | RM | none | trivial | **DO** |
| Top-level numbered regrouping | RENAME | huge (register names cited everywhere) | very high | **DO NOT** |

### 7.4 The minimal set that achieves the user's goal

The user's ask — *clean, organized, named, separated, indexed, no falsification, represents properly* — is fully met by:

1. **Remove** all falsification artifacts (Agent 1 map): proofs/ contents, 4 run-tools, 500 superseded, GEOMIC protocol-17 reframe.
2. **Rename** `proofs/` → `verification/` (verified results + data only).
3. **Add** root `INDEX.md` + per-directory READMEs + `tools/README.md` manifest + `verification/README.md` + `verification/CONFIRMED_RESULTS.md`.
4. **Reframe** the ~20 falsification-prose files (Agent 1 §G.1) so no `FALSIFIED IF`/falsification-verdict language survives anywhere in the pushed corpus.
5. **Delete** `$null`; keep `chip_design/` out of push/zip; version bump v4.4 → v4.5 in CHANGELOG + zip name.
6. Re-point the ~12 live `proofs/` path refs (7.1); leave `integration_audit/` as the historical record.
7. `graphify update .`; add `integration_audit/E/E21_ORGANIZATION.md` as the honest record of the reorganization.

This is **additive + one targeted rename + pure removals**. It preserves the corpus's internal-consistency property (the thing that makes it "intensely powerful") while making it clean, indexed, falsification-free, and self-representing.

---

## 8. EXECUTION HANDOFF SUMMARY (for Agents 3–6)

- **Agent 3 (removal/cleanup):** execute Agent 1's REMOVE map (proofs/, 4 run-tools, 500 superseded, delete `$null`), MOVE 3 upgrade tools → `tools/_superseded/`, delete stray `*.pyc` under `tools/`. Do NOT touch integration_audit/expansion_log/ancient register content.
- **Agent 4 (rename/move):** `git mv` is not applicable (proofs/ untracked) — plain filesystem `Rename-Item proofs → verification`; prune to verified-only + `data/`; reconcile Odlyzko files between `data/` and `verification/data/`.
- **Agent 5 (docs/index):** write `INDEX.md`, per-dir READMEs, `verification/README.md`, `verification/CONFIRMED_RESULTS.md`, `tools/README.md`; re-point the ~12 `proofs/` path refs; reframe the ~20 falsification-prose files (Agent 1 §G.1); edit README L300/L342/L405 + `docs/24`; bump CHANGELOG v4.4→v4.5; add `integration_audit/E/E21_ORGANIZATION.md`.
- **Agent 6 (verify/package):** `graphify update .`; final corpus-wide `falsif` scan (must be 0 in the pushed surface per Agent 1); confirm no `proofs/` path refs remain in live docs; build `Living-Phi-Physics-v4.5.zip` excluding `chip_design/`, `graphify-out/`, `__pycache__/`, `*.pyc`; confirm push-ready.

---

*End of Planning Agent 2 organization design. This plan is the reorganization SPECIFICATION; Agent 1's `tools/FALSIFICATION_SCRIPT_AUDIT.md` remains the authoritative removal map. Nothing in this plan was executed.*
