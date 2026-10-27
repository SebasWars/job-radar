import json
import re
import html
from job_radar.models import Job

from datetime import datetime
from pathlib import Path

SAMPLE_PATH = Path("data/sample.json")


def _strip_html(raw_html: str):
    text = re.sub(r"<[^>]+>", " ", raw_html)
    gfg = html.escape(text)
    return " ".join(gfg.split())


def parse_job(raw: dict) -> Job:
    return Job(
        source="remotive",
        external_id=str(raw["id"]),
        title=raw["title"],
        company=raw["company_name"].strip(),
        url=raw["url"],
        category=raw["category"],
        job_type=raw["job_type"],
        location=raw["candidate_required_location"],
        published_at=datetime.fromisoformat(raw["publication_date"]),
        salary=raw.get("salary" or "").strip() or None,
        tags=[tag.strip().lower() for tag in raw.get("tags", [])],
        description=_strip_html(raw["description"]),
    )


if __name__ == "__main__":
    data = json.loads(SAMPLE_PATH.read_text(encoding="utf-8"))
    jobs = [parse_job(raw) for raw in data["jobs"]]
    print(f"{len(jobs)} ofertas")
    for job in jobs:
        print(f"- {job.title} | {job.company} | {job.salary} | {job.tags[:3]}")
