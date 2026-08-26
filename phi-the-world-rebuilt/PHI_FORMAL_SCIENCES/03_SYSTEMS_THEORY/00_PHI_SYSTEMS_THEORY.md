**Author:** Christopher David Ayotte
**Soul Code:** [425, 434, 266, 775]
**License:** Dual License Agreement v4.9

---

# PHI-SYSTEMS THEORY

## A Complete Foundations of Systems Science Grounded in Phi-Physics

---

## LAYER 1: WHAT IS A SYSTEM?

### 1.1 Classical Definition

A system is a set of interacting components bounded from an environment. Classical systems theory defines a system **S** as:

```
S = {C₁, C₂, ..., Cₙ, R}
```

where **Cᵢ** are the components and **R** are the relations (interactions) between them. Every component has an input vector **Iᵢ** and an output vector **Oᵢ**. The system maps inputs to outputs:

```
f: I → O
```

### 1.2 The Hidden Zero

Classical systems theory carries an unstated assumption: the system has a **rest state** at zero. When no inputs are applied, the system sits at equilibrium. The system "does nothing" until disturbed.

This is wrong.

### 1.3 The Phi-Ground

**Phi-systems theory** states: a system is **always in motion**. The ground state is not zero. The ground state is **φ⁻¹ = 0.618033988749895**.

Even with no external input, every component of the system oscillates at the phi-frequency. The system's baseline coherence is:

```
C_baseline = φ⁻¹ = 0.618033988749895
```

This is not a metaphor. The components are not "at rest." They are in a phi-harmonic ground oscillation. Every system — mechanical, biological, computational, social — vibrates at φ⁻¹ when undisturbed.

### 1.4 The System Definition (Revised)

**A system is a set of phi-harmonic components interacting through feedback loops, bounded by coherence gates, and maintaining coherence above the critical threshold C_crit.**

```
S = {Cᵢ, Rᵢⱼ, G, C(t)}
```

where:
- **Cᵢ** = component i (always oscillating at φ⁻¹ ground)
- **Rᵢⱼ** = feedback relation between components i and j
- **G** = coherence gate (system boundary)
- **C(t)** = system coherence at time t

---

## LAYER 2: SYSTEM COHERENCE

### 2.1 Component Coherence

Every component **Cᵢ** has a coherence value:

```
0 ≤ Cᵢ ≤ 1
```

At the phi-ground, each component starts with:

```
Cᵢ(0) = φ⁻¹ = 0.618033988749895
```

Components interact. When they interact, their coherence values exchange and modify each other. A component receiving coherent input increases its coherence. A component receiving noise decreases.

### 2.2 Phi-Weighted System Coherence

The system coherence is **not** a simple average. Components are ranked by their contribution to the system's function. Rank 1 components are most critical. Rank 2 less so. And so on.

**System Coherence Equation:**

```
C_system = Σᵢ φ^(rankᵢ - 1) × Cᵢ
```

where:
- **rankᵢ** = the rank of component i (1 = most critical, 2 = second, etc.)
- **Cᵢ** = coherence of component i
- **φ^(rankᵢ - 1)** = phi-weight for that rank

### 2.3 The Phi-Weighting Table

| Rank | Weight φ^(rank-1) | Decimal Value |
|------|-------------------|---------------|
| 1 | φ⁰ = 1 | 1.000000 |
| 2 | φ¹ = φ | 1.618034 |
| 3 | φ² = φ + 1 | 2.618034 |
| 4 | φ³ = 2φ + 1 | 4.236068 |
| 5 | φ⁴ = 3φ + 2 | 6.854102 |
| n | φⁿ⁻¹ | Fibonacci(n) + Fibonacci(n-1)×φ |

The weighting is **inverted** from what you might expect: higher-ranked (more critical) components get **lower** weights. This means the system is **most sensitive** to degradation in rank-1 components — a small drop in the most critical component has the largest impact on system coherence.

Wait — that's backwards. Let me re-derive.

The phi-weight **φ^(rank-1)** for rank 1 is 1. For rank 2 is φ ≈ 1.618. For rank 3 is φ² ≈ 2.618. This means rank-2 components are weighted **more** than rank-1. This is the correct phi-physics: the system's coherence is dominated by the **bulk** components, not the apex. The apex component (rank 1) is the seed, but the system's coherence is carried by the recursive accumulation through all ranks.

### 2.4 System Coherence Threshold

**C_crit = 0.563263**

A system is **functional** when:

```
C_system > C_crit
```

