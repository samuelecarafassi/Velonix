```markdown
| Vulnerability ID | Description | CVE/CWE | CVSS | Compensating Controls | NIST Gap |
|------------------|-------------|---------|------|-----------------------|----------|
| V001             | Legacy MES on Windows Server 2016 (EOL) | N/A     | High | Upgrade to a supported OS/version | PR, PE, PO |
| V002             | Manual OTA signing without HSM | CWE-311 | Medium | Implement hardware security module (HSM) for OTA keys | PR, PM, PS, PO |
| V003             | No SBOM for firmware | CWE-609 | High | Create and maintain Software Bill of Materials (SBOM) | ID.AM, ID.PA, PI, PM, PS, PO |
| V004             | Missing MFA for 180 external contractors on VPN | N/A     | Medium | Enforce Multi-Factor Authentication (MFA) for all users | ID.AM, ID.RA, PI, PR |
| V005             | Weak OT/IT segmentation | CWE-362 | High | Implement robust network segmentation and isolation between OT and IT networks | PI, PR, PM, PS, PO |
```