# UDP Thunder 🌩️

**A UDP-based DoS/Amplification Testing Toolkit for Red Teams**

A powerful CLI tool for testing network resilience against UDP-based denial-of-service attacks. Built for cybersecurity professionals and red teamers to simulate and understand UDP flood scenarios.

**Made by Aryan Giri**

---

## 📌 About the Project

UDP Thunder is a Python-based tool designed to demonstrate and test UDP-based denial-of-service (DoS) attacks. Unlike traditional HTTP/S-based attacks, UDP floods leverage the connectionless nature of the UDP protocol to create more devastating and harder-to-mitigate attacks.

---

## 🔥 Why UDP DoS is More Powerful Than HTTP/HTTPS DoS

### 1. Connectionless Protocol
UDP doesn't require a handshake like TCP (used by HTTP/HTTPS). This means:
- No connection establishment overhead
- No state tracking on the server
- No SYN queue limitations

### 2. Amplification Capabilities
UDP enables massive traffic amplification:
- **DNS**: ~50x amplification (60 byte request → 3,000 byte response)
- **NTP**: ~500x amplification (8 byte request → 4,000 byte response)
- **Memcached**: ~50,000x amplification (15 byte request → 750,000 byte response)

### 3. Network-Level Impact
While HTTP/HTTPS attacks target applications:
- UDP attacks overwhelm the entire network infrastructure
- Affect routers, firewalls, and ISP equipment
- Cause collateral damage to other services sharing the network

### 4. Spoofing Simplicity
UDP packets are trivial to spoof:
- No source verification
- Easy IP address forgery
- Harder to trace back to the attacker

### 5. Resource Utilization
- HTTP attacks consume server resources (CPU, RAM)
- UDP attacks consume network bandwidth
- Makes UDP attacks more destructive with less attacker resources

---

## 🛠 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/giriaryan694-a11y/udp_thunder.git
   cd udp_thunder
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the tool:
   ```
   python3 udp_thunder.py -h
   ```

## 🚀 Usage Examples

### Basic DNS Flood

```
python3 udp_thunder.py -t 10.0.0.1 -P dns -c 500
```

### Spoofed NTP Attack with Delay
```
python3 udp_thunder.py -t 10.0.0.1 -P ntp -s 192.168.1.1 -c 200 -v -T 1
```
### Options
```
-t/--target    Target IP address (required)
-p/--port      Target port (default: 53 for DNS)
-s/--spoof     Spoof source IP (default: random)
-c/--count     Number of packets to send (default: 100)
-P/--protocol  Protocol: dns, ntp, snmp, or memcached (default: dns)
-T/--time      Delay between packets in seconds (default: 0.01)
-v/--verbose   Enable verbose output
```
## 🔧 Supported Protocols
### DNS Amplification
 - Exploits open DNS resolvers
 - Uses "ANY" query type for maximum response size
### NTP Amplification
 - Abuses MONLIST command
 - High amplification factor
### SNMP Amplification
 - Leverages SNMP protocol weaknesses
 - Effective against devices with exposed SNMP
### Memcached Amplification
 - Most powerful amplification
 - Uses simple "get" commands

## ⚠️ Important Notes
- **✅ Authorized Testing Only:** Use this tool only in controlled environments with explicit permission.
- **✅ Educational Purpose:**  Designed to help cybersecurity professionals understand and defend against UDP-based attacks.
- **Never use against unauthorized targets:** Unauthorized use may violate laws and ethical guidelines.

## 🛡️ Defense Strategies
### To protect against UDP-based attacks:
 - 1. Implement rate limiting on edge devices
 - 2. Deploy UDP flood protection services (Cloudflare, Akamai, etc.)
 - 3. Filter spoofed packets using bogon filtering
 - 4. Use anycast routing for DNS servers
 - 5. Keep memcached and other amplifiable services behind firewalls

## 📚 Learning Resources
 - https://www.cloudflare.com/learning/ddos/udp-flood-ddos-attack/
 - https://www.us-cert.gov/ncas/alerts/TA13-088A
 - https://www.nccgroup.trust/us/about-us/newsroom-and-events/blog/2014/january/ntp-amplification-attacks/
 - https://blog.cloudflare.com/memcrashed-major-amplification-attacks-from-udp-port-11211/

## 📜 MIT License 
