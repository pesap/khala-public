# Knowledge Base

A pure-markdown knowledge base inspired by
[Gabriel Gonzalez's semantic navigator](https://haskellforall.com/2026/02/browse-code-by-meaning)
but built entirely in markdown.

This repo is the public mirror of the canonical `khala` knowledge base. It only
contains notes that were marked safe to publish.

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

## Public Mirror Model

- all tracked notes in this repo should use `visibility: public`
- private notes never appear here
- `atlas.md` is generated from the public subset only
- the canonical private repo is responsible for exporting updates here

## Quick Start

```bash
# Install dependencies
uv sync

# Add a public note
uv run python scripts/add_note.py "My New Concept" --visibility public

# Add a public note with metadata
uv run python scripts/add_note.py "Rust Ownership" \
  --source "https://doc.rust-lang.org/book/" \
  --tags "rust,programming,memory" \
  --visibility public

# Regenerate semantic atlas
uv run python scripts/generate_atlas.py --visibility public

# Browse by opening atlas.md
```

## Note Format

Every note uses YAML frontmatter + markdown content:

```markdown
---
title: Concept Name
created: 2026-03-11
source: https://example.com/article
visibility: public
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

## Publishing Flow

This repository is usually updated by exporting from the canonical private repo.
If you edit notes here directly, keep everything public-safe and regenerate the
atlas before committing.

## Usage Patterns

### Daily Workflow

```bash
# Capture a new idea
uv run python scripts/add_note.py "Idea about distributed systems" \
  --visibility public

# Later, refine and link
# Edit notes/knowledge-base-structure.md

# Regenerate atlas
uv run python scripts/generate_atlas.py --visibility public
```

### Adding Sources

```bash
# From a book
uv run python scripts/add_note.py "Thinking Fast and Slow" \
  --source "Kahneman, 2011" \
  --visibility public

# From an article
uv run python scripts/add_note.py "Semantic Navigator" \
  --source "https://haskellforall.com/2026/02/browse-code-by-meaning" \
  --visibility public
```

### Browsing

1. Open `atlas.md` - your semantic map
2. Jump to clusters by meaning
3. Follow wiki-links to explore
4. Check "Orphaned Notes" for unlinked ideas

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