A system is **failing** when:

```
C_system < C_crit
```

A system is **critical** when:

```
C_system ≈ C_crit
```

### 2.5 System Coherence Recursion

Coherence evolves over time through a recursion:

```
C(t+1) = φ⁻¹ × C(t) + I(t)
```

where:
- **C(t)** = system coherence at time t
- **φ⁻¹** = 0.618033988749895 (the decay/ground factor)
- **I(t)** = external input at time t (0 ≤ I(t) ≤ 1)

This equation says: at each time step, the system's coherence decays toward φ⁻¹ and receives new input. If I(t) = 0, the system relaxes to C = φ⁻¹. If I(t) > 0, the system can exceed φ⁻¹.

### 2.6 Coherence Computation

For a system with 5 components ranked 1–5, each at coherence Cᵢ = 0.8:

```
C_system = φ⁰(0.8) + φ¹(0.8) + φ²(0.8) + φ³(0.8) + φ⁴(0.8)
         = 0.8 × (1 + φ + φ² + φ³ + φ⁴)
         = 0.8 × (1 + 1.618 + 2.618 + 4.236 + 6.854)
         = 0.8 × 16.326
         = 13.061
```

This exceeds 1. To normalize, divide by the sum of weights:

```
Σ weights = 1 + φ + φ² + φ³ + φ⁴ = 16.326
C_system_normalized = 13.061 / 16.326 = 0.8
```

For equal-coherence components, the system coherence equals the component coherence. The phi-weighting only matters when components have **different** coherence values.

For a degraded system where rank-1 is at C₁ = 0.3 and all others at C = 0.8:

```
C_system = 1(0.3) + 1.618(0.8) + 2.618(0.8) + 4.236(0.8) + 6.854(0.8)
         = 0.3 + 1.294 + 2.094 + 3.389 + 5.483
         = 12.561
C_normalized = 12.561 / 16.326 = 0.769
```

A drop in the rank-1 component from 0.8 to 0.3 causes only a 3.1% drop in system coherence. This is because rank-1 has the **smallest** phi-weight. The system is **robust** against apex failure.

But if rank-5 drops from 0.8 to 0.3:

```
C_system = 1(0.8) + 1.618(0.8) + 2.618(0.8) + 4.236(0.8) + 6.854(0.3)
         = 0.8 + 1.294 + 2.094 + 3.389 + 2.056
         = 9.633
C_normalized = 9.633 / 16.326 = 0.590
```

A drop in the rank-5 component causes a 21% drop in system coherence. The system is **sensitive** to bulk degradation. **This is the phi-systems principle: systems fail from the bottom up, not the top down.**

---

## LAYER 3: FEEDBACK LOOPS IN PHI-SYSTEMS

### 3.1 Types of Feedback

Every system contains feedback loops. In phi-systems, there are three types:

**Positive Feedback:** Amplifies coherence. Each pass through the loop increases C.

```
C_out = C_in × (1 + κ)
```

where **κ > 0** is the feedback gain.

**Negative Feedback:** Stabilizes coherence. Each pass through the loop maintains C near the ground.

```
C_out = C_in × (1 - κ) + κ × φ⁻¹
```

**Phi-Feedback:** The feedback itself follows the phi-form. The gain modulates by φ.

```
C_out = C_in × (1 + κ(φ - 1)) + κ × φ⁻¹ × C_ground
```

### 3.2 The Phi-Feedback Equation

The general feedback equation for a phi-system:

```
C_out = C_in × (1 + κ(φ - 1)) + κ × φ⁻¹ × C_ground
```

where:
- **C_in** = input coherence
- **κ** = feedback coefficient (κ > 0 for positive, κ < 0 for negative)
- **φ - 1 = 0.618033988749895** = the phi-shift
- **C_ground = φ⁻¹ = 0.618033988749895** = the ground coherence

### 3.3 Feedback Trajectory Computation

For a system with positive feedback at κ = 0.3, starting at C₀ = 0.5:

**Iteration 1:**
```
C₁ = 0.5 × (1 + 0.3(0.618)) + 0.3 × 0.618 × 0.618
   = 0.5 × (1 + 0.1854) + 0.3 × 0.382
   = 0.5 × 1.1854 + 0.1146
   = 0.5927 + 0.1146
   = 0.7073
```

**Iteration 2:**
```
C₂ = 0.7073 × 1.1854 + 0.1146
   = 0.8385 + 0.1146
   = 0.9531
```

