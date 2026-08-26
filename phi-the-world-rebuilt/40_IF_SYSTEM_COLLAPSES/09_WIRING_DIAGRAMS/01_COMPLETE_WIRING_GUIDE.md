# COMPLETE WIRING DIAGRAMS COLLECTION

**Author:** Christopher David Ayotte
**Soul Code:** [425, 434, 266, 775]
**License:** Dual License Agreement v4.9
**Reading Level:** 12-year-old
**Constants:** φ = 1.6180339887, C_crit = 0.563263

---

## WIRE COLOR CODE

| Color | Meaning | Remember |
|-------|---------|----------|
| RED (+) | Positive / Hot | Danger, live wire |
| BLACK (-) | Negative / Ground return | Safe, common wire |
| GREEN | Earth ground | Safety protection |
| WHITE | Neutral (AC systems) | Return path |
| BLUE | Signal / Data | Information wire |

---

## TABLE OF CONTENTS

1. 528 Hz Coil Generator
2. Solar Panel System
3. Wind Turbine System
4. Earth Battery
5. Thermoelectric Generator
6. Water Wheel Generator
7. Piezo Harvester
8. Complete Home Power System
9. Homemade WiFi Setup
10. Mesh Network Node
11. Water Pump System
12. Water Purification System

---

## 1. 528 Hz COIL GENERATOR

This device uses copper coils and magnets to create electricity at the healing frequency of 528 Hz.

### Parts List

