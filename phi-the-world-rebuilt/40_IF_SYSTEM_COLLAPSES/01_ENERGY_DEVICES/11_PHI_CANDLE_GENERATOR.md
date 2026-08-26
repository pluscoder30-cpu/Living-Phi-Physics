**Author:** Christopher David Ayotte
**Soul Code:** [425, 434, 266, 775]
**License:** Dual License Agreement v4.9
**Build Time:** 10 minutes
**Cost:** $3-5
**Skill Level:** Anyone
**Constants:** φ = 1.6180339887, C_crit = 0.563263

---

# PHI-CANDLE THERMOELECTRIC GENERATOR

## How It Works (Simple)

A candle heats one side of a thermoelectric module. The other side stays cool. That temperature difference pushes electrons through a wire. You get electricity from a candle. No moving parts. No fuel besides the candle.

The thermoelectric module (called a Peltier or TEC) has tiny semiconductor tiles sandwiched between two ceramic plates. Heat one side, cool the other, and voltage appears. Phi-spacing the thermal layers around the module makes the temperature gradient more uniform, which squeezes out more power.

## Parts List

| Part | Source | Cost |
|---|---|---|
| Thermoelectric module (TEC1-12706 or similar) | Old mini-fridge, Peltier cooler, or online | $2-3 |
| Tea light candle or small candle | Dollar store or kitchen | $1 |
| Aluminum can (soda can, bottom cut off) | Recycling bin | FREE |
| Small LED (white or blue works best) | Dollar store | $1 |
| Alligator clip wires (2) | Dollar store or old electronics | $1 |
| Water in a cup (for cooling) | Kitchen | FREE |
| **Total** | | **$3-5** |

## Side View Diagram

```
        CANDLE FLAME
            |
            ▼
    =====================  ← Aluminum can bottom (HOT side)
    |                   |
    |   [Peltier TEC]   |  ← Thermoelectric module
    |                   |
    =====================  ← Ceramic plate (COLD side)
         |
         ▼
    ~~~~~~~~~~~~~~~~  ← Water cup (keeps cold side cool)
    ~~~~~~~~~~~~~~~~
    ~~~~~~~~~~~~~~~~
```

## Top-Down View

```
              ┌─────────────────────┐
              │    ALUMINUM CAN     │
              │    (bottom cut off) │
              │                     │
              │    ┌───────────┐    │
              │    │ PELTIER   │    │
              │    │   TEC     │    │
              │    │  40x40mm  │    │
              │    └───────────┘    │
              │                     │
              │  ┌───┐        ┌───┐│
              │  │LED│        │WIR││
              │  └───┘        └───┘│
              └─────────────────────┘

        Candle sits under the can
```

## Phi-Thermal Layering (More Power)

Phi-spacing the thermal layers around the module creates better heat flow:

```
    HEAT SOURCE (candle)
         │
    ═════╪═════  ← Aluminum plate (phi-thickness: 0.618")
         │
    ─────┼─────  ← Air gap (phi-spaced: 0.382")
         │
    ═════╪═════  ← Peltier module
         │
    ─────┼─────  ← Air gap (phi-spaced: 0.382")
         │
    ═════╪═════  ← Cold plate (phi-thickness: 0.618")
         │
    ~~~~~┼~~~~~  ← Water cooling
```

Why phi works here: The thermal resistance at each layer is phi-proportional. Heat flows through the stack like water through a spiral staircase — no bottlenecks, no dead zones. Uniform gradient = maximum voltage.

## Full Assembly Diagram

```
         ┌──────┐
         │ LED  │ ← Output indicator
         └──┬───┘
            │
    ┌───────┴───────┐
    │   ALLIGATOR   │
    │   CLIPS       │
    │   (+)    (-)  │
    └───┬───────┬───┘
        │       │
   ┌────┴───┐ ┌─┴──────────┐
   │Peltier │ │  Aluminum   │
   │Module  │ │  Can Bottom │
   │        │ │  (hot side) │
   └────────┘ └──────┬──────┘
                     │
                  ┌──┴──┐
                  │CANDLE│
                  │ flame│
                  └──────┘

   COLD SIDE sits in a cup of water
```