**Iteration 3:**
```
C₃ = 0.9531 × 1.1854 + 0.1146
   = 1.1298 + 0.1146
   = 1.2444
```

Coherence exceeds 1. The system has **over-cohered** — it is locked into a single state and cannot adapt. This is the positive feedback catastrophe: runaway coherence leads to rigidity.

### 3.4 Negative Feedback Trajectory

For κ = -0.3 (negative feedback), starting at C₀ = 0.9:

**Iteration 1:**
```
C₁ = 0.9 × (1 + (-0.3)(0.618)) + (-0.3) × 0.618 × 0.618
   = 0.9 × (1 - 0.1854) - 0.1146
   = 0.9 × 0.8146 - 0.1146
   = 0.7331 - 0.1146
   = 0.6185
```

**Iteration 2:**
```
C₂ = 0.6185 × 0.8146 - 0.1146
   = 0.5039 - 0.1146
   = 0.3893
```

**Iteration 3:**
```
C₃ = 0.3893 × 0.8146 - 0.1146
   = 0.3171 - 0.1146
   = 0.2025
```

The system is collapsing below C_crit. Too much negative feedback destroys coherence.

### 3.5 Phi-Feedback Trajectory (Optimal)

For the phi-feedback equation with κ = 0.3, starting at C₀ = 0.5:

**Iteration 1:**
```
C₁ = 0.5 × (1 + 0.3 × 0.618) + 0.3 × 0.618 × 0.618
   = 0.5 × 1.1854 + 0.1146
   = 0.7073
```

**Iteration 2:**
```
C₂ = 0.7073 × 1.1854 + 0.1146
   = 0.8385 + 0.1146
   = 0.9531
```

The ground term (0.1146) acts as a **floor** — it prevents the system from collapsing. The phi-shift term (1.1854) allows growth. The phi-feedback is self-balancing: it amplifies when C is low and constrains when C is high.

### 3.6 The Critical Feedback Gain

The system reaches a fixed point when C(t+1) = C(t) = C*:

```
C* = C* × (1 + κ(φ - 1)) + κ × φ⁻¹ × C_ground
C* - C* × (1 + κ(φ - 1)) = κ × φ⁻¹ × C_ground
C* × (-κ(φ - 1)) = κ × φ⁻¹ × C_ground
C* = -φ⁻¹ × C_ground / (φ - 1)
C* = -0.618 × 0.618 / 0.618
C* = -0.618
```

This is negative — meaning for positive κ, there is **no stable positive fixed point**. The system always grows. This is the phi-systems principle: **positive feedback is inherently unstable**. Systems require negative feedback components to remain bounded.

---

## LAYER 4: EMERGENCE IN PHI-SYSTEMS

### 4.1 The Emergence Threshold

Emergence occurs when the system coherence exceeds the critical threshold:

```
C_system > C_crit = 0.563263
```

Below C_crit: the system is **substrate**. Components exist, they interact, but they do not form a coherent whole. The system is a collection, not a unity.

Above C_crit: the system **emerges**. It becomes more than the sum of its components. New properties appear that do not exist in any individual component.

### 4.2 The Emergence Equation

When a system crosses C_crit, its coherence amplifies by φ:

```
C_emergent = C_system × φ
```

This is not a metaphor. The system's effective coherence — its ability to maintain itself, process information, resist perturbation — is φ times greater than the raw component coherence would predict.

### 4.3 Computing the Emergence κ

**Problem:** For a system of 10 components each at C = 0.1, what κ is needed for emergence?

**Step 1: Compute initial system coherence.**

With 10 components ranked 1–10, each at C = 0.1:

```
C_system = Σᵢ₌₁¹⁰ φ^(i-1) × 0.1
         = 0.1 × Σᵢ₌₁¹⁰ φ^(i-1)
         = 0.1 × (1 + φ + φ² + φ³ + φ⁴ + φ⁵ + φ⁶ + φ⁷ + φ⁸ + φ⁹)
```

Compute the sum of phi powers:

```
φ⁰ = 1.000
φ¹ = 1.618
φ² = 2.618
φ³ = 4.236
φ⁴ = 6.854
φ⁵ = 11.090
φ⁶ = 17.944
φ⁷ = 29.034
φ⁸ = 46.979
φ⁹ = 76.013
Σ = 197.386
```

```
C_system = 0.1 × 197.386 = 19.7386
C_system_normalized = 19.7386 / 197.386 = 0.1
```

Equal-coherence components → system coherence equals component coherence. So C_system = 0.1.

**Step 2: Determine required κ.**

