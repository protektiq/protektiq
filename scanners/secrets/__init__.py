import subprocess
import json
from scanners.finding_schema import Finding

class TruffleHogScanner:
    def __init__(self):
        self.name = "trufflehog"

    def run(self, target_path):
        result = subprocess.run([
            "trufflehog", "filesystem", "--json", target_path
        ], capture_output=True, text=True)
        findings = []
        try:
            for line in result.stdout.splitlines():
                try:
                    data = json.loads(line)
                    # TruffleHog JSON lines contain a 'SourceMetadata' and 'Raw' fields
                    file_path = data.get("SourceMetadata", {}).get("Data", {}).get("Filesystem", {}).get("file", "")
                    line_number = data.get("SourceMetadata", {}).get("Data", {}).get("Filesystem", {}).get("line")
                    rule_id = data.get("DetectorName", "")
                    title = data.get("Raw", "")[:80]  # Truncate for title
                    description = data.get("DetectorType", "")
                    severity = "HIGH"  # TruffleHog doesn't provide severity, default to HIGH
                    findings.append(Finding(
                        scanner=self.name,
                        file_path=file_path,
                        line=line_number,
                        severity=severity,
                        rule_id=rule_id,
                        title=title,
                        description=description,
                        recommendation=None,
                        raw_finding=data
                    ))
                except Exception as e:
                    print(f"[TruffleHogScanner] Error parsing finding: {e}")
        except Exception as e:
            print(f"[TruffleHogScanner] Error parsing output: {e}")
        return findings 