# Scripts

Documentation for all the scripts in the
Pocket SOC Toolkit rootless version.

## soc_scanner_v1.py

### Description
Parses nmap XML output and generates an
automated SOC report with risk assessment
for each discovered service.

### Requirements
- Python 3
- Nmap scan XML output file

### Usage
Run nmap scan first:
nmap --unprivileged -sT -sV [Target IP] -oA ../scans/scan
Then run the scanner:
python3 soc_scanner_v1.py

### Output
Prints report to terminal showing:
- Total open ports discovered
- Port number
- Service name
- Risk level (CRITICAL/HIGH/MEDIUM/LOW)
- Critical findings summary
- Saves report to ../scans/soc_report.txt

### Known Limitations
- Requires existing nmap XML file
- Paths are hardcoded to scans folder
- No argument parsing
- No color output

### Version History
v1 - Initial implementation
     Basic XML parsing
     Risk assessment
     Report generation
     Saved to text file