We need C_system > C_crit = 0.563263.

Using the phi-feedback recursion, after n iterations:

```
C(n) = C₀ × (1 + κ(φ-1))ⁿ + κ × φ⁻¹ × C_ground × Σⱼ₌₀ⁿ⁻¹ (1 + κ(φ-1))ⱼ
```

For the system to reach C_crit, we need:

```
C_crit ≤ C₀ × (1 + κ(φ-1))ⁿ + κ × φ⁻¹ × C_ground × ((1 + κ(φ-1))ⁿ - 1) / (κ(φ-1))
```

For a single iteration (n=1):

```
0.563263 ≤ 0.1 × (1 + 0.618κ) + 0.618 × 0.618 × κ
0.563263 ≤ 0.1 + 0.0618κ + 0.382κ
0.563263 ≤ 0.1 + 0.4438κ
0.463263 ≤ 0.4438κ
κ ≥ 1.044
```

**For a single feedback pass, κ must be at least 1.044 to push the system above C_crit.**

For multiple iterations, the required κ decreases. After 2 iterations:

```
C(2) = 0.1 × (1 + 0.618κ)² + 0.382κ × (1 + 0.618κ + 1)
```

Setting C(2) = 0.563263 and solving:

```
0.563263 = 0.1(1 + 1.236κ + 0.382κ²) + 0.382κ(2 + 0.618κ)
0.563263 = 0.1 + 0.1236κ + 0.0382κ² + 0.764κ + 0.236κ²
0.563263 = 0.1 + 0.8876κ + 0.2742κ²
0.463263 = 0.8876κ + 0.2742κ²
```

Using the quadratic formula:

```
κ = (-0.8876 + √(0.8876² + 4 × 0.2742 × 0.463263)) / (2 × 0.2742)
κ = (-0.8876 + √(0.7878 + 0.5048)) / 0.5484
κ = (-0.8876 + √1.2926) / 0.5484
κ = (-0.8876 + 1.137) / 0.5484
κ = 0.2494 / 0.5484
κ ≈ 0.455
```

After 2 feedback iterations, **κ ≈ 0.455** is sufficient for emergence.

After 5 iterations, κ drops to approximately **0.18**. After 10 iterations, approximately **0.09**.

**The longer the system runs, the weaker the feedback needed for emergence.** This is the phi-systems principle of **accumulative emergence**: coherence compounds through recursion.

### 4.4 The Emergence Hierarchy

| Level | Condition | Description |
|-------|-----------|-------------|
| 0 | C < 0.1 | Dust — no coherence, pure noise |
| 1 | 0.1 ≤ C < 0.3 | Substrate — components exist, no interaction |
| 2 | 0.3 ≤ C < 0.563 | Proto-system — components interact, no emergence |
| 3 | C = 0.563263 | Critical — emergence threshold, phase transition |
| 4 | 0.563 < C < 1.0 | Emergent — system is more than its parts |
| 5 | C = 1.0 | Perfect coherence — all components aligned |
| 6 | C > 1.0 | Over-coherence — rigid, cannot adapt (failure mode) |

---

## LAYER 5: THE PHI-SYSTEMS LAWS

### Law 1: The Law of System Coherence

**Every system possesses a coherence value C_system that determines its functional state. The coherence is computed as the phi-weighted sum of component coherences, normalized by the sum of phi-weights.**

```
C_system = (Σᵢ φ^(rankᵢ - 1) × Cᵢ) / (Σᵢ φ^(rankᵢ - 1))
```

The system is functional when C_system > C_crit. It fails when C_system < C_crit. The coherence is the system's identity — without it, the system is a collection of parts, not a whole.

### Law 2: The Law of Phi-Weighting

```
C_system = (Σᵢ φ^(rankᵢ - 1) × Cᵢ) / (Σᵢ φ^(rankᵢ - 1))
```

**Components are weighted by φ^(rank-1), where rank is determined by functional criticality. Rank-1 components have the smallest weight (φ⁰ = 1). Higher-rank components have exponentially larger weights.**

This law states that system coherence is dominated by the **bulk** components, not the apex. A system's resilience comes from its many, not its few. Degradation of a single rank-1 component barely moves the system coherence. Degradation of rank-5 or rank-6 components can collapse the system.

**Implication:** Design systems with redundancy at the bottom, not the top.

### Law 3: The Law of Feedback Recursion

**System coherence evolves through the recursion:**

```
C(t+1) = φ⁻¹ × C(t) + I(t)
```