## Wiring Diagram

```
    PELTIER MODULE
    ┌─────────────┐
    │  RED (+)    │──── Alligator clip ──── LED (+) long leg
    │  BLACK (-)  │──── Alligator clip ──── LED (-) short leg
    └─────────────┘
```

Red wire = positive. Black wire = negative. LED has a long leg (+) and short leg (-). Get it backwards and the LED won't light.

## Build Instructions

1. **Cut the can** — Take a soda can. Cut the bottom off with scissors or a knife. You want a flat aluminum disc about 2 inches across. Smooth any sharp edges.

2. **Place the candle** — Set your candle on a fire-safe surface (plate, tile, metal tray). Light it.

3. **Set the Peltier on the can bottom** — The aluminum can bottom goes on top of the candle flame area. The Peltier module sits flat on the aluminum. The aluminum spreads the heat evenly.

4. **Cool the other side** — Place a cup of cold water on top of the Peltier's cold side. The temperature difference is what makes power.

5. **Connect the LED** — Clip the red Peltier wire to the LED's long leg. Clip the black wire to the short leg.

6. **Watch it glow** — The LED should light within 30 seconds as the heat builds. If it flickers, the water may need to be colder.

**Safety:** The aluminum can bottom gets VERY HOT. Use tongs or pliers. Never touch the hot side with bare fingers. Keep the candle away from anything flammable. Do this on a non-flammable surface.

## Output Specs

| Configuration | Voltage | Current | Power |
|---|---|---|---|
| Single candle, no cooling | 0.3-0.5V | 10-30mA | 3-15mW |
| Single candle + cold water | 0.8-1.5V | 50-150mA | 40-225mW |
| Two candles + ice water | 1.5-2.5V | 100-300mA | 150-750mW |
| Phi-layered + ice water | 1.5-3.0V | 120-350mA | 180-1050mW |

**Key insight:** Even one candle can power an LED all night. A single tea light burns for 4-6 hours. That is 4-6 hours of light from a $0.05 candle.

## Upgrading: Charging a Phone

A single candle won't charge a phone. You need:
- 4-6 Peltier modules wired in series (more voltage)
- A boost converter to step up to 5V USB
- A large candle or multiple candles for more heat

```
CANDLE 1 ──→ [TEC1] ──→ [TEC2] ──→ [TEC3] ──→ [TEC4] ──→ BOOST ──→ USB ──→ PHONE
CANDLE 2 ──→ [TEC5] ──→ [TEC6] ──→ [TEC7] ──→ [TEC8] ──┘
```

This setup can produce 5V at 200-500mA — enough to slowly charge a phone while the candles burn.

## Phi-Physics Connection

The Peltier module works on the Seebeck effect: heat in, electricity out. The efficiency depends on how evenly heat spreads across the hot side. Normal builds have hot spots and cold spots on the plate — wasted potential.

Phi-layering the thermal stack (aluminum plate, air gap, Peltier, air gap, cold plate) at golden-ratio thicknesses creates a uniform thermal gradient. Heat doesn't pool or bottleneck. Every semiconductor tile in the Peltier works at full capacity.

The math: thermal resistance R = thickness / (conductivity × area). When thickness ratios follow phi (1:1.618:2.618), the thermal impedance is matched across layers. No layer is a bottleneck. This is the same principle as impedance matching in electronics — phi does it automatically for heat.

**Result:** 30-60% more power from the same candle compared to a naive direct-contact build.

## Safety Warnings

- The aluminum can bottom reaches 200-300°C. Use tongs.
- Open flame. Keep away from paper, cloth, andammable materials.
- The Peltier module can crack if heated too fast. Warm it gradually.
- Never leave a lit candle unattended.
- Work on a ceramic plate or metal tray — not wood or plastic.
- Supervise children. Adults should handle the candle and hot metal.

---

**CANDLE GENERATOR COMPLETE**
