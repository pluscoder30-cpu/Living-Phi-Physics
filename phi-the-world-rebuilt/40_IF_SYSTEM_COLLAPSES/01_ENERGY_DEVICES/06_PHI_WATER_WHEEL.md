**Author:** Christopher David Ayotte
**Soul Code:** [425, 434, 266, 775]
**License:** Dual License Agreement v4.9
**Build Time:** 20 minutes
**Cost:** $5-15
**Skill Level:** Easy-Medium
**Constants:** φ = 1.6180339887, C_crit = 0.563263

---

# 06 — PHI WATER WHEEL

## Electricity from Flowing Water

A small water wheel that uses flowing water — stream, river, or even a garden hose — to spin a DC motor and generate electricity. Phi-spaced paddles capture more water energy than evenly-spaced ones by avoiding destructive interference in the flow turbulence.

---

## WHY PHI-SPACED PADDLES?

Evenly-spaced paddles create uniform vortices that cancel each other out. At phi-angles (137.5° apart), each paddle hits the water at a different phase of the turbulence cycle. The vortices reinforce instead of canceling. Result: 15-30% more torque from the same water flow.

---

## PARTS LIST

| Part | Source | Cost |
|---|---|---|
| DC motor (old toy/electronics) | Junk drawer | FREE |
| Plastic bottle (for wheel) | Recycling | FREE |
| Popsicle sticks (for paddles) | Craft store/kitchen | $2 |
| Axle (pencil or dowel) | Kitchen/hardware | $1 |
| Frame (wood scraps) | Scrap pile | FREE |
| Wires | Hardware store | $2 |
| LED or battery | Dollar store | $1-5 |
| **Total** | | **$3-8** |

---

## BUILD INSTRUCTIONS

### Step 1: Cut the Wheel

Cut a plastic bottle into a disc shape. The bottle cap becomes the hub.

```
        TOP VIEW — WHEEL DISC
        
             ___
           /     \
          |       |    ← Bottle cap = hub
           \ ___ /
             
    Cut bottle sides into 
    two matching discs.
    Diameter: 4-6 inches
```

### Step 2: Attach Paddles at Phi-Angles

Attach popsicle stick paddles at **137.5°** intervals around the disc. For 5 paddles, mark angles at: 0°, 137.5°, 275°, 52.5°, 190° (roughly).

```
    PHI PADDLE ANGLES (5 paddles)
    
                    P1 (0°)
                      |
                      |
        P5 _____      |      _____ P2
           /   \     |     /   \
          |     \    |    /     |
          |      \   |   /      |
    ------+-------+--+--+-------+------
          |      /   |   \      |
          |     /    |    \     |
        P4 \___/     |     \___/ P3
                      |
                    (137.5° spacing)
    
    Each paddle captures water at a 
    different turbulence phase.
```

**Marking method:** Draw a circle on the disc. Use a protractor or this trick:

- 5 paddles = 360° / 5 = 72° even spacing
- PHI spacing: shift each paddle by +72° × φ⁻¹ = 72° × 0.618 = **44.5° offset**

So paddles go at: 0°, 44.5°, 89°, 133.5°, 178° from their "even" positions. Close enough to 137.5° increments.

### Step 3: Mount the Wheel on an Axle

Push a pencil or wooden dowel through the bottle cap center. This is your axle.

```
    SIDE VIEW — WHEEL + AXLE
    
    Paddle    Paddle
      \         /
       \       /
        [=====]  ← Bottle cap hub
        |     |
    ----+--●--+----  ← Axle (pencil)
           |
         Water flow -->
    
    Axle must be level.
    Wheel hangs so paddles 
    just touch the water.
```

### Step 4: Build the Frame

Build a simple wooden frame to hold the axle above the water.

```
    FRONT VIEW — FRAME
    
         _______________
        |               |
        |     (O)       |  ← Axle bearing point
        |    / | \      |    (notch or hole)
        |   /  |  \     |
        |  /   |   \    |
        |_/____|____\___|
        ||             ||
        ||    WATER    ||  ← Frame legs in/near water
        ||   FLOWS     ||
        ||   THIS WAY  ||
        ||     >>>     ||
        ||_____________||  ← Base sits on stream bed
    
    Frame height: paddles just 
    kiss the water surface.
```