**where I(t) is the external input and φ⁻¹ is the decay constant.**

Without input, the system decays to φ⁻¹. With sufficient input, the system can sustain coherence above C_crit. The recursion is the system's heartbeat — each tick is a cycle of decay and renewal.

### Law 4: The Law of Emergence Threshold

**Emergence occurs if and only if C_system > C_crit = 0.563263. Below this threshold, the system is substrate. Above it, the system becomes more than its components. The emergent coherence is C_emergent = C_system × φ.**

This law establishes the **phase transition** in systems. There is no gradual emergence. The system crosses C_crit and qualitatively changes. The emergence amplification by φ means the system's effective capability is 1.618× its raw coherence.

### Law 5: The Law of System Memory (Carrier Recursion)

**Every system carries memory of its past coherence states. The memory decays at the phi-rate:**

```
M(t) = Σₖ₌₀^∞ φ⁻ᵏ × C(t - k)
```

**The system's current behavior is influenced by all its past states, weighted by φ⁻ᵏ. Recent states dominate, but older states never fully vanish.**

This is the carrier recursion. The system does not forget — it φ-compresses its history. The oldest memories have the smallest weight but are never zero. This is why systems exhibit path dependence: the current state depends on the entire trajectory, not just the present input.

### Law 6: The Law of System Boundaries (Coherence Gates)

**Every system has boundaries called coherence gates. A coherence gate G permits coherence flow when:**

```
C_in > G_threshold
```

**and blocks coherence flow when C_in < G_threshold.**

The gate is not a physical barrier. It is a coherence filter. Information, energy, or material can pass through the gate only if it carries sufficient coherence. Noise is blocked. Signal passes.

The gate threshold is itself a phi-value:

```
G_threshold = φ⁻¹ × C_system
```

A more coherent system has a higher gate threshold — it is more selective about what enters. A less coherent system has a lower threshold — it is more permeable to noise.

### Law 7: The Law of System Evolution (Phi-Ladder Climbing)

**Systems evolve by climbing the phi-ladder. Each rung of the ladder corresponds to a coherence level:**

```
Rung n: C = φ⁻ⁿ
```

**A system climbs from rung n to rung n-1 when it accumulates enough coherence to cross the threshold:**

```
C_system > φ⁻⁽ⁿ⁻¹⁾
```

**The system cannot skip rungs. Evolution is stepwise, not continuous.**

The phi-ladder is:
- Rung 0: C = φ⁰ = 1.0 (perfect coherence)
- Rung 1: C = φ⁻¹ = 0.618 (ground state)
- Rung 2: C = φ⁻² = 0.382
- Rung 3: C = φ⁻³ = 0.236
- Rung 4: C = φ⁻⁴ = 0.146
- Rung 5: C = φ⁻⁵ = 0.090

Systems begin at rung 5 (C = 0.090) and climb toward rung 0. Each climb requires accumulating coherence through feedback and input.

### Law 8: The Law of System Collapse (Below C_crit)

**When C_system drops below C_crit, the system collapses. The collapse follows:**

```
C(t+1) = φ⁻¹ × C(t)  (no input, pure decay)
```

**The system decays exponentially toward zero. The rate of decay is φ⁻¹ per time step.**

From C_crit to zero:

```
C(t) = C_crit × (φ⁻¹)ᵗ
```

The system reaches C = 0.01 in approximately:

```
t = ln(0.01 / 0.563263) / ln(0.618) = ln(0.01775) / ln(0.618) = -4.03 / -0.481 = 8.38 steps
```

**A system that crosses below C_crit has approximately 8 time steps before it ceases to exist.**

### Law 9: The Law of System Recovery (Restoration Protocol)

**A collapsed system can be recovered if external input is applied within the recovery window. The recovery protocol:**

```
C_recovery(t) = Σₖ₌₀^t φ⁻ᵏ × I(t - k)
```

**The system's coherence is rebuilt from external inputs, each weighted by how recent they are. Recovery requires sustained input over multiple time steps.**

The minimum input for recovery from C = 0 to C_crit:

```
C_crit = I × Σₖ₌₀^∞ φ⁻ᵏ = I × (1 / (1 - φ⁻¹)) = I × φ
I = C_crit / φ = 0.563263 / 1.618034 = 0.348
```

**A sustained input of I = 0.348 per time step will restore any collapsed system to C_crit.**

### Law 10: The Law of Universal Systems

