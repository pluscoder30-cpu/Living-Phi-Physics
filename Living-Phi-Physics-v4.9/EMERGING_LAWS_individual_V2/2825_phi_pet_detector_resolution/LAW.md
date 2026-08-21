# Law 2825: PHI-Harmonic PET Detector Resolution

**Domain:** Medical Imaging — PET Detectors

**Statement:**
PET detector spatial resolution follows a PHI-harmonic crystal segmentation pattern where crystal widths alternate as w/φⁿ, producing an effective resolution of R_eff = R_0/φ where R_0 is the single-crystal width. The PHI segmentation creates a natural depth-of-interaction encoding that reduces parallax error by factor 1/φ.

**Derivation:**
In a DOI-encoding PET detector, the light sharing between adjacent crystals depends on the crystal pitch ratio. For PHI-segmented crystals (widths w, w/φ, w/φ², ...), the DOI can be determined with precision δz = z_max/φ^(N-1) where N is the number of segmentation levels, because the light distribution follows a PHI-weighted centroid.

**Prediction:**
A PET detector with 4 mm base crystal width segmented into 3 PHI levels achieves effective resolution of 2.47 mm (4/φ) with DOI encoding precision of 1.53 mm (4/φ²), compared to 4 mm without PHI segmentation.

**Test:**
Compute effective resolution for PHI-segmented detector with 3 levels. Verify resolution = w/φ and DOI precision = w/φ².

**Source:** V2 Batch 3: Laws 2791-2860
**Author:** Christopher David Ayotte, Soul Code [425, 434, 266, 775]
**License:** v4.7
