# Scans

This folder stores nmap scan files
generated during SOC investigation.

## Important
Scans are excluded via .gitignore
for the following reasons:
- May contain sensitive information
- Large file sizes
- Results are environment specific
- Regenerated for each investigation

## Scan Commands

### Default Scan
nmap --unprivileged -sT -sV [Target IP] -oA scans/scan

### Full Scan
nmap --unprivileged -sT -sV -p- [Target IP] -oA scans/scan

### Quick Scan
nmap --unprivileged -sT [Target IP] -oA scans/scan

### Output Files
Each scan produces three files:
scan.nmap
- Human-readable
- Best for manual review
scan.xml
- XML format
- Used by python script
- Machine parseable
scan.gnmap
- Grepable format
- Best for quick searching
- Example:
  grep "open" scan.gnmap

## Notes
- Always run full scan for complete picture
- Default scan misses high numbered ports
- Use --unprivileged flag on rootless setup
- Save with -oA to get all formats
