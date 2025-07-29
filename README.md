# Protektiq

Protektiq is an ambitious AppSec pipeline orchestrator designed to unify and automate application security scanning across your entire software development lifecycle. The goal is to provide a single, extensible CLI tool that:

- Runs multiple security scanners (SAST, secrets, SCA, IaC, DAST, etc.)
- Correlates and deduplicates findings from all tools
- Summarizes risk using AI (LLMs)
- Generates actionable, developer-friendly reports (text, CSV, SARIF, Mermaid diagrams, etc.)
- Integrates easily into CI/CD pipelines

## Vision
Protektiq aims to become the "orchestrator" for all your AppSec needs, making it easy to:
- Plug in new scanners with minimal effort
- Get a unified, deduplicated view of all security findings
- Understand risk at a glance with AI-powered summaries
- Automate reporting and compliance

## Current Status (Prototype)
- Runs Semgrep (SAST) and TruffleHog (secrets) scanners
- CLI interface for running a pipeline scan on a target directory
- Prints findings from both scanners to the console

## Installation
1. Clone this repo
2. Install Python dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Install Semgrep and TruffleHog (Go version):
   ```
   pip install semgrep
   # Download and install TruffleHog Go binary from https://github.com/trufflesecurity/trufflehog/releases
   # Make sure 'trufflehog' is in your PATH
   ```

## Usage (Current Prototype)
To run the pipeline on a folder (e.g., a test app):
```
python -m cli.main --target-path <folder>
```
Example:
```
python -m cli.main --target-path vulnerable_app/
```

You will see findings from Semgrep and TruffleHog printed to the console.

## Roadmap
- Add more scanner integrations (SCA, IaC, DAST, etc.)
- Implement finding correlation and deduplication
- Add AI-powered risk summarization
- Generate reports in multiple formats
- Add CI/CD integration examples

## Credits
- [TruffleHog](https://github.com/trufflesecurity/trufflehog)
- [Semgrep](https://semgrep.dev/)

## License
[AGPL-3.0](LICENSE)
