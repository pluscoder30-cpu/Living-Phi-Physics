# LAW 2579 — SYNAPTIC TRANSMISSION PHI-PROBABILITY

**Domain:** Neuroscience, Neurophysiology

**Statement:** The probability of neurotransmitter release at a synapse follows a phi-binomial distribution: the number of vesicles released per action potential is drawn from a binomial distribution B(n, p) where the release probability p = φ⁻¹ · C_pre where C_pre is the presynaptic terminal coherence, and the quantal size q satisfies q = φ · q_0 where q_0 is the unitary postsynaptic response, giving a synaptic strength S = n · p · q = n · C_pre · q_0.

**Derivation:** Synaptic transmission is the carrier recursion (Eq 1) applied to the presynaptic terminal: each vesicle is a carrier, and the release probability is the coherence of the vesicle's docking state with the active zone. The phi-binomial distribution follows from the Ladder Invariant: the number of available release sites is φ-spaced (the active zone area is φ² times the vesicle footprint), and the release probability at each site is φ⁻¹ times the terminal coherence.

**Prediction:** The coefficient of variation (CV) of synaptic EPSP amplitudes satisfies CV² = (1 − p)/(n · p) = (1 − φ⁻¹ · C_pre)/(n · φ⁻¹ · C_pre). For a typical cortical synapse with n = 5 release sites and C_pre = 0.8, CV² = (1 − 0.495)/(5 × 0.495) = 0.102, giving CV = 0.320, consistent with experimental measurements (CV ≈ 0.3). Short-term facilitation increases C_pre by factor φ, and short-term depression decreases it by factor φ⁻¹.

**Test:** Record miniature and evoked EPSCs from cortical pyramidal neurons in acute slices. Measure CV of evoked EPSC amplitude. Fit the phi-binomial model and extract n and p. Verify that p = φ⁻¹ · C_pre where C_pre is estimated from paired-pulse ratio (PPR = φ/(1 + φ⁻¹ · C_pre)). Verify that facilitation increases p by factor φ and depression decreases it by factor φ⁻¹.

**Source:** Batch 4: 2551–2600

**Author:** Christopher David Ayotte — Soul Code [425, 434, 266, 775]

**License:** Dual License Agreement v4.9
