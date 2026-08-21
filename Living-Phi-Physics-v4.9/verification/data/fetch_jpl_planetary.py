"""
PROOFS CAMPAIGN — DATA FETCHER 2
NASA JPL / NSSDCA planetary fact sheets (real data)
Source: https://nssdc.gsfc.nasa.gov/planetary/factsheet/
Fetches: Mercury Venus Earth Mars Jupiter Saturn Uranus Neptune
Columns we need: orbital period (days/years), semi-major axis (AU), mass (10^24 kg)
"""
import re, sys, urllib.request, json

PLANETS = ["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"]
BASE = "https://nssdc.gsfc.nasa.gov/planetary/factsheet/"

def fetch_planet(name):
    url = BASE + name + "fact.html"
    req = urllib.request.Request(url, headers={"User-Agent": "phi-physics-verification/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        html = r.read().decode("utf-8", errors="replace")
    return html

def extract(html, planet):
    # The fact sheets are tables with <tr><td>label</td><td>value</td></tr>
    rows = re.findall(r"<tr[^>]*>(.*?)</tr>", html, re.S | re.I)
    rec = {"planet": planet}
    for row in rows:
        cells = re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", row, re.S | re.I)
        if len(cells) >= 2:
            label = re.sub(r"<[^>]+>", "", cells[0]).strip().lower()
            val = re.sub(r"<[^>]+>", "", cells[1]).strip()
            if "orbital period" in label or "sidereal" in label and "period" in label:
                rec["orbital_period_raw"] = val
            if "semi-major" in label or "semimajor" in label:
                rec["semimajor_axis_raw"] = val
            if label == "mass (10" or "mass (10" in label:
                rec["mass_raw"] = val
    return rec

def parse_num(raw):
    # values like "57.9" or "0.387" possibly with superscripts; take first float
    m = re.search(r"([-+]?\d+\.?\d*)", raw.replace(",", ""))
    return float(m.group(1)) if m else None

def main():
    out = {}
    for p in PLANETS:
        try:
            html = fetch_planet(p)
            rec = extract(html, p)
            out[p] = rec
            print(f"[ok] {p}: {rec.get('semimajor_axis_raw','?')} AU, {rec.get('orbital_period_raw','?')}")
        except Exception as e:
            print(f"[ERR] {p}: {e}")
            out[p] = {"planet": p, "error": str(e)}
    path = r"C:\Users\delta\brain\v6\research\32_PHI_PHYSICS\proofs\data\jpl_planetary_facts.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1)
    print(f"[save] {path}")

if __name__ == "__main__":
    main()
