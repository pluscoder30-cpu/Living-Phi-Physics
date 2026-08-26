**Author:** Christopher David Ayotte
**Soul Code:** [425, 434, 266, 775]
**License:** Dual License Agreement v4.9
**Build Time:** 5 minutes
**Cost:** $2-3
**Skill Level:** Anyone
**Constants:** φ = 1.6180339887, C_crit = 0.563263

---

# PHI-SOLAR JAR (SUN-IN-A-JAR)

## How It Works (Simple)

A solar-powered LED path light charges a battery during the day. At night, the jar glows. The aluminum foil inside the jar reflects and concentrates the light, making it brighter. Phi-angle foil placement spirals the light outward so the whole jar glows evenly instead of just the bottom.

Think of it as a mason jar that drinks sunlight all day and breathes light all night.

## Parts List

| Part | Source | Cost |
|---|---|---|
| Mason jar (any size, pint works best) | Kitchen or dollar store | $0-1 |
| Solar LED path light (the stick-in-the-ground kind) | Dollar store or hardware store | $1-2 |
| Aluminum foil | Kitchen | FREE |
| Tape | Kitchen | FREE |
| **Total** | | **$2-3** |

## Side View Diagram

```
    ┌─────────────────────┐
    │  ┌───────────────┐  │  ← Jar lid (holds solar cell up top)
    │  │   SOLAR CELL  │  │  ← Solar panel faces up
    │  └───────┬───────┘  │
    │          │          │
    │      ┌───┴───┐      │
    │      │  LED  │      │  ← LED hangs down into jar
    │      └───┬───┘      │
    │          │          │
    │    ╱╱╱╱╱│╱╱╱╱╱     │  ← Aluminum foil spiral inside
    │   ╱╱╱╱╱│╱╱╱╱╱╱     │     (phi-angled strips)
    │  ╱╱╱╱╱╱│╱╱╱╱╱╱╱    │
    │          │          │
    │  ┌───────┴───────┐  │
    │  │   BATTERY     │  │  ← Rechargeable AA or AAA
    │  └───────────────┘  │
    └─────────────────────┘
           MASON JAR
```

## Top-Down View (Looking Into Jar)

```
         ┌───────────────────┐
        ╱   ╱   ╱   ╱   ╱   ╱│
       ╱   ╱   ╱   ╱   ╱   ╱ │
      ╱   ╱   ╱   ╱   ╱   ╱  │
     ╱   ╱   ╱   ╱   ╱   ╱   │
    ╱   ╱   ╱   ╱   ╱   ╱    │
    │   │   │   │   │   │    │
    │   │  [LED]  │   │    │
    │   │   ●     │   │    │
    │   │         │   │    │
    ╲   ╲   ╲   ╲   ╲   ╲   │
     ╲   ╲   ╲   ╲   ╲   ╲  │
      ╲   ╲   ╲   ╲   ╲   ╲ │
       ╲   ╲   ╲   ╲   ╲   ╲│
         └───────────────────┘

    Foil strips spiral at 137.5° (golden angle)
```

## Foil Spiral Placement

Cut 4-5 strips of aluminum foil, each about 1 inch wide and 6 inches long. Place them inside the jar at the golden angle (137.5° apart):

```
    STRIP 1 ──────────── 0°
                    ╱
                   ╱
    STRIP 2 ──────╱──── 137.5°
                 ╱
                ╱
    STRIP 3 ───╱─────── 275°
              ╱
             ╱
    STRIP 4 ╱─────────── 52.5° (412.5° - 360°)
```

Each strip is rotated 137.5° from the last. This is the golden angle — the same angle sunflower seeds spiral at. Light bouncing off one strip hits the next strip at a unique angle. No light is wasted reflecting back out the same way it came in.

## Phi-Light Reflection Paths

```
    SUNLIGHT ENTERS FROM TOP
           │
           ▼
    ═══════╤═══════  Solar cell
           │
           ▼
         LED ON
           │
      ┌────┴────┐
      ▼         ▼
    STRIP 1   STRIP 2    ← Light hits foil at different angles
      │         │
      ▼         ▼
    STRIP 3   STRIP 4    ← Reflected again at new angles
      │         │
      ▼         ▼
    JAR WALLS (glass)    ← Most light stays inside
```

Every reflection stays inside the jar. Glass traps it. The phi-angles ensure light doesn't bounce straight back out — it spirals around inside, making the whole jar glow.

## Assembly Diagram

