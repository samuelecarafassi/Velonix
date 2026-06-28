COMPANY_SECTOR = "automotive"
COMPANY_CONTEXT = """
Company: Velonix S.p.A.
HQ: Turin, Italy. Sites: Turin, Milan, Kraków, Valencia.
Employees: 1,100 + 180 contractors. Revenue: €310M/year.
Sector: Automotive Tier 1 supplier (embedded ECUs, V2X gateways, fleet SaaS).
Products: VeloECU (engine control units with OTA), VeloLink (V2X telematics gateway,
  deployed in ~340,000 vehicles), VeloFleet (SaaS diagnostics platform).
Key OEM customers: Stellantis, BMW, Renault (+ 3 others).
Regulatory: UNECE WP.29 R155/R156, ISO/SAE 21434, GDPR, NIS2, ISO 27001.
Architecture: On-prem Turin HQ (ERP, MES, AD, R&D, CI/CD) + Azure EU (VeloFleet,
  OTA distribution, AI inference) + OT plant floor (PLCs/MES, partial IT connectivity)
  + 340k connected VeloLink gateways (MQTT → Azure IoT Hub → VeloFleet API).
Third-party SaaS: SAP S/4HANA, Okta IAM, Palo Alto NGFW/SIEM, GitHub Enterprise.
Known weaknesses:
  1. Legacy MES on Windows Server 2016 (EOL Jan 2027), no upgrade roadmap.
  2. OTA signing is manual, no HSM; private key on engineer workstation.
  3. No SBOM for VeloECU or VeloLink firmware.
  4. MFA not enforced for 180 external contractors on VPN.
  5. OT/IT segmentation incomplete: Turin plant floor reachable from corporate LAN.
"""
REGULATORY_CONTEXT = """
Applicable regulations for Velonix S.p.A.:
- UNECE WP.29 R155 (cybersecurity management) and R156 (OTA updates):
  mandatory for all vehicle types approved after July 2024 in EU.
  Non-compliance blocks OEM type approval.
- ISO/SAE 21434:2021: contractually required by Stellantis and BMW.
  Clause 15 maps to NIST ID.RA; Clause 10 maps to NIST PR.
- NIS2 Directive (Art. 21): Velonix is an 'important entity' in the
  automotive sector. Requires risk management measures, incident
  reporting within 24h. Max fine: €10M or 2% global turnover.
- GDPR (Art. 83): VeloLink telemetry = personal data (location,
  driving behaviour). Max fine: €20M or 4% global turnover.
- ISO/IEC 27001:2022: Velonix is certified. Assessment findings
  must align with existing ISMS scope.
"""
ASSETS = """
Known systems and components to include in the inventory (expand with
reasonable, clearly-labelled inferred assets where needed, e.g. databases,
network devices, or supporting services typical of this architecture):

On-prem Turin HQ:
- SAP S/4HANA ERP
- Legacy MES (Windows Server 2016, plant floor control)
- Active Directory / DNS
- R&D source code repository (firmware, design files)
- CI/CD pipeline (GitHub Enterprise)
- OTA signing workstation (holds private signing key, no HSM)

Azure EU — VeloFleet platform:
- VeloFleet diagnostics API
- Vehicle telemetry database (~340,000 vehicles, PII/GDPR scope)
- AI diagnostic model (proprietary)
- OTA firmware distribution service

OT / plant floor (Turin, Kraków):
- PLCs and industrial robots
- MES-to-OT integration layer

Connected fleet edge:
- VeloLink V2X telematics gateway (deployed in vehicles)
- VeloECU engine control unit firmware

Third-party / IAM:
- Okta IAM
- Palo Alto NGFW/SIEM
- VPN gateway (180 external contractors, no MFA enforced)
"""