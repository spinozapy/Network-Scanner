# Network Scanner

A professional Python tool to scan networks, detect live hosts, and perform port scans on specific IP addresses.

## Requirements
- Python 3.x
- `colorama` library (Install using `pip install colorama`)

## Installation

1. Clone the repository.
2. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the tool:
    ```bash
    python main.py
    ```

## Usage
1. Choose an option:
    - Type `1` to run the ping sweep and enter the network to discover live hosts.
    - Type `2` to run the port scan and enter the IP address to scan for open ports.
    - Type `3` to view the list of common ports.
    - Type `4` to add new ports to the list of common ports.

2. Follow the prompts to enter the network address, IP address, view results, or add new ports. For adding ports, type each new port number and press Enter. Type `exit` to finish adding.

## Features
- Scans networks to find live hosts (Ping Sweep).
- Scans specific IP addresses for open ports.
- Displays common ports.
- Allows users to add custom ports.

## Example

```bash
Network Scanner
=================

Choose an option (type 'exit' to quit):

1  = Run Ping Sweep
2  = Run Port Scan
3  = List of Common Ports
4  = Add Ports

root@you:~$ 1
[Network Scanner]: Enter the network (e.g., 192.168.1): 192.168.1

[Network Scanner]: Pinging hosts in network 192.168.1.0/24...
[Network Scanner]: 192.168.1.1 is up
[Network Scanner]: 192.168.1.2 is down

root@you:~$ 2

[Network Scanner]: Enter the IP address: 192.168.1.1

[Network Scanner]: Port Scan Results
Open Ports:
  22
  80
  443

root@you:~$ 3

[Network Scanner]: Common Ports
Common Ports:
  21
  22
  23
  25
  53
  80
  110
  123
  135
  139
  143
  443
  445
  993
  995
  1723
  3306
  3389
  5900
  8080

root@you:~$ 4
[Network Scanner]: Enter ports to add (type 'exit' to finish adding):
Add Port: 8081

[Network Scanner]: Added port: 8081

Add Port: 8888

[Network Scanner]: Added port: 8888

Add Port: exit

[Network Scanner]: Port addition finished.

```

## Usage Caution
- For educational or testing purposes only.
- Do not use for malicious activities.
- Follow ethical standards while using this tool.
