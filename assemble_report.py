from pathlib import Path

OUTPUT_DIR = Path("output")

ORDER = [
    ("1. Asset Inventory", "phase1_assets.md"),
    ("2. Threat Landscape", "phase2_threats.md"),
    ("3. Vulnerability Analysis", "phase3_vulnerabilities.md"),
    ("4. Risk Assessment", "phase4_risk_scoring.md"),
    ("5. Control Mapping", "phase5_controls.md"),
    ("6. Remediation Roadmap", "phase6_roadmap.md"),
]


def read_file(filename):
    path = OUTPUT_DIR / filename

    if not path.exists():
        return f"Missing file: {filename}"

    return path.read_text(encoding="utf-8")


def extract_executive_summary(text):
    lower = text.lower()

    marker = "executive summary"

    idx = lower.find(marker)

    if idx == -1:
        return "Executive summary not found."

    return text[idx:]


def main():
    report = []

    report.append("# Velonix S.p.A. Cybersecurity Risk Assessment\n")

    report.append(
        "## Methodology\n"
        "NIST CSF 2.0 + ISO 27005 + ENISA Threat Landscape 2025 + MITRE ATT&CK\n"
    )


    for title, filename in ORDER:

        report.append(f"\n\n# {title}\n")
        report.append(read_file(filename))

    output_path = OUTPUT_DIR / "Velonix_Risk_Assessment.md"

    output_path.write_text(
        "\n".join(report),
        encoding="utf-8"
    )

    print(f"Report generated: {output_path}")


if __name__ == "__main__":
    main()