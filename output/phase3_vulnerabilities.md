| Vulnerability ID | Description | CVE/CWE | CVSS | Compensating Controls |[1D[K
| NIST Gap |
| --- | --- | --- | --- | --- | --- |
| V001 | Legacy MES on Windows Server 2016 with no upgrade roadmap is vulne[5D[K
vulnerable to known vulnerabilities, leading to potential exploitation by a[1D[K
attackers. | CVE-2021-44228 | 9.8 | N/A (No immediate compensating controls[8D[K
controls) | CM, PR.A |
| V002 | Manual OTA signing without an HSM exposes the private key on engin[5D[K
engineer workstations, increasing risk of compromise and potential for mali[4D[K
malicious firmware distribution. | CWE-311: Missing Encryption on Critical [K
Data | 9.5 | Use HSM for firmware signing | CM, PR.D |
| V003 | No SBOM for VeloECU or VeloLink firmware makes it difficult to tra[3D[K
track components, verify authenticity, and identify vulnerabilities. | N/A [K
| N/A | Implement SBOM for firmware components | AC, ID.AM |
| V004 | Missing MFA for 180 external contractors on VPN increases risk of [K
unauthorized access and potential data breaches. | CWE-327: Use of a Broken[6D[K
Broken Authentication Mechanism | 6.5 | Enforce MFA for all external contra[6D[K
contractor access | CM, PR.A |
| V005 | Weak OT/IT segmentation allows Turin plant floor to be reachable f[1D[K
from corporate LAN, enabling attackers to potentially compromise both OT an[2D[K
and IT environments. | N/A | N/A | Implement comprehensive OT/IT segmentati[10D[K
segmentation | AC, PR.PT |

