# enisa_threats.py
# Source: ENISA Threat Landscape 2025 (October 2025)
# Reporting period: July 2024 – June 2025
# Manually curated for the automotive / manufacturing sector.

ENISA_ETL_2025_AUTOMOTIVE = {
    "report": "ENISA Threat Landscape 2025",
    "published": "October 2025",
    "sector_notes": (
        "The manufacturing sector (including automotive) rose from 7th to 4th place among "
        "NIS2 sectors compared to ETL 2024, accounting for 2.9% of total incidents. Within "
        "identified subsectors, there is a clear targeting focus on automotive and defence "
        "entities. Cybercrime is the primary threat to manufacturing, driving 59.3% of sector "
        "activity and the highest impact, while hacktivism (39.3% of activities) frequently "
        "targets operational technology (OT) systems and subsector websites."
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
                "Remains at the core of intrusion activity. In the manufacturing sector, "
                "the most frequently deployed ransomware strains are Akira (48.7%), "
                "Qilin (20.5%), and FOG (10.3%), causing severe business continuity disruptions."
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
                "Part of the dominant cybercriminal activity (59.3%) targeting manufacturing. "
                "State-aligned threat groups also leverage stealthy malware frameworks and "
                "exploit signed drivers to maintain persistent access to infrastructure."
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
                "Phishing continues to be the dominant primary intrusion vector overall (60%). "
                "By early 2025, AI-supported phishing campaigns escalated dramatically, "
                "representing over 80% of observed social engineering activity globally."
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
                "Data breaches constitute a significant portion of cybercrime impact within "
                "manufacturing, accounting for 20.5% of the sector's reported incidents."
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
                "Hacktivist activities represent 39.3% of the sector's threats. Websites "
                "within the automotive and defence subsectors are heavily targeted, making up "
                "45.8% of all manufacturing targeting by hacktivist groups."
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
                "State-aligned threat groups have intensified long-term cyberespionage "
                "campaigns targeting EU manufacturing and logistics, demonstrating advanced "
                "tradecraft such as supply chain compromise and open-source repository abuse."
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
                "Foreign Information Manipulation and Interference (FIMI) campaigns frequently "
                "aim to publicly link manufacturers to geopolitical conflicts, using "
                "AI-assisted tools like voice cloning and AI-operated botnets (e.g., Green Cicada)."
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
                "Unauthorised access by insider threats accounts for a small but still meaningful "
                "share (0.8%) of observed initial intrusion vectors across the landscape."
            ),
        },
    ],
}


def get_threat_summary_for_prompt(sector: str) -> str:
    """
    Returns a formatted string summarising ENISA ETL 2025 threats
    for the given sector, ready to be injected into a Phase 2 prompt.
    """
    data = ENISA_ETL_2025_AUTOMOTIVE  # extend with other sectors if needed
    lines = [
        f"## ENISA ETL 2025 — Threat Intelligence ({sector} sector)",
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