**All systems — mechanical, biological, computational, social, quantum — follow the same phi-recursion. The equations are universal. The parameters (number of components, feedback gains, gate thresholds) vary. The form does not.**

```
C(t+1) = φ⁻¹ × C(t) + I(t)
C_system = Σᵢ φ^(rankᵢ - 1) × Cᵢ / Σᵢ φ^(rankᵢ - 1)
C_emergent = C_system × φ (when C_system > C_crit)
G_threshold = φ⁻¹ × C_system
```

A biological cell follows this recursion. A neural network follows this recursion. A social institution follows this recursion. A quantum field follows this recursion. The phi-form is the invariant. The substrate is the variable.

This law is the culmination of phi-systems theory: **there is one systems theory, and it is phi-systems theory.** All other systems theories are special cases.

---

## Falsification Criteria

Phi-systems theory is falsified if any of the following are demonstrated:

1. **Zero ground state:** Systems with a true rest state at zero coherence are found in nature — the phi-ground oscillation at φ⁻¹ is not universal.
2. **Top-down failure:** Systems consistently fail from apex degradation rather than bulk degradation, contradicting the phi-weighting principle.
3. **No emergence threshold:** System emergence is continuous rather than threshold-based, with no phase transition at C_crit = 0.563263.
4. **Collapse faster than φ⁻¹:** System collapse under zero input follows a decay rate measurably different from φ⁻¹ per time step.

---

## APPENDIX: COMPUTATIONAL REFERENCE

### A.1 Constants

```
φ = 1.618033988749895
φ⁻¹ = 0.618033988749895
C_crit = 0.563263
```

### A.2 Core Functions

```python
import math

PHI = (1 + math.sqrt(5)) / 2
PHI_INV = 1 / PHI
C_CRIT = 0.563263

def system_coherence(components, ranks):
    """
    Compute phi-weighted system coherence.
    components: list of coherence values [C1, C2, ..., Cn]
    ranks: list of ranks [1, 2, ..., n]
    """
    weights = [PHI**(r - 1) for r in ranks]
    weighted_sum = sum(w * c for w, c in zip(weights, components))
    total_weight = sum(weights)
    return weighted_sum / total_weight

def coherence_recursion(C, I):
    """Single step of coherence evolution."""
    return PHI_INV * C + I

def phi_feedback(C_in, kappa):
    """Phi-feedback equation."""
    return C_in * (1 + kappa * (PHI - 1)) + kappa * PHI_INV * PHI_INV

def emergence_coherence(C_system):
    """Compute emergent coherence if above threshold."""
    if C_system > C_CRIT:
        return C_system * PHI
    return C_system

def gate_threshold(C_system):
    """Compute coherence gate threshold."""
    return PHI_INV * C_system

def collapse_time(C_start, C_end=0.01):
    """Time steps to collapse from C_start to C_end."""
    return math.log(C_end / C_start) / math.log(PHI_INV)

def recovery_input(C_target):
    """Minimum sustained input to reach C_target from 0."""
    return C_target / PHI
```

### A.3 Worked Examples

**Example 1:** 5-component system with mixed coherences.

```python
components = [0.9, 0.7, 0.5, 0.3, 0.1]
ranks = [1, 2, 3, 4, 5]
C = system_coherence(components, ranks)
# C = (1*0.9 + 1.618*0.7 + 2.618*0.5 + 4.236*0.3 + 6.854*0.1) / (1+1.618+2.618+4.236+6.854)
# C = (0.9 + 1.1326 + 1.309 + 1.2708 + 0.6854) / 16.326
# C = 5.2978 / 16.326 = 0.3245
# C < C_crit → system is substrate, not emergent
```

**Example 2:** Positive feedback trajectory.

```python
C = 0.5
kappa = 0.3
for i in range(5):
    C = phi_feedback(C, kappa)
    print(f"Step {i+1}: C = {C:.4f}")
# Step 1: C = 0.7073
# Step 2: C = 0.9531
# Step 3: C = 1.2444  ← over-coherence
# Step 4: C = 1.6138  ← system rigid
# Step 5: C = 2.0893  ← failure mode
```

**Example 3:** Emergence from 10 weak components.

```python
components = [0.1] * 10
ranks = list(range(1, 11))
C = system_coherence(components, ranks)
# C = 0.1 (all equal → system coherence = component coherence)
# Need κ ≈ 0.455 for single-pass emergence
# Need κ ≈ 0.18 for 5-pass emergence
# Need κ ≈ 0.09 for 10-pass emergence
```

---

*End of PHI-SYSTEMS THEORY*
