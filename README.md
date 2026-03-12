# Knowledge Base

A pure-markdown knowledge base inspired by
[Gabriel Gonzalez's semantic navigator](https://haskellforall.com/2026/02/browse-code-by-meaning)
but built entirely in markdown.

This repo is the canonical private knowledge base. Notes can be marked `public`
or `private`, and public notes can be exported into a separate `khala-public`
repository.

## Philosophy

- **Browse by meaning**, not by arbitrary folder structure
- **Pure markdown** - no proprietary formats or required tools
- **Wiki-links** for explicit connections: `[[Concept Name]]`
- **Auto-generated atlas** - semantic map that updates as you add notes
- **Portable** - works in any text editor, viewer, or git

## Structure

```
kb/
├── notes/          # All notes in flat structure (filename = slug)
├── atlas.md        # Auto-generated semantic map (start here!)
├── templates/      # Note templates
├── scripts/        # Note creation, atlas generation, public export
└── README.md       # This file
```

## Visibility Model

- `visibility: private` means the note stays only in this repo
- `visibility: public` means the note can be exported to `khala-public`
- `atlas.md` in this repo includes all notes
- Public export fails if a public note links to a private note title

## Quick Start

```bash
# Install dependencies
uv sync

# Add a new private note (default)
uv run python scripts/add_note.py "My New Concept"

# Add a public note with metadata
uv run python scripts/add_note.py "Rust Ownership" \
  --source "https://doc.rust-lang.org/book/" \
  --tags "rust,programming,memory" \
  --visibility public

# Regenerate semantic atlas
uv run python scripts/generate_atlas.py

# Export only public notes to a sibling repo
uv run python scripts/export_public.py ../khala-public

# Browse by opening atlas.md
```

## Note Format

Every note uses YAML frontmatter + markdown content:

```markdown
---
title: Concept Name
created: 2026-03-11
source: https://example.com/article
visibility: private
semantic_cluster: programming
tags: [rust, memory]
---

# Concept Name

Content here with [[Other Concept]] links.

## Backlinks

- [[Incoming Link 1]]
```

## How It Works

The atlas is your entry point. It shows:

1. **Semantic Clusters**: Notes grouped by meaning (not folders)
2. **Subclusters**: Large clusters subdivided automatically
3. **Recent Notes**: Last 10 additions
4. **Orphaned Notes**: Unlinked notes needing connections

### Clustering Strategy

Unlike Gabriel's tool (which uses embeddings), this KB uses a hybrid approach:

1. **Manual hints**: Set `semantic_cluster` in frontmatter
2. **Tag-based**: First tag refines cluster category
3. **Keyword matching**: Auto-suggest clusters on note creation
4. **Future**: Add optional embedding-based clustering

## Public Export

Public export is an explicit step. It copies only `visibility: public` notes and
the supporting public-safe project files into another repo.

```bash
uv run python scripts/export_public.py ../khala-public
```

Before exporting, the validator checks that:

- no public note links to a private note with `[[Wiki Links]]`
- no public and private notes share the same title
- no public and private notes share the same slug

## Usage Patterns

### Daily Workflow

```bash
# Capture a new idea
uv run python scripts/add_note.py "Idea about distributed systems"

# Later, refine and link
# Edit notes/knowledge-base-structure.md

# Regenerate atlas
uv run python scripts/generate_atlas.py

# Export public notes when ready
uv run python scripts/export_public.py ../khala-public
```

### Adding Sources

```bash
# From a book
uv run python scripts/add_note.py "Thinking Fast and Slow" \
  --source "Kahneman, 2011"

# From an article
uv run python scripts/add_note.py "Semantic Navigator" \
  --source "https://haskellforall.com/2026/02/browse-code-by-meaning"
```

### Browsing

1. Open `atlas.md` - your semantic map
2. Jump to clusters by meaning
3. Follow wiki-links to explore
4. Check "Orphaned Notes" for unlinked ideas
5. Export public notes into `khala-public` when you want to publish them

## Future Enhancements

Optional features you can add:

- **Embeddings**: Store vector in frontmatter for perfect clustering
- **Graph visualization**: Export to Cytoscape/D3
- **Search**: Add full-text indexing
- **Validation**: Check for broken wiki-links
- **Backlink auto-generation**: Parse all files to fill Backlinks sections

## Comparison

| Feature           | Obsidian | Roam      | This KB     |
| ----------------- | -------- | --------- | ----------- |
| Local files       | ✅       | ❌        | ✅          |
| Pure markdown     | ⚠️       | ❌        | ✅          |
| Wiki-links        | ✅       | ✅        | ✅          |
| Semantic browsing | ❌       | ⚠️        | ✅          |
| Graph view        | ✅       | ✅        | (via atlas) |
| Cost              | Free/$   | Expensive | Free        |
| Lock-in           | Medium   | High      | None        |

## License

Your knowledge is yours. No proprietary formats, no lock-in.
