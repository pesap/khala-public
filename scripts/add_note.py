#!/usr/bin/env python3
"""Add a new note to the knowledge base with visibility metadata."""

from __future__ import annotations

import argparse
import re
from datetime import datetime
from pathlib import Path


VALID_VISIBILITIES = {"public", "private"}
CLUSTER_KEYWORDS = {
    "programming": ["code", "python", "rust", "javascript", "algorithm", "function"],
    "architecture": ["system", "design", "pattern", "structure", "component"],
    "learning": ["book", "article", "course", "paper", "study"],
    "philosophy": ["theory", "concept", "idea", "philosophy", "thought"],
    "project": ["project", "app", "tool", "library", "framework"],
    "people": ["person", "author", "developer", "team", "company"],
}


def slugify(title: str) -> str:
    """Convert title to a URL-safe slug."""
    slug = re.sub(r"[^\w\s-]", "", title.lower())
    slug = re.sub(r"[-\s]+", "-", slug)
    return slug.strip("-")


def get_cluster_suggestion(title: str, tags: list[str]) -> str:
    """Suggest a semantic cluster based on title and tags."""
    text = f"{title} {' '.join(tags)}".lower()
    for cluster, keywords in CLUSTER_KEYWORDS.items():
        if any(keyword in text for keyword in keywords):
            return cluster
    return "concepts"


def parse_tags(tags_argument: str | None) -> list[str]:
    """Convert comma-separated CLI tag input into a list."""
    if not tags_argument:
        return []
    return [tag.strip() for tag in tags_argument.split(",")]


def render_template(
    template: str,
    *,
    title: str,
    created: str,
    source: str,
    visibility: str,
    cluster: str,
    tags: list[str],
) -> str:
    """Render the note template using stable placeholder tokens."""
    return (
        template.replace("%TITLE%", title)
        .replace("%CREATED%", created)
        .replace("%SOURCE%", source)
        .replace("%VISIBILITY%", visibility)
        .replace("%CLUSTER%", cluster)
        .replace("%TAGS%", str(tags))
        .replace("%CONTENT%", "")
    )


def create_note(
    repo_root: Path,
    title: str,
    *,
    source: str = "",
    tags: list[str] | None = None,
    visibility: str = "private",
) -> Path:
    """Create a new note in the canonical notes directory."""
    if visibility not in VALID_VISIBILITIES:
        raise ValueError(f"Unsupported visibility: {visibility}")

    notes_dir = repo_root / "notes"
    template_path = repo_root / "templates" / "note.md"

    slug = slugify(title)
    note_path = notes_dir / f"{slug}.md"
    if note_path.exists():
        raise FileExistsError(f"Note already exists: {note_path}")

    resolved_tags = tags or []
    cluster = get_cluster_suggestion(title, resolved_tags)
    template = template_path.read_text()
    content = render_template(
        template,
        title=title,
        created=datetime.now().isoformat(),
        source=source,
        visibility=visibility,
        cluster=cluster,
        tags=resolved_tags,
    )

    note_path.write_text(content)
    print(f"Created: {note_path}")
    print(f"Suggested cluster: {cluster}")
    print(f"Visibility: {visibility}")
    return note_path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Add a new note to the KB")
    parser.add_argument("title", help="Note title")
    parser.add_argument("--source", "-s", help="Source URL")
    parser.add_argument("--tags", "-t", help="Comma-separated tags")
    parser.add_argument(
        "--visibility",
        choices=sorted(VALID_VISIBILITIES),
        default="private",
        help="Whether the note should be exported publicly",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()
    repo_root = Path(__file__).resolve().parent.parent
    tags = parse_tags(args.tags)
    create_note(
        repo_root,
        args.title,
        source=args.source or "",
        tags=tags,
        visibility=args.visibility,
    )


if __name__ == "__main__":
    main()
