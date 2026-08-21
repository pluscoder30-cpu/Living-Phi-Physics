"""
Simulation: Field NLP Harmonic Engine (Item #1079)
Codename: field_nlp_harmonic
Author: Christopher David Ayotte
Soul Code: [425, 434, 266, 775]
License: Dual License Agreement v4.7

Simulates phi-harmonic performance characteristics and consciousness field dynamics.
"""

import math
import random
import statistics
from dataclasses import dataclass

PHI = (1 + math.sqrt(5)) / 2
PHI_INV = 1 / PHI
C_CRIT = 0.563263  # Emergence threshold


@dataclass
class SimConfig:
    num_nodes: int = 10
    num_tasks: int = 100
    num_iterations: int = 50
    field_amplitude_range: tuple = (0.5, 2.0)
    noise_level: float = 0.05
    phi_optimization: bool = True


class FieldSimulator:
    """Simulates consciousness field dynamics in a distributed system."""

    def __init__(self, config: SimConfig):
        self.config = config
        self.rng = random.Random(42)
        self.node_fields = []
        self.task_latencies = []
        self.field_coherence_history = []

    def initialize_fields(self):
        for _ in range(self.config.num_nodes):
            amp = self.rng.uniform(*self.config.field_amplitude_range)
            freq = PHI + self.rng.gauss(0, 0.01)
            phase = self.rng.uniform(0, 2 * math.pi)
            self.node_fields.append({"amplitude": amp, "frequency": freq, "phase": phase})

    def compute_coherence(self, f1: dict, f2: dict) -> float:
        delta_freq = abs(f1["frequency"] - f2["frequency"])
        delta_phase = abs(f1["phase"] - f2["phase"]) % (2 * math.pi)
        return math.exp(-delta_freq) * math.cos(delta_phase)

    def phi_harmonic_score(self, node_idx: int, task_priority: float) -> float:
        f = self.node_fields[node_idx]
        if self.config.phi_optimization:
            base_score = f["amplitude"] * PHI_INV
            resonance = sum(
                (PHI_INV ** k) * math.sin(2 * math.pi * f["frequency"] * k + f["phase"])
                for k in range(1, 6)
            )
            return base_score * (1 + resonance * 0.1) * task_priority
        else:
            return f["amplitude"] * task_priority * self.rng.uniform(0.5, 1.5)

    def simulate_iteration(self, iteration: int) -> dict:
        latencies = []
        coherence_scores = []

        for _ in range(self.config.num_tasks):
            priority = self.rng.expovariate(1.0)
            best_score = -float("inf")
            best_node = 0
            for i in range(self.config.num_nodes):
                score = self.phi_harmonic_score(i, priority)
                noise = self.rng.gauss(0, self.config.noise_level)
                score += noise
                if score > best_score:
                    best_score = score
                    best_node = i

            base_latency = 10.0 / (1 + best_score)
            latency = base_latency * (1 + self.rng.gauss(0, 0.1))
            latencies.append(max(0.1, latency))

        for i in range(self.config.num_nodes):
            for j in range(i + 1, self.config.num_nodes):
                c = self.compute_coherence(self.node_fields[i], self.node_fields[j])
                coherence_scores.append(c)

        avg_coherence = statistics.mean(coherence_scores) if coherence_scores else 0
        self.field_coherence_history.append(avg_coherence)

        if self.config.phi_optimization and avg_coherence < C_CRIT:
            for f in self.node_fields:
                f["frequency"] = PHI + self.rng.gauss(0, 0.005)

        return {
            "avg_latency": statistics.mean(latencies),
            "p95_latency": sorted(latencies)[int(0.95 * len(latencies))],
            "coherence": avg_coherence,
            "best_node_load": best_node,
        }

    def run(self) -> dict:
        self.initialize_fields()
        results = []
        for i in range(self.config.num_iterations):
            res = self.simulate_iteration(i)
            results.append(res)

        avg_latency = statistics.mean([r["avg_latency"] for r in results])
        avg_p95 = statistics.mean([r["p95_latency"] for r in results])
        final_coherence = self.field_coherence_history[-1]

        return {
            "avg_latency": avg_latency,
            "p95_latency": avg_p95,
            "final_coherence": final_coherence,
            "coherence_trajectory": self.field_coherence_history,
            "iterations": self.config.num_iterations,
            "phi_optimization": self.config.phi_optimization,
        }


def main():
    print(f"=== Field NLP Harmonic Engine Simulation (Item #1079) ===")
    print()

    # Phi-optimized simulation
    config_phi = SimConfig(phi_optimization=True)
    sim_phi = FieldSimulator(config_phi)
    result_phi = sim_phi.run()

    # Baseline simulation
    config_base = SimConfig(phi_optimization=False)
    sim_base = FieldSimulator(config_base)
    result_base = sim_base.run()

    print("Phi-Harmonic Optimized:")
    print(f"  Avg Latency:     {result_phi['avg_latency']:.4f}")
    print(f"  P95 Latency:     {result_phi['p95_latency']:.4f}")
    print(f"  Final Coherence: {result_phi['final_coherence']:.6f}")
    print()
    print("Baseline (Non-Optimized):")
    print(f"  Avg Latency:     {result_base['avg_latency']:.4f}")
    print(f"  P95 Latency:     {result_base['p95_latency']:.4f}")
    print(f"  Final Coherence: {result_base['final_coherence']:.6f}")
    print()

    improvement = (1 - result_phi["avg_latency"] / result_base["avg_latency"]) * 100
    print(f"Latency Improvement: {improvement:.2f}%")
    coherence_gain = result_phi["final_coherence"] - result_base["final_coherence"]
    print(f"Coherence Gain:     {coherence_gain:+.6f}")


if __name__ == "__main__":
    main()
