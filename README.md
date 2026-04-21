# SDN Mininet-Based Bandwidth Measurement using POX Controller

##  Project Overview

This project demonstrates **Software Defined Networking (SDN)** using Mininet and a POX controller.
It implements a **learning switch (simple_switch.py)** and measures **network bandwidth** using multiple clients with `iperf`.

The goal is to observe how **bandwidth changes as the number of clients increases**.

---

##  Concepts Used

* Software Defined Networking (SDN)
* Control Plane vs Data Plane
* OpenFlow Protocol
* Flow Tables
* Learning Switch
* Network Congestion & Bandwidth Sharing

---

##  Project Files

| File               | Description                                     |
| ------------------ | ----------------------------------------------- |
| `topology.py`      | Defines Mininet topology (hosts, switch, links) |
| `simple_switch.py` | POX controller implementing learning switch     |
| `README.md`        | Project documentation                           |

---

## Network Topology

* 1 Switch (s1)
* 1 Server (h1)
* Multiple Clients (h2, h3, h4, h5, h6)

All hosts are connected to a single switch, creating a **shared bandwidth environment**.

---

##  Requirements

* Ubuntu (VirtualBox recommended)
* Mininet
* POX Controller
* Python 3
* iperf

---

##  How to Run

### Step 1: Start POX Controller

Open Terminal 1:

```bash
cd pox
./pox.py simple_switch
```
<img width="720" height="193" alt="image" src="https://github.com/user-attachments/assets/dee9873c-dbee-4f97-a2a1-c05e750a65f3" />

---

### Step 2: Run Mininet Topology

Open Terminal 2:

```bash
sudo python3 topology.py
```

You will see:

```
mininet>
```

---

##  Bandwidth Testing

### Step 1: Start Server

```bash
h1 iperf -s &
```

---

### Step 2: Run Clients

#### Single Client

```bash
h2 iperf -c h1 -t 10
```
<img width="807" height="443" alt="image" src="https://github.com/user-attachments/assets/fd274533-c1f6-4cc0-90b5-e8f0b358c0e0" />


####  Multiple Clients (Parallel)

```bash
h2 iperf -c h1 -t 10 &
h3 iperf -c h1 -t 10 &
h4 iperf -c h1 -t 10 &
```
<img width="811" height="497" alt="image" src="https://github.com/user-attachments/assets/5f9dd5e8-c2b7-479a-8e03-7de8d8150250" />

####  More Clients

```bash
h2 iperf -c h1 -t 10 &
h3 iperf -c h1 -t 10 &
h4 iperf -c h1 -t 10 &
h5 iperf -c h1 -t 10 &
h6 iperf -c h1 -t 10 &
```

---

##  Expected Results

| Clients | Bandwidth | Observation              |
| ------- | --------- | ------------------------ |
| 1       | High      | Full bandwidth available |
| 3       | Medium    | Shared bandwidth         |
| 5       | Lower     | Network congestion       |

---

##  Working Explanation

1. When a packet arrives at the switch:

   * If no rule exists → switch sends **Packet_In** to controller
2. Controller (simple_switch):

   * Learns MAC address
   * Decides output port
   * Installs flow rule
3. Switch forwards packets based on flow table

---

##  Flow of Execution

```
Host → Switch → Controller → Flow Rule → Switch → Destination
```

---

##  Key Observations

* Bandwidth decreases as number of clients increases
* All clients share a common link → congestion
* Controller dynamically installs flow rules
* SDN enables centralized control of network behavior

---



---

##  Conclusion

This project successfully demonstrates:

* SDN architecture using Mininet and POX
* Dynamic flow rule installation
* Bandwidth variation under multi-client load
* Impact of congestion in shared networks

---

##  Author

* Name: P.SAMREEN
* SRN: PES2UG24AM108
* Project: SDN Bandwidth Analysis using Mininet

---



