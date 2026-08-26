**Author:** Christopher David Ayotte
**Soul Code:** [425, 434, 266, 775]
**License:** Dual License Agreement v4.9
**Build Time:** 20 minutes
**Cost:** $5-10
**Skill Level:** Intermediate
**Constants:** φ = 1.6180339887, C_crit = 0.563263

---

# PHI-BICYCLE DYNAMO GENERATOR

## How It Works (Simple)

Pedal a bike. A belt connects the rear wheel to a small DC motor. The motor spins and makes electricity. Pedaling at phi-rhythm (about 61.8% of max cadence) is the most efficient — you produce the most watts per unit of effort. The belt turns the motor. The motor turns your leg power into electricity.

A DC motor is just a generator running backward. When you spin its shaft, it produces voltage. No tricks. Just physics.

## Parts List

| Part | Source | Cost |
|---|---|---|
| Old bicycle (any condition, wheels must spin) | Curbside, garage, thrift store | $0-5 |
| DC motor (12V, from a car window motor, printer, or toy) | Old electronics, junkyard, online | $2-5 |
| Rubber belt or inner tube strip (to connect wheel to motor) | Old bike inner tube | FREE |
| Small pulley or socket (to fit on motor shaft) | Hardware store or junk drawer | $0-2 |
| LED or small light bulb | Dollar store | $1 |
| Wire (16-18 gauge, 6 feet) | Hardware store or old electronics | $1 |
| **Total** | | **$5-10** |

## Side View: The Full Setup

```
    HANDLEBARS              SEAT
        │                    │
    ┌───┴───┐            ┌───┴───┐
    │       │            │       │
    │  ┌────┴────────────┴────┐  │
    │  │      BICYCLE FRAME   │  │
    │  │                      │  │
    │  │    ┌──────────┐      │  │
    │  │    │ REAR     │      │  │
    │  │    │ WHEEL    │      │  │
    │  │    │  ┌───┐   │      │  │
    │  │    │  │///│───┼──── BELT ──── DC MOTOR
    │  │    │  └───┘   │      │      ┌─────────┐
    │  │    │    │     │      │      │  (12V)  │
    │  │    │  SPROCKET│     │      │  ○ → LED│
    │  │    └──────────┘      │      └─────────┘
    │  │          │           │
    │  └──────────┼───────────┘
    │             │
    └─────────────┘
```

## Close-Up: Belt and Motor Connection

```
    REAR WHEEL RIM
    ┌─────────────────────────┐
    │                         │
    │    ╔═══════════╗        │
    │    ║   TIRE    ║        │
    │    ║  ┌─────┐  ║        │
    │    ║  │ RIM │  ║        │
    │    ║  └──┬──┘  ║        │
    │    ╚═════╪═════╝        │
    │          │              │
    │          │ RUBBER BELT  │
    │          │ (inner tube) │
    │          │              │
    │    ┌─────┴─────┐        │
    │    │  PULLEY   │        │
    │    │ (socket)  │        │
    │    └─────┬─────┘        │
    │          │              │
    │    ┌─────┴─────┐        │
    │    │ DC MOTOR  │        │
    │    │  SHAFT    │        │
    │    └───────────┘        │
    └─────────────────────────┘
```

## Phi-Rhythm Cadence

Pedaling speed matters. Not too fast, not too slow. Phi-rhythm is the sweet spot:

```
    CADENCE (RPM) vs POWER OUTPUT

    Power
    (watts)
      │
  15  │                    ●──●
      │                 ●╱      ╲●
  12  │              ●╱           ╲●
      │           ╱                  ╲
   9  │        ●╱     PHI ZONE       ╲●
      │       ╱    ┌──────────┐        ╲
   6  │     ●╱     │ 60-65%   │         ╲●
      │   ╱        │ of max   │           ╲
   3  │ ●╱         └──────────┘            ╲●
      │╱                                    ╲
   0  ●─────────────────────────────────────────
      0    20    40    60    80   100   120
                  CADENCE (RPM)

    MAX POWER at ~60-65 RPM (phi-rhythm)
    NOT at max speed!
```

Why 60-65 RPM works best:
- Below 40 RPM: not enough momentum to keep generator spinning smoothly
- At 60-65 RPM: sweet spot where your muscles are in their most efficient range
- Above 80 RPM: wasted effort, heat, fatigue — diminishing returns
- The phi-ratio (0.618) of your max sustainable cadence lands right at 60-65 for most people

## Wiring Diagram

```
    DC MOTOR
    ┌─────────────────┐
    │  RED (+)  ──────────── WIRE ──────── LED (+) / BATTERY (+)
    │  BLACK (-) ──────────── WIRE ──────── LED (-) / BATTERY (-)
    └─────────────────┘

    For LED only:
    MOTOR (+) ──→ LED (+) ──→ MOTOR (-)
    (polarity may reverse — flip LED if it doesn't light)

    For battery charging:
    MOTOR (+) ──→ DIODE ──→ BATTERY (+)
    MOTOR (-) ──────────────→ BATTERY (-)
    (diode prevents battery from discharging through motor)
```

