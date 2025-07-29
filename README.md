## Protektiq: Open-Source AppSec Pipeline Orchestrator

Protektiq is a wrapper-based Application Security (AppSec) pipeline orchestrator that unifies open-source scanners (SCA, SAST, Secrets, IaC, IAST, DAST) into a single continuous workflow for any CI/CD pipeline. It builds the app, runs security tests in sequence, deduplicates findings, performs attack-path correlation, and summarizes business risk using LLMs. The output is a digestible risk brief for both executives and developers.

### Core Components
- **Orchestrator:** Manages the pipeline and coordinates scanner execution.
- **Scanner Wrappers:** Adapters for each tool (SAST, SCA, Secrets, IaC, IAST, DAST, Build).
- **Correlation Engine:** Deduplicates and correlates findings (DefectDojo + custom logic).
- **AI Summary Engine:** Uses LangChain + GPT-4 to generate risk briefs.
- **Reporting:** Generates Mermaid diagrams, PDFs, SARIF, and CSV reports.
- **CLI:** User-friendly command-line interface for running the pipeline.

### Usage

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the pipeline:**
   ```bash
   python cli/main.py pipeline --target-path vulnerable_app/
   ```
   Or scan any directory or file:
   ```bash
   python cli/main.py pipeline --target-path /path/to/your/code
   ```

### Directory Structure

```
protektiq/
  orchestrator/         # Pipeline logic
  scanners/             # Wrappers for each tool
    sast/
    sca/
    secrets/
    iac/
    iast/
    dast/
    build/
  correlation/          # Deduplication, attack-path logic
  ai_summary/           # LLM risk summarization
  reporting/            # Reporting outputs
  cli/                  # CLI entrypoint
  config/               # Config files
  tests/                # Tests
  requirements.txt
  README.md
```

### Roadmap
- Add scanner wrappers for each tool
- Implement deduplication and correlation
- Integrate AI risk summarization
- Expand reporting formats
- CI/CD integration examples
