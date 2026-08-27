# Living-Phi-Physics-v4.9.zip — How to Recombine

The complete corpus is split into 2 parts (each under GitHub's 100 MB file limit):

- `Living-Phi-Physics-v4.9.part1.zip` (59 MB)
- `Living-Phi-Physics-v4.9.part2.zip` (59 MB)

## To Recombine (Windows PowerShell)

```powershell
# Concatenate the parts into the full zip
cmd /c copy /b Living-Phi-Physics-v4.9.part1.zip + Living-Phi-Physics-v4.9.part2.zip Living-Phi-Physics-v4.9.zip
```

## To Recombine (macOS / Linux)

```bash
# Concatenate the parts into the full zip
cat Living-Phi-Physics-v4.9.part1.zip Living-Phi-Physics-v4.9.part2.zip > Living-Phi-Physics-v4.9.zip
```

## To Extract

Once recombined, extract the zip normally:

```powershell
# Windows
Expand-Archive -Path Living-Phi-Physics-v4.9.zip -DestinationPath .\Living-Phi-Physics-v4.9
```

```bash
# macOS / Linux
unzip Living-Phi-Physics-v4.9.zip -d Living-Phi-Physics-v4.9
```

## What's Inside

The complete corpus:
- 2,395 corrected laws of physics
- 600 emerging laws (250 V1 + 350 V2) with simulations and validations
- 1,600 redesigned devices (800 original + 800 corporate) with prototypes and simulations
- 15,000 field-AI laws
- 50,814 conscious-mathematics equations
- 150 questions + 15 research papers
- 10 surprise papers
- 70 geomic proofs
- 18 geomic protocols
- 42 field-interaction prototypes
- All registers, docs, tools, simulations, and validations

**Author:** Christopher David Ayotte — Soul Code [425, 434, 266, 775]
**License:** Dual License Agreement v4.9