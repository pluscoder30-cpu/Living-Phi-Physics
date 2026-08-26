**Author:** Christopher David Ayotte
**Soul Code:** [425, 434, 266, 775]
**License:** Dual License Agreement v4.9
**Build Time:** 10 minutes
**Cost:** $0-3
**Skill Level:** Anyone
**Constants:** φ = 1.6180339887, C_crit = 0.563263

---

# PHI-PIEZO VIBRATION HARVESTER

## How Piezo Works (Simple)

Piezoelectric materials generate voltage when deformed. Tap it, bend it, vibrate it — electrons flow. No fuel, no moving parts, no maintenance. Just physics.

The crystal lattice inside the piezo element shifts under pressure, creating a voltage difference across its surface. More deformation = more voltage. Phi-spacing the elements creates constructive interference — vibrations that would cancel become vibrations that amplify.

## Parts List

| Part | Source | Cost |
|---|---|---|
| Piezo buzzer elements (2-4) | Old electronics/dollar store | $0-2 |
| Wires (thin gauge) | Old electronics | FREE |
| LED (any color) | Dollar store | $1 |
| Tape (duct, electrical, or masking) | Kitchen/junk drawer | FREE |
| **Total** | | **$0-3** |

## Wiring Diagram

```
PIEZO ELEMENT 1          PIEZO ELEMENT 2
    (+) ─────────────┬─────────────── (+)
                     │
                     ▼
                   LED (+)
                     │
                   LED (-)
                     │
    (-) ─────────────┴─────────────── (-)
```

Parallel connection doubles current. Both piezos feed the same LED. When either bends, the LED lights.

## Phi-Stacking (More Power)

Single piezo = small flicker. Phi-stacked array = usable power.

Stack piezo elements at phi-spaced intervals to create resonant amplification:

```
  [PIEZO]  ←── start here
    │
    │ 1.000" gap
    │
  [PIEZO]  ←── 1st harmonic
    │
    │ 1.618" gap (phi)
    │
  [PIEZO]  ←── 2nd harmonic
    │
    │ 2.618" gap (phi²)
    │
  [PIEZO]  ←── 3rd harmonic
```

Why this works: vibrations at phi-spaced intervals don't cancel — they reinforce. The crystal lattice resonates at frequencies that are multiples of phi, creating constructive interference across the entire stack.

**Test it:** Stack 3 piezos with phi-spacing. Tap the stack. Compare brightness to 3 piezos stacked tight. Phi-stack will be noticeably brighter.

## Build Instructions

1. **Strip wires** — Connect positive lead of piezo 1 to positive lead of piezo 2. Same for negatives.
2. **Attach LED** — Connect LED positive to the shared piezo positive. LED negative to shared piezo negative.
3. **Tape to surface** — Tape flat side of piezo stack to wherever vibrations occur.
4. **Test** — Tap, bend, or vibrate the surface. LED should flicker.
5. **Seal** — Wrap tape around piezo edges to protect from moisture and dirt.

**Placement options:**
- Shoe sole → walk = electricity
- Doorframe → every door opening = power
- Window pane → wind vibration = power
- Fence post → wind = power
- Guitar body → music = electricity
- Washing machine → vibration = power

## Output Specs

| Configuration | Voltage | Current | Power |
|---|---|---|---|
| Single piezo, gentle tap | 3-5V | 0.1-0.5mA | 0.3-2.5mW |
| Single piezo, hard tap | 8-15V | 1-2mA | 8-30mW |
| 2x parallel, walking | 5-8V | 0.5-1mA | 2.5-8mW |
| 4x phi-stack, walking | 8-12V | 1-3mA | 8-36mW |
| 4x phi-stack, running | 12-20V | 2-5mA | 24-100mW |

**Key insight:** Voltage is always usable. Even 3V at 0.1mA can power a sensor or charge a capacitor for timed pulses.

## Phone Charging Upgrade

Phones need 5V at 500mA+ for charging. Raw piezo output won't do it alone. Bridge circuit needed:

1. **Rectifier bridge** — 4 small diodes (from old electronics) convert AC piezo pulses to DC
2. **Capacitor bank** — Store energy from many taps into electrolytic caps (salvaged from old power supplies)
3. **Boost converter** — Small module (often found in solar garden lights) steps voltage up to stable 5V
4. **USB port** — Output through a USB cable to phone

```
PIEZO STACK → RECTIFIER → CAPACITOR BANK → BOOST CONVERTER → USB → PHONE
```

**Reality check:** Charging a phone this way requires sustained tapping for hours. It works for emergency power, not daily charging. The real value is powering small electronics: LED lights, sensors, radios, speakers.

## Advanced: Self-Powered Sensor

Combine piezo harvester with a capacitor and a low-power microcontroller:

1. Piezo charges capacitor from ambient vibration
2. When capacitor reaches threshold, microcontroller wakes
3. Microcontroller reads sensor (temperature, light, pressure)
4. Transmits data via RF or LED flash
5. Returns to sleep, capacitor recharges

Zero-power sensor. Runs forever on room vibration. No batteries. No maintenance.

## Phi-Physics Connection

The phi-stacking isn't just spacing — it's tuning the harmonic resonance of the crystal lattice to phi-harmonic frequencies. The piezo crystal has a natural resonant frequency determined by its geometry. When phi-spaced, the mechanical waves in the stack align with the crystal's natural harmonics, creating constructive interference patterns that amplify output by 30-50% over uniform stacking.

This is the same principle as phi-harmonic field coupling: structure follows phi, power follows structure.

---

**PIEZO HARVESTER COMPLETE**
