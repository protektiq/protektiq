import subprocess
import json
from scanners.finding_schema import Finding

class SemgrepScanner:
    def __init__(self):
        self.name = "semgrep"

    def run(self, target_path):
        result = subprocess.run([
            "semgrep", "--json", target_path
        ], capture_output=True, text=True)
        findings = []
        try:
            data = json.loads(result.stdout)
            for finding in data.get("results", []):
                findings.append(Finding(
                    scanner=self.name,
                    file_path=finding.get("path", ""),
                    line=finding.get("start", {}).get("line"),
                    severity=finding.get("extra", {}).get("severity", "UNKNOWN"),
                    rule_id=finding.get("check_id", ""),
                    title=finding.get("extra", {}).get("message", ""),
                    description=finding.get("extra", {}).get("metadata", {}).get("description", ""),
                    recommendation=finding.get("extra", {}).get("metadata", {}).get("recommendation"),
                    raw_finding=finding
                ))
        except Exception as e:
            print(f"[SemgrepScanner] Error parsing output: {e}")
        return findings 