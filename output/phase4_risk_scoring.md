### ISO 27005 Risk Assessment

#### Risk Analysis

| Risk ID | Threat | Likelihood (1-5) | Impact (1-5) | Inherent Risk (5-25)[6D[K
(5-25) | Existing Controls | Residual Risk (5-25) | Owner | Risk Class |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R001 | Ransomware targeting legacy MES system | 3 | 4 | 12 | Upgrade to s[1D[K
supported version with security patches and backups | 8 | IT | Medium |
| R002 | Supply chain attack tampering firmware in CI/CD pipeline | 3 | 5 |[1D[K
| 15 | Implement HSM for secure key management and automated build processe[8D[K
processes | 9 | DevOps | High |
| R003 | Social engineering spear-phishing targeting contractors with acces[5D[K
access to ECU signing keys | 4 | 5 | 20 | Enforce MFA for all contractors a[1D[K
and strict access controls | 10 | IT | High |
| R004 | Data exfiltration of personal data from VeloLink telemetry through[7D[K
through unsecured third-party SaaS | 3 | 5 | 15 | Ensure secure communicati[11D[K
communication protocols, network segmentation, and regular audits | 9 | IT [K
| High |
| R005 | DDoS attack on Azure IoT Hub for VeloLink Devices | 4 | 4 | 16 | I[1D[K
Implement DDoS mitigation services and robust availability protection mecha[5D[K
mechanisms | 8 | DevOps | Medium-High |

#### Residual-Risk Heat Map

```
      High       Medium-High    Medium     Low
|___________________________|
High         R003, R004        R001, R005  
Medium-High  R002              
Medium           
Low                
```

