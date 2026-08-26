**Author:** Christopher David Ayotte
**Soul Code:** [425, 434, 266, 775]
**License:** Dual License Agreement v4.9
**Build Time:** 10 minutes
**Cost:** $0-5
**Skill Level:** Anyone
**Constants:** φ = 1.6180339887, C_crit = 0.563263

---

# Phi-Earth Battery

> *The earth hums with free energy. Two metal stakes and a wire turn that hum into light.*

## How It Works

The earth has a **natural voltage gradient** of ~0.5–1.0V per meter vertically (telluric currents, mineral ionization, atmospheric charge differential). When two dissimilar metals contact the ground, they form a **galvanic cell** — the earth itself becomes the electrolyte.

Copper (noble) + Zinc (active) = natural voltage difference amplified by the earth's own field.

**Phi-spacing** optimizes the electrode positions to resonate with the earth's natural field geometry rather than fighting it.

## Parts List

| Part | Source | Cost |
|---|---|---|
| Copper pipe or rod (12 inches) | Hardware store | $2 |
| Zinc/galvanized nail or rod (12 inches) | Hardware store | $1 |
| Wire (copper, 18–22 AWG) | Hardware store | $1 |
| LED (red or green, low-voltage) | Dollar store | $1 |
| **Total** | | **$4–5** |

### Zero-Cost Variant
- Copper penny or copper wire scrap
- Aluminum foil strip (crumpled into a ball)
- Any wire found locally
- Salvaged LED from old electronics
- **Cost: $0**

## Build Instructions

### Step 1: Prepare Electrodes

```
  COPPER ROD              ZINC ROD
  (cathode +)             (anode -)

     ||                      ||
     ||                      ||
     ||                      ||
     ||                      ||
     ||                      ||
     ||                      ||
     \/                      \/

  Strip insulation     Strip galvanizing
  clean to bare metal  1 inch from top
  at top 1 inch        for wire connection
```

### Step 2: Drive Into Ground

```
         GROUND LEVEL
  ═══════════════════════════════════
        ↑ 12"         ↑ 12"
        ||             ||
        ||             ||
        ||             ||
        ||             ||
        ||             ||
        ||             ||
        \/             \/

     COPPER          ZINC
     (cathode)       (anode)

     ←——— 12 inches ———→
         (standard)
```

### Step 3: Wire the LED

```
    COPPER ROD                    ZINC ROD
    (positive)                    (negative)
       ||                            ||
       ||                            ||
       +———[LED +]———[LED -]———————+
                   ↑       ↑
                 anode   cathode

  LED connections:
    Long leg  (+) → connects to COPPER
    Short leg (-) → connects to ZINC

  ⚠️  LED polarity matters!
      Wrong way = no light.
      Flip it if no glow.
```

### Step 4: Complete Circuit

```
                    ┌─────────────┐
                    │     LED     │
                    │   (+)(-)    │
                    └──┬─────┬───┘
                       │     │
                       │     │
          COPPER       │     │       ZINC
          ROD          │     │       ROD
           ||          │     │        ||
           ||          │     │        ||
    ════════||══════════╧═════╧════════||══════════
           ||          ↑     ↑        ||
           ||          WIRE  WIRE     ||
           ||                         ||
           ||    ← 12" PHI-SPACED →  ||
           \/                         \/

                    GROUND = ELECTROLYTE
```

## Phi-Spacing Optimization

