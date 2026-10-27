from dataclasses import dataclass, field
from datetime import datetime

@dataclass(frozen=True)
class Job:
    source: str
    external_id: str
    title: str
    company: str
    url: str
    category: str
    job_type: str
    location: str
    published_at : datetime
    description : str
    salary: str | None = None
    tags: list[str] = field(default_factory=list)