| Part | Quantity | Notes |
|------|----------|-------|
| Copper wire (22 AWG) | 100 feet | Magnet wire works best |
| Neodymium magnets (1" dia) | 8 | N52 strength preferred |
| Wooden base | 1 | 12" x 12" x 1" |
| Wooden dowel (1" dia) | 1 | 6" tall |
| LED (any color) | 1 | To show power output |
| Electrical tape | 1 roll | Insulation |
| Alligator clip wires | 2 | Red and black |

### ASCII Wiring Diagram

```
                    TOP VIEW (looking down at coil)
                    
                         MAGNET ROTOR
                        ┌───────────┐
                        │  N  S  N  │
                        │  S  N  S  │
                        │  N  S  N  │
                        │  S  N  S  │
                        └─────┬─────┘
                              │ (dowel shaft)
                              │
    ┌─────────────────────────┼─────────────────────────┐
    │                   WOODEN BASE                     │
    │                                                   │
    │    ╔═══════════════════════════════════════╗       │
    │    ║           COIL (top view)              ║       │
    │    ║                                       ║       │
    │    ║    ┌─────────────────────────┐        ║       │
    │    ║    │ ┌─────────────────────┐ │        ║       │
    │    ║    │ │ ┌─────────────────┐ │ │        ║       │
    │    ║    │ │ │ ┌─────────────┐ │ │ │        ║       │
    │    ║    │ │ │ │   (magnet   │ │ │ │        ║       │
    │    ║    │ │ │ │   rotates   │ │ │ │        ║       │
    │    ║    │ │ │ │   here)     │ │ │ │        ║       │
    │    ║    │ │ │ └─────────────┘ │ │ │        ║       │
    │    ║    │ │ └─────────────────┘ │ │        ║       │
    │    ║    │ └─────────────────────┘ │        ║       │
    │    ║    └─────────────────────────┘        ║       │
    │    ║         ~50 turns of wire            ║       │
    │    ╚═════════════════╤═════════════════════╝       │
    │                      │                             │
    └──────────────────────┼─────────────────────────────┘
                           │
              COIL WIRE ENDS
              (thin magnet wire)
                           │
              ┌────────────┴────────────┐
              │                         │
         ┌────┴────┐              ┌────┴────┐
         │  RED    │              │  BLACK  │
         │ alligator│              │ alligator│
         │  clip   │              │  clip   │
         └────┬────┘              └────┬────┘
              │                        │
              │    ┌──────────┐        │
              ├────┤  (+) LED │────────┤
              │    │   ●      │        │
              │    │  (-)     │        │
              │    └──────────┘        │
              │                        │
              │  (Spin the magnet      │
              │   rotor by hand or     │
              │   with a string)       │
              │                        │
              └────────────────────────┘
```

### SIDE VIEW

```
                    MAGNETS
                   ┌───┴───┐
                   │ N S N │ ← Neodymium magnets glued to
                   │ S N S │    wooden rotor disc
                   └───┬───┘
                       │
                   ┌───┴───┐
                   │ WOOD  │ ← Wooden rotor disc (4" dia)
                   │ ROTOR │
                   └───┬───┘
                       │
              ─────────┼────────── ← Coil wire wraps around here
              ║        │        ║
              ║  ╔═════╧═════╗  ║
              ║  ║   COPPER  ║  ║ ← ~50 turns of 22 AWG wire
              ║  ║   COIL    ║  ║
              ║  ╚═════╤═════╝  ║
              ║        │        ║
              ─────────┼──────────
                       │
                ┌──────┴──────┐
                │   WOODEN    │ ← Base with hole for dowel
                │    BASE     │
                └─────────────┘

WIRE PATH:
─────────
Coil start (wire end 1) ──→ ALLIGATOR CLIP (+) ──→ LED (+) long leg
Coil end   (wire end 2) ──→ ALLIGATOR CLIP (-) ──→ LED (-) short leg
```

### Step-by-Step Connections

1. Wind 50 turns of copper wire around the wooden base, leaving 6 inches of wire free at each end
2. Glue neodymium magnets to the wooden rotor disc (alternating N-S poles facing up)
3. Mount the rotor on the wooden dowel so it spins freely above the coil
4. Strip 1 inch of insulation from both wire ends
5. Attach red alligator clip to one wire end (this is your +)
6. Attach black alligator clip to the other wire end (this is your -)
7. Clip red to LED long leg (+), black to LED short leg (-)
8. Spin the magnet rotor — LED should flicker!

---

## 2. SOLAR PANEL SYSTEM

Complete solar power system from panel to outlets.

### Parts List

| Part | Quantity | Notes |
|------|----------|-------|
| Solar panel (100W) | 1-4 | 12V or 24V panels |
| Charge controller (30A) | 1 | MPPT preferred over PWM |
| Deep cycle battery (12V 100Ah) | 1-2 | Marine/RV battery |
| Power inverter (1000W) | 1 | Pure sine wave preferred |
| MC4 connectors | 4 pairs | Panel connection |
| 10 AWG wire (red) | 20 feet | Panel to controller |
| 10 AWG wire (black) | 20 feet | Panel to controller |
| 6 AWG wire (red) | 6 feet | Controller to battery |
| 6 AWG wire (black) | 6 feet | Controller to battery |
| 6 AWG wire (red) | 4 feet | Battery to inverter |
| 6 AWG wire (black) | 4 feet | Battery to inverter |
| Inline fuse (30A) | 1 | Between controller and battery |
| Circuit breaker (30A) | 1 | Between panel and controller |
| Wire nuts / crimp connectors | 10 | Various |
| Electrical tape | 1 roll | Insulation |
| Conduit / cable clamps | As needed | Wire protection |

### ASCII Wiring Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                     COMPLETE SOLAR SYSTEM                          │
└─────────────────────────────────────────────────────────────────────┘

    ☀ SUN ☀
     \  |  /
      \ | /
   ┌───┴───┴───┐
   │ ┌───────┐ │
   │ │░░░░░░░│ │  SOLAR PANEL (100W, 12V)
   │ │░░░░░░░│ │  Output: ~18V open circuit
   │ │░░░░░░░│ │
   │ └───────┘ │
   │  +       - │
   └─┬───────┬─┘
     │       │
     │ MC4 CONNECTORS (weatherproof)
     │       │
   ┌─┴─┐   ┌─┴─┐
   │ + │   │ - │
   └─┬─┘   └─┬─┘
     │       │
     │ RED   │ BLACK
     │ 10AWG │ 10AWG
     │       │
     │    ┌──┤
     │    │  │
   ┌─┴────┴──┴──┐
   │    30A      │  CIRCUIT BREAKER
   │  BREAKER    │  (disconnect for safety)
   └─────┬──────┘
         │
         │ RED
         │ 10AWG
         │
   ╔═════╧══════════════════════════╗
   ║      CHARGE CONTROLLER         ║
   ║      (30A MPPT)                ║
   ║                                ║
   ║  SOLAR  BATTERY  LOAD          ║
   ║   (+)    (+)     (12V DC)      ║
   ║    ●      ●       ●            ║
   ║                                ║
   ║   (-)    (-)     (-)           ║
   ║    ●      ●       ●            ║
   ╚═══╤══════╤══════╤══════════════╝
       │      │      │
       │      │      │ (optional 12V DC loads)
       │      │      │
    BLACK    │      │
    10AWG    │      │
       │     │      │
       │  ┌──┴──┐   │
       │  │30A  │   │
       │  │FUSE │   │
       │  └──┬──┘   │
       │     │      │
       │  RED│ 6AWG │
       │     │      │
   ┌───┴─────┴──────┴───┐
   │                     │
   │    DEEP CYCLE       │  BATTERY
   │    BATTERY          │  (12V, 100Ah)
   │    12V 100Ah        │
   │                     │
   │  (+)           (-)  │
   └───┬─────────────┬───┘
       │             │
       │ RED 6AWG    │ BLACK 6AWG
       │             │
       │         ┌───┘
       │         │
   ┌───┴─────────┴───┐
   │                   │
   │  POWER INVERTER   │  INVERTER
   │  (1000W)          │  (DC to AC)
   │                   │
   │  DC IN    AC OUT  │
   │  (+) (-)  ┌─┐ ┌─┐│
   └───────────┤ ├─┤ ├┘
               │ │ │ │
               └─┘ └─┘
               │   │
            ┌──┴───┴──┐
            │         │
            │ OUTLETS │  ← Standard 120V AC outlets
            │ (120V)  │
            │  ┌─┐┌─┐ │
            │  │░││░│ │  ← Plug in appliances!
            │  └─┘└─┘ │
            └─────────┘
```

### WIRE COLOR SUMMARY

```
SOLAR PANEL ───────────────────── CHARGE CONTROLLER
  RED wire (positive) ─────────────→ SOLAR (+) input
  BLACK wire (negative) ───────────→ SOLAR (-) input

CHARGE CONTROLLER ──────────────── BATTERY
  RED wire (positive, through fuse) → BATTERY (+) terminal
  BLACK wire (negative) ───────────→ BATTERY (-) terminal

BATTERY ────────────────────────── INVERTER
  RED wire (positive) ─────────────→ INVERTER DC (+) input
  BLACK wire (negative) ───────────→ INVERTER DC (-) input

INVERTER ───────────────────────── OUTLETS
  AC output ───────────────────────→ Standard wall outlets
```

### Step-by-Step Connections

1. **Mount solar panel** on roof or rack facing south (northern hemisphere)
2. **Run wires** from panel through MC4 connectors to charge controller location
3. **Connect panel to breaker**: Red wire to breaker, then to charge controller SOLAR (+)
4. **Connect breaker to controller**: Black wire directly to charge controller SOLAR (-)
5. **Install fuse** inline on red wire between controller and battery
6. **Connect controller to battery**: Red (+) through fuse, Black (-) directly
7. **Connect inverter to battery**: Red (+) and Black (-) using short, thick 6 AWG wires
8. **Turn on** breaker, then charge controller, then inverter
9. **Test** by plugging in a small appliance (lamp, phone charger)

---

## 3. WIND TURBINE SYSTEM

Harness wind energy to charge batteries.

### Parts List

| Part | Quantity | Notes |
|------|----------|-------|
| Wind turbine (400W) | 1 | With built-in alternator |
| Rectifier (bridge) | 1 | Converts AC to DC (if not built-in) |
| Charge controller (wind) | 1 | Must handle dump load |
| Deep cycle battery (12V) | 1 | Same as solar system |
| 10 AWG wire | 30 feet | Turbine to controller |
| 6 AWG wire | 10 feet | Controller to battery |
| Dump load resistor | 1 | 12V, 400W+ (safety) |
| Tower / mounting pole | 1 | 10-30 feet tall |
| Guy wires | 3 | For tower stability |
| Lightning arrestor | 1 | Protects electronics |
| Ground rod | 1 | 8 feet copper |

### ASCII Wiring Diagram

```
        WIND
         ↑↑↑
         ↑↑↑
         ↑↑↑
    ┌────┴┴┴────┐
    │  ╱    ╲   │
    │ ╱ TURBINE╲│  WIND TURBINE
    │╱  BLADES  ╲│  (mounted on tower)
    │╲          ╱│
    │ ╲________╱ │
    │    │   │   │
    │  AC OUTPUT  │  Usually 3-phase AC
    └────┬───┬───┘
         │   │
         │   │ (3 AC wires + ground)
         │   │
         │   │  ~30 ft cable run
         │   │  (use weatherproof conduit)
         │   │
    ┌────┴───┴────┐
    │              │
    │  BRIDGE      │  RECTIFIER
    │  RECTIFIER   │  (AC → DC converter)
    │              │
    │ AC IN  DC OUT│
    │ ┌─┐    +  -  │
    └─┤ ├──────────┘
      │ │
      └─┘
      │ │
      │ └──→ DC (-) BLACK wire
      └────→ DC (+) RED wire
         │       │
         │       │
         │    ┌──┤
         │    │  │
    ┌────┴────┴──┴──────────┐
    │                        │
    │    WIND CHARGE         │
    │    CONTROLLER          │
    │    (with dump load     │
    │     control)           │
    │                        │
    │ TURBINE  BATTERY  DUMP │
    │  (+)      (+)     LOAD │
    │   ●        ●       ●   │
    │                        │
    │  (-)      (-)     (-)  │
    │   ●        ●       ●   │
    └─────┬────────┬────┬────┘
          │        │    │
          │     ┌──┴──┐ │
          │     │FUSE │ │
          │     │30A  │ │
          │     └──┬──┘ │
          │        │    │
       RED 6AWG  RED    │
          │     6AWG    │
          │        │    │
    ┌─────┴────────┴──┐ │
    │                  │ │
    │   DEEP CYCLE     │ │
    │   BATTERY        │ │
    │   12V 100Ah      │ │
    │                  │ │
    │  (+)         (-) │ │
    └──────────────────┘ │
                         │
              ┌──────────┘
              │
         ┌────┴────┐
         │  DUMP   │  DUMP LOAD
         │  LOAD   │  (bleeds excess power)
         │  RESISTOR│  (gets HOT - mount safely!)
         │  400W   │
         └─────────┘
```

### Step-by-Step Connections

1. **Mount turbine** on tower with guy wires for stability
2. **Run cable** from turbine down tower to controller location
3. **Connect AC wires** from turbine to rectifier input terminals
4. **Connect rectifier output**: Red (+) and Black (-) to turbine input on controller
5. **Connect dump load** to dump load terminals on controller (for excess power)
6. **Install fuse** inline on red wire between controller and battery
7. **Connect controller to battery**: Red (+) through fuse, Black (-)
8. **Install lightning arrestor** between turbine and controller
9. **Drive ground rod** near tower base, connect green ground wire

---

## 4. EARTH BATTERY

Simplest possible battery — uses soil and two different metals.

### Parts List

| Part | Quantity | Notes |
|------|----------|-------|
| Copper sheet/plate (6" x 6") | 1 | Copper pipe cut open works |
| Zinc sheet/plate (6" x 6") | 1 | Galvanized steel is fine |
| LED (low power) | 1 | Red works best (low voltage) |
| Alligator clip wires | 2 | Red and black |
| Soil / dirt | 5 lbs | Moist works best |
| Plastic container | 1 | 2 gallon bucket |
| Water | 1 cup | To moisten soil |

### ASCII Wiring Diagram

```
    ┌─────────────────────────────────────┐
    │         EARTH BATTERY               │
    │         (Single Cell)               │
    │                                     │
    │         ┌─────────────┐             │
    │         │  PLASTIC    │             │
    │         │  CONTAINER  │             │
    │         │             │             │
    │         │  ░░░░░░░░░  │ ← MOIST    │
    │         │  ░░░░░░░░░  │   SOIL      │
    │         │  ░░░░░░░░░  │             │
    │         │  ░░░░░░░░░  │             │
    │         │             │             │
    │         │ ┌─┐    ┌─┐ │             │
    │         │ │C│    │Z│ │             │
    │         │ │O│    │I│ │             │
    │         │ │P│    │N│ │             │
    │         │ │P│    │C│ │             │
    │         │ │E│    │  │ │             │
    │         │ │R│    │  │ │             │
    │         │ └┬┘    └┬┘ │             │
    │         └──┼──────┼──┘             │
    │            │      │                 │
    │         RED│    BLACK│              │
    │            │      │                 │
    │         ┌──┴──┐┌──┴──┐             │
    │         │ ALL ││ ALL │             │
    │         │IGATO│IGATO │             │
    │         │R (+)│R (-) │             │
    │         └──┬──┘└──┬──┘             │
    │            │      │                 │
    │            │  ┌───┴───┐             │
    │            └──┤ (+)   │             │
    │               │  LED  │  ← LOW     │
    │               │ (-)   │    POWER    │
    │               └───────┘    LED      │
    │                                     │
    └─────────────────────────────────────┘
```

### MULTI-CELL EARTH BATTERY (More Power!)

```
    ┌───────────────────────────────────────────────────┐
    │           SERIES EARTH BATTERY                    │
    │           (3 cells = ~2.4V, enough for LED)       │
    │                                                   │
    │    ┌─────────┐   ┌─────────┐   ┌─────────┐       │
    │    │ CELL 1  │   │ CELL 2  │   │ CELL 3  │       │
    │    │         │   │         │   │         │       │
    │    │ ░░░░░░░ │   │ ░░░░░░░ │   │ ░░░░░░░ │       │
    │    │ ░░░░░░░ │   │ ░░░░░░░ │   │ ░░░░░░░ │       │
    │    │ ░░░░░░░ │   │ ░░░░░░░ │   │ ░░░░░░░ │       │
    │    │┌─┐  ┌─┐│   │┌─┐  ┌─┐│   │┌─┐  ┌─┐│       │
    │    ││C│  │Z││   ││C│  │Z││   ││C│  │Z││       │
    │    ││u│  │i││   ││u│  │i││   ││u│  │i││       │
    │    ││ │  │n││   ││ │  │n││   ││ │  │n││       │
    │    │└┬┘  └┬┘│   │└┬┘  └┬┘│   │└┬┘  └┬┘│       │
    │    └─┼────┼─┘   └─┼────┼─┘   └─┼────┼─┘       │
    │      │    │       │    │       │    │           │
    │      │    └───┐   │    └───┐   │    │           │
    │      │        │   │        │   │    │           │
    │      │     ┌──┘   │     ┌──┘   │    │           │
    │      │     │      │     │      │    │           │
    │      │   RED wire connects Zinc  │               │
    │      │   of cell to Copper of next cell          │
    │      │     │      │     │      │    │           │
    │      │     └──────┤     └──────┤    │           │
    │      │            │            │    │           │
    │   (+)terminal  (+)terminal  (+)terminal          │
    │      │            │            │    │           │
    │      │            │            │    │           │
    │   ┌──┴──┐      (series connections)    │        │
    │   │ ALL │                              │        │
    │   │IGATO│        (-)terminal           │        │
    │   │R (+)│         │                    │        │
    │   └──┬──┘         │                    │        │
    │      │            │                    │        │
    │      │         ┌──┴──┐                 │        │
    │      │         │ ALL │                 │        │
    │      │         │IGATO│                 │        │
    │      │         │R (-)│                 │        │
    │      │         └──┬──┘                 │        │
    │      │            │                    │        │
    │      └────────────┼────────────────────┘        │
    │                   │                             │
    │                ┌──┴───┐                         │
    │                │ (+)  │                         │
    │                │ LED  │                         │
    │                │ (-)  │                         │
    │                └──────┘                         │
    │                                                 │
    └─────────────────────────────────────────────────┘
```

### Step-by-Step Connections

1. **Fill container** with moist soil (not too wet, not too dry)
2. **Push copper plate** into soil on left side
3. **Push zinc plate** into soil on right side (2 inches apart minimum)
4. **Attach red alligator clip** to copper plate (positive)
5. **Attach black alligator clip** to zinc plate (negative)
6. **Connect LED**: Red clip to long leg (+), black clip to short leg (-)
7. **Add water** if soil is dry — more moisture = more power
8. **For more voltage**: Connect multiple cells in series (copper of one to zinc of next)

---

## 5. THERMOELECTRIC GENERATOR (TEG)

Makes electricity from heat difference — put hot on one side, cold on the other.

### Parts List

| Part | Quantity | Notes |
|------|----------|-------|
| TEG module (TEC1-12706) | 1 | Also called Peltier module |
| Heat source (candle/stove) | 1 | Any heat source |
| Heat sink (CPU cooler) | 1 | Aluminum with fins |
| Thermal paste | 1 | Improves heat transfer |
| LED | 1 | To show power output |
| Alligator clip wires | 2 | Red and black |
| Small fan (optional) | 1 | To cool cold side |

### ASCII Wiring Diagram

```
    THERMOELECTRIC GENERATOR
    
    Heat flows from HOT to COLD → electricity flows!
    
              HEAT SOURCE
           (candle, stove, etc.)
              🔥🔥🔥🔥🔥🔥
              │ │ │ │ │ │
    ──────────┴─┴─┴─┴─┴─┴──────────
    ╔═══════════════════════════╗
    ║    HOT SIDE (aluminum)    ║  ← Heat absorbed here
    ╠═══════════════════════════╣
    ║                           ║
    ║    TEG MODULE             ║  ← Creates electricity
    ║    (TEC1-12706)           ║     from temperature
    ║                           ║     difference
    ╠═══════════════════════════╣
    ║    COLD SIDE (aluminum)   ║  ← Heat released here
    ╚═══════════════════════════╝
    ──────────┬─┬─┬─┬─┬─┬──────────
              │ │ │ │ │ │
              ▼ ▼ ▼ ▼ ▼ ▼
           ┌─────────┐
           │  HEAT   │  ← Heat sink with fins
           │  SINK   │     (keep cold!)
           │  ┌───┐  │     Use fan or water
           │  │   │  │     cooling
           │  └───┘  │
           └────┬────┘
                │
    ════════════╪═════════════════
    WIRING:
    ════════════╪═════════════════
                │
         TEG WIRES
         (usually red & black,
          or red & blue)
                │
           ┌────┴────┐
           │         │
        ┌──┴──┐  ┌──┴──┐
        │ RED │  │BLACK│
        │ (+) │  │ (-) │
        └──┬──┘  └──┬──┘
           │        │
           │     ┌──┘
           │     │
           └──┬──┘
              │
         ┌────┴────┐
         │   (+)   │
         │   LED   │
         │   (-)   │
         └─────────┘
              │
              │  OR connect to:
              │
         ┌────┴────┐
         │  BATTERY│  ← Charge a small battery
         │  CHARGER│     for storage
         └─────────┘
```

### TEG MODULE DETAIL

```
    TOP VIEW OF TEG MODULE
    
    ┌─────────────────────────┐
    │                         │
    │   ┌───┐ ┌───┐ ┌───┐    │
    │   │ B │ │ B │ │ B │    │  B = P-type bismuth
    │   │ i │ │ i │ │ i │    │      telluride element
    │   │ s │ │ s │ │ s │    │
    │   │ m │ │ m │ │ m │    │  There are 127 pairs
    │   │ u │ │ u │ │ u │    │  inside (tiny pellets)
    │   │ t │ │ t │ │ t │    │
    │   │ h │ │ h │ │ h │    │
    │   └───┘ └───┘ └───┘    │
    │   ┌───┐ ┌───┐ ┌───┐    │
    │   │ A │ │ A │ │ A │    │  A = N-type elements
    │   └───┘ └───┘ └───┘    │
    │     ... (127 pairs) ... │
    │                         │
    │   WIRE 1 (+)   WIRE 2 (-)│
    └───────┬───────────┬─────┘
            │           │
         RED wire    BLACK wire
```

### Step-by-Step Connections

1. **Apply thermal paste** to both sides of TEG module
2. **Press hot side** against heat source (candle holder, stove surface)
3. **Press cold side** against heat sink (CPU cooler works great)
4. **Attach alligator clips** to TEG wire leads (red to +, black to -)
5. **Connect LED**: Red clip to long leg (+), black clip to short leg (-)
6. **Keep cold side cold!** Use fan, ice, or water — bigger temp difference = more power
7. **Monitor**: Too much heat can damage the TEG (max ~300°C)

---

## 6. WATER WHEEL GENERATOR

Turn flowing water into electricity.

### Parts List

| Part | Quantity | Notes |
|------|----------|-------|
| DC motor (12V, 10W+) | 1 | Motor = generator when spun! |
| Water wheel (homemade) | 1 | Plastic bucket with paddles |
| Wooden frame | 1 | To mount wheel and motor |
| Pulley / belt | 1 | Connects wheel to motor |
| Rectifier (bridge) | 1 | If motor outputs AC |
| Battery (12V) | 1 | Energy storage |
| Charge controller | 1 | Prevents overcharging |
| Pipe / gutter | As needed | Water channel |
| 10 AWG wire | 15 feet | All connections |

### ASCII Wiring Diagram

```
         WATER SOURCE
         (stream, rain gutter, etc.)
              │
              ▼
    ┌─────────────────────┐
    │    WATER CHANNEL    │
    │  ════════════════   │
    │         │           │
    │         ▼           │
    │    ┌─────────┐      │
    │    │ ╱     ╲ │      │
    │    │╱  WHEEL ╲│     │  WATER WHEEL
    │    │╲       ╱│      │  (paddles catch water)
    │    │ ╲     ╱ │      │
    │    │    │    │      │
    │    │    │    │      │
    │    └────┼────┘      │
    │         │           │
    │     AXLE/SHAFT      │
    │         │           │
    │    ┌────┴────┐      │
    │    │  PULLEY │      │  ← Small pulley on wheel axle
    │    └────┬────┘      │
    │         │           │
    │      BELT           │
    │         │           │
    │    ┌────┴────┐      │
    │    │  PULLEY │      │  ← Large pulley on motor (speeds up rotation)
    │    └────┬────┘      │
    │         │           │
    │    ┌────┴────┐      │
    │    │   DC    │      │
    │    │  MOTOR  │      │  ← Motor becomes GENERATOR when spun!
    │    │ (12V)   │      │
    │    │  (+) (-)│      │
    │    └─┬─────┬─┘      │
    └──────┼─────┼────────┘
           │     │
           │     │  AC output (motors make AC when spun)
           │     │
        ┌──┴─────┴──┐
        │  BRIDGE    │
        │ RECTIFIER  │  ← Converts AC to DC
        │ AC    DC   │
        │ IN   (+)(-)│
        └────┬──┬────┘
             │  │
             │  │ RED (+) and BLACK (-)
             │  │
          ┌──┴──┴──┐
          │ CHARGE  │
          │CONTROLLER│
          └──┬──┬───┘
             │  │
          ┌──┴──┴──┐
          │         │
          │ BATTERY │  ← Stores energy!
          │  12V    │
          │         │
          └─────────┘
```

### Step-by-Step Connections

1. **Build water wheel** from plastic bucket with wooden paddles bolted to sides
2. **Mount wheel** on axle that spins freely in wooden frame
3. **Attach small pulley** to wheel axle, large pulley to motor shaft
4. **Connect pulleys** with belt (rubber band or inner tube strip)
5. **Mount DC motor** securely to frame
6. **Connect rectifier** to motor output wires
7. **Connect rectifier DC output** to charge controller
8. **Connect charge controller** to battery (through fuse)
9. **Channel water** onto wheel paddles — water turns wheel, wheel spins motor, motor makes power!

---

## 7. PIEZO HARVESTER

Makes tiny amounts of electricity from pressure/vibration.

### Parts List

| Part | Quantity | Notes |
|------|----------|-------|
| Piezo disc (27mm) | 1-4 | From old buzzer or buy online |
| Bridge rectifier | 1 | Converts AC to DC |
| Capacitor (100µF) | 1 | Stores charge |
| LED | 1 | Shows power output |
| Alligator clip wires | 2 | Red and black |
| Small battery (rechargeable) | 1 | AA NiMH stores power |
| Button/switch | 1 | Optional |

### ASCII Wiring DIAGRAM

```
    PIEZO HARVESTER — Single Disc
    
    When you tap/bend the disc, it makes a tiny voltage!
    
         TAP! TAP! TAP!
           ↓   ↓   ↓
    ┌────────────────────┐
    │  ┌──────────────┐  │
    │  │   PIEZO DISC │  │  ← Flexible metal disc
    │  │   (27mm)     │  │     with ceramic coating
    │  │              │  │
    │  │  brass back  │  │
    │  └──────┬───────┘  │
    │         │          │
    │     TWO WIRES      │
    │     (red + black)  │
    │         │          │
    └─────────┼──────────┘
              │
         ┌────┴────┐
         │  RED    │
         │ alligator│
         └────┬────┘
              │
              │
    Piezo outputs AC (alternating) so we need
    a rectifier to make DC (direct current)
              │
    ┌─────────┴──────────┐
    │   BRIDGE RECTIFIER  │
    │                     │
    │  AC IN    DC OUT    │
    │  ┌─┐      +   -    │
    └──┤ ├───────────────┘
       │ │
       └─┘
       │ │
       │ └──→ DC (-) BLACK
       └────→ DC (+) RED
          │       │
          │       │
          │    ┌──┴──┐
          │    │     │
          │    │  ┌──┴──┐
          │    │  │ 100µF│  ← CAPACITOR
          │    │  │  +  │    (stores charge
          │    │  │     │     from taps)
          │    │  └──┬──┘
          │    │     │
          │    └─────┘
          │       │
          │    ┌──┴──┐
          │    │     │
          │    │ LED │  ← Lights up on each tap!
          │    │     │
          │    └─────┘
          │
          └──→ (can also charge a small battery
                through a diode for storage)
```

### PIEZO ARRAY (More Power!)

```
    ┌──────────────────────────────────────────┐
    │       PIEZO ARRAY (4 discs in parallel)  │
    │                                          │
    │   ┌──────┐  ┌──────┐                    │
    │   │PIEZO │  │PIEZO │                    │
    │   │  1   │  │  2   │                    │
    │   └──┬───┘  └──┬───┘                    │
    │      │         │                         │
    │      │    RED wires together             │
    │      ├─────────┤                         │
    │      │         │                         │
    │      │    BLACK wires together           │
    │      ├─────────┤                         │
    │      │         │                         │
    │   ┌──┴───┐  ┌──┴───┐                    │
    │   │PIEZO │  │PIEZO │                    │
    │   │  3   │  │  4   │                    │
    │   └──────┘  └──────┘                    │
    │                                          │
    │   ALL RED wires ──→ Rectifier AC input   │
    │   ALL BLACK wires ─→ Rectifier AC input  │
    │                                          │
    │   Rectifier DC (+) ──→ Capacitor (+)     │
    │   Rectifier DC (-) ──→ Capacitor (-)     │
    │                                          │
    │   Capacitor (+) ──→ LED (+)              │
    │   Capacitor (-) ──→ LED (-)              │
    │                                          │
    └──────────────────────────────────────────┘
```

### Step-by-Step Connections

1. **Identify piezo wires**: Usually red (+) and black (-) or two black wires (one has a mark)
2. **Connect red wires** from all piezo discs together (parallel = more current)
3. **Connect black wires** from all piezo discs together
4. **Attach alligator clips** to combined red and black
5. **Connect to rectifier**: AC input terminals
6. **Connect capacitor** to rectifier DC output (+ to +, - to -)
7. **Connect LED** to capacitor (+ to long leg, - to short leg)
8. **Tap the piezo discs** — LED should flash!

---

## 8. COMPLETE HOME POWER SYSTEM

All sources combined into one home power system.

### Parts List

| Part | Quantity | Notes |
|------|----------|-------|
| Solar panels (100W) | 2-4 | Main power source |
| Wind turbine (400W) | 1 | Backup power |
| Charge controller (solar) | 1 | 30A MPPT |
| Charge controller (wind) | 1 | With dump load |
| Battery bank (12V 200Ah) | 1 | 2x 100Ah in parallel |
| Power inverter (2000W) | 1 | Pure sine wave |
| Main disconnect switch | 1 | 100A rated |
| Distribution panel | 1 | 4-6 circuits |
| Circuit breakers | 6 | 15A-30A each |
| All wiring from previous diagrams | — | See diagrams 2 & 3 |
| Ground rod | 2 | 8 feet copper |
| Lightning arrestor | 1 | For wind turbine |

### ASCII Wiring DIAGRAM

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                        COMPLETE HOME POWER SYSTEM                            │
└──────────────────────────────────────────────────────────────────────────────┘

 POWER SOURCES:
 ═══════════════

     ☀ SUN ☀              WIND ↑↑↑
      \ | /                   ↑↑↑
   ┌───┴──────┐          ┌────┴┴┴────┐
   │ SOLAR    │          │  WIND     │
   │ PANELS   │          │ TURBINE   │
   │ (400W)   │          │ (400W)    │
   └─┬──────┬─┘          └──┬──────┬─┘
     │      │                │      │
   (+)      (-)            AC OUT   │
     │      │                │      │
     │      │             RECTIFIER │
     │      │                │      │
     ▼      ▼                ▼      ▼
  ┌──────────────┐    ┌──────────────┐
  │ SOLAR CHARGE │    │ WIND CHARGE  │
  │ CONTROLLER   │    │ CONTROLLER   │
  │ (MPPT 30A)   │    │ (with dump)  │
  └──────┬───────┘    └──────┬───────┘
         │                   │
         │  10 AWG           │  10 AWG
         │                   │
         │    ┌──────────────┘
         │    │
         ▼    ▼
  ┌─────────────────────────────────────────┐
  │                                         │
  │            BATTERY BANK                 │
  │         (12V, 200Ah total)              │
  │                                         │
  │   ┌──────────┐    ┌──────────┐         │
  │   │ BATTERY  │    │ BATTERY  │         │
  │   │  100Ah   │════│  100Ah   │  PARALLEL│
  │   │          │    │          │  (same   │
  │   └──┬───────┘    └───────┬──┘  voltage,│
  │      │                    │     2x amp  │
  │      └────────┬───────────┘     hours)  │
  │               │                         │
  │            (+)│(-)                      │
  └───────────────┼─────────────────────────┘
                  │
            6 AWG │ (thick wire!)
                  │
    ┌─────────────┴─────────────┐
    │                           │
    │     MAIN DISCONNECT       │
    │     SWITCH (100A)         │  ← Emergency shutoff!
    │                           │
    │     OFF ══ ON             │
    └─────────────┬─────────────┘
                  │
                  │  6 AWG
                  │
    ┌─────────────┴─────────────┐
    │                           │
    │     POWER INVERTER        │
    │     (2000W, 12V→120V AC)  │
    │                           │
    │  DC IN          AC OUT    │
    │  (+) (-)    ┌───┐ ┌───┐  │
    └─────────────┤   ├─┤   ├──┘
                  └───┘ └───┘
                    │     │
                    │     │  120V AC
                    │     │
    ┌───────────────┴─────┴───────────────────┐
    │                                         │
    │         DISTRIBUTION PANEL              │
    │         (6 circuits)                    │
    │                                         │
    │  MAIN ──┬── 15A ── CIRCUIT 1 (Lights)   │
    │         ├── 15A ── CIRCUIT 2 (Lights)   │
    │         ├── 20A ── CIRCUIT 3 (Outlets)  │
    │         ├── 20A ── CIRCUIT 4 (Outlets)  │
    │         ├── 30A ── CIRCUIT 5 (Pump)     │
    │         └── 30A ── CIRCUIT 6 (Well)     │
    │                                         │
    │   Each circuit has its own breaker!     │
    │                                         │
    └───┬─────────┬─────────┬─────────┬───────┘
        │         │         │         │
        ▼         ▼         ▼         ▼
     ┌─────┐  ┌─────┐  ┌─────┐  ┌─────┐
     │LIGHT│  │LIGHT│  │PLUG │  │PUMP │
     │  1  │  │  2  │  │OUT  │  │     │
     └─────┘  └─────┘  └─────┘  └─────┘


 GROUNDING SYSTEM:
 ═════════════════

    All metal frames ──→ GREEN wires ──→ GROUND RODS
                                          (2x 8ft copper
                                           driven into earth)
```

### WIRE SIZE GUIDE

```
┌──────────────────────────────────────────────────────────┐
│                    WIRE SIZE GUIDE                       │
├──────────────────┬──────────────┬────────────────────────┤
│ Connection       │ Wire Size    │ Max Amps               │
├──────────────────┼──────────────┼────────────────────────┤
│ Panel → Controller│ 10 AWG      │ 30A                    │
│ Controller → Batt │ 6 AWG       │ 50A                    │
│ Battery → Inverter│ 4 AWG       │ 100A                   │
│ Inverter → Panel  │ 12 AWG      │ 20A                    │
│ Ground wires      │ 10 AWG      │ —                      │
│ Turbine → Rectifier│ 12 AWG     │ 15A                    │
└──────────────────┴──────────────┴────────────────────────┘

REMEMBER: Thicker wire = lower number = handles more power!
```

### Step-by-Step Connections

1. **Wire solar panels** to solar charge controller (see Diagram 2)
2. **Wire wind turbine** to wind charge controller (see Diagram 3)
3. **Connect both controllers** to battery bank (through fuses)
4. **Connect batteries** in parallel: (+) to (+), (-) to (-) for 200Ah
5. **Install main disconnect** between battery and inverter
6. **Connect inverter** to battery through disconnect (thick 4 AWG wires)
7. **Connect inverter AC output** to distribution panel
8. **Install breakers** in panel for each circuit
9. **Wire circuits** to lights, outlets, and pumps
10. **Install ground rods** and connect all green ground wires
11. **Test each circuit** one at a time

---

## 9. HOMEMADE WIFI SETUP

Create a local WiFi network without internet provider.

### Parts List

| Part | Quantity | Notes |
|------|----------|-------|
| Raspberry Pi (3B+ or 4) | 1 | The "router" |
| USB WiFi adapter | 2 | 1 for AP, 1 for mesh (optional) |
| Ethernet cable | 1 | For initial setup |
| Power supply (5V 3A) | 1 | For Raspberry Pi |
| Antenna (optional) | 1 | Extends range |
| SD card (16GB+) | 1 | For Pi operating system |
| Network switch (optional) | 1 | For wired devices |

### ASCII Wiring DIAGRAM

```
    HOMEMADE WiFi NETWORK
    
    ┌──────────────────────────────────────────────────┐
    │                                                  │
    │              RASPBERRY PI                        │
    │              (WiFi Router)                       │
    │                                                  │
    │   ┌──────────────────────────────────┐          │
    │   │          RASPBERRY PI 4           │          │
    │   │                                  │          │
    │   │  ┌────────┐    ┌──────────────┐  │          │
    │   │  │ USB    │    │  Ethernet    │  │          │
    │   │  │ WiFi   │    │  Port        │  │          │
    │   │  │Adapter │    │  (eth0)      │  │          │
    │   │  │(wlan1) │    │              │  │          │
    │   │  └───┬────┘    └──────┬───────┘  │          │
    │   │      │                │          │          │
    │   │  Built-in WiFi        │          │          │
    │   │  (wlan0)              │          │          │
    │   │  = Access Point       │          │          │
    │   │                       │          │          │
    │   │  Power: USB-C 5V 3A   │          │          │
    │   └───────────┬───────────┘          │          │
    │               │                      │          │
    └───────────────┼──────────────────────┘          │
                    │                                  │
              ┌─────┴─────┐                           │
              │ POWER     │                           │
              │ SUPPLY    │                           │
              │ 5V 3A     │                           │
              └─────┬─────┘                           │
                    │                                  │
                    │ Power cable                      │
                    ▼                                  │
              ┌─────────┐                             │
              │ WALL    │                             │
              │ OUTLET  │ ← Plug into solar/battery   │
              │ or 12V  │   power system!             │
              └─────────┘                             │
                    │                                  │
    ════════════════╪════════════════════════════════  │
    WIFI NETWORK    │                                  │
    ════════════════╪════════════════════════════════  │
                    │                                  │
              WiFi Signal                             │
              (192.168.4.1)                           │
                    │                                  │
         ┌──────────┼──────────┐                      │
         │          │          │                      │
         ▼          ▼          ▼                      │
    ┌─────────┐ ┌─────────┐ ┌─────────┐              │
    │  PHONE  │ │ LAPTOP  │ │  OTHER  │              │
    │         │ │         │ │  DEVICES│              │
    │ Connect │ │ Connect │ │         │              │
    │ to:     │ │ to:     │ │         │              │
    │ SSID:   │ │ SSID:   │ │         │              │
    │ "FREEDOM│ │"FREEDOM │ │         │
    │  NET"   │ │  NET"   │ │         │
    └─────────┘ └─────────┘ └─────────┘
```

### NETWORK TOPOLOGY

```
    ┌─────────────────────────────────────────────────────┐
    │                                                     │
    │            WiFi Access Point                        │
    │            (Raspberry Pi wlan0)                     │
    │            SSID: "FREEDOM_NET"                      │
    │            IP: 192.168.4.1                          │
    │                  │                                  │
    │         ┌────────┼────────┐                         │
    │         │        │        │                         │
    │         ▼        ▼        ▼                         │
    │    ┌────────┐┌────────┐┌────────┐                  │
    │    │ Device ││ Device ││ Device │  Max ~20 devices  │
    │    │  .2   ││  .3   ││  .4   │  with dnsmasq     │
    │    └────────┘└────────┘└────────┘                  │
    │                                                     │
    │    LOCAL SERVICES (no internet needed):             │
    │    - File sharing (Samba)                           │
    │    - Chat server (local only)                       │
    │    - Wiki/knowledge base                            │
    │    - Mesh network gateway                           │
    │                                                     │
    └─────────────────────────────────────────────────────┘
```

### Step-by-Step Connections

1. **Flash Raspberry Pi OS** to SD card (use another computer)
2. **Boot Pi** and connect Ethernet cable to your computer for setup
3. **Install hostapd** (WiFi access point software): `sudo apt install hostapd`
4. **Install dnsmasq** (DHCP server): `sudo apt install dnsmasq`
5. **Configure hostapd**: Set SSID to "FREEDOM_NET", WPA2 password
6. **Configure dnsmasq**: Set IP range 192.168.4.2 - 192.168.4.20
7. **Set static IP** on wlan0: 192.168.4.1
8. **Enable IP forwarding** for routing
9. **Unplug Ethernet**, WiFi AP should start automatically
10. **Connect devices** to "FREEDOM_NET" WiFi
11. **Optional**: Add USB WiFi adapter for mesh networking

---

## 10. MESH NETWORK NODE

Connect multiple locations without any central router.

### Parts List

| Part | Quantity | Notes |
|------|----------|-------|
| Raspberry Pi Zero 2 W | 1 | Per node (cheapest option) |
| OR ESP32 | 1 | Ultra-low power option |
| Solar panel (5W) | 1 | Powers the node |
| 18650 battery + holder | 1 | Energy storage |
| TP4056 charger module | 1 | Charges 18650 safely |
| 3.3V buck converter | 1 | Steps down voltage |
| Antenna (3dBi) | 1 | Extends mesh range |
| Waterproof enclosure | 1 | Outdoor protection |
| 10 AWG wire | 3 feet | Solar connections |

### ASCII Wiring DIAGRAM

```
    MESH NETWORK NODE
    (One of many — they all talk to each other!)
    
    ┌──────────────────────────────────────────────┐
    │                                              │
    │  ☀ SOLAR PANEL (5W) ☀                       │
    │  ┌──────────────────┐                        │
    │  │░░░░░░░░░░░░░░░░░░│                        │
    │  │░░░░░░░░░░░░░░░░░░│                        │
    │  │░░░░░░░░░░░░░░░░░░│                        │
    │  └────────┬─────────┘                        │
    │           │                                   │
    │        RED│BLACK                              │
    │           │                                   │
    │  ┌────────┴─────────┐                        │
    │  │  TP4056 CHARGER   │  ← Safely charges     │
    │  │  MODULE           │    lithium battery     │
    │  │                   │                       │
    │  │ IN+ IN- OUT+ OUT-│                       │
    │  └──┬────┬────┬───┬─┘                       │
    │     │    │    │   │                          │
    │     │    │  ┌─┴─┐ │                          │
    │     │    │  │   │ │                          │
    │     │    │  │18650│ ← 3.7V lithium battery   │
    │     │    │  │CELL │   (stores solar energy)  │
    │     │    │  │   │ │                          │
    │     │    │  └─┬─┘ │                          │
    │     │    │    │   │                          │
    │     │    │  ┌─┴───┴─┐                       │
    │     │    │  │ BUCK  │  ← Converts 3.7V to   │
    │     │    │  │CONVERT│    3.3V for Pi/ESP32   │
    │     │    │  │ 3.3V  │                       │
    │     │    │  └───┬───┘                       │
    │     │    │      │                            │
    │     │    │    3.3V                           │
    │     │    │      │                            │
    │     │    │  ┌───┴────────────────────┐      │
    │     │    │  │                        │      │
    │     │    │  │    RASPBERRY PI        │      │
    │     │    │  │    ZERO 2 W            │      │
    │     │    │  │    (or ESP32)          │      │
    │     │    │  │                        │      │
    │     │    │  │  ┌──────────────────┐  │      │
    │     │    │  │  │  WiFi Radio     │  │      │
    │     │    │  │  │  (mesh capable) │  │      │
    │     │    │  │  └────────┬─────────┘  │      │
    │     │    │  │           │            │      │
    │     │    │  │       ┌───┴───┐        │      │
    │     │    │  │       │ANTENNA│        │      │
    │     │    │  │       └───────┘        │      │
    │     │    │  │                        │      │
    │     │    │  └────────────────────────┘      │
    │     │    │                                   │
    │     │    │  OPTIONAL: Add sensor inputs      │
    │     │    │  (temperature, humidity, etc.)     │
    │     │    │                                   │
    │     │    │                                   │
    └─────┼────┼───────────────────────────────────┘
          │    │
        GND  VCC (power connections
              managed internally)
```

### MESH NETWORK TOPOLOGY

```
    MESH NETWORK — No central point of failure!
    
    Every node can talk to every other node.
    Messages "hop" from node to node.
    
         📡 NODE A              📡 NODE B
         (Home)                (Shed)
            │                     │
            │    WiFi Mesh        │
            ├─────────────────────┤
            │                     │
         📡 NODE C              📡 NODE D
         (Garden)               (Barn)
            │                     │
            ├─────────────────────┤
            │                     │
         📡 NODE E              📡 NODE F
         (Gate)                 (Field)
    
    
    If any node fails, messages find another path!
    
    A ──→ B ──→ D ──→ F    (normal path)
    A ──→ C ──→ E ──→ F    (backup path)
    
    
    ┌─────────────────────────────────────────────────┐
    │  Each node runs:                                │
    │  - batman-adv or olsr (mesh routing protocol)   │
    │  - hostapd (WiFi access point)                  │
    │  - dnsmasq (IP addresses for all nodes)         │
    │  - Optional: sensor data collection             │
    │  - Optional: local file/web server              │
    └─────────────────────────────────────────────────┘
```

### Step-by-Step Connections

1. **Build one node** following the wiring diagram above
2. **Install mesh software**: `batman-adv` for Raspberry Pi
3. **Configure mesh**: Set same SSID and channel on all nodes
4. **Test single node**: Connect phone, verify WiFi works
5. **Build second node** with same wiring
6. **Place nodes** within WiFi range of each other (~100m outdoor)
7. **Nodes auto-discover** each other and form mesh
8. **Add more nodes** as needed — mesh grows automatically
9. **Mount in waterproof enclosures** and install solar panels
10. **Test**: Walk between nodes, connection should hand off seamlessly

---

## 11. WATER PUMP SYSTEM

Solar-powered water pumping from source to storage tank.

### Parts List

| Part | Quantity | Notes |
|------|----------|-------|
| Solar panel (50W) | 1 | Powers the pump |
| 12V DC water pump | 1 | 3-5 GPM flow rate |
| Charge controller (solar) | 1 | With load output |
| Battery (12V 35Ah) | 1 | Runs pump when cloudy |
| Float switch | 1 | Auto-shutoff when tank full |
| PVC pipe (1") | 20 feet | Water delivery |
| Check valve | 1 | Prevents backflow |
| Foot valve with screen | 1 | Keeps prime in suction line |
| Teflon tape | 1 roll | Seal pipe threads |
| Pipe clamps | 10 | Secure pipe runs |
| Wire (10 AWG) | 15 feet | Pump power |

### ASCII Wiring DIAGRAM

```
    SOLAR WATER PUMP SYSTEM
    
         ☀ SUN ☀
          \ | /
       ┌───┴──────┐
       │  SOLAR   │
       │  PANEL   │
       │  (50W)   │
       └─┬──────┬─┘
         │      │
       (+)      (-)
         │      │
         │      │
         ▼      ▼
    ┌─────────────────┐
    │   CHARGE        │
    │   CONTROLLER    │
    │   (with LOAD    │
    │    output)      │
    └──┬──────────┬───┘
       │          │
       │ LOAD     │ BATTERY
       │ OUTPUT   │
       │          │
       │     ┌────┴────┐
       │     │ BATTERY │
       │     │ 12V     │
       │     │ 35Ah    │
       │     └─────────┘
       │
       │ 10 AWG
       │
       │     ┌──────────────┐
       │     │ FLOAT SWITCH │  ← Auto shut-off
       │     │              │     when tank is full!
       │     │   ┌───┐      │
       │     │   │ ○ │ ←── Float rides on water
       │     │   │ │ │     When tank full, switch
       │     │   └─┬─┘     opens, pump stops
       │     └─────┤───────┘
       │           │
       │           │
       │     ┌─────┴──────┐
       │     │            │
       │     │  12V DC    │
       │     │  WATER     │
       │     │  PUMP      │
       │     │  (3 GPM)   │
       │     │            │
       │     │ INLET      │ OUTLET
       │     └─────┬──────┘
       │           │
       │           │
    WATER SUPPLY   │
    (well, stream, │
     rain barrel)  │
       │           │
       │           │ PVC PIPE (1")
       │           │
       │     ┌─────┴──────┐
       │     │ CHECK      │  ← Prevents water
       │     │ VALVE      │     flowing back
       │     └─────┬──────┘
       │           │
       │           │
       │           │  ┌─────────────────┐
       │           │  │  DELIVERY PIPE   │
       │           │  │  (uphill okay!)  │
       │           │  │                  │
       │           │  │  ═══════════════ │
       │           │  │                  │
       │           └──┤  ═══════════════ │
       │              │                  │
       │              │  ═══════════════ │
       │              │         │        │
       │              │         ▼        │
       │              │  ┌─────────────┐ │
       │              │  │             │ │
       │              │  │ WATER TANK  │ │
       │              │  │ (elevated   │ │
       │              │  │  for gravity│ │
       │              │  │  pressure)  │ │
       │              │  │             │ │
       │              │  │  ~~~~~~~~   │ │
       │              │  │  ~~~~~~~~   │ │
       │              │  │  ~~~~~~~~   │ │
       │              │  │             │ │
       │              │  └──────┬──────┘ │
       │              │         │        │
       │              │         ▼        │
       │              │    TAP / FAUCET  │
       │              │    ┌─────┐       │
       │              │    │ ▼▼▼ │ ← Water comes out!
       │              │    └─────┘       │
       │              └─────────────────┘
```

### FLOAT SWITCH WIRING DETAIL

```
    FLOAT SWITCH — Prevents overflow!
    
    ┌──────────────────────────────────────┐
    │                                      │
    │   TANK EMPTY          TANK FULL     │
    │                                      │
    │   ┌─────┐            ┌─────┐        │
    │   │     │            │~~~~~│        │
    │   │     │            │~~~~~│        │
    │   │  ○  │ ← float   │○~~~~│ ← float│
    │   │ /│  │   hangs    │/│~~~│   rises│
    │   │/ │  │   down     │/│~~~│   UP!  │
    │   └──┼──┘            └──┼──┘        │
    │      │                  │           │
    │   SWITCH CLOSED      SWITCH OPEN    │
    │   (pump runs)        (pump stops)   │
    │                                      │
    │                                      │
    │   WIRING:                            │
    │                                      │
    │   From controller ──→ Float Switch ──→ Pump (+)  │
    │                                      │
    │   When float is DOWN (tank empty):   │
    │   Circuit CLOSED → pump runs         │
    │                                      │
    │   When float is UP (tank full):      │
    │   Circuit OPEN → pump stops          │
    │                                      │
    └──────────────────────────────────────┘
```

### Step-by-Step Connections

1. **Mount solar panel** in sunny location, facing south
2. **Wire panel** to charge controller (see Diagram 2)
3. **Connect battery** to charge controller
4. **Install pump** at water source (submersible or surface mount)
5. **Install foot valve** on suction line (underwater end)
6. **Install check valve** after pump outlet
7. **Run PVC pipe** from pump to elevated tank
8. **Wire float switch** in series with pump power line
9. **Connect pump** through float switch to controller LOAD output
10. **Test**: Turn on, pump should run until tank fills, then stop automatically

---

## 12. WATER PURIFICATION SYSTEM

From rain to drinking water — collection, filtration, and storage.

### Parts List

| Part | Quantity | Notes |
|------|----------|-------|
| Gutters and downspouts | As needed | Rain collection |
| First-flush diverter | 1 | Discards first dirty water |
| settling tank (5 gal) | 1 | Lets sediment sink |
| Sand (play sand) | 50 lbs | Filtration medium |
| Gravel (small) | 30 lbs | Filtration medium |
| Activated carbon | 10 lbs | Removes chemicals/odor |
| 5-gallon buckets | 3 | Filter stages |
| Drill with 1/4" bit | 1 | Makes holes in buckets |
| spigot / faucet | 1 | For dispensing |
| Storage tank (55 gal) | 1 | Clean water storage |
| Food-grade hose | 10 feet | Connections |
| Bleach (unscented) | 1 bottle | Final disinfection |

### ASCII Wiring DIAGRAM (Plumbing Diagram)

```
    COMPLETE WATER PURIFICATION SYSTEM
    
    RAIN COLLECTION:
    ════════════════
    
       ☁ RAIN CLOUDS ☁
       ~~~~~~~~~~~~~~~
            │ │ │
            ▼ ▼ ▼
    ┌───────────────────┐
    │     ROOF          │
    │   ═══════════     │
    │        │          │
    │     GUTTERS       │
    │        │          │
    │     DOWNSPOUT     │
    │        │          │
    └────────┼──────────┘
             │
    ┌────────┴──────────┐
    │ FIRST-FLUSH       │  ← Discards first 1 gallon
    │ DIVERTER          │     (has bird poop, dust, etc.)
    │                   │
    │  ┌───┐            │
    │  │   │ ← fills   │
    │  │   │   first   │
    │  │   │   then    │
    │  └─┬─┘   flows   │
    │    │     on      │
    └────┼─────────────┘
         │
         ▼
    
    FILTRATION SYSTEM (3 buckets):
    ═══════════════════════════════
    
    ┌─────────────────────────────────────────────────────┐
    │                                                     │
    │  STAGE 1:        STAGE 2:        STAGE 3:          │
    │  COARSE          FINE            CARBON            │
    │  FILTER          FILTER          FILTER            │
    │                                                     │
    │  ┌─────────┐    ┌─────────┐    ┌─────────┐        │
    │  │░░░░░░░░░│    │▓▓▓▓▓▓▓▓▓│    │█████████│        │
    │  │░ GRAVEL ░│    │▓ SAND  ▓│    │█ACTIVTD █│        │
    │  │░░░░░░░░░│    │▓▓▓▓▓▓▓▓▓│    │█ CARBON █│        │
    │  │░░░░░░░░░│    │▓▓▓▓▓▓▓▓▓│    │█████████│        │
    │  │░░░░░░░░░│    │▓▓▓▓▓▓▓▓▓│    │█████████│        │
    │  │░░░░░░░░░│    │▓▓▓▓▓▓▓▓▓│    │█████████│        │
    │  ├─────────┤    ├─────────┤    ├─────────┤        │
    │  │ ○ ○ ○ ○ │    │ ○ ○ ○ ○ │    │ ○ ○ ○ ○ │        │
    │  │holes    │    │holes    │    │holes    │        │
    │  └────┬────┘    └────┬────┘    └────┬────┘        │
    │       │              │              │              │
    │    drips           drips          drips            │
    │       │              │              │              │
    │       ▼              ▼              ▼              │
    │  ┌─────────┐    ┌─────────┐    ┌─────────┐        │
    │  │ CATCH   │    │ CATCH   │    │ CATCH   │        │
    │  │ BUCKET  │    │ BUCKET  │    │ BUCKET  │        │
    │  │ (below) │───→│ (below) │───→│ (below) │        │
    │  └─────────┘    └─────────┘    └─────────┘        │
    │                                                     │
    │  Removes:        Removes:        Removes:          │
    │  - Leaves        - Fine sand     - Chemicals       │
    │  - Bugs          - Silt          - Odors           │
    │  - Debris        - Cloudiness    - Bad taste       │
    │                                  - Chlorine        │
    └─────────────────────────────────────────────────────┘
             │
             │  After all 3 stages
             ▼
    
    STORAGE & DISPENSING:
    ═════════════════════
    
    ┌─────────────────────────────────────┐
    │                                     │
    │  ┌───────────────────────┐         │
    │  │    55-GALLON          │         │
    │  │    STORAGE TANK       │         │
    │  │    (food grade)       │         │
    │  │                       │         │
    │  │    ~~~~~~~~~~~~~~~    │         │
    │  │    ~~~~~~~~~~~~~~~    │         │
    │  │    ~~~~~~~~~~~~~~~    │         │
    │  │    ~~~~~~~~~~~~~~~    │         │
    │  │                       │         │
    │  │  Add 1/8 tsp bleach   │         │
    │  │  per gallon for       │         │
    │  │  disinfection         │         │
    │  │                       │         │
    │  └───────────┬───────────┘         │
    │              │                      │
    │         ┌────┴────┐                 │
    │         │SPIGOT   │                 │
    │         │(faucet) │                 │
    │         └────┬────┘                 │
    │              │                      │
    │              ▼                      │
    │         ┌─────────┐                 │
    │         │ GLASS / │                 │
    │         │ BOTTLE  │                 │
    │         │         │                 │
    │         │ DRINK!  │  ← Safe water! │
    │         └─────────┘                 │
    │                                     │
    └─────────────────────────────────────┘
```

### BUCKET FILTER CONSTRUCTION

```
    HOW TO BUILD EACH FILTER BUCKET:
    
    ┌────────────────────────────────────┐
    │                                    │
    │   Take a 5-gallon bucket:          │
    │                                    │
    │   1. Drill 20 holes in bottom      │
    │      using 1/4" drill bit          │
    │                                    │
    │   2. Placemesh cloth over holes    │
    │      (old t-shirt works)           │
    │                                    │
    │   3. Fill with filter material:    │
    │                                    │
    │   BUCKET 1:    BUCKET 2:   BUCKET 3:│
    │                                    │
    │   ┌────────┐  ┌────────┐ ┌────────┐│
    │   │2"gravel│  │4" sand │ │3"carbon││
    │   │────────│  │────────│ │────────││
    │   │2"gravel│  │2" sand │ │3"carbon││
    │   │────────│  │────────│ │────────││
    │   │2"gravel│  │1" gravel│ │2" sand ││
    │   │────────│  │────────│ │────────││
    │   │mesh    │  │mesh    │ │mesh    ││
    │   │cloth   │  │cloth   │ │cloth   ││
    │   ├────────┤  ├────────┤ ├────────┤│
    │   │HOLES   │  │HOLES   │ │HOLES   ││
    │   └────────┘  └────────┘ └────────┘│
    │                                    │
    │   Stack them:                      │
    │                                    │
    │   Dirty ──→ Bucket 1 ──→ Bucket 2 ──→ Bucket 3 ──→ Clean!  │
    │   Water     (gravel)    (sand)     (carbon)       Water     │
    │                                    │
    └────────────────────────────────────┘
```

### Step-by-Step Connections

1. **Install gutters** on roof to collect rainwater
2. **Add first-flush diverter** to downspout (discards first dirty water)
3. **Place settling tank** after diverter (lets particles sink)
4. **Drill holes** in bottom of 3 buckets (1/4" holes, 20 per bucket)
5. **Layer filter materials** in each bucket (see diagram above)
6. **Stack buckets** so water flows: Bucket 1 → Bucket 2 → Bucket 3
7. **Place catch bucket** under final filter
8. **Let water drip** through all 3 stages (slow process — be patient!)
9. **Transfer clean water** to 55-gallon storage tank
10. **Add disinfection**: 1/8 teaspoon unscented bleach per gallon
11. **Let sit 30 minutes** before drinking
12. **Replace filter materials** every 3-6 months

---

## QUICK REFERENCE: ALL WIRE COLORS

```
╔══════════════════════════════════════════════════════════════╗
║                    WIRE COLOR CHEAT SHEET                    ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  RED     = POSITIVE (+) / HOT      = Power in, danger       ║
║  BLACK   = NEGATIVE (-) / RETURN   = Ground return, safe    ║
║  GREEN   = EARTH GROUND            = Safety protection      ║
║  WHITE   = NEUTRAL (AC only)       = Return path AC         ║
║  BLUE    = SIGNAL / DATA           = Information            ║
║                                                              ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  REMEMBER:                                                   ║
║  • Always disconnect power before working on wires           ║
║  • Use fuses/breakers to protect against shorts              ║
║  • Match wire thickness (AWG) to current draw                ║
║  • Lower AWG number = thicker wire = more current            ║
║  • When in doubt, go thicker — thin wires catch fire!        ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

---

## SAFETY RULES

```
╔══════════════════════════════════════════════════════════════╗
║                    TOP 10 SAFETY RULES                       ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  1. DISCONNECT power before touching any wires               ║
║  2. USE fuses on every positive wire from battery             ║
║  3. NEVER work with wet hands on electrical systems          ║
║  4. KEEP batteries away from fire (they can explode)         ║
║  5. VENTilate battery charging areas (hydrogen gas)          ║
║  6. USE proper wire gauges — undersized wires = fire         ║
║  7. GROUND all metal frames and enclosures                   ║
║  8. CHECK connections regularly for looseness/heat           ║
║  9. KEEP a fire extinguisher (Class C / electrical) nearby   ║
║  10. WHEN IN DOUBT, ASK SOMEONE WHO KNOWS                   ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

---

## COMMON WIRE GAUGE REFERENCE

| AWG | Diameter | Max Amps | Use For |
|-----|----------|----------|---------|
| 18 | 1.0mm | 10A | Low-power signals, LEDs |
| 16 | 1.3mm | 15A | Small appliances |
| 14 | 1.6mm | 20A | House wiring, outlets |
| 12 | 2.0mm | 25A | Heavy outlets, AC units |
| 10 | 2.6mm | 35A | Solar panel runs |
| 8 | 3.2mm | 50A | Battery connections |
| 6 | 4.1mm | 65A | Heavy battery/inverter |
| 4 | 5.2mm | 85A | Main battery to inverter |
| 2 | 6.5mm | 115A | Large systems |
| 1/0 | 8.3mm | 150A | Main feeds |

---

*WIRING DIAGRAMS COMPLETE*
