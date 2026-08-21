# LAW 2588 — GENE EXPRESSION PHI-NOISE

**Domain:** Molecular Biology, Systems Biology

**Statement:** The intrinsic noise in gene expression (the cell-to-cell variability in protein levels for identically regulated genes) follows a phi-distribution: the coefficient of variation squared CV2 = sigma2/mu2 equals phi_inv = 0.618 for a single-copy gene in a single cell, and for a gene with n copies, CV2 = phi_inv/n, giving the fundamental noise floor of gene expression as phi_inv per gene copy.

**Derivation:** Gene expression noise is the carrier recursion's stochastic fluctuations: each mRNA molecule is a carrier, and the noise arises from the discrete nature of transcription and translation. The phi-noise follows from the Ladder Invariant: the product of noise amplitude (frequency analog) and gene copy number (depth analog) is conserved at phi_inv, giving CV2 = phi_inv/n. The phi-factor (rather than the classical 1/n for Poisson noise) arises because gene expression is not a Poisson process but a phi-coherent process with correlations between transcription events.

**Prediction:** Single-cell protein measurements (using flow cytometry or smFISH) will show CV2 = 0.618/n for genes with n copies, rather than the classical Poisson prediction CV2 = 1/n. For a single-copy gene (n = 1), CV2 = 0.618, and for a two-copy gene (n = 2), CV2 = 0.309. The phi-noise predicts that gene expression is inherently noisier than Poisson, with the excess noise factor = phi.

**Test:** Measure protein levels of a single-copy fluorescent reporter gene (e.g., GFP integrated at a single locus) in 10,000 individual E. coli cells using flow cytometry. Compute the mean and variance of fluorescence. Verify CV2 = 0.618 +/- 0.05. Repeat for a two-copy reporter and verify CV2 = 0.309 +/- 0.03. Compare with the Poisson prediction (CV2 = 1/n) and show the phi-correction is significant.

**Source:** Batch 4: 2551-2600

**Author:** Christopher David Ayotte -- Soul Code [425, 434, 266, 775]

**License:** Dual License Agreement v4.9
