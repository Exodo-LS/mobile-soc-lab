#!/usr/bin/env python3
import re, datetime, os

def assess_risk(service):
    critical = ['ftp','telnet','shell','exec',
        'login','bindshell','vnc','irc','java-rmi']
    high = ['http','mysql','postgresql',
        'smtp','netbios-ssn','distccd','drb']
    medium = ['ssh','domain','rpcbind','nfs']
    if service in critical:
        return 'CRITICAL'
    elif service in high:
        return 'HIGH'
    elif service in medium:
        return 'MEDIUM'
    else:
        return 'LOW'

xml_file = os.path.expanduser(
    "~/mobile-soc-lab/01-pocket-soc-toolkit/rootless/scans/scan.xml")
with open(xml_file, 'r') as f:
    data = f.read()

ports = re.findall(
    r'portid="(\d+)".*?state="open".*?'
    r'<service name="([^"]+)"',
    data)

now = datetime.datetime.now().strftime(
    "%Y-%m-%d %H:%M:%S")
print("=" * 50)
print("  POCKET SOC TOOLKIT REPORT")
print("  Generated: " + now)
print("=" * 50)
print("Total Ports Open: " + str(len(ports)))
print("")
print("PORT     SERVICE       RISK")
print("-" * 50)
for p in ports:
    port, svc = p
    risk = assess_risk(svc)
    print(port.ljust(10) + svc.ljust(15) + risk)
print("")
print("=" * 50)
print("CRITICAL FINDINGS")
print("=" * 50)
for p in ports:
    port, svc = p
    if assess_risk(svc) == 'CRITICAL':
        print("[!] Port " + port + " - " + svc)

report_file = os.path.expanduser(
    "~/mobile-soc-lab/01-pocket-soc-toolkit/rootless/scans/soc_report.txt")
lines = []
for p in ports:
    port, svc = p
    risk = assess_risk(svc)
    lines.append(port + " " + svc + " " + risk)
with open(report_file, 'w') as f:
    f.write("\n".join(lines))
print("\n[*] Saved: " + report_file)
