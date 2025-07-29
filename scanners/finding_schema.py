from dataclasses import dataclass
from typing import Optional

@dataclass
class Finding:
    scanner: str
    file_path: str
    line: Optional[int]
    severity: str
    rule_id: str
    title: str
    description: str
    recommendation: Optional[str] = None
    raw_finding: Optional[dict] = None 