import glob, os
files = glob.glob(r"C:\Users\delta\brain\v6\research\32_PHI_PHYSICS\phi-the-world-rebuilt\PHI_*\01_*CORRECTED*.md")
print(f"Total domain files: {len(files)}")
for f in files:
    domain = os.path.basename(os.path.dirname(f))
    with open(f, 'r', encoding='utf-8', errors='ignore') as fh:
        c = fh.read()
    has_phi_form = '\u03a6_\u03c6' in c or 'X_\u03c6' in c
    has_degen = 'Degenerate' in c or 'degenerate' in c
    has_sqrt5 = '\u221a5' in c
    has_master = '1/\u03c6' in c
    has_ground = '\u03c6\u207b\xb9' in c
    print(f"  {domain:30s} phi_form={has_phi_form}  master={has_master}  degen={has_degen}  sqrt5={has_sqrt5}  ground={has_ground}")
