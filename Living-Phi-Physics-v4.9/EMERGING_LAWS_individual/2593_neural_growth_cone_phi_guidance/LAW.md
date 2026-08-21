# LAW 2593 — NEURAL GROWTH CONE PHI-GUIDANCE

**Domain:** Neuroscience, Developmental Biology

**Statement:** The growth cone of a developing axon navigates using a phi-weighted averaging of guidance cues: the turning angle theta of the growth cone in response to a guidance cue (attractant or repellent) satisfies tan(theta) = phi_inv * (C_attract - C_repel) / (C_attract + C_repel) where C_attract and C_repel are the concentrations of attractant and repellent at the growth cone, and the maximum turning angle is theta_max = phi_inv * 90 degrees = 55.6 degrees.

**Derivation:** The growth cone is a carrier navigator (Eq 1 applied to the axon tip): its steering is the carrier recursion's direction update, and guidance cues are the coherence gradients that bias the recursion. The phi-weighting arises from the Ladder Invariant: the growth cone's response is optimized when the attractant and repellent signals are weighted by the golden section. The maximum turning angle theta_max = phi_inv * 90 degrees follows from the constraint that the growth cone cannot turn faster than the phi-rate.

**Prediction:** In a choice assay with equal concentrations of attractant (netrin-1) and repellent (Slit2), the growth cone will turn toward the attractant. The prediction is that the growth cone's turning angle scales linearly with the concentration ratio C_attract/C_repel, with slope phi_inv.

**Test:** Perform growth cone turning assays with dorsal root ganglion neurons on a choice assay with graded netrin-1 (attractant) and Slit2 (repellent). Measure turning angles for 10 concentration ratios (C_attract/C_repel = 0.5, 1, 2, 3, 5, 8, 10, 20, 50, 100). Plot tan(theta) vs (C_attract - C_repel)/(C_attract + C_repel) and verify slope = phi_inv = 0.618 +/- 0.05.

**Source:** Batch 4: 2551-2600

**Author:** Christopher David Ayotte -- Soul Code [425, 434, 266, 775]

**License:** Dual License Agreement v4.9
