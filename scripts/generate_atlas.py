#!/usr/bin/env python3
"""Generate semantic atlas files from notes with visibility filtering."""

from __future__ import annotations

import argparse
import re
from collections import defaultdict
from pathlib import Path
from typing import Any

import yaml


VALID_VISIBILITY_FILTERS = {"all", "public", "private"}
NOTE_VISIBILITIES = {"public", "private"}


def split_frontmatter(content: str) -> tuple[dict[str, Any], str]:
    """Return parsed YAML frontmatter and markdown body."""
    if not content.startswith("---\n"):
        return {}, content

    parts = content.split("---", 2)
    if len(parts) != 3:
        return {}, content

    _, frontmatter_text, body = parts
    frontmatter = yaml.safe_load(frontmatter_text) or {}
    if not isinstance(frontmatter, dict):
        raise ValueError("Frontmatter must be a mapping")
    return frontmatter, body.lstrip("\n")


def parse_note(path: Path) -> dict[str, Any]:
    """Parse note metadata and extracted content from a markdown note."""
    content = path.read_text()
    frontmatter, body = split_frontmatter(content)

    wiki_links = re.findall(r"\[\[([^\]]+)\]\]", body)
    normalized_links = [link.split("|", 1)[0] for link in wiki_links]
    body_tags = re.findall(r"#([\w-]+)", body)

    tags = frontmatter.get("tags", []) or []
    if not isinstance(tags, list):
        raise ValueError(f"tags must be a list in {path}")

    visibility = str(frontmatter.get("visibility", "public")).strip().lower()
    if visibility not in NOTE_VISIBILITIES:
        raise ValueError(f"Unsupported visibility '{visibility}' in {path}")

    return {
        "path": path,
        "title": str(frontmatter.get("title", path.stem)),
        "visibility": visibility,
        "cluster": str(frontmatter.get("semantic_cluster", "uncategorized")),
        "source": str(frontmatter.get("source", "") or ""),
        "tags": [str(tag) for tag in tags] + body_tags,
        "created": str(frontmatter.get("created", "") or ""),
        "links": normalized_links,
        "content": body,
    }


def collect_note_paths(repo_root: Path) -> list[Path]:
    """Return all notes in the canonical notes directory."""
    notes_dir = repo_root / "notes"
    if not notes_dir.exists():
        return []
    return sorted(notes_dir.glob("*.md"))


def filter_notes(notes: list[dict[str, Any]], visibility_filter: str) -> list[dict[str, Any]]:
    """Filter notes by visibility."""
    if visibility_filter not in VALID_VISIBILITY_FILTERS:
        raise ValueError(f"Unsupported visibility filter: {visibility_filter}")
    if visibility_filter == "all":
        return notes
    return [note for note in notes if note["visibility"] == visibility_filter]


def cluster_by_semantics(notes: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    """Cluster notes by semantic similarity using cluster metadata and tags."""
    clusters: defaultdict[str, list[dict[str, Any]]] = defaultdict(list)

    for note in notes:
        cluster_name = note["cluster"]
        if cluster_name == "concepts" and note["tags"]:
            cluster_name = note["tags"][0]
        clusters[cluster_name].append(note)

    return dict(clusters)


def find_subclusters(
    notes: list[dict[str, Any]], max_per_cluster: int = 7
) -> list[tuple[str, list[dict[str, Any]]]]:
    """Find semantic subclusters within a cluster."""
    if len(notes) <= max_per_cluster:
        return [("all", notes)]

    tag_groups: defaultdict[str, list[dict[str, Any]]] = defaultdict(list)
    for note in notes:
        first_tag = note["tags"][0] if note["tags"] else "misc"
        tag_groups[first_tag].append(note)

    sorted_groups = sorted(tag_groups.items(), key=lambda item: len(item[1]), reverse=True)
    result: list[tuple[str, list[dict[str, Any]]]] = []
    misc_notes: list[dict[str, Any]] = []

    for tag, group_notes in sorted_groups:
        if len(group_notes) >= 2:
            result.append((tag, group_notes))
        else:
            misc_notes.extend(group_notes)

    if misc_notes:
        result.append(("other", misc_notes))

    return result


def format_atlas(clusters: dict[str, list[dict[str, Any]]]) -> str:
    """Generate atlas markdown content from clustered notes."""
    lines = [
        "# Atlas",
        "",
        "Semantic map of the knowledge base. Browse by meaning, not by folder.",
        "",
        "---",
        "",
    ]

    def wiki_link(note: dict[str, Any]) -> str:
        return f"[[{note['title']}|{note['path'].stem}]]"

    sorted_clusters = sorted(clusters.items(), key=lambda item: len(item[1]), reverse=True)

    for cluster_name, notes in sorted_clusters:
        display_name = cluster_name.replace("-", " ").replace("_", " ").title()

        lines.append(f"## {display_name}")
        lines.append(f"{len(notes)} notes")
        lines.append("")

        subclusters = find_subclusters(notes)
        if len(subclusters) == 1 and subclusters[0][0] == "all":
            for note in sorted(notes, key=lambda item: item["title"]):
                lines.append(f"- {wiki_link(note)}")
                if note["source"]:
                    lines.append(f"  Source: {note['source']}")
        else:
            for sub_name, sub_notes in subclusters:
                sub_display = sub_name.replace("-", " ").title()
                lines.append(f"### {sub_display}")
                lines.append(f"{len(sub_notes)} notes")
                lines.append("")
                for note in sorted(sub_notes, key=lambda item: item["title"]):
                    lines.append(f"- {wiki_link(note)}")
                lines.append("")

        lines.append("")

    lines.extend(["---", "", "## Navigation", "", "### Recent Notes"])

    all_notes = [note for notes in clusters.values() for note in notes]
    recent = sorted(all_notes, key=lambda item: item.get("created", ""), reverse=True)[:10]
    for note in recent:
        created = note.get("created", "unknown")[:10]
        lines.append(f"- {wiki_link(note)} - {created}")

    lines.extend(["", "### Orphaned Notes (no links)"])
    orphans = [note for note in all_notes if not note["links"]]
    if orphans:
        for note in orphans[:10]:
            lines.append(f"- {wiki_link(note)}")
    else:
        lines.append("All notes are connected.")

    return "\n".join(lines) + "\n"


def generate_atlas(
    repo_root: Path,
    *,
    visibility_filter: str = "all",
    output_path: Path | None = None,
) -> Path:
    """Generate an atlas file for the selected note visibility."""
    note_paths = collect_note_paths(repo_root)
    notes = [parse_note(note_path) for note_path in note_paths]
    visible_notes = filter_notes(notes, visibility_filter)
    clusters = cluster_by_semantics(visible_notes)
    atlas_content = format_atlas(clusters)

    target_path = output_path or (repo_root / "atlas.md")
    target_path.write_text(atlas_content)
    return target_path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate atlas from notes")
    parser.add_argument(
        "--visibility",
        choices=sorted(VALID_VISIBILITY_FILTERS),
        default="all",
        help="Which note visibility to include in the atlas",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Where to write the atlas (defaults to repo_root/atlas.md)",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    repo_root = Path(__file__).resolve().parent.parent
    atlas_path = generate_atlas(
        repo_root,
        visibility_filter=args.visibility,
        output_path=args.output,
    )
    print(f"Generated: {atlas_path}")


if __name__ == "__main__":
    main()
