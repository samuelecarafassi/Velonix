**Velonix Asset Inventory**
=====================================

| Asset ID | Name | Category | Criticality (1-5) | Classification | Owner | NIST CSF 2.0 Reference |
| --- | --- | --- | --- | --- | --- | --- |
| IT001 ⭐⚠️ | SAP S/4HANA ERP | Business System | 5 | Confidential, High Availability | IT Department | ID.AM.1, GV.RM |
| IT002 ⚠️ | Legacy MES (Windows Server 2016) | OT System | 4 | Confidential, Operational Continuity | Manufacturing Department | ID.AM.2, GV.RM |
| IT003 | Active Directory / DNS | Identity Management | 3 | Confidential, Access Control | IT Department | PR.AA.1, ID.IM.1 |
| IT004 | R&D source code repository (firmware, design files) | Development Environment | 5 | Confidential, Innovation | R&D Department | ID.AM.3, GV.RR |
| IT005 | CI/CD pipeline (GitHub Enterprise) | Development Environment | 4 | Confidential, Agility | DevOps Team | ID.IM.2, PR.PS.1 |
| IT006 ⚠️ | OTA signing workstation | Business System | 5 | Confidential, Signing Key Management | Engineering Department | GV.RR, ID.AM.4 |
| IT007 | VeloFleet diagnostics API | Application | 3 | Confidential, Telemetry Data | Software Development Team | PR.DS.1, ID.IM.3 |
| IT008 | Vehicle telemetry database (~340,000 vehicles) | Database | 5 | Personal Data, GDPR Scope | Data Analytics Team | PR.DS.2, ID.AM.5 |
| IT009 | AI diagnostic model (proprietary) | Application | 4 | Confidential, Diagnostic Insights | Data Science Team | PR.PS.2, ID.IM.4 |
| OT001 ⚠️ | PLCs and industrial robots | Industrial Control System | 4 | Operational Continuity, Safety | Manufacturing Department | ID.AM.6, GV.RM |
| OT002 | MES-to-OT integration layer | Industrial Control System | 3 | Operational Continuity, Agility | Manufacturing Department | ID.IM.5, PR.PS.3 |
| ED001 ⭐ | VeloLink V2X telematics gateway (deployed in vehicles) | Edge Device | 5 | Confidential, Vehicle Safety | Engineering Department | GV.RR, ID.AM.7 |
| ED002 ⭐⚠️ | VeloECU engine control unit firmware | Embedded System | 5 | Confidential, Vehicle Performance | Engineering Department | GV.RR, ID.AM.8 |
| IAM001 | Okta IAM | Identity Management | 3 | Confidential, Access Control | IT Department | PR.AA.2, ID.IM.6 |
| IAM002 | Palo Alto NGFW/SIEM | Network Security System | 4 | Confidential, Threat Detection | IT Department | PR.IR.1, DE.CM |
| VPN001 | VPN gateway (180 external contractors) | Network Security System | 3 | Confidential, Access Control | IT Department | PR.AA.3, ID.IM.7 |

**Legend:**

* ⭐: Crown jewel
* ⚠️: Legacy/EOL system

Note that this inventory is not exhaustive and may require further refinement based on the organization's specific needs.