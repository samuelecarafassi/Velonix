from pathlib import Path
import json
import urllib.request

from config import (
    COMPANY_CONTEXT,
    REGULATORY_CONTEXT,
)

OUTPUT_DIR = Path("output")


SYSTEM_PROMPT = """
You are a senior cybersecurity auditor reviewing an AI-generated
cybersecurity risk assessment.

You must act as an independent reviewer.

Your task is NOT to rewrite or improve the assessment.

Your task is to identify:

- inaccuracies
- unsupported assumptions
- hallucinations
- weak risk scoring logic
- missing threats
- missing controls
- regulatory mistakes
- weak NIST mappings
- weak ISO 27005 scoring rationale

Be skeptical.

Where evidence is missing, explicitly state it.

Output markdown.
"""


def ask_ai(prompt: str,model_name = "qwen2.5-coder:7b") -> str:

    # Configure a clean HTTP API request to the local Ollama instance
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": model_name,
        "prompt": prompt,
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


def load_assessment():

    files = [
        "phase1_assets.md",
        "phase2_threats.md",
        "phase3_vulnerabilities.md",
        "phase4_risk_scoring.md",
        "phase5_controls.md",
        "phase6_roadmap.md",
    ]

    content = []

    for file in files:

        path = OUTPUT_DIR / file

        if not path.exists():
            raise FileNotFoundError(path)

        content.append(
            f"\n\n# {file}\n\n"
            + path.read_text(encoding="utf-8")
        )

    return "\n".join(content)


def build_review_prompt(assessment_text):

    return f"""
{SYSTEM_PROMPT}

# Company Context

{COMPANY_CONTEXT}

# Regulatory Context

{REGULATORY_CONTEXT}

# Assessment To Review

{assessment_text}

# Task

Perform a critical review of this AI-generated cybersecurity
assessment.

Use the following structure.

# Executive Review

Provide a short overall assessment.

# Weaknesses

List weaknesses and explain why they matter.

# Hallucination Risk

Identify statements that may not be supported by evidence.

For each item provide:

| Finding | Reason | Confidence |

Confidence:
Low / Medium / High

# Accuracy Assessment

Evaluate:

- Asset inventory accuracy
- Threat identification accuracy
- Vulnerability analysis accuracy
- Risk scoring accuracy
- Control mapping accuracy
- Regulatory alignment accuracy

Score each from 0-100.

# Missing Risks

Identify important threats that appear absent.

Consider:

- Supply chain attacks
- Vehicle safety risks
- OTA infrastructure compromise
- CI/CD compromise
- Insider threats
- Cloud attacks
- Ransomware

# Human Validation Recommendations

Describe what a security engineer should manually verify.

# Mitigations Against AI Errors

Provide practical controls:

- Independent review
- Threat intelligence validation
- SME sign-off
- Evidence requirements
- Cross-framework validation

# Final Verdict

Provide:

Overall Confidence Score (0-100)

and

Whether the assessment is suitable for:
- Internal planning
- Compliance preparation
- Executive reporting
- External audit

Explain why.
"""


def main():

    print("Loading assessment...")

    assessment = load_assessment()

    print("Generating critical review...")

    review = ask_ai(
        build_review_prompt(assessment)
    )

    output_file = OUTPUT_DIR / "phase7_critical_review.md"

    output_file.write_text(
        review,
        encoding="utf-8"
    )

    print(f"Saved: {output_file}")


if __name__ == "__main__":
    main()