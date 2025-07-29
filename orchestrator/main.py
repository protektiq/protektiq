from scanners.sast.semgrep_scanner import SemgrepScanner

class Orchestrator:
    def run_pipeline(self, target_path="."):
        print("[Protektiq] Orchestrator running pipeline...")
        semgrep = SemgrepScanner()
        findings = semgrep.run(target_path)
        print(f"[Protektiq] Semgrep findings ({len(findings)}):")
        for finding in findings:
            print(f"- {finding.severity} | {finding.file_path}:{finding.line} | {finding.title}") 