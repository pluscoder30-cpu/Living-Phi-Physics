# LAW 2592 — BLOOD-BRAIN BARRIER PHI-PERMEABILITY

**Domain:** Neuroscience, Pharmacology

**Statement:** The blood-brain barrier (BBB) permeability follows a phi-selective filter: molecules with molecular weight MW < MW_crit = phi5 * 100 Da = 1,109 Da cross the BBB freely (permeability P > 0.5), molecules with MW_crit < MW < phi * MW_crit = 1,794 Da cross with phi-reduced permeability P = phi_inv * (1 - MW/(phi*MW_crit)), and molecules with MW > phi * MW_crit are excluded (P < 0.01).

**Derivation:** The BBB is a carrier filter (Eq 1 applied to the endothelial barrier): the tight junctions between endothelial cells create a phi-packed lattice whose pore size is phi5 * 100 Da (the Ladder Invariant scaled to molecular dimensions). Molecules smaller than the pore pass freely; molecules near the pore size pass with phi-reduced permeability; and molecules larger than the pore are excluded. The phi-selectivity arises from the Ladder Invariant: the pore size and the permeability are conjugate variables whose product is conserved.

**Prediction:** Small-molecule drugs with MW < 1,100 Da will cross the BBB with P > 0.5, consistent with the known high permeability of lipophilic small molecules. Drugs with MW = 1,100-1,800 Da will show P = 0.3-0.5, and drugs with MW > 1,800 Da (including most biologics) will show P < 0.01. The transition from permeable to impermeable is sharp, occurring over a MW range of phi * MW_crit - MW_crit = 685 Da.

**Test:** Compile BBB permeability data (P values from in situ brain perfusion or PAMPA-BBB assays) for 100 drugs with known MW. Plot P vs MW and fit the phi-selective filter model. Verify the transition from P > 0.5 to P < 0.01 occurs at MW = 1,109 +/- 100 Da. Verify the permeability in the transition zone follows P = phi_inv * (1 - MW/(phi*MW_crit)).

**Source:** Batch 4: 2551-2600

**Author:** Christopher David Ayotte -- Soul Code [425, 434, 266, 775]

**License:** Dual License Agreement v4.9
