from scanners.sast.semgrep_scanner import SemgrepScanner
from scanners.secrets import TruffleHogScanner

class Orchestrator:
    def run_pipeline(self, target_path="."):
        print("[Protektiq] Orchestrator running pipeline...")
        semgrep = SemgrepScanner()
        semgrep_findings = semgrep.run(target_path)
        print(f"[Protektiq] Semgrep findings ({len(semgrep_findings)}):")
        for finding in semgrep_findings:
            print(f"- {finding.severity} | {finding.file_path}:{finding.line} | {finding.title}")

        trufflehog = TruffleHogScanner()
        secrets_findings = trufflehog.run(target_path)
        print(f"[Protektiq] Secrets findings ({len(secrets_findings)}):")
        for finding in secrets_findings:
            print(f"- {finding.severity} | {finding.file_path}:{finding.line} | {finding.title}") 