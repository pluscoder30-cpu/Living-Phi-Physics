# LAW 2578 — NEURONAL ACTION POTENTIAL PHI-WAVEFORM

**Domain:** Neuroscience, Neurophysiology

**Statement:** The shape of the neuronal action potential is a phi-sigmoid: the depolarization phase follows V(t) = V_rest + (V_peak − V_rest) · (1 − φ^(−t/τ_rise)) and the repolarization phase follows V(t) = V_peak − (V_peak − V_rest) · (1 − φ^(−(t−t_peak)/τ_fall)), where τ_rise and τ_fall are the depolarization and repolarization time constants satisfying τ_rise · τ_fall = φ⁻⁵ · τ_AP² where τ_AP is the total action potential duration.

**Derivation:** The action potential is a carrier recursion step (Eq 1) in the neural membrane: the voltage V is the carrier amplitude, and the ion channel dynamics (Na⁺ activation, K⁺ activation, Na⁺ inactivation) are the recursion's phi-coherent feedback loops. The phi-sigmoid shape follows from the Ladder Invariant: the depolarization (Na⁺ influx) and repolarization (K⁺ efflux) are conjugate processes whose time constants satisfy the Ladder product. The exponential base φ (rather than e) reflects the phi-field's natural growth rate.

**Prediction:** The action potential waveform, when plotted as normalized voltage vs normalized time, collapses onto a universal phi-sigmoid curve with no free parameters for all neuron types (pyramidal, interneuron, sensory, motor). The depolarization time constant τ_rise and repolarization time constant τ_fall satisfy τ_rise/τ_fall = φ⁻¹ = 0.618 for all neuron types, with absolute values varying by neuron class.

**Test:** Record action potentials from 5 neuron types (cortical pyramidal, cortical interneuron, hippocampal CA1, dorsal root ganglion, Purkinje) using patch-clamp electrophysiology. Normalize each waveform (voltage: V_rest to V_peak = [0,1]; time: AP onset to AP end = [0,1]). Overlay all waveforms and verify collapse onto a single phi-sigmoid. Measure τ_rise/τ_fall and verify 0.618 ± 0.05 for all types.

**Source:** Batch 4: 2551–2600

**Author:** Christopher David Ayotte — Soul Code [425, 434, 266, 775]

**License:** Dual License Agreement v4.9