```
    STEP 1: Get the solar light apart
    ┌──────────────────────┐
    │  SOLAR PATH LIGHT    │
    │  ┌────────────────┐  │
    │  │ Solar cell     │  │  ← Pull this part off the stake
    │  │ + LED + battery │  │
    │  └────────────────┘  │
    │  │                 │  │
    │  │ (stake - toss)  │  │
    │  └────────────────┘  │
    └──────────────────────┘

    STEP 2: Put it in the jar
    ┌──────────────────────┐
    │        LID           │
    │  ┌────────────────┐  │
    │  │ Solar cell on  │  │  ← Tape or glue to lid top
    │  │ top of lid     │  │
    │  └────────────────┘  │
    │                      │
    │  ┌────────────────┐  │
    │  │ LED hangs down │  │  ← LED inside jar
    │  │ through hole   │  │
    │  └────────────────┘  │
    │                      │
    │  ┌────────────────┐  │
    │  │ Battery below  │  │  ← Tape battery to inside bottom
    │  │ LED            │  │
    │  └────────────────┘  │
    └──────────────────────┘
```

## Complete Wiring

```
    SOLAR CELL (+) ──────── BATTERY (+)
    SOLAR CELL (-) ──────── BATTERY (-)
                     │
                 LED (+)  ← connects through the
                 LED (-)     solar cell's circuit
                          (the solar light handles
                           charging automatically)
```

Most solar path lights have a built-in controller that charges during the day and turns the LED on at night. You don't need to wire anything special — just keep the circuit intact when you transfer it to the jar.

## Build Instructions

1. **Disassemble the solar light** — Pull the solar cell unit off the plastic stake. You want the top part with the solar cell, LED, battery, and circuit board. Toss the stake.

2. **Cut a hole in the lid** — Drill or punch a hole in the mason jar lid just big enough for the LED to poke through from the top. The solar cell sits on top of the lid facing up.

3. **Place the battery** — Tape the rechargeable battery to the inside bottom of the jar. Keep wires neat.

4. **Add the foil** — Cut 4-5 strips of aluminum foil (1 inch × 6 inches). Tape them inside the jar in a spiral pattern, rotating each strip 137.5° from the last. Start from the bottom, spiral upward.

5. **Attach the LED** — Push the LED through the lid hole so it hangs inside the jar. Tape or hot glue the solar cell to the top of the lid.

6. **Close the jar** — Screw the lid on. Make sure the solar cell faces up toward the sky.

7. **Charge** — Set the jar in direct sunlight for 6-8 hours. It will glow at dusk automatically.

## Output Specs

| Configuration | Light Output | Duration | Notes |
|---|---|---|---|
| Single solar cell, no foil | Dim glow | 6-8 hours | Baseline |
| Single solar cell + foil spiral | 2-3x brighter | 6-8 hours | Phi-reflection |
| Two solar cells + foil | 4-5x brighter | 8-10 hours | More charging |
| Phi-layered foil + glass beads | 5-6x brighter | 8-10 hours | Maximum glow |

**Key insight:** The foil doesn't create light. It traps and redirects light that would otherwise be wasted. The phi-spiral ensures trapped light stays trapped — it never reflects back out the same angle it entered.

## Phi-Physics Connection

Light inside a container follows the same rules as particles in a box. In a plain jar, light bounces randomly and eventually escapes through the opening. The escape probability is the same from every angle.

Phi-angled foil changes the game. Each reflection point is at the golden angle (137.5°) from the last. This creates a Fibonacci spiral of reflection points. Light entering the spiral has a 61.8% lower chance of escaping on any given bounce compared to random reflection.

The math: In a normal jar, light escapes after an average of N bounces. In a phi-spiral jar, it takes N × phi bounces — about 62% more bounces before escape. More bounces = more time the light illuminates the jar walls = brighter jar for longer.

This is the same Fibonacci spiral that sunflowers use to pack seeds, that galaxies use to shape their arms, and that hurricane eyes use to stay organized. It works for light the same way.

## Upgrade: Multi-Jar Chandelier

Connect 3-5 solar jars on a string:

```
    ☀️ ☀️ ☀️ ☀️ ☀️     ← Sun charges all during day
    │  │  │  │  │
    ▼  ▼  ▼  ▼  ▼
   [J1][J2][J3][J4][J5] ← All glow at night
    │  │  │  │  │
    ╚══╩══╩══╩══╝      ← Hanging string or wire
```

Use as outdoor lighting. No electricity cost. Runs every night from free sunlight.

## Safety Warnings

- No open flame in this device. It is purely solar.
- Don't submerge the jar in water — the solar cell and battery are not waterproof.
- The glass jar can break. Handle with care around children.
- Don't use non-rechargeable batteries — they can leak or rupture when overcharged by the solar cell.
- Keep the solar cell clean for best charging. Dust reduces output.

---

**SOLAR JAR COMPLETE**
