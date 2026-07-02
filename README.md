# Velonix S.p.A. — AI-Assisted Cybersecurity Risk Assessment

> University project for course **Security and Risk: Management and Certifications**  

---

## Overview

This project implements a six-phase, AI-assisted cybersecurity risk assessment for **Velonix S.p.A.**, a fictional Italian automotive Tier 1 supplier. The assessment is produced by an agentic Python workflow that calls the **Ollama** command line tool with model **qwen2.5**, accumulating context across phases and saving each output as a structured markdown file.

The methodology combines four complementary frameworks:

| Role | Framework |
|------|-----------|
| Process structure | NIST CSF 2.0 |
| Risk scoring | ISO 27005 (5×5 matrix) |
| Threat intelligence | ENISA Threat Landscape 2025 |
| Technical attack detail | MITRE ATT&CK v14 |

Regulatory context (UNECE WP.29, ISO/SAE 21434, NIS2, GDPR, ISO 27001) is injected into Phases 5 and 6 only.

---

## Project Structure

```
velonix/
│
├── config.py               # Company profile, regulatory context — edit this first
├── enisa_threats.py        # ENISA ETL 2024 data, auto-injected into Phase 2
├── risk_assessment.py      # Main orchestrator — runs all 6 phases
├── assemble_report.py      # Stitches phase outputs into a single final report
├── review_report.py        # Evaluate the generated report using the AI
│
└── output/                 # Generated automatically on first run
    ├── phase1_assets.md
    ├── phase2_threats.md
    ├── phase3_vulnerabilities.md
    ├── phase4_risk_scoring.md
    ├── phase5_controls.md
    ├── phase6_roadmap.md
    ├── phase7_critical_review.md    # Report review, not included in the assembled document
    └── Velonix_Risk_Assessment.md   # Final assembled report
```

---

## Prerequisites

- Python 3.10 or later
- ollama

---

## Setup (one-time)

### 1. Install ollama

```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama --version          # verify installation
```


### 2. (Optional) Create a Python virtual environment

```bash
cd velonix/
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
```

---

## Running the Assessment

### Full run (all 6 phases, ~3–5 minutes)

```bash
source .venv/bin/activate
python risk_assessment.py
```

Phase outputs are saved incrementally to `output/` as each phase completes.


### Assembling the final report

After all six phases are complete:

```bash
python assemble_report.py
```

This produces `output/Velonix_Risk_Assessment.md` with the executive summary on page one, followed by all six phase sections in order.

---

## Configuration

All company-specific inputs live in `config.py`. This is the **only file you need to edit** to adapt the workflow to a different organisation.

| Variable | Purpose | Used in phases |
|----------|---------|----------------|
| `COMPANY_SECTOR` | Controls ENISA sector profile selection | 2 |
| `COMPANY_CONTEXT` | Full company description and known weaknesses | 1–6 |
| `ASSETS` | Concrete asset list for the inventory | 1 |
| `REGULATORY_CONTEXT` | Applicable regulations with article numbers | 5, 6 |

`enisa_threats.py` is not intended to be edited unless you change sector or wish to update the threat data to a newer ETL edition.

---

## The Six Phases

| Phase | Goal | NIST CSF Ref | Output file |
|-------|------|-------------|-------------|
| 1 — Asset Inventory | ≥15 assets, crown jewels flagged | ID.AM | `phase1_assets.md` |
| 2 — Threat Identification | Top 8 threats, ENISA + ATT&CK dual map | ID.RA | `phase2_threats.md` |
| 3 — Vulnerability Analysis | CVE/CWE, CVSS, NIST gaps per threat | ID.RA-05 | `phase3_vulnerabilities.md` |
| 4 — Risk Scoring | Inherent and residual scores, heat map | ID.RA | `phase4_risk_scoring.md` |
| 5 — Control Mapping | NIST controls, priority, regulatory refs | PR | `phase5_controls.md` |
| 6 — Roadmap | 12-month plan + board executive summary | GV | `phase6_roadmap.md` |

---

## How the Agentic Loop Works

qwen has no memory between calls. The workflow implements a **chain-of-context** pattern: each phase appends its output to a shared `context` string, which is prepended to every subsequent AI call. This means Phase 6 has full visibility of everything produced in Phases 1–5.

```
context = ""
Phase 1 → output → context += Phase 1 output
Phase 2 → (context + ENISA data) → output → context += Phase 2 output
Phase 3 → context → output → context += Phase 3 output
...
```

ENISA threat data is injected into Phase 2 only, via `get_threat_summary_for_prompt()` from `enisa_threats.py`. Regulatory context is injected into Phases 5 and 6 only, from `REGULATORY_CONTEXT` in `config.py`.

---

## Privacy Considerations

This workflow allows to preserve privacy since ollama models run locally. Moreover fictional company data is used, so no privacy concerns apply.


---

## Important Limitations

- **AI output must be reviewed by a human expert.** Every phase output is a starting point for analyst review, not a finished deliverable. The analyst is responsible under NIS2 Art. 20 for the accuracy of the final report.
- **Scores are AI-generated estimates.** Likelihood and impact values in Phase 4 reflect AI model reasoning given the inputs provided. They should be validated against internal incident history and expert judgment.
- **ENISA data in `enisa_threats.py` was manually curated.** The accuracy of Phase 2 depends entirely on the fidelity of this file to the source report. Always cross-check against the original ENISA ETL 2024 PDF available at [enisa.europa.eu](https://www.enisa.europa.eu).
- **Context window limits.** For very large organisations with extensive asset inventories, the accumulated context string may approach token limits in later phases. Mitigate by summarising earlier phase outputs before injecting them.

---

## Dependencies

```
# No external Python packages required beyond the standard library.
# The only runtime dependency is the ollama
```

---

## License

This project is produced for educational purposes as part of a university assignment. The company Velonix S.p.A. is entirely fictional. No real company data is represented.
