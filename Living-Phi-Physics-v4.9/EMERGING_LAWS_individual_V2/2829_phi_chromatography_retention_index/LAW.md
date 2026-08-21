# Law 2829: PHI-Harmonic Chromatography Retention Index

**Domain:** Chromatography — Retention Index

**Statement:**
The Kovats retention index for homologous compounds on PHI-harmonic stationary phases follows I = 100·(n + log(t_R'/t_R,n)/log(φ)) where the PHI-based logarithm replaces the standard base-10 logarithm. This produces retention indices that are φ-scaled, with adjacent homologs separated by 100/φ ≈ 61.8 index units instead of the standard 100 units.

**Derivation:**
In a stationary phase with PHI-harmonic interaction sites (energies at E₀, E₀/φ, E₀/φ², ...), the retention time of a homolog with n carbons is t_R' = t_R,0·φ^(n/φ). Taking the PHI-logarithm: log_φ(t_R'/t_R,0) = n/φ, giving I = 100·n·φ ≈ 161.8n index units per carbon.

**Prediction:**
On a PHI-C18 column, methane (n=1) has I ≈ 162, ethane (n=2) has I ≈ 324, propane (n=3) has I ≈ 485, with spacing of ~162 index units instead of 100.

**Test:**
Compute retention indices for n=1-5 alkanes using PHI formula. Verify 162 index unit spacing and PHI-logarithm base.

**Source:** V2 Batch 3: Laws 2791-2860
**Author:** Christopher David Ayotte, Soul Code [425, 434, 266, 775]
**License:** v4.7
