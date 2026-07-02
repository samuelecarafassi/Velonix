# Executive Summary

**Top Risks:**
1. **Ransomware targeting Legacy MES (R001)** - High risk, potential loss of control over critical systems.
2. **Supply chain compromise through open-source repository abuse (R004)** - Very high risk, significant impact on product security.
3. **Data exfiltration from vehicle telemetry database (R005)** - Medium risk, severe regulatory penalties and customer trust damage.

**Regulatory Exposure:**
- Compliance with GDPR, UNECE R155/R156, ISO/SAE 21434, and NIS2 required for various controls to ensure ongoing compliance.

**Cost of Inaction:**
- Potential financial fines up to €40M (GDPR max fine + NIS2 maximum fine).
- Operational disruptions, loss of business continuity, and damage to reputation.

**Investment Request:**
- Total estimated investment: €500k for controls over 12 months.
- Key initiatives include upgrading Legacy MES, implementing HSMs, MFA enforcement, and network segmentation.

---

# 12-Month Remediation Roadmap

| Initiative | Timeline | Risks Addressed | NIST Controls | Estimated Cost | FTE Required | KPI |
|------------|----------|-----------------|---------------|----------------|--------------|-----|
| **Upgrade Legacy MES** | Month 1-2 | R001, V001 | PR, PE, PO | €150k | 3 | Complete implementation within 2 weeks |
| **Implement HSM for OTA keys** | Month 3-5 | R008, V002 | PR, PM, PS, PO | €200k | 4 | Hardware security module fully operational within 3 weeks |
| **Enforce MFA for all users** | Month 6 | R002, R005, R007 | ID.AM, ID.RA, PI, PR | €100k | 2 | Multi-factor authentication enabled for all users in 1 week |
| **Create and maintain SBOM for firmware** | Month 7-8 | R004, V003 | ID.AM, ID.PA, PI, PM, PS, PO | €50k | 3 | Software Bill of Materials fully documented within 4 weeks |
| **Implement robust network segmentation** | Month 9-12 | R003, R006 | PI, PR, PM, PS, PO | €100k | 4 | Network segmentation complete by end of 4th month |

Total Estimated Cost: €500k
FTE Required: 14
KPIs:
- Completion of all initiatives within specified timelines.
- Reduction in risk scores to below predefined thresholds by the end of each quarter.

This roadmap prioritizes critical controls that address high and very high-risk vulnerabilities, ensuring compliance with relevant regulations while minimizing business disruption.