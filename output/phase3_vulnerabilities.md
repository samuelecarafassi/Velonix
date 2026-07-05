```markdown
| Vulnerability ID | Description | CVE/CWE | CVSS | Compensating Controls | NIST Gap |
|------------------|-------------|---------|------|-----------------------|----------|
| 1                | Legacy MES on Windows Server 2016 (EOL Jan 2027) without upgrade roadmap. | N/A     | N/A  | None                    | GV.ID.AM, GV.PR.IR |
| 2                | Manual OTA signing with private key on engineer workstation without HSM. | CVE-XXXXX | X.X  | Implement HSM for firmware signing | GV.ID.AM, GV.PR.PS, GV.RS.MI |
| 3                | No SBOM for VeloECU or VeloLink firmware. | N/A     | N/A  | Develop and maintain SBOM | GV.SD.GD |
| 4                | MFA not enforced for 180 external contractors on VPN. | CVE-YYYYY | X.X  | Implement MFA for all external contractor access | GV.PR.AA |
| 5                | Weak OT/IT segmentation allowing Turin plant floor reachable from corporate LAN. | N/A     | N/A  | Improve OT/IT segmentation with firewalls and segmentation solutions | GV.PR.PS |
```