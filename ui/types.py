from dataclasses import dataclass
from datetime import datetime


@dataclass
class LogEntry:
    timestamp: datetime
    level: str
    source: str
    message: str


@dataclass
class AlarmEntry:
    key: str
    timestamp: datetime
    level: str
    message: str
    active: bool = True
    acknowledged: bool = False
