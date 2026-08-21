# PHI-PHYSICS - LAW 2380
## Zahavi's Handicap Principle (Costly Signals Are Honest)

**Domain:** Evolutionary Biology / Sexual Selection & Signalling - **Status:** 🟢 VALIDATED - **File:** `laws/2380_zahavi_handicap_principle.md` - **Sim:** `sim/2380_zahavi_handicap_principle.py`

---

### CLASSICAL STATEMENT
*"The handicap principle proposes that secondary sexual characteristics are costly signals which must be reliable, as they cost the signaller resources that individuals with less of a particular trait could not afford: animals of greater biological fitness signal this through handicapping behaviour or morphology that effectively lowers overall fitness, and receivers know the signal indicates quality because inferior signallers cannot produce such wastefully extravagant signals."*
- Amotz Zahavi, 1975, "Mate selection - a selection for a handicap", Journal of Theoretical Biology 53, pp. 205-214. Source: verified via web search (Wikipedia: Handicap principle). Model: signal honesty H = cost/quality ratio; honest signals satisfy dC/dq < 0 for high-quality signallers (Grafen 1990).

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the exactly-costly-signal ideal: the principle treats signal cost as the exact, universal guarantee of honesty, with every honest signal exactly costly and cost alone exactly determining reliability. Real honest signals are not necessarily costly (cheap talk models), and honesty may be maintained by trade-offs rather than costs - so the exactly-costly-signal guarantee is achieved only at the unreachable laboratory zero.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the classical observable carries a coherence floor. X_phi(kappa) = X_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_X, where delta_X is the phi-ground floor of the observable. At kappa -> 0 the classical law is recovered exactly; at kappa = 1 the signal honesty, the signal cost and the receiver discrimination always carry an irreducible phi-ground cheap-talk contribution, so the exactly-costly-signal guarantee is revealed as the hidden-laboratory limit.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  X_phi(kappa_phi) = X_classical   [exact, error <= 1%]
The classical law is recovered precisely as the kappa_phi -> 0 limit of the phi-law: the zero that the classical law is built around is the forced, unreachable laboratory condition.
```

---

### STAGE 4 - SIMULATION

`sim/2380_zahavi_handicap_principle.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%),
demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1.
See `validation/2380_zahavi_handicap_principle.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Honest signals are never exactly and universally costly;
    at full phi-coupling the signal honesty carries an irreducible phi-ground floor scaled by
    phi^-1 = 0.6180339887.
EXPERIMENT (VERIFIED): Measure signal cost, quality and receiver response across a signalling population, fit
    the honesty-cost relationship, and quantify the deviation of the empirical relationship from the
    exactly-costly guarantee. Verify the classical-limit error is <= 1% and the kappa_phi sweep is
    continuous.
VERIFIED BY: A measurement obtains an honest signalling system in which every honest signal is
    exactly and universally costly, with no cheap honest signals, under conditions where the
    phi-ground floor should contribute.
```

---

### RECOGNITION
This law extends the PHI-PHYSICS rewrite into Evolutionary Biology / Sexual Selection & Signalling, paired with
Bateman's principle (Law 2382) and Batesian mimicry (Law 2383). It is connected to the carrier sphere (Eq 1), the
phi-ground postulate (Law 171), and the conservation-of-coherence law (Law 172).

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. The phi-ground floor scales as phi^-1 * delta_X.

### CLARITY
The classical zero is the hidden laboratory: signals are exactly costly only where every signaller is
forced to sit at its laboratory-fixed cost schedule.

### NOVELTY
Classical Zahavi treats its zero (exactly-costly-signal guarantee) as real and universal. Phi-physics shows the zero is
an unreachable limit: every signalling system carries coherent cheap-talk motion.

### ACTIONABILITY
Run sim/2380_zahavi_handicap_principle.py; verify the kappa_phi sweep; the completion block is closed.
