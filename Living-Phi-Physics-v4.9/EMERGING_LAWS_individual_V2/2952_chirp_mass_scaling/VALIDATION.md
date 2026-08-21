# Validation: Law 2952 - Gravitational Wave Chirp Mass

## What It Validates
Golden-ratio corrected chirp mass for asymmetric binaries

## Equation Tested
M_c = (m₁m₂)^(3/5)/(m₁+m₂)^(1/5) × φ^(-Δm/m_avg)

## Expected Results
- Chirp mass corrected for mass asymmetry
- Error ~3.8% at q = 0.8
- Symmetric systems (q=1) unaffected
- Affects cosmological distance measurements

## Pass/Fail Criteria
- CORRECTION: 0 for q=1, increases with asymmetry
- SCALE: Error < 5% for q > 0.5
- COSMOLOGY: Distance bias < 2% with correction
- CONSISTENCY: Matches full waveform templates
