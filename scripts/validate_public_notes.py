#!/usr/bin/env python3
"""Validate that public notes do not leak private note references."""

from __future__ import annotations

import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from generate_atlas import collect_note_paths, parse_note  # noqa: E402


def find_collisions(values_a: set[str], values_b: set[str]) -> list[str]:
    """Return sorted values that appear in both sets."""
    return sorted(values_a & values_b)


def validate_public_notes(repo_root: Path) -> None:
    """Raise ValueError if public notes expose private note information."""
    notes = [parse_note(note_path) for note_path in collect_note_paths(repo_root)]
    public_notes = [note for note in notes if note["visibility"] == "public"]
    private_notes = [note for note in notes if note["visibility"] == "private"]

    public_titles = {note["title"] for note in public_notes}
    private_titles = {note["title"] for note in private_notes}
    title_collisions = find_collisions(public_titles, private_titles)
    if title_collisions:
        raise ValueError(f"Title collision between public and private notes: {title_collisions}")

    public_slugs = {note["path"].stem for note in public_notes}
    private_slugs = {note["path"].stem for note in private_notes}
    slug_collisions = find_collisions(public_slugs, private_slugs)
    if slug_collisions:
        raise ValueError(f"Slug collision between public and private notes: {slug_collisions}")

    for note in public_notes:
        leaked_links = sorted(link for link in note["links"] if link in private_titles)
        if leaked_links:
            raise ValueError(
                f"Public note '{note['title']}' links to private notes: {leaked_links}"
            )


def main() -> None:
    repo_root = Path(__file__).resolve().parent.parent
    try:
        validate_public_notes(repo_root)
    except ValueError as error:
        print(error)
        raise SystemExit(1) from error
    print("Public note visibility validated")


if __name__ == "__main__":
    main()
