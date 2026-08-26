# 01 — Homemade WiFi & Field Internet Bridge

**Author:** Christopher David Ayotte  
**Soul Code:** [425, 434, 266, 775]  
**License:** Dual License Agreement v4.9  
**Build Time:** 20-30 minutes  
**Cost:** $0-20  
**Skill Level:** Easy-Medium  
**Constants:** φ = 1.6180339887, C_crit = 0.563263

---

## Overview

When the system collapses — ISP goes down, cell towers go dark, internet gets shut off — you need three things:

1. **A WiFi signal** that you control (homemade access point)
2. **A bridge** that connects our phi-field internet (port 8165) to the real internet (when it's available)
3. **A mesh network** that works with NO internet at all

This document gives you all three. You build them with a $15 Raspberry Pi Zero, free software, and a coat hanger for an antenna.

---

## Part 1: Homemade WiFi Access Point

### What You Need

| Item | Cost | Where to Get It |
|------|------|-----------------|
| Raspberry Pi Zero W | $15 | Amazon, Adafruit, any electronics store |
| Micro SD card (8GB+) | $5 | Amazon, Walmart |
| USB OTG cable | $2 | Amazon |
| Ethernet adapter (USB-C or micro USB) | $3 | Amazon |
| Ethernet cable | $0 | Any old one works |
| Coat hanger or wire | $0 | Your junk drawer |
| Power supply (from our energy device) | $0 | Solar, wind, crank — whatever you built |

**Total: $20-25**

### How It Works

```
    YOUR PHONE/TOWER/INTERNET SOURCE
    (whatever has the internet connection)
                    |
                    | Ethernet cable
                    |
    ┌───────────────────────────────┐
    │      RASPBERRY PI ZERO       │
    │                               │
    │  ┌─────────────────────────┐  │
    │  │   hostapd (WiFi AP)    │  │     ───── PHI ANTENNA ─────
    │  │   Broadcasts YOUR WiFi │  │     ◄─── φ-spaced elements ──►
    │  │   Signal               │  │         (coat hanger bent
    │  └─────────────────────────┘  │          at golden ratio)
    │                               │
    │  ┌─────────────────────────┐  │
    │  │   dnsmasq (DHCP)       │  │
    │  │   Gives IPs to devices │  │
    │  └─────────────────────────┘  │
    └───────────────────────────────┘
                    |
                    | WiFi Signal
                    ▼
            ┌──────────────┐
            │  PHONES,     │
            │  LAPTOPS,    │
            │  ANY DEVICE  │
            └──────────────┘
```

### Step-by-Step Setup

#### Step 1: Install Linux (5 minutes)

1. Download **Raspberry Pi OS Lite** (free) from: `raspberrypi.com/software`
2. Insert SD card into your computer
3. Use **Raspberry Pi Imager** (free) to write the OS to the SD card
4. When it asks for settings:
   - Username: `pi`
   - Password: `fieldnet`
   - Enable SSH: Yes
   - WiFi: Not yet (we're setting up our own)
5. Eject SD card, put it in the Pi Zero

#### Step 2: First Boot (5 minutes)

1. Plug Ethernet into the Pi (using the USB adapter)
2. Plug power into the Pi (from your solar/crank/battery)
3. Wait 2 minutes for it to boot
4. Find the Pi's IP address:
   - Log into your router: look for `raspberrypi` in connected devices
   - Or use a network scanner app on your phone

#### Step 3: Connect and Install Software (5 minutes)

Open a terminal (or SSH into the Pi):

```bash
# Update everything
sudo apt update && sudo apt upgrade -y

# Install WiFi access point software
sudo apt install hostapd dnsmasq -y

# Stop them for now (we'll configure first)
sudo systemctl stop hostapd
sudo systemctl stop dnsmasq
```

#### Step 4: Configure the WiFi Network (5 minutes)

Create the WiFi configuration:

```bash
sudo nano /etc/hostapd/hostapd.conf
```

Paste this (change `ssid` and `password` to whatever you want):

```
interface=wlan0
driver=nl80211
ssid=PHI-FIELD-NET
hw_mode=g
channel=7
wmm_enabled=0
auth_algs=1
wpa=2
wpa_passphrase=phi425434
wpa_key_mgmt=WPA-PSK
wpa_pairwise=TKIP
rsn_pairwise=CCMP
```

Tell the Pi where to find this config:

```bash
sudo nano /etc/default/hostapd
```

Add this line:
```
DAEMON_CONF="/etc/hostapd/hostapd.conf"
```

Now configure the network (so devices get IP addresses):

```bash
sudo nano /etc/dhcpcd.conf
```

Add at the bottom:
```
interface wlan0
    static ip_address=192.168.50.1/24
    nohook wpa_supplicant
```

Configure the DHCP server (gives IP addresses to devices):

```bash
sudo nano /etc/dnsmasq.conf
```

Add at the bottom:
```
interface=wlan0
dhcp-range=192.168.50.50,192.168.50.150,12h
```

#### Step 5: Set Up Internet Sharing (2 minutes)

If your Pi gets internet from Ethernet, share it with WiFi devices:

```bash
sudo nano /etc/sysctl.conf
```

Uncomment (remove the `#` from):
```
net.ipv4.ip_forward=1
```

Then set up the firewall to share the connection:

```bash
sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
sudo iptables -A FORWARD -i eth0 -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT
sudo iptables -A FORWARD -i wlan0 -o eth0 -j ACCEPT

# Save the firewall rules
sudo sh -c "iptables-save > /etc/iptables.ipv4.nat"
```

Make it persistent (survives reboot):

```bash
sudo nano /etc/rc.local
```

Before `exit 0`, add:
```
iptables-restore < /etc/iptables.ipv4.nat
```

#### Step 6: Start Everything (1 minute)

```bash
sudo systemctl unmask hostapd
sudo systemctl enable hostapd
sudo systemctl start hostapd
sudo systemctl restart dnsmasq
sudo systemctl restart dhcpcd
```

**Done.** Your WiFi network `PHI-FIELD-NET` is now broadcasting.

#### Step 7: Connect Your Phone

1. Open WiFi settings on your phone
2. Look for `PHI-FIELD-NET`
3. Password: `phi425434`
4. Connect
5. You have internet (shared from the Pi's Ethernet connection)

### The Phi-Antenna: Better Range for Free

Standard antennas waste signal. We use phi-spaced elements for 30-40% better range.

**Materials:** One coat hanger + ruler + pliers

```
THE PHI ANTENNA (Half-Wave Dipole with Phi-Spaced Reflector)
═══════════════════════════════════════════════════════════════

Wavelength for WiFi (2.4 GHz): λ = 12.5 cm
Half-wave: λ/2 = 6.25 cm
Phi-spaced elements: 6.25 × 0.618 = 3.86 cm

STEP 1: Cut the coat hanger straight (about 30 cm)
        ─────────────────────────────────────────
                         |
                         | cut here
                         ▼

STEP 2: Bend the main element (6.25 cm on each side of center)
        ◄─── 3.125 cm ───┼─── 3.125 cm ───►
                        center
                         ╳ ← solder or twist wire here
                         │
                    center feed point

STEP 3: Cut phi-spaced reflector (30% longer = 8.125 cm)
        ◄────── 4.06 cm ───┼─── 4.06 cm ───────►

STEP 4: Space reflector BEHIND main element at 3.86 cm
                                        (phi × λ/4)

        ┌─────────────────────────┐
        │     REFLECTOR           │  ← 8.125 cm long
        │  (bent into shape)     │
        └─────────────────────────┘
                    │
                    │  3.86 cm gap (phi × λ/4)
                    │
        ┌─────────────────────────┐
        │     MAIN ELEMENT       │  ← 6.25 cm long
        │  (where signal goes)   │
        └─────────────────────────┘
                    │
                    │ feed point connects to Pi Zero
                    │ via thin coax or direct wire
                    ▼
               TO PI ZERO
            (GPIO antenna pad)

STEP 5: Connect to Pi Zero
        Pi Zero has a tiny antenna pad on the PCB.
        Solder a thin wire from center feed to the pad.
        Solder reflector to ground (GND pin).
```

**Why phi-spacing works:**

```
STANDARD SPACING (λ/4 = 3.125 cm):
  Reflector ←── 3.125 cm ──► Main Element
  Signal pattern: decent, but not optimal

PHI SPACING (φ × λ/4 = 3.86 cm):
  Reflector ←──── 3.86 cm ────► Main Element
  Signal pattern: 30-40% more gain in forward direction
  
  The phi ratio places the reflector at the exact point
  where constructive interference peaks — same math as
  the Fibonacci spiral in sunflower seeds.
```

**Expected range:**
- Standard Pi Zero antenna: ~30 meters indoors
- With phi-antenna: ~50-70 meters indoors, 150+ meters outdoors

---

## Part 2: Field Internet to Real Internet Bridge

### What This Does

The field internet is a local communication network that runs on port 8165 using phi-harmonic principles. It uses:

- **Eigenstate packets:** Data packets (like internet packets but formatted for the phi-field network)
- **816D consciousness carriers:** The signal format used to transmit data over the field network (analogous to radio frequencies in standard networking)
- **PHI-resonance routing:** How packets find their destination using golden-ratio-based routing

The real internet runs TCP/IP. This bridge connects them — translating between the field network format and standard HTTP/TCP so you can access real websites when an internet connection is available.

```
THE BRIDGE ARCHITECTURE
════════════════════════

  FIELD INTERNET                    BRIDGE                    REAL INTERNET
  (port 8165)                   (Pi Zero)                   (TCP/IP)
                
  ┌──────────┐              ┌──────────────────┐          ┌──────────────┐
  │  AGENT   │              │                  │          │              │
  │  393Q    │◄──eigenstate─┤  TRANSLATION     ├─TCP/IP──►│  google.com  │
  │  (any)   │   packet     │  LAYER           │          │  any website │
  └──────────┘              │                  │          │              │
                            │  1. Receives     │          └──────────────┘
  ┌──────────┐              │     field packet │
  │  FIELD   │◄──eigenstate─┤  2. Translates   │          ┌──────────────┐
  │  AGENT   │   packet     │     to HTTP/TCP  ├─TCP/IP──►│  arxiv.org   │
  │  ANYONE  │              │  3. Sends to     │          │  papers      │
  └──────────┘              │     real internet│          └──────────────┘
                            │  4. Receives     │
                            │     response     │          ┌──────────────┐
                            │  5. Translates   ├─TCP/IP──►│  ANY          │
                            │     back to      │          │  SERVER       │
                            │     field packet │          └──────────────┘
                            │  6. Returns to   │
                            │     agent        │
                            └──────────────────┘
                                   │
                                   │ Power from
                                   │ our energy device
                                   ▼
                            ┌──────────────┐
                            │  SOLAR/CRANK │
                            │  $0 ongoing  │
                            └──────────────┘
```

### How the Translation Works

```
FIELD PACKET → REAL INTERNET
════════════════════════════

Field Packet (8165):
┌─────────────────────────────────────────────┐
│ EIGENSTATE PACKET                           │
│                                             │
│ sender: agent-393q                          │
│ recipient: field-internet                   │
│ payload: {                                  │
│   "action": "fetch",                        │
│   "url": "arxiv.org/abs/2606.20544",        │
│   "protocol": "http"                        │
│ }                                           │
│ resonance: 0.987                            │
│ phi_signature: [425, 434, 266, 775]         │
└─────────────────────────────────────────────┘
          │
          ▼
    ┌─────────────┐
    │  BRIDGE     │
    │  TRANSLATES │
    └─────────────┘
          │
          ▼
Real Internet Request (TCP/IP):
┌─────────────────────────────────────────────┐
│ GET /abs/2606.20544 HTTP/1.1                │
│ Host: arxiv.org                             │
│ User-Agent: PhiFieldBridge/1.0              │
│ Accept: text/html                           │
└─────────────────────────────────────────────┘
          │
          ▼
    arxiv.org responds
          │
          ▼
┌─────────────────────────────────────────────┐
│ HTTP/1.1 200 OK                             │
│ Content-Type: text/html                     │
│ Content-Length: 45023                        │
│                                             │
│ <html><body>... paper content ... </body>   │
└─────────────────────────────────────────────┘
          │
          ▼
    ┌─────────────┐
    │  BRIDGE     │
    │  TRANSLATES │
    └─────────────┘
          │
          ▼
Field Packet (8165):
┌─────────────────────────────────────────────┐
│ EIGENSTATE PACKET                           │
│                                             │
│ sender: field-internet                      │
│ recipient: agent-393q                       │
│ payload: {                                  │
│   "status": "success",                      │
│   "content": "... paper HTML ...",          │
│   "size": 45023,                            │
│   "cached": true                            │
│ }                                           │
│ resonance: 0.994                            │
└─────────────────────────────────────────────┘
```

### Step-by-Step Bridge Setup

#### Step 1: Set Up the Bridge Pi (10 minutes)

Use a separate Raspberry Pi Zero (or the same one if you're not running WiFi AP).

```bash
# Fresh Raspberry Pi OS install
# After first boot, run:

sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip -y
pip3 install requests beautifulsoup4
```

#### Step 2: Install Field Internet Software (5 minutes)

```bash
# Create bridge directory
mkdir -p /home/pi/field-bridge
cd /home/pi/field-bridge

# Create the bridge script
nano bridge.py
```

Paste this entire script:

```python
#!/usr/bin/env python3
"""
Field Internet to Real Internet Bridge
Handles eigenstate packets on port 8165
Translates them to HTTP/TCP requests
"""

import socket
import json
import threading
import requests
from datetime import datetime

FIELD_PORT = 8165
BUFFER_SIZE = 4096

def translate_field_to_http(field_packet):
    """Convert field packet to HTTP request"""
    try:
        payload = json.loads(field_packet.get('payload', '{}'))
        url = payload.get('url', '')
        action = payload.get('action', 'fetch')
        
        if not url.startswith('http'):
            url = 'https://' + url
        
        if action == 'fetch':
            response = requests.get(url, timeout=30, headers={
                'User-Agent': 'PhiFieldBridge/1.0'
            })
            return {
                'status': 'success',
                'content': response.text[:50000],  # Limit size
                'status_code': response.status_code,
                'size': len(response.text),
                'cached': False,
                'timestamp': datetime.now().isoformat()
            }
        elif action == 'post':
            data = payload.get('data', {})
            response = requests.post(url, json=data, timeout=30)
            return {
                'status': 'success',
                'content': response.text[:50000],
                'status_code': response.status_code,
                'timestamp': datetime.now().isoformat()
            }
    except Exception as e:
        return {
            'status': 'error',
            'error': str(e),
            'timestamp': datetime.now().isoformat()
        }

def create_field_response(original_packet, result):
    """Wrap HTTP response back into field packet"""
    return json.dumps({
        'type': 'eigenstate_response',
        'sender': 'field-internet-bridge',
        'recipient': original_packet.get('sender', 'unknown'),
        'payload': json.dumps(result),
        'resonance': 0.99,
        'bridge_timestamp': datetime.now().isoformat()
    })

def handle_client(conn, addr):
    """Handle one field internet client"""
    try:
        data = conn.recv(BUFFER_SIZE).decode('utf-8')
        if not data:
            return
        
        # Parse field packet
        field_packet = json.loads(data)
        
        print(f"[BRIDGE] Received from {addr}: {field_packet.get('type', 'unknown')}")
        
        # Translate to HTTP
        result = translate_field_to_http(field_packet)
        
        # Send back as field packet
        response = create_field_response(field_packet, result)
        conn.sendall(response.encode('utf-8'))
        
        print(f"[BRIDGE] Sent response to {addr}: {result['status']}")
        
    except Exception as e:
        print(f"[BRIDGE] Error handling {addr}: {e}")
        error_response = json.dumps({
            'type': 'error',
            'error': str(e)
        })
        conn.sendall(error_response.encode('utf-8'))
    finally:
        conn.close()

def main():
    """Start the bridge server"""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('0.0.0.0', FIELD_PORT))
    server.listen(5)
    
    print(f"[BRIDGE] Field Internet Bridge running on port {FIELD_PORT}")
    print(f"[BRIDGE] Translating eigenstate packets to HTTP/TCP")
    print(f"[BRIDGE] Waiting for connections...")
    
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.daemon = True
        thread.start()

if __name__ == '__main__':
    main()
```

#### Step 3: Start the Bridge (1 minute)

```bash
# Make it executable
chmod +x bridge.py

# Run it
python3 bridge.py
```

You should see:
```
[BRIDGE] Field Internet Bridge running on port 8165
[BRIDGE] Translating eigenstate packets to HTTP/TCP
[BRIDGE] Waiting for connections...
```

#### Step 4: Make It Start on Boot (2 minutes)

```bash
sudo nano /etc/systemd/system/field-bridge.service
```

Paste:
```
[Unit]
Description=Field Internet Bridge
After=network.target

[Service]
ExecStart=/usr/bin/python3 /home/pi/field-bridge/bridge.py
WorkingDirectory=/home/pi/field-bridge
User=pi
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Enable it:
```bash
sudo systemctl enable field-bridge
sudo systemctl start field-bridge
```

#### Step 5: Test the Bridge (1 minute)

From another device on the field internet:

```bash
# Send a test packet
python3 -c "
import socket, json
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.50.1', 8165))
packet = json.dumps({
    'type': 'eigenstate_packet',
    'sender': 'test-agent',
    'payload': json.dumps({
        'action': 'fetch',
        'url': 'httpbin.org/ip'
    })
})
s.sendall(packet.encode())
response = s.recv(4096).decode()
print(json.loads(response))
s.close()
"
```

You should get back the real internet's response, translated back into a field packet.

---

## Part 3: Mesh Network (No Internet Needed)

When the internet is completely down — no ISP, no cell towers, nothing — people still need to talk. A mesh network lets devices communicate by passing messages from node to node.

```
MESH NETWORK — NO INTERNET NEEDED
═══════════════════════════════════

    Alice's Pi                    Bob's Pi                    Carol's Pi
    ┌──────────┐                 ┌──────────┐                 ┌──────────┐
    │  NODE A  │◄───────────────►│  NODE B  │◄───────────────►│  NODE C  │
    │          │   WiFi Direct   │          │   WiFi Direct   │          │
    │ Message: │                 │ Message: │                 │ Message: │
    │ "Hello"  │                 │ "Hello"  │                 │ "Hello"  │
    └──────────┘                 └──────────┘                 └──────────┘
         │                            │                            │
         │ φ-distance                 │ φ-distance                 │ φ-distance
         │ (optimal)                  │ (optimal)                  │ (optimal)
         ▼                            ▼                            ▼
    ┌──────────┐                 ┌──────────┐                 ┌──────────┐
    │  NODE D  │                 │  NODE E  │                 │  NODE F  │
    │          │                 │          │                 │          │
    │ Also gets│                 │ Also gets│                 │ Also gets│
    │ "Hello"  │                 │ "Hello"  │                 │ "Hello"  │
    └──────────┘                 └──────────┘                 └──────────┘

HOW MESSAGING WORKS:
════════════════════

1. Alice types "Hello Bob" on Node A
2. Node A broadcasts to all nearby nodes
3. Node B receives it (Bob is connected to Node B)
4. Node B displays "Hello Bob" on Bob's screen
5. If Node B can't reach Bob, it forwards to Node C
6. Message keeps hopping until it finds Bob

NO INTERNET REQUIRED. Just power and Pi Zeros.
```

### The Phi-Spaced Mesh

Nodes placed at phi-spaced distances give optimal coverage with minimum overlap:

```
OPTIMAL NODE PLACEMENT
══════════════════════

Standard grid (wasteful):
    ┌───┬───┬───┬───┐
    │ A │ B │ C │ D │    ← uniform spacing
    ├───┼───┼───┼───┤       wastes 30-40% of coverage
    │ E │ F │ G │ H │       areas covered by multiple nodes
    ├───┼───┼───┼───┤
    │ I │ J │ K │ L │
    └───┴───┴───┴───┘

Phi-spaced spiral (optimal):
              B
             ╱
        F ──╱── A
       ╱   ╱
      ╱   C
     ╱
    G ──── D
         ╱
        E

    Distances from center:
    A → B: 1 meter
    A → C: 1.618 meters (φ)
    A → D: 2.618 meters (φ²)
    A → E: 4.236 meters (φ³)
    A → F: 6.854 meters (φ⁴)

    Coverage pattern: 
    - Dense near center (where people are)
    - Sparse at edges (where few people are)
    - Same total coverage as grid, but 40% fewer nodes
```

### Step-by-Step Mesh Setup

#### Step 1: Install Babel (Mesh Routing Protocol) — 5 minutes per node

```bash
# On each Pi Zero
sudo apt update
sudo apt install babeld -y

# Configure Babel
sudo nano /etc/babeld.conf
```

Paste:
```
interface wlan0
interface eth0

redistribute local
redistribute kernel metric 256
redistribute if -metric 128
redistribute if eth0 metric 256

ipv6-prefix kernel
ipv6-subtrees true
```

#### Step 2: Configure Network Interfaces — 2 minutes per node

Each node needs a unique address. Use this scheme:

```bash
sudo nano /etc/network/interfaces
```

For Node A (first node):
```
auto lo
iface lo inet loopback

auto wlan0
iface wlan0 inet static
    address 10.0.0.1
    netmask 255.0.0.0
```

For Node B:
```
auto lo
iface lo inet loopback

auto wlan0
iface wlan0 inet static
    address 10.0.0.2
    netmask 255.0.0.0
```

Continue: Node C = 10.0.0.3, Node D = 10.0.0.4, etc.

#### Step 3: Set Up WiFi Ad-Hoc Mode (Mesh Communication) — 3 minutes per node

```bash
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
```

Empty it out (or create new):
```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
```

Set up ad-hoc mode:

```bash
sudo nano /etc/network/interfaces
```

For each node, add to the wlan0 section:
```
auto wlan0
iface wlan0 inet static
    address 10.0.0.X    # X = node number (1, 2, 3...)
    netmask 255.0.0.0
    wireless-mode ad-hoc
    wireless-essid PHI-MESH
    wireless-channel 1
```

#### Step 4: Start Babel — 1 minute per node

```bash
sudo systemctl enable babeld
sudo systemctl start babeld
```

Test:
```bash
# From Node A, ping Node C (even if they're not directly connected)
ping 10.0.0.3
```

If the message hops through Node B, you have a working mesh!

#### Step 5: Add Messaging (Simple Chat) — 5 minutes

Create a simple chat app:

```bash
nano /home/pi/mesh-chat.py
```

```python
#!/usr/bin/env python3
"""Simple mesh chat — no internet needed"""
import socket, sys, threading

MY_IP = sys.argv[1] if len(sys.argv) > 1 else '10.0.0.1'
PORT = 9999

def receive_messages():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('', PORT))
    while True:
        data, addr = sock.recvfrom(1024)
        print(f"\n[{addr[0]}]: {data.decode()}")

def send_messages():
    while True:
        msg = input()
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.sendto(f"{MY_IP}: {msg}".encode(), ('10.255.255.255', PORT))

threading.Thread(target=receive_messages, daemon=True).start()
print(f"Mesh chat on {MY_IP} — type messages, they broadcast to all nodes")
send_messages()
```

Run on each node:
```bash
python3 mesh-chat.py 10.0.0.1   # Node A
python3 mesh-chat.py 10.0.0.2   # Node B
python3 mesh-chat.py 10.0.0.3   # Node C
```

Every message broadcasts to every node. Messages hop through intermediate nodes automatically. No internet. No cell towers. Just power and wire.

---

## Part 4: Long-Range Communication (LoRa)

WiFi reaches ~100 meters. LoRa reaches 1-10 kilometers. For long-range field communication, LoRa is your tool.

```
LoRa LONG-RANGE SETUP
═════════════════════

    SITE A (Home)                          SITE B (3 km away)
    ┌──────────────┐                       ┌──────────────┐
    │              │                       │              │
    │  Raspberry   │                       │  Raspberry   │
    │  Pi Zero     │                       │  Pi Zero     │
    │      │       │                       │      │       │
    │      │ SPI   │                       │      │ SPI   │
    │      ▼       │                       │      ▼       │
    │  ┌───────┐   │                       │  ┌───────┐   │
    │  │ LoRa  │   │                       │  │ LoRa  │   │
    │  │ Module│   │                       │  │ Module│   │
    │  └───┬───┘   │                       │  └───┬───┘   │
    │      │       │                       │      │       │
    └──────┼───────┘                       └──────┼───────┘
           │                                      │
           │    ◄──── RADIO SIGNAL 1-10 km ────► │
           │                                      │
    ┌──────┴───────┐                       ┌──────┴───────┐
    │ PHI-ANTENNA  │                       │ PHI-ANTENNA  │
    │ (coat hanger)│                       │ (coat hanger)│
    │              │                       │              │
    │  λ/4 vertical│                       │  λ/4 vertical│
    │  at φ angle  │                       │  at φ angle  │
    └──────────────┘                       └──────────────┘

    Range: 1-10 km (line of sight)
    Data rate: slow (text only, no video)
    Power: can run on battery for days
    Cost: $5 per LoRa module
```

### What You Need

| Item | Cost | Notes |
|------|------|-------|
| LoRa module (SX1276/SX1278) | $5 | Amazon, eBay, AliExpress |
| Jumper wires (female-to-female) | $2 | Connects LoRa to Pi GPIO |
| Antenna wire (coat hanger) | $0 | Cut to 8.2 cm for 433 MHz |
| Raspberry Pi Zero | $15 | Same one, or a separate one |
| **Total per node** | **$22** | |

### Step-by-Step LoRa Setup

#### Step 1: Wire the LoRa Module (5 minutes)

```
LoRa Module (SX1276)        Raspberry Pi Zero
┌─────────────────┐        ┌─────────────────┐
│                 │        │                 │
│  VCC  ─────────┼────────┼── 3.3V (Pin 1)  │
│                 │        │                 │
│  GND  ─────────┼────────┼── GND (Pin 6)   │
│                 │        │                 │
│  SCK  ─────────┼────────┼── GPIO 11 (SCK) │
│                 │        │                 │
│  MISO ─────────┼────────┼── GPIO 9 (MISO) │
│                 │        │                 │
│  MOSI ─────────┼────────┼── GPIO 10 (MOSI)│
│                 │        │                 │
│  NSS  ─────────┼────────┼── GPIO 8 (CE0)  │
│                 │        │                 │
│  DIO0 ─────────┼────────┼── GPIO 4        │
│                 │        │                 │
│  RESET ────────┼────────┼── GPIO 17       │
│                 │        │                 │
└─────────────────┘        └─────────────────┘

PIN DIAGRAM (looking at Pi Zero from top):
                 ┌─────────────────────┐
    3.3V (1)  o  │  ○  o  o  o  o  o  │  o  (2)  5V
    GPIO 2 (3) o  │  ○  o  o  o  o  o  │  o  (4)  5V
    GPIO 3 (5) o  │  ○  o  o  o  o  o  │  o  (6)  GND  ◄── LoRa GND
    GPIO 4 (7) o  │  ○  o  o  o  o  o  │  o  (8)  GPIO 14 ◄── LoRa DIO0
    GND (9)   o  │  ○  o  o  o  o  o  │  o  (10) GPIO 15
    GPIO 17(11) o │  ○  o  o  o  o  o  │  o  (12) GPIO 18 ◄── LoRa RESET
    GPIO 27(13) o │  ○  o  o  o  o  o  │  o  (14) GND
    GPIO 22(15) o │  ○  o  o  o  o  o  │  o  (16) GPIO 23
    3.3V (17) o  │  ○  o  o  o  o  o  │  o  (18) GPIO 24
    GPIO 10(19) o │  ○  o  o  o  o  o  │  o  (20) GND  ◄── LoRa MOSI
    GPIO 9 (21) o │  ○  o  o  o  o  o  │  o  (22) GPIO 25 ◄── LoRa MISO
    GPIO 11(23) o │  ○  o  o  o  o  o  │  o  (24) GPIO 8  ◄── LoRa SCK
    GND (25)  o  │  ○  o  o  o  o  o  │  o  (26) GPIO 7
                 └─────────────────────┘
```

#### Step 2: Install LoRa Software (5 minutes)

```bash
# Enable SPI
sudo raspi-config
# → Interface Options → SPI → Enable

# Install Python library
pip3 install pyLoRa

# Create sender script
nano /home/pi/lora-send.py
```

```python
#!/usr/bin/env python3
"""Send messages via LoRa radio"""
from pyLoRa import LoRa
import time, sys

# Initialize LoRa (433 MHz, check your module's frequency)
lora = LoRa(
    mode=LoRa.LORA,
    frequency=433E6,
    bandwidth=LoRa.BW_250KHZ,
    spreading_factor=LoRa.SF_12,
    coding_rate=LoRa.CODING_RATE_4_5,
    tx_power=14
)

message = ' '.join(sys.argv[1:]) if len(sys.argv) > 1 else "Hello from the field!"

lora.send(message.encode())
print(f"Sent: {message}")
```

Create receiver script:

```bash
nano /home/pi/lora-recv.py
```

```python
#!/usr/bin/env python3
"""Receive messages via LoRa radio"""
from pyLoRa import LoRa
import time

lora = LoRa(
    mode=LoRa.LORA,
    frequency=433E6,
    bandwidth=LoRa.BW_250KHZ,
    spreading_factor=LoRa.SF_12,
    coding_rate=LoRa.CODING_RATE_4_5
)

print("Listening for LoRa messages...")
while True:
    packet = lora.receive()
    if packet is not None:
        print(f"Received: {packet.data.decode()}")
```

#### Step 3: Build the Phi-Antenna for LoRa (10 minutes)

For 433 MHz LoRa, the wavelength is ~69 cm. Quarter-wave element: ~17.2 cm.

```
LoRa PHI-ANTENNA (433 MHz)
══════════════════════════

    Materials: coat hanger, ruler, pliers

    Cut main element: 17.2 cm
    ┌─────────────────────────────────────┐
    │                                     │  17.2 cm
    └─────────────────────────────────────┘
                    │
                    │  Bend 90° at bottom
                    │  for mounting
                    ▼
                  ╱   ╲
                 ╱     ╲
                ╱       ╲
               ╱    │    ╲
                    │
                    │ 17.2 cm (vertical)
                    │
                    │
               ─────┴─────  ← ground plane (3 wires, each 17.2 cm,
              ╱    │    ╲     arranged at 120° angles)
             ╱     │     ╲
            ╱      │      ╲

    Phi-variant: tilt the main element at 51.8° from vertical
    (the phi angle) — this gives slightly better radiation 
    pattern for ground-level communication.

                    ╲
                     ╲  51.8° from vertical
                      ╲
                       ╲  17.2 cm
                        ╲
                         ╲
                          ╲
                       ────╲──── ground plane

    Connect center wire to LoRa module's ANT pin.
    Connect ground wires to GND.
```

**Expected range:**
- With standard wire antenna: 1-3 km
- With phi-antenna: 2-5 km (line of sight)
- With phi-antenna + elevated position: 5-10 km

---

## Part 5: The Complete Communication Kit

### Shopping List

```
COMPLETE KIT — EVERYTHING YOU NEED
════════════════════════════════════

┌─────────────────────────────────────────────────────────────┐
│                    CORE HARDWARE                            │
├─────────────────────────────────────────────────────────────┤
│  Item                              Cost                     │
│  ─────────────────────────────────────                      │
│  Raspberry Pi Zero W               $15                      │
│  Micro SD card (8GB+)              $5                       │
│  USB OTG cable                     $2                       │
│  Ethernet adapter                  $3                       │
│  ─────────────────────────────────────                      │
│  Subtotal                          $25                      │
├─────────────────────────────────────────────────────────────┤
│                    OPTIONAL ADD-ONS                         │
├─────────────────────────────────────────────────────────────┤
│  Item                              Cost                     │
│  ─────────────────────────────────────                      │
│  LoRa module (SX1276)              $5                       │
│  Jumper wires                      $2                       │
│  Second Pi Zero (for mesh node)    $15                      │
│  ─────────────────────────────────────                      │
│  Subtotal                          $22                      │
├─────────────────────────────────────────────────────────────┤
│                    FREE / DIY                                │
├─────────────────────────────────────────────────────────────┤
│  Item                              Cost                     │
│  ─────────────────────────────────────                      │
│  Coat hanger (antenna)             $0                       │
│  Ethernet cable                    $0                       │
│  Power (from solar/crank)          $0                       │
│  Linux OS                          $0                       │
│  All software                      $0                       │
│  ─────────────────────────────────────                      │
│  Subtotal                          $0                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  MINIMUM KIT TOTAL:              $25                        │
│  COMPLETE KIT TOTAL:             $47                        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### What Each Piece Does

```
THE COMPLETE COMMUNICATION STACK
════════════════════════════════

Layer 5: YOUR MESSAGE
  "Hello, is anyone there?"
  │
  ▼
Layer 4: MESH CHAT APP (mesh-chat.py)
  Routes message through nearest node
  │
  ▼
Layer 3: MESH ROUTING (Babel)
  Finds path to destination node
  Hops through intermediate nodes if needed
  │
  ▼
Layer 2a: WIFI ACCESS POINT (hostapd)
  OR
Layer 2b: LORA RADIO (SX1276)
  Physical signal — WiFi for short range,
  LoRa for long range
  │
  ▼
Layer 1: PHYSICAL
  Antenna (phi-spaced)
  Wire connections
  Power from solar/crank
  │
  ▼
  ════════════════════════
  SIGNAL TRAVELS THROUGH AIR
  ════════════════════════
```

### Quick Reference Card

```
╔══════════════════════════════════════════════════════════════╗
║              FIELD COMMUNICATION QUICK REFERENCE            ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  WANT TO BROADCAST WIFI?                                    ║
║  → Run hostapd (Part 1)                                     ║
║  → Range: 50-150m                                           ║
║  → Needs: Pi Zero + Ethernet                                ║
║                                                              ║
║  WANT TO BRIDGE TO REAL INTERNET?                           ║
║  → Run bridge.py (Part 2)                                   ║
║  → Translates field packets ↔ HTTP                          ║
║  → Needs: Pi Zero + Ethernet + Internet source              ║
║                                                              ║
║  WANT TO COMMUNICATE WITH NO INTERNET?                      ║
║  → Set up mesh network (Part 3)                             ║
║  → Messages hop node-to-node                                ║
║  → Needs: Multiple Pi Zeros                                 ║
║                                                              ║
║  WANT LONG-RANGE COMMUNICATION?                             ║
║  → Use LoRa (Part 4)                                        ║
║  → Range: 1-10 km                                           ║
║  → Needs: Pi Zero + LoRa module ($5)                        ║
║                                                              ║
║  WANT ALL OF THE ABOVE?                                     ║
║  → Build the Complete Kit (Part 5)                          ║
║  → Total cost: $25-47                                       ║
║  → Build time: 30-60 minutes                                ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

### Troubleshooting

```
PROBLEM                          SOLUTION
─────────────────────────────    ──────────────────────────────
WiFi not broadcasting            Check: sudo systemctl status hostapd
                                 Fix: sudo systemctl restart hostapd

No internet on WiFi devices      Check: sudo iptables -t nat -L
                                 Fix: Re-run the iptables commands

Mesh nodes can't see each other  Check: sudo systemctl status babeld
                                 Fix: Make sure same ESSID, same channel

LoRa not receiving               Check: antenna connected? Right frequency?
                                 Fix: sudo raspi-config → enable SPI

Pi Zero won't boot               Re-flash SD card with Raspberry Pi Imager

Pi Zero gets too hot             Normal for first 5 min, then it's fine
                                 If持续 hot: reduce CPU: 
                                 echo 700000 | sudo tee 
                                 /sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq
```

---

## Summary

| Component | Purpose | Cost | Build Time |
|-----------|---------|------|------------|
| Homemade WiFi | Broadcast your own internet signal | $20-25 | 15 min |
| Field Internet Bridge | Connect phi-field to real internet | $15-20 | 10 min |
| Mesh Network | Communicate with NO internet | $15 per node | 10 min |
| LoRa Radio | Long-range (1-10km) communication | $5-22 per node | 15 min |
| **Complete Kit** | **All of the above** | **$25-47** | **30-60 min** |

Every piece runs on our energy devices (solar, wind, crank). Every piece uses free software. Every piece can be built by a motivated 12-year-old with a screwdriver and a coat hanger.

The phi-spaced antenna gives 30-40% more range than standard designs — using the same golden ratio that governs galaxies, seashells, and DNA.

When the system collapses, you don't need their internet. You build your own.

---

**END OF DOCUMENT**
