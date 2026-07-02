```markdown
| Risk ID | Threat Description | Likelihood (1-5) | Impact (1-5) | Inherent Risk | Existing Controls | Residual Risk | Owner | Risk Class |
|---------|--------------------|------------------|--------------|---------------|-------------------|---------------|-------|------------|
| R001    | Ransomware targeting the Legacy MES system | 2                | 4            | 8             | Upgrade to a supported OS/version | 6             | OT/IT | High       |
| R002    | Malware infection through phishing emails to external contractors | 3                | 3            | 9             | Enforce Multi-Factor Authentication (MFA) for all users | 7             | IT    | Medium     |
| R003    | DDoS attacks targeting the VeloFleet API and Azure IoT Hub | 2                | 4            | 8             | Implement robust network segmentation and isolation between OT and IT networks | 6             | IT    | High       |
| R004    | Supply chain compromise through open-source repository abuse | 3                | 5            | 15            | Create and maintain Software Bill of Materials (SBOM) | 12            | IT    | Very High  |
| R005    | Data exfiltration from the vehicle telemetry database | 3                | 4            | 12            | Enforce Multi-Factor Authentication (MFA) for all users | 9             | IT    | Medium     |
| R006    | Insider threat accessing the R&D source code repository | 3                | 5            | 15            | Implement robust network segmentation and isolation between OT and IT networks | 12            | IT    | Very High  |
| R007    | Social engineering through AI-assisted phishing campaigns | 3                | 3            | 9             | Enforce Multi-Factor Authentication (MFA) for all users | 7             | IT    | Medium     |
| R008    | Malware in the CI/CD pipeline compromising build artifacts | 2                | 5            | 10            | Implement hardware security module (HSM) for OTA keys | 6             | IT    | High       |

**Residual-Risk Heat Map**

| Risk Class     | Very High | High        | Medium      |
|----------------|-----------|-------------|-------------|
| R004, R006     |           |             |             |
| R001, R003     |           |             |             |
| R008           |           |             |             |
| R002, R005     |           |             |             |
```