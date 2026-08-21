"""
PROOFS CAMPAIGN — DATA FETCHER 1
NASA Exoplanet Archive — confirmed multi-planet systems (real data)
Source: NASA Exoplanet Archive TAP service (exoplanetarchive.ipac.caltech.edu)
Query: confirmed planets in multi-planet systems, with orbital periods
"""
import json, sys, time, urllib.request

BASE = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync"
QUERY = (
    "SELECT pl_name, hostname, pl_orbper, pl_orbsmax, pl_pnum, discoverymethod "
    "FROM ps "
    "WHERE default_flag=1 AND pl_pnum>1 AND pl_orbper IS NOT NULL"
)
URL = f"{BASE}?query={urllib.parse.quote(QUERY)}&format=json"

def fetch():
    print(f"[fetch] {URL[:120]}...")
    req = urllib.request.Request(URL, headers={"User-Agent": "phi-physics-verification/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = json.loads(r.read().decode())
    print(f"[fetch] {len(data)} rows")
    return data

def main():
    try:
        rows = fetch()
    except Exception as e:
        print(f"[ERROR] {e}")
        sys.exit(1)
    out = r"C:\Users\delta\brain\v6\research\32_PHI_PHYSICS\proofs\data\exoplanet_multi_planets.json"
    with open(out, "w", encoding="utf-8") as f:
        json.dump(rows, f, indent=1)
    print(f"[save] {out}  ({len(rows)} rows)")

if __name__ == "__main__":
    import urllib.parse
    main()