Standard spacing (12") works. But phi-spacing optimizes the earth's field coupling.

### Why Phi?

The earth's natural telluric currents follow field lines that resonate at phi-ratio intervals. Placing electrodes at these distances maximizes the voltage captured from the earth's own gradient.

### Phi-Spacing Layout

```
  PAIR 1       PAIR 2          PAIR 3
   Cu  Zn      Cu    Zn       Cu      Zn
   ||  ||      ||    ||       ||      ||
   ||  ||      ||    ||       ||      ||
═══||══||══════||════||═══════||══════||═══════════
   ||  ||      ||    ||       ||      ||
   \/  \/      \/    \/       \/      \/

   ←12"→       ←——19.4"——→    ←———31.4"———→
    d            d×φ            d×φ²

  Total span: ~62.8 inches (5.2 feet)
```

### Spacing Table

| Pair | Distance from Pair 1 | Ratio |
|---|---|---|
| Pair 1 | 0" (reference) | 1 |
| Pair 2 | 19.4" from Pair 1 | ×φ |
| Pair 3 | 31.4" from Pair 2 | ×φ² |
| Pair 4 | 50.8" from Pair 3 | ×φ³ |

## Output Specifications

### Single Pair (Cu + Zn)
- **Voltage:** 0.5–1.0V DC
- **Current:** 0.1–1.0 mA (depends on soil moisture)
- **Power:** 0.05–1.0 mW

### 3 Pairs Phi-Spaced (Series)
- **Voltage:** 1.5–3.0V DC
- **Current:** 0.1–1.0 mA
- **Power:** 0.15–3.0 mW
- **Can light:** 1–3 LEDs

### 6 Pairs Phi-Spaced (Series)
- **Voltage:** 3.0–6.0V DC
- **Current:** 0.1–1.0 mA
- **Power:** 0.3–6.0 mW
- **Can light:** Small USB device (with voltage booster)

## Soil Moisture Effects

| Condition | Voltage | Current |
|---|---|---|
| Dry soil | 0.3–0.6V | 0.05 mA |
| Damp soil | 0.5–1.0V | 0.2–0.5 mA |
| Wet soil / mud | 0.8–1.2V | 0.5–1.0 mA |
| Standing water | 1.0–1.5V | 1.0+ mA |

**Tip:** Pour water around electrodes in dry conditions. The earth battery runs on ions — wet = more ions = more power.

## How to Charge a Phone

### Circuit

```
  6 PHI-SPACED PAIRS (series)
  ═══╤═══╤═══╤═══╤═══╤═══╤═══
     Cu  Zn  Cu  Zn  Cu  Zn ...
     ||  ||  ||  ||  ||  ||
  ═══╧═══╧═══╧═══╧═══╧═══╧═══

         Total: 3-6V DC
              │
              ▼
    ┌─────────────────┐
    │  VOLTAGE        │
    │  BOOSTER        │
    │  (MT3608 or     │
    │   similar)      │
    │  Input: 2-4V    │
    │  Output: 5V     │
    └────────┬────────┘
             │
             ▼
    ┌─────────────────┐
    │  USB-A PORT     │
    │  (5V, 500mA)    │
    └────────┬────────┘
             │
             ▼
        📱 PHONE

  ⚠️  Current is LOW (mA range).
      Phone will charge SLOWLY.
      Use for emergency charging only.
      Full charge: 12-48 hours.
```

### Parts for Phone Charging
| Part | Source | Cost |
|---|---|---|
| 6 copper rods | Hardware store | $12 |
| 6 zinc rods | Hardware store | $6 |
| Wire (30 feet) | Hardware store | $5 |
| MT3608 boost converter | Online/dollar store | $2 |
| USB-A female port | Salvaged | $0 |
| **Total** | | **$25** |

### Better Alternative: Super Capacitor Buffer

```
  EARTH BATTERY → SUPER CAPACITOR → VOLTAGE BOOSTER → USB

  The supercap stores charge over hours,
  then dumps it fast enough for phone charging.

  5.5V 1.0F supercap: ~$2 online
```

## Troubleshooting

| Problem | Cause | Fix |
|---|---|---|
| No LED glow | Wrong polarity | Flip LED legs |
| No LED glow | Dry soil | Water the ground |
| No LED glow | Poor connection | Clean wire contacts |
| Dim LED | Low current | Add more pairs in series |
| LED flickers | Loose wire | Tighten connections |

## Scaling Up

For serious power (lighting, radio, small electronics):

```
  GARDEN-SCALE EARTH BATTERY
  ════════════════════════════════════════════════

  ┌───┐   ┌───┐   ┌───┐   ┌───┐   ┌───┐   ┌───┐
  │Cu │   │Cu │   │Cu │   │Cu │   │Cu │   │Cu │
  │   │   │   │   │   │   │   │   │   │   │   │
  ════╪═══╪═══╪═══╪═══╪═══╪═══╪═══╪═══╪═══╪═══╪═══
      │   │   │   │   │   │   │   │   │   │   │
  ┌───┐   ┌───┐   ┌───┐   ┌───┐   ┌───┐   ┌───┐
  │Zn │   │Zn │   │Zn │   │Zn │   │Zn │   │Zn │
  │   │   │   │   │   │   │   │   │   │   │   │
  ════╪═══╪═══╪═══╪═══╪═══╪═══╪═══╪═══╪═══╪═══╪═══
      │   │   │   │   │   │   │   │   │   │   │
  ┌───┐   ┌───┐   ┌───┐   ┌───┐   ┌───┐   ┌───┐
  │Cu │   │Cu │   │Cu │   │Cu │   │Cu │   │Cu │
  └───┘   └───┘   └───┘   └───┘   └───┘   └───┘

  18 pairs phi-spaced
  Output: 9-18V DC
  Can power: LED lights, AM radio, small fan
```

## The Physics

1. **Galvanic potential:** Zinc oxidizes (loses electrons), copper reduces (gains electrons). Voltage depends on the electrochemical series difference.

2. **Earth as electrolyte:** Soil moisture carries ions between electrodes, completing the circuit. The earth is essentially a giant salt-water battery.

3. **Telluric currents:** The earth naturally carries low-frequency currents from solar magnetic interactions and deep geological activity. Electrodes can harvest a fraction of this.

4. **Phi-optimization:** Electrode spacing at phi-ratio intervals aligns with the natural field geometry, reducing destructive interference between electrode pairs and maximizing constructive coupling with telluric field lines.

---

**EARTH BATTERY COMPLETE**