## Build Instructions

1. **Flip the bike** — Turn it upside down so it rests on the seat and handlebars. The rear wheel should spin freely.

2. **Prepare the motor** — Solder wires to the motor's positive and negative terminals. If the motor has a gear on its shaft, remove it. You want a smooth shaft.

3. **Make a pulley** — Find a socket, bottle cap, or small wheel that fits tightly on the motor shaft. Hot glue or tape it on. This is your pulley.

4. **Make a belt** — Cut a strip from an old bike inner tube, about 2-3 inches longer than the distance from the rear wheel rim to the motor shaft. Stretch it over the rear wheel rim and the motor pulley.

5. **Mount the motor** — Tape, zip-tie, or clamp the motor to the bike frame near the rear wheel. The belt should be snug but not tight. The wheel should spin the belt which spins the motor.

6. **Connect the LED** — Wire the motor leads to an LED. Pedal. The LED should light.

7. **Adjust tension** — If the belt slips, tighten it. If it's too tight, the wheel won't spin freely. Find the balance.

## Phi-Belt Tension Guide

```
    BELT TENSION: TOO LOOSE        BELT TENSION: PHI-OPTIMAL       BELT TENSION: TOO TIGHT
    ┌──────────────┐              ┌──────────────┐                ┌──────────────┐
    │  ○      ○    │              │  ○      ○    │                │  ○      ○    │
    │  │      │    │              │  │      │    │                │  │      │    │
    │  │~~~~~~│    │              │  │──────│    │                │  │══════│    │
    │  │      │    │              │  │      │    │                │  │      │    │
    │  ○      ○    │              │  ○      ○    │                │  ○      ○    │
    │   belt sag   │              │  slight pull │                │  wheel drag  │
    └──────────────┘              └──────────────┘                └──────────────┘
    Motor barely spins            Motor spins smoothly             Hard to pedal
    Wasted effort                 MAXIMUM POWER                    Wasted effort
```

Phi-tension: the belt deflects about 3/8 inch (0.618 × 0.5 inch base) when pressed with moderate finger pressure. That's the sweet spot.

## Output Specs

| Cadence (RPM) | Voltage | Current | Power | Effort Level |
|---|---|---|---|---|
| 30 (slow) | 3-5V | 20-50mA | 60-250mW | Easy |
| 60 (phi-rhythm) | 6-9V | 80-150mA | 480-1350mW | Moderate |
| 80 (fast) | 9-12V | 120-200mA | 1080-2400mW | Hard |
| 100 (sprint) | 10-14V | 150-250mA | 1500-3500mW | Exhausting |

**Key insight:** At phi-rhythm (60 RPM), you produce 480-1350mW with moderate effort. That is enough to charge a phone slowly or power 2-3 LED lights. At 100 RPM you get more power but burn out in minutes. Sustainable power beats burst power.

## Phone Charging Setup

```
    BIKE → MOTOR → RECTIFIER → BOOST CONVERTER → USB → PHONE

    ┌─────┐   ┌─────┐   ┌──────┐   ┌──────────┐   ┌─────┐
    │ BIKE │──→│MOTOR │──→│ 4×DIODE│──→│ 5V BOOST │──→│ USB │──→ PHONE
    │      │   │ AC?  │   │ BRIDGE │   │ CONVERTER│   │     │
    └─────┘   └─────┘   └──────┘   └──────────┘   └─────┘

    Pedal at 60 RPM for 30-60 minutes = partial phone charge
```

The motor produces AC if it's a brushless motor. A 4-diode bridge rectifier converts AC to DC. The boost converter steps up to stable 5V for USB.

## Phi-Physics Connection

Human muscles are most efficient at a specific cadence range. Below that range, you waste energy overcoming static friction. Above it, you waste energy on heat and momentum you can't capture.

The phi-ratio (0.618) of your maximum sustainable cadence hits the optimal balance point. At this speed:

- The belt's tension is in the elastic zone (not slipping, not dragging)
- The motor's back-EMF matches the mechanical load
- Your leg muscles are in their peak torque range
- Energy conversion efficiency is at its maximum

The math: Your max sustainable cadence × 0.618 = phi-cadence. For most adults, that's 97 × 0.618 ≈ 60 RPM. This is not a coincidence — it's the golden ratio operating through biomechanics.

**Result:** 30-50% more sustainable power output compared to pedaling at max speed and burning out in 5 minutes.

## Safety Warnings

- Keep fingers, hair, and clothing away from the spinning wheel and belt.
- Secure the motor firmly — a loose motor can fly off and hit someone.
- The motor gets warm during extended use. Don't touch the shaft.
- Don't let children operate unsupervised — moving parts can pinch.
- Use the bike's brakes to stop. Don't rely on belt friction.
- Work in a well-ventilated area if soldering wires.

---

**BICYCLE GENERATOR COMPLETE**