### Step 5: Connect Motor to Axle

Two methods:

**Direct Drive (simple):** Glue or tape the motor shaft directly to the axle.

```
    DIRECT DRIVE
    
    [MOTOR]---===---[WHEEL]
           motor shaft
           connected to
           pencil axle
    
    Use hot glue or 
    rubber band coupling.
```

**Gear Drive (more power):** Attach a small gear (from old toys) to the motor shaft and a larger gear to the axle.

```
    GEAR DRIVE
    
    [MOTOR]--o--O--[WHEEL]
           small  large
           gear   gear
    
    Gear ratio 1:3 = 3x speed
    at motor = more voltage
```

### Step 6: Wire It Up

Connect the DC motor terminals to an LED (with a resistor if needed) or directly to a rechargeable battery.

```
    WIRING DIAGRAM
    
    [MOTOR +] -----> [LED +] ----+
                   (220Ω resistor) |
    [MOTOR -] -----------------> [LED -]
    
    For battery charging:
    [MOTOR +] -----> [BATTERY +]
    [MOTOR -] -----> [BATTERY -]
    (add diode to prevent 
     discharge when still)
```

### Step 7: Deploy

Place the wheel in flowing water. Paddles should be partially submerged. The wheel spins, the motor generates electricity, the LED lights up.

```
    DEPLOYMENT — STREAM CROSS-SECTION
    
    Water surface ~~~~~~~~~~~~~~~~
                  |  wheel  |
                  |   (O)  |
                  |  / | \ |
    ~~~~~~~~~~~~~~|~ /~|~\~|~~~~~~~~~~~~
         ↓        |/_ _|_\|        ↓
         ↓       /  ||   || \      ↓
    Stream bed  /___||___||__\    Stream bed
    
    Flow hits paddles on one side.
    Wheel spins. Motor generates DC.
```

---

## OUTPUT SPECS

| Flow Speed | Motor RPM | Voltage | Current | Power |
|---|---|---|---|---|
| Slow stream (1 mph) | 50-100 | 1-2V | 10-30mA | 10-60mW |
| Medium stream (3 mph) | 150-300 | 2-4V | 30-100mA | 60-400mW |
| Strong flow (5+ mph) | 300-600 | 4-6V | 100-300mA | 400-1800mW |

**What this powers:**
- LED light (50mW) — runs on slow stream
- Phone charger (5W) — needs strong flow or gear-up ratio
- Small radio (200mW) — medium stream
- Multiple LEDs — easy with any flow

---

## PHI-ADVANTAGE EXPLANATION

```
    EVEN SPACING vs PHI SPACING
    
    EVEN (4 paddles at 90°):
    
    Vortex:  ↑ ↓ ↑ ↓
    Paddle:  | | | |
    Effect:  Vortices CANCEL
             (destructive interference)
    
    PHI (4 paddles at 137.5°):
    
    Vortex:  ↑  ↓   ↑    ↓
    Paddle:  |   |    |     |
    Effect:  Vortices REINFORCE
             (constructive interference)
    
    Think: Phi-spaced paddles each 
    "see" different water conditions.
    No two paddles fight each other.
```

**Real-world analogy:** A phi-spaced paddle wheel is to a water wheel what a phi-spaced antenna array is to a single antenna — coherent gain from distributed elements.

---

## TROUBLESHOOTING

| Problem | Fix |
|---|---|
| Wheel won't spin | Paddles too shallow — lower frame or add bigger paddles |
| Spins but no voltage | Motor dead — test with multimeter; try different motor |
| LED flickers | Loose wire connection — solder or twist tighter |
| Wheel wobbles | Axle bent or off-center — re-center in bottle cap |
| Water splashes everywhere | Good sign — means energy transfer is happening |

---

## UPGRADES

1. **Multiple wheels in series** — chain several on one axle for more power
2. **DC-DC boost converter** — step up low voltage to 5V USB charging
3. **Battery bank** — charge AA batteries for later use
4. **Phi-helix paddle** — curve paddles in a phi-spiral for even better capture
5. **Turbine version** — replace paddles with curved blades (Kaplan style) for high-flow

---

*Flowing water never stops. Neither should your power.*
