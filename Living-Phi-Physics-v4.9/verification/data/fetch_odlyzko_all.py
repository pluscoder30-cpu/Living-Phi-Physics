"""
VERIFICATION — FETCH ALL ODLYZKO ZERO TABLES (zeros1..zeros8)
Source: http://www.dtc.umn.edu/~odlyzko/zeta_tables/
zeros1 = first 100,001 zeros; zeros2..zeros8 = 100,000 each -> 800,001 total.
Goal: feed the verified Riemann result toward the 10^6 zero verification scale.
"""
import urllib.request, ssl, os, time

HERE = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(HERE, "..", "data")
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

BASE = "http://www.dtc.umn.edu/~odlyzko/zeta_tables/"
FILES = [f"zeros{i}" for i in range(1, 9)]

def fetch(name):
    url = BASE + name
    out = os.path.join(DATA_DIR, f"odlyzko_{name}.txt")
    if os.path.exists(out) and os.path.getsize(out) > 100000:
        print(f"[skip] {name} already present ({os.path.getsize(out)} bytes)")
        return out
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=120, context=ctx) as r:
        data = r.read()
    with open(out, "wb") as f:
        f.write(data)
    print(f"[ok] {name}: {len(data)} bytes in {time.time()-t0:.1f}s -> {out}")
    return out

for f in FILES:
    try:
        fetch(f)
    except Exception as e:
        print(f"[ERR] {f}: {e}")

# count total zeros fetched
total = 0
for f in FILES:
    p = os.path.join(DATA_DIR, f"odlyzko_{f}.txt")
    if os.path.exists(p):
        with open(p) as fh:
            total += sum(1 for line in fh if line.strip())
print(f"\nTOTAL zeros available: {total}")
