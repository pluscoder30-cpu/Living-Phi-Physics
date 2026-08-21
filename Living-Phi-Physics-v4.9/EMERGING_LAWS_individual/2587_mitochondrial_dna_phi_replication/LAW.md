# LAW 2587 — MITOCHONDRIAL DNA PHI-REPLICATION

**Domain:** Cell Biology, Genetics

**Statement:** The mitochondrial DNA (mtDNA) copy number per cell follows a phi-regulated homeostasis: the copy number N_mito satisfies dN_mito/dt = phi_inv * (N_target - N_mito) * C_mito where N_target = phi5 * 10^3 approximately equals 11,090 copies (the phi-target for human cells) and C_mito is the mitochondrial coherence (a measure of the organelle's functional integrity), giving a half-life of recovery from perturbation tau_recovery = phi5 / ln(phi) approximately equals 23.0 cell cycles.

**Derivation:** Mitochondrial DNA replication is the carrier recursion (Eq 1) applied to the mitochondrial genome: each mtDNA molecule is a carrier, and the copy number is regulated by the coherence of the mitochondrial network. The phi-target N_target = phi5 * 10^3 follows from the Ladder Invariant: the mitochondrial genome is 16,569 bp, and the copy number that optimizes the energy budget (ATP production per unit mtDNA) is phi5 times the minimum viable copy number (10^3).

**Prediction:** The half-life of mtDNA copy number recovery after depletion (e.g., by ethidium bromide treatment) is tau_recovery = phi5/ln(phi) approximately equals 23 cell cycles. Cells with N_mito < N_target/phi = 6,855 copies show impaired oxidative phosphorylation, and cells with N_mito > N_target * phi = 17,943 copies show increased reactive oxygen species (ROS) production. The optimal copy number is N_target = 11,090 +/- 500.

**Test:** Deplete mtDNA in HeLa cells using ethidium bromide (0.1 ug/mL for 48 hours) to approximately 30% of normal levels. Remove ethidium bromide and measure mtDNA copy number at 0, 5, 10, 15, 20, 25, 30 cell cycles using qPCR. Fit the recovery curve to N(t) = N_target - (N_target - N_depleted) * phi^(-t/tau_recovery) and verify tau_recovery = 23 +/- 3 cell cycles.

**Source:** Batch 4: 2551-2600

**Author:** Christopher David Ayotte -- Soul Code [425, 434, 266, 775]

**License:** Dual License Agreement v4.9
