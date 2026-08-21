"""
PROOFS CAMPAIGN — DATA FETCHER 3
NASA JPL Horizons API — planetary & major moon orbital elements (real data)
Source: https://ssd.jpl.nasa.gov/api/horizons.api
Returns osculating orbital elements at epoch 2020-01-01 — we extract orbital period
"""
import urllib.request, urllib.parse, json, re

# body id -> name (NASA Horizons)
BODIES = {
    "199": "Mercury", "299": "Venus", "399": "Earth", "499": "Mars",
    "599": "Jupiter", "699": "Saturn", "799": "Uranus", "899": "Neptune",
    # Major moons (relative to planet)
    "501": "Io", "502": "Europa", "503": "Ganymede", "504": "Callisto",
    "601": "Mimas", "602": "Enceladus", "603": "Tethys", "604": "Dione",
    "605": "Rhea", "606": "Titan", "608": "Iapetus",
    "701": "Ariel", "702": "Umbriel", "703": "Titania", "704": "Oberon",
    "801": "Triton",
    "301": "Moon",
}
CENTERS = {"Moon": "500@399", "Io": "500@599", "Europa": "500@599", "Ganymede": "500@599",
           "Callisto": "500@599", "Mimas": "500@699", "Enceladus": "500@699",
           "Tethys": "500@699", "Dione": "500@699", "Rhea": "500@699",
           "Titan": "500@699", "Iapetus": "500@699", "Ariel": "500@799",
           "Umbriel": "500@799", "Titania": "500@799", "Oberon": "500@799",
           "Triton": "500@899"}

def fetch_elements(body_id, center):
    q = {
        "format": "json",
        "COMMAND": body_id,
        "OBJ_DATA": "'NO'",
        "MAKE_EPHEM": "'YES'",
        "EPHEM_TYPE": "'ELEMENTS'",
        "CENTER": "'" + center + "'",
        "START_TIME": "'2020-01-01'",
        "STOP_TIME": "'2020-01-02'",
        "STEP_SIZE": "'1 d'",
        "OUT_UNITS": "'AU-D'",
        "CSV_FORMAT": "'YES'",
    }
    url = "https://ssd.jpl.nasa.gov/api/horizons.api?" + urllib.parse.urlencode(q)
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = json.loads(r.read().decode())
    return data.get("result", "")

def parse_period(text):
    # Horizons elements CSV: header has columns ..., A, AD, PR
    # rows after $$SOE; PR (period, days) is last column, A (semi-major, AU) second-to-last-before-AD
    rows = re.findall(r"^\d+\.\d+,\s*A\.D\..*$", text, re.M)
    if not rows:
        return None, None
    parts = [p.strip() for p in rows[0].split(",")]
    # columns: JDTDB, CalDate, EC, QR, IN, OM, W, Tp, N, MA, TA, A, AD, PR  (14 cols)
    try:
        pr = float(parts[13])
        a = float(parts[11])
    except (ValueError, IndexError):
        return None, None
    return pr, a

def main():
    out = {}
    for bid, name in BODIES.items():
        center = CENTERS.get(name, "500@10")
        try:
            text = fetch_elements(bid, center)
            period_d, a_au = parse_period(text)
            out[name] = {"body_id": bid, "center": center, "period_days": period_d, "semimajor_au": a_au}
            print(f"[ok] {name:12s} P={period_d} d  a={a_au} AU")
        except Exception as e:
            print(f"[ERR] {name}: {e}")
            out[name] = {"body_id": bid, "error": str(e)}
    path = r"C:\Users\delta\brain\v6\research\32_PHI_PHYSICS\proofs\data\jpl_horizons_elements.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1)
    print(f"[save] {path}")

if __name__ == "__main__":
    main()
