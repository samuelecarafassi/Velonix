```markdown
| Control                                  | NIST CSF Reference         | Priority   | Effort   | Regulatory Benefit                                                                 |
|------------------------------------------|----------------------------|------------|----------|----------------------------------------------------------------------------------|
| Upgrade Legacy MES to a supported OS/version| PR, PE, PO                   | High       | 2 weeks  | Compliance with UNECE R155/R156 and NIS2                                         |
| Implement HSM for OTA keys                | PR, PM, PS, PO               | High       | 3 weeks  | Compliance with GDPR, ISO/SAE 21434, and UNECE R155/R156                         |
| Enforce MFA for all users                   | ID.AM, ID.RA, PI, PR         | Medium     | 1 week   | Compliance with GDPR, NIS2, and ISO/SAE 21434                                   |
| Create and maintain SBOM for firmware       | ID.AM, ID.PA, PI, PM, PS, PO   | High       | 4 weeks  | Compliance with UNECE R155/R156 and ISO/SAE 21434                               |
| Implement robust network segmentation       | PI, PR, PM, PS, PO            | Very High  | 4 weeks  | Compliance with GDPR, NIS2, and ISO/SAE 21434                                   |

**Regulatory Exposure Summary**

- **GDPR**: Risk reduction through MFA for external contractors (R002), which mitigates data exposure risks.
- **NIS2**: Improved segmentation reduces the risk of OT/IT breaches impacting vehicle telemetry data (R005).
- **UNECE R155/R156**: Compliance with enhanced cybersecurity controls, including OTA signing and network segmentation.

**UNECE R155/R156 Mapping**

- UNECE R155: Enhanced controls for managing security of critical systems, including Legacy MES (V001) and R&D source code repository (V003).
- UNECE R156: OTA signing and network segmentation fall under enhanced cybersecurity measures.

**NIS2 Mapping**

- NIS2: Enhanced controls include MFA enforcement (R002), network segmentation (R003, R005, R006), and HSM implementation for OTA keys (R008).

**GDPR Mapping**

- GDPR: MFA enforcement reduces risks associated with data breaches affecting vehicle telemetry data (R005).
```