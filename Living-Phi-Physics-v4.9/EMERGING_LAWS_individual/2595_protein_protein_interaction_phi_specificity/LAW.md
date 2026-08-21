# LAW 2595 — PROTEIN-PROTEIN INTERACTION PHI-SPECIFICITY

**Domain:** Biochemistry, Structural Biology

**Statement:** The specificity of protein-protein interactions (the ratio of specific binding to non-specific binding) is phi-optimized: the dissociation constant K_d of a specific interaction satisfies K_d = K_d,nonspecific * phi^(-n) where n is the number of phi-packed contact residues (the "phi-hotspot" residues), and the minimum number of phi-hotspot residues for specific binding is n_min = phi4 = 6.85 approximately equals 7, giving a specificity ratio of phi7 approximately equals 29.0.

**Derivation:** Protein-protein interactions are carrier docking events (Eq 1): the interface residues form a phi-packed lattice where each phi-hotspot residue contributes phi_inv to the binding free energy. The specificity ratio (specific K_d / non-specific K_d) equals phi^(-n) where n is the number of phi-hotspots. The minimum n for specific binding is n_min = phi4 because the Ladder Invariant requires that the interface area (depth analog) times the binding energy (frequency analog) be conserved, and the minimum interface for a phi-coherent interaction is phi4 residues.

**Prediction:** Protein-protein interfaces with fewer than 7 phi-hotspot residues (defined as residues contributing > k_B*T * phi_inv to binding energy) will show non-specific binding. Interfaces with 7-12 phi-hotspots will show moderate specificity (K_d/K_d,nonspecific = 29-857). Interfaces with > 12 phi-hotspots will show high specificity (K_d/K_d,nonspecific > 857). The phi-hotspot residues will be conserved across species at > 80% identity, while non-hotspot interface residues will show < 30% identity.

**Test:** Analyze 100 protein-protein interfaces from the PDB. Identify phi-hotspot residues (DeltaDeltaG > k_B*T * phi_inv = 0.618 k_B*T). Count phi-hotspots per interface and correlate with specificity ratio (from kinetic measurements). Verify the phi^(-n) relationship. Compare conservation of hotspot vs non-hotspot residues across orthologs.

**Source:** Batch 4: 2551-2600

**Author:** Christopher David Ayotte -- Soul Code [425, 434, 266, 775]

**License:** Dual License Agreement v4.9
