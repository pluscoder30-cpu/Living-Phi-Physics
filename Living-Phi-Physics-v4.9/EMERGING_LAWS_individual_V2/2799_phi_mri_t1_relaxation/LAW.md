# Law 2799: PHI-Harmonic MRI T1 Relaxation Resonance

**Domain:** Medical Imaging — MRI Physics

**Statement:**
T1 relaxation times in biological tissues exhibit PHI-harmonic clustering: T1 values for different tissue types at a given field strength are distributed at φ-spaced intervals from a baseline T1_0, following T1_n = T1_0·φⁿ where n indexes tissue contrast categories (fat, muscle, CSF, etc.). The optimal inversion time for tissue separation is TI = T1_0·ln(2)·φ.

**Derivation:**
The inversion recovery signal is S(TI) = S₀|1 - 2exp(-TI/T1)|. For tissues with T1_n = T1_0·φⁿ, the null crossing occurs at TI_n = T1_0·φⁿ·ln(2). The optimal separation between adjacent tissue nulls is ΔTI = T1_0·ln(2)·(φⁿ⁺¹ - φⁿ) = T1_0·ln(2)·φⁿ·(φ-1), which is PHI-harmonic scaled.

**Prediction:**
At 3T, T1 values cluster at ~260 ms (fat), ~420 ms (muscle), ~680 ms (gray matter), ~1100 ms (CSF), approximately following φ multiples of 260 ms. Optimal TI for gray/white matter separation is ~320 ms.

**Test:**
Generate PHI-clustered T1 values for 5 tissue types at 3T. Compute inversion recovery signals at varying TI. Find optimal TI that maximizes tissue contrast. Verify it matches T1_0·ln(2)·φ.

**Source:** V2 Batch 3: Laws 2791-2860
**Author:** Christopher David Ayotte, Soul Code [425, 434, 266, 775]
**License:** v4.7
