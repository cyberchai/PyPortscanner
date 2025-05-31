# PyPortscanner

**Author:** Chaira Harder
**Project:** Network Security – Port Scanner

This command-line Python tool scans open and closed ports on a specified IP address using different scanning modes (normal, SYN, FIN) and allows users to choose between scanning all ports or only known ones, with results displayed in real-time.

## Features

* Scans target IP for open and closed ports
* Supports three scanning modes: `normal`, `syn`, and `fin`
* Option to scan all ports (0–65535) or only known ports (0–1023)
* Scanning order can be sequential or randomized
* Displays corresponding services (when available)

## Usage

```bash
python3 portscanner.py <target_ip> [options]
```

### Options

| Option          | Description                              | Default  |
| --------------- | ---------------------------------------- | -------- |
| `-m`, `--mode`  | Scanning mode: `normal`, `syn`, or `fin` | `normal` |
| `-o`, `--order` | Scanning order: `order` or `random`      | `order`  |
| `-p`, `--ports` | Port set: `all` or `known`               | `all`    |

### Example

```bash
python3 portscanner.py 192.168.1.1 -m syn -o random -p known
```

## Requirements

* Python 3.x
* Admin/root privileges for SYN/FIN scan modes (uses raw sockets)

## Important!

This tool is intended for **educational purposes only**! Please use responsibly and only on networks and devices you own or have permission to scan.
