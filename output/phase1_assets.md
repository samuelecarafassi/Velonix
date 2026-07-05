```markdown
| Asset ID        | Name                         | Category                          | Criticality | Classification | Owner       | NIST CSF 2.0 Reference |
|-----------------|------------------------------|-----------------------------------|-------------|------------------|-------------|------------------------|
| SAP S/4HANA ERP  | On-prem ERP                  | Business Processes                | 5           | High             | IT          | GV.PR.PS               |
| Legacy MES      | Plant floor control          | Operational Technology            | 4           | Medium           | OT          | GV.ID.AM, GV.PR.IR     |
| AD / DNS        | Active Directory/DNS         | Identity Management                 | 3           | Low              | IT          | GV.PR.AA               |
| R&D Repository  | Firmware & Design Files      | Software Development              | 4           | Medium           | R&D         | GV.ID.AM, GV.PR.IR     |
| CI/CD Pipeline  | GitHub Enterprise              | Continuous Integration/Continuous Delivery | 3           | Low              | DevOps       | GV.ID.AM, GV.PR.IR     |
| OTA Signing Wkstn | Manual signing of firmwares   | Security Operations               | 4           | Medium           | Engineering  | GV.ID.AM, GV.PR.PS, GV.RS.MI |
| VeloFleet API   | VeloFleet diagnostics API    | Software as a Service             | 5           | High             | DevOps       | GV.GV.OC               |
| Telemetry DB    | Vehicle telemetry data        | Data Security                     | 5           | High             | IT          | GV.GD, GV.PR.DS, GV.RS.MI |
| AI Model        | Proprietary diagnostic model   | Data Protection                   | 4           | Medium           | R&D         | GV.GV.OC               |
| OTA Firmware Distro | Distribution service       | Network Security                  | 5           | High             | DevOps       | GV.GV.OC, GV.PR.IR     |
| PLCs & Robots   | Industrial equipment          | Operational Technology            | 4           | Medium           | OT          | GV.ID.AM, GV.PR.IR     |
| MES-to-OT Integ | Integration layer               | Network Security                  | 3           | Low              | IT          | GV.GV.OC               |
| VeloLink GWs    | Telematics gateways         | IoT Devices                       | 4           | Medium           | Field Ops   | GV.ID.AM, GV.PR.IR     |
| VeloECU Firmware | Engine control unit firmware  | Software Development              | 3           | Low              | R&D         | GV.ID.AM               |
| Okta IAM        | Identity and Access Management | Identity Management                 | 4           | Medium           | IT          | GV.PR.AA               |
| Palo Alto NGFW/SIEM | Firewall & SIEM             | Network Security                  | 5           | High             | IT          | GV.GV.OC, GV.PR.PS     |
| VPN Gateway     | External contractor access   | Identity Management                 | 3           | Low              | IT          | GV.PR.AA               |
```