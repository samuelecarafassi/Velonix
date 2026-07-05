### ISO 27005 Risk Assessment

| Risk ID | Threat | Likelihood (1-5) | Impact (1-5) | Inherent Risk (5) | Existing Controls | Residual Risk (3) | Owner | Risk Class |
|---------|--------|--------------------|--------------|-------------------|-------------------|-------------------|-------|------------|
| 1.1     | Ransomware on SAP S/4HANA ERP | 2 | 4 | 8                 | Encryption, Regular Backups | 5               | IT    | Low        |
| 1.2     | Ransomware on CI/CD Pipeline   | 3 | 4 | 12                | Automated Security Checks | 7               | DevOps| Medium     |
| 1.3     | Ransomware on VeloFleet API    | 2 | 4 | 8                 | Encryption, Regular Backups | 5               | DevOps| Low        |
| 1.4     | Ransomware on Telemetry DB      | 3 | 4 | 12                | Regular Data Encryption | 7               | IT    | Medium     |
| 2.1     | Malware on Legacy MES          | 3 | 4 | 12                | Antivirus, Security Patches | 7               | OT    | Medium     |
| 2.2     | Malware on R&D Repository      | 3 | 4 | 12                | Antivirus, Security Patches | 7               | R&D   | Medium     |
| 2.3     | Malware on VeloFleet API        | 3 | 4 | 12                | Encryption, Regular Backups | 7               | DevOps| Medium     |
| 2.4     | Malware on AI Model             | 3 | 4 | 12                | Antivirus, Security Patches | 7               | R&D   | Medium     |
| 3.1     | Social Engineering on Legacy MES | 4 | 4 | 16                | MFA, Access Controls | 9               | OT    | High       |
| 3.2     | Social Engineering on R&D Repository | 4 | 4 | 16                | MFA, Access Controls | 9               | R&D   | High       |
| 3.3     | Social Engineering on CI/CD Pipeline | 4 | 4 | 16                | MFA, Access Controls | 9               | DevOps| High       |
| 3.4     | Social Engineering on VPN Gateway | 4 | 4 | 16                | MFA, Access Controls | 9               | IT    | High       |
| 4.1     | Data Threats on Telemetry DB   | 3 | 5 | 15                | Encryption, Regular Backups | 8               | IT    | Medium     |
| 4.2     | Data Threats on VeloFleet API    | 3 | 5 | 15                | Regular Data Encryption | 8               | DevOps| Medium     |
| 5.1     | DDoS Attacks on VeloLink GWs   | 4 | 4 | 16                | Firewall, Load Balancers | 9               | Field Ops| High       |
| 5.2     | DDoS Attacks on OT Plant Floor Reachable from Corporate LAN | 3 | 4 | 12                | Improved OT/IT Segmentation | 7               | IT    | Medium     |
| 6.1     | Supply Chain Attacks on GitHub Enterprise | 4 | 5 | 20                | Regular Security Audits | 10              | DevOps| High       |
| 6.2     | Supply Chain Attacks on Third-party SaaS (e.g., VeloFleet API) | 3 | 5 | 15                | Regular Vendor Assessments | 8               | DevOps| Medium     |
| 7.1     | Information Manipulation on Publicly Accessible Data | 2 | 4 | 8                 | Strong Access Controls | 5               | IT    | Low        |
| 7.2     | Information Manipulation on Social Media | 3 | 4 | 12                | Regular Monitoring | 7               | IT    | Medium     |
| 8.1     | Insider Threats on Legacy MES   | 3 | 5 | 15                | Strong Access Controls | 9               | OT    | High       |
| 8.2     | Insider Threats on MFA for External Contractors | 4 | 4 | 16                | Enhanced Access Controls | 10              | IT    | High       |

### Residual-Risk Heat Map

| Risk Class  | Low | Medium | High |
|-------------|-----|--------|------|
| Ransomware    |     |        | 🟥   |
| Malware       |     | 🟠     |      |
| Social Engineering | 🟥  |        |      |
| Data Threats  | 🟠  |        |      |
| Availability Attacks | 🟥 | 🟠     |      |
| Supply Chain Attacks | 🟥 |        |      |
| Information Manipulation | 🟠 | 🟠    |      |
| Insider Threats | 🟥  | 🟠    |      |

**Legend:**
- 🟥 : High Residual Risk
- 🟠 : Medium Residual Risk