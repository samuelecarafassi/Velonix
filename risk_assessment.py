import json
import urllib.request
from pathlib import Path

from config import (
    COMPANY_CONTEXT,
    COMPANY_SECTOR,
    REGULATORY_CONTEXT,
    ASSETS,
    NIST_CSF2_CATEGORIES
)

from enisa_threats import get_threat_summary_for_prompt


OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)

SYSTEM_PROMPT = """
You are a senior cybersecurity risk analyst with 15 years of experience.

Rules:
- Use NIST CSF 2.0 references.
- Use ISO 27005 likelihood (1-5) × impact (1-5).
- Always distinguish inherent and residual risk.
- Reference ENISA ETL 2025 categories where relevant.D
- Consider GDPR, NIS2, UNECE WP.29 R155/R156 and ISO/SAE 21434.
- Format tables in markdown (.md file).
- Be concise but complete.
- Respond immediately with the final output
- Do not include conversational filler, introductory remarks, transition phrases, or closing commentary
"""


def ask_ai(prompt: str, context: str = "",model_name = "llama3.1:8b") -> str:
    full_prompt = f"""
{SYSTEM_PROMPT}

# Company Context
{COMPANY_CONTEXT}

# Regulatory Context
{REGULATORY_CONTEXT}

# Previous Assessment Context
{context}

# Task
{prompt}
"""
     
    # Configure a clean HTTP API request to the local Ollama instance
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": model_name,
        "prompt": full_prompt,
        "stream": False  # disables streaming animation codes
    }
    
    headers = {"Content-Type": "application/json"}
    data = json.dumps(payload).encode("utf-8")
    
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    
    try:
        with urllib.request.urlopen(req) as response:
            res_body = json.loads(response.read().decode("utf-8"))
            return res_body["response"]
    except Exception as e:
        raise RuntimeError(f"Ollama API request failed: {e}")

    return ""


PHASES = [
    (
        "phase1_assets.md",
        """
Generate a structured asset inventory for Velonix.

Columns:
Asset ID | Name | Category | Criticality (1-5) |
Classification | Owner | NIST CSF 2.0 Reference

Requirements:
- At least 15 assets.
- Flag crown jewels with ⭐.
- Flag legacy/EOL systems with ⚠️.
- Use NIST ID.AM references.

""" + ASSETS + "\n" + NIST_CSF2_CATEGORIES
    ),
    (
        "phase2_threats.md",
        f"""
Using ENISA ETL 2025 as the strategic baseline and MITRE ATT&CK
for technical precision, identify the top 8 threats for Velonix.

{get_threat_summary_for_prompt(COMPANY_SECTOR)}

For each threat include:

Threat ID |
Threat |
ENISA Category |
MITRE Technique |
Affected Assets |
Threat Actor |
NIST ID.RA Reference

""" + NIST_CSF2_CATEGORIES
    ),
    (
        "phase3_vulnerabilities.md",
        """
For the top 5 threats analyse vulnerabilities.

Reference the known weaknesses:

- Legacy MES
- Manual OTA signing
- No HSM
- No SBOM
- Missing MFA for contractors
- Weak OT/IT segmentation

Columns:

Vulnerability ID |
Description |
CVE/CWE |
CVSS |
Compensating Controls |
NIST Gap
"""
    ),
    (
        "phase4_risk_scoring.md",
        """
Create an ISO 27005 risk assessment.

For all threats provide:

Risk ID |
Threat |
Likelihood |
Impact |
Inherent Risk |
Existing Controls |
Residual Risk |
Owner |
Risk Class

Then create a residual-risk heat map.
"""
    ),
    (
        "phase5_controls.md",
        """
For the top risks map remediation controls.

Columns:

Control |
NIST CSF Reference |
Priority |
Effort |
Regulatory Benefit

Include:

- 5 Quick Wins (< 2 weeks)
- Regulatory Exposure Summary
- UNECE R155/R156 mapping
- NIS2 mapping
- GDPR mapping
"""
    ),
    (
        "phase6_roadmap.md",
        """
Create:

1. 12-month remediation roadmap

For each initiative provide:
- Timeline
- Risks addressed
- NIST controls
- Estimated cost
- FTE
- KPI

2. Executive Summary (max 250 words)

Board-focused:
- Top 3 risks
- Regulatory exposure
- Cost of inaction
- Investment request
"""
    ),
]


if __name__ == "__main__":
    context = ""

    for filename, prompt in PHASES:

        print(f"Running {filename}...")

        output = ask_ai(prompt, context)

        (OUTPUT_DIR / filename).write_text(
            output,
            encoding="utf-8"
        )

        context += f"\n\n# {filename}\n{output}\n"

    print("Assessment completed.")