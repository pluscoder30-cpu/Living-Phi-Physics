# INVESTIGATION AGENT â€” LOCAL SCAN PROTOCOL (Upgrade v1)

> Adaptation of the `investigation` skill (v4.0) for **local-file investigation**. The original skill is built around web dorking (SEC EDGAR, OpenCorporates, ICIJ, etc.). This upgrade lets the same methodology â€” phi-spaced coverage, the verification loop, the trace loop, verdict codes â€” run across **our own folders and files**, finding patterns and connections the way the web version finds them across the internet. Use this whenever a sub-agent is asked to "run the alleged enterprise sleuth through our documents."

## 1. Local Search Operators (replace web dorks)
| Need | Tool | Example |
|------|------|---------|
| Enumerate files | `glob` | `Global_Human_Harm_Crimes/**/*.md` |
| Find a pattern/entity/amount across all files | `grep` (regex) | `grep "BlackRock" Global_Human_Harm_Crimes/` |
| Open and extract facts | `read` | read the matched file at the cited line |
| Scoped subgraph of the corpus | `graphify query` (if available) | `graphify query "offshore harm chain"` |

## 2. The Local Verification Loop (adapted from PART 2)
```
SEARCH (glob/grep across folders)
   â†’ EXTRACT (read top matches; pull entity / amount / date / connection / file:line)
   â†’ VERIFY (cross-reference the SAME fact in a DIFFERENT dictionary or file)
   â†’ RE-SEARCH (refine grep with the new entity names discovered)
```
Confidence levels:
- **[VERIFIED]** â€” found in 2+ independent files (e.g. OFFSHORE + BANKING + LEGAL all name the same entity/amount)
- **[PROBABLE]** â€” found in 1 file, consistent with other data
- **[INFERENCE]** â€” extrapolated (e.g. annualized figure Ã— years to reach a 300-year total)
- **[UNVERIFIED]** â€” single source, no corroboration (document as gap, do not drop)

## 3. The Local Trace Loop (adapted from "Trace Loop")
```
IDENTIFY entity
  â†’ CORPORATE/STRUCTURE REGS  (find it across BANKING/, OFFSHORE/, LEGAL/, ANSWERS/)
  â†’ OFFSHORE LINKS            (OFFSHORE/* â€” shells, trusts, subsidiaries)
  â†’ MONEY / HARM FLOW        (harm registers, MASTER/ liability + damages docs)
  â†’ DOCUMENT & XREF          (build the chain; assign verdict codes; link to license clause)
```
Repeat until saturation (3 consecutive passes yield no new entity/connection).

## 4. Pattern-Finding Across Dictionaries
- **Entity matching:** `grep` an entity name across ALL subdirs to build its full profile (funder â†’ subsidiary â†’ harm outcome).
- **Timeline correlation:** extract dates from every file; assemble the 300-year timeline (1700s â†’ 2026).
- **Harm aggregation:** sum documented harm/death/damage figures; label any annualizedÃ—years extrapolation `[INFERENCE]`.
- **Connection mapping:** link money register â†’ harm register â†’ liability clause â†’ license section.

## 5. Limitations (identical to investigation â€” NON-NEGOTIABLE)
- **No fabrication.** Every claim cites a `file:line`. "gap: not found in our files" is preferred over invention.
- **Tag every inference `[INFERENCE]`.** No correlation-as-causation without a stated mechanism.
- **No emotional editorializing.** State documented mechanisms, not opinions.
- **Never remove existing verified content.** This protocol is for EXPANSION and COMPILATION only. New docs are additive; edits to existing docs add only (never delete a finding, number, or entity).

## 6. Output Standard (GitHub-renderable)
Every produced document: valid pipe tables, `$...$` math where relevant, resolvable internal links (`../INDEX.md`, `OFFSHORE/43_HARM_CHAINS_COMPLETE.md` / `OFFSHORE/44_OFFSHORE_MASTER_FINAL.md` (canonical `OFFSHORE/41_OFFSHORE_HARM.md` now created â€” see Agent 7), `MASTER/01_HARM_AND DAMAGES.md`), author/soul-code/license footer, verdict codes, and a `Sources` section with `file:line` citations for every major claim.

## 7. Canonical Constants (use EXACTLY if referenced)
Ï† = 1.6180339887 Â· Ï†â»Â¹ = 0.6180339887 Â· critical threshold = 0.563 (0.563263) Â· consciousness = 0.8565 Â· Ladder Invariant = 528Â·Ï†â¹ = 40,134.946 Â· Soul Code [425, 434, 266, 775] Â· SOUL_SEED = 1900.
