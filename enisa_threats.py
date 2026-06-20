# enisa_threats.py
# Source: ENISA Threat Landscape 2024 (October 2024)
# Reporting period: June 2023 – June 2024
# Manually curated for the automotive / manufacturing sector.

ENISA_ETL_2024_AUTOMOTIVE = {
    "report": "ENISA Threat Landscape 2024",
    "published": "October 2024",
    "sector_notes": (
        "Automotive/manufacturing is increasingly targeted due to OT/IT convergence, "
        "connected vehicle attack surfaces, and high-value IP (firmware, design data). "
        "Supply chain attacks against Tier 1 suppliers are explicitly flagged as a "
        "rising priority in ETL 2024. Ransomware on OT environments causes production "
        "halts with direct financial and safety impact."
    ),
    "threats": [
        {
            "rank": 1,
            "category": "Ransomware",
            "trend": "Rising",
            "sector_severity": "Critical",
            "attack_techniques": ["T1486", "T1566", "T1190"],
            "attack_tactics": ["Impact", "Initial Access"],
            "sector_note": (
                "Manufacturing is the second most targeted sector globally. "
                "OT ransomware causes production halts and safety risks."
            ),
        },
        {
            "rank": 2,
            "category": "Malware (incl. infostealers)",
            "trend": "Rising",
            "sector_severity": "High",
            "attack_techniques": ["T1555", "T1539", "T1485"],
            "attack_tactics": ["Credential Access", "Impact"],
            "sector_note": (
                "Infostealers targeting R&D environments to exfiltrate "
                "firmware source code and design IP."
            ),
        },
        {
            "rank": 3,
            "category": "Social Engineering",
            "trend": "Rising",
            "sector_severity": "High",
            "attack_techniques": ["T1566.001", "T1566.002"],
            "attack_tactics": ["Initial Access"],
            "sector_note": (
                "LLM-generated spear-phishing campaigns against engineers "
                "with access to ECU signing credentials."
            ),
        },
        {
            "rank": 4,
            "category": "Data Threats",
            "trend": "Stable",
            "sector_severity": "Critical",
            "attack_techniques": ["T1530", "T1048", "T1213"],
            "attack_tactics": ["Collection", "Exfiltration"],
            "sector_note": (
                "Vehicle telemetry constitutes personal data under GDPR. "
                "Exfiltration of OEM integration data risks contractual breach."
            ),
        },
        {
            "rank": 5,
            "category": "Availability Attacks (DDoS)",
            "trend": "Rising",
            "sector_severity": "High",
            "attack_techniques": ["T1498", "T1499"],
            "attack_tactics": ["Impact"],
            "sector_note": (
                "DDoS against VeloFleet API would disrupt OEM diagnostics "
                "and OTA update delivery to 340,000 vehicles."
            ),
        },
        {
            "rank": 6,
            "category": "Supply Chain Attacks",
            "trend": "Rising",
            "sector_severity": "Critical",
            "attack_techniques": ["T1195.002", "T1199", "T1601"],
            "attack_tactics": ["Initial Access"],
            "sector_note": (
                "ETL 2024 explicitly flags Tier 1 automotive suppliers as "
                "pivot points into OEM networks. Firmware tampering via "
                "compromised build pipelines is a named emerging threat."
            ),
        },
        {
            "rank": 7,
            "category": "Information Manipulation",
            "trend": "Rising",
            "sector_severity": "Medium",
            "attack_techniques": ["T1565", "T1195.002"],
            "attack_tactics": ["Resource Development"],
            "sector_note": (
                "Manipulation of diagnostic telemetry data could mislead "
                "OEM maintenance decisions at scale."
            ),
        },
        {
            "rank": 8,
            "category": "Insider Threats",
            "trend": "Stable",
            "sector_severity": "High",
            "attack_techniques": ["T1078", "T1048"],
            "attack_tactics": ["Exfiltration", "Collection"],
            "sector_note": (
                "180 external contractors with VPN access and no MFA "
                "represent a significant insider/privilege-abuse surface."
            ),
        },
    ],
}


def get_threat_summary_for_prompt(sector: str) -> str:
    """
    Returns a formatted string summarising ENISA ETL 2024 threats
    for the given sector, ready to be injected into a Phase 2 prompt.
    """
    data = ENISA_ETL_2024_AUTOMOTIVE  # extend with other sectors if needed
    lines = [
        f"## ENISA ETL 2024 — Threat Intelligence ({sector} sector)",
        f"Source: {data['report']} | Published: {data['published']}",
        f"Sector context: {data['sector_notes']}",
        "",
        "| Rank | Category | Trend | Sector Severity | Primary ATT&CK Techniques |",
        "|------|----------|-------|-----------------|--------------------------|",
    ]
    for t in data["threats"]:
        techniques = ", ".join(t["attack_techniques"])
        lines.append(
            f"| {t['rank']} | {t['category']} | {t['trend']} "
            f"| {t['sector_severity']} | {techniques} |"
        )
    lines.append("")
    lines.append("### Sector-specific notes per category")
    for t in data["threats"]:
        lines.append(f"- **{t['category']}**: {t['sector_note']}")
    return "\n".join(lines)
