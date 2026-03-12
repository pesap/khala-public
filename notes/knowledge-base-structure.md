---
title: Knowledge Base Structure
created: 2026-03-11T06:00:00
source:
visibility: public
semantic_cluster: meta
tags: [system, design, structure]
---

# Knowledge Base Structure

Designing a pure-markdown knowledge base with semantic organization.

## Goals

1. Pure Markdown: no proprietary formats or required tools
2. Semantic Organization: browse by meaning, not folders
3. Wiki Links: standard `[[Note Name]]` syntax
4. Auto-Generated Atlas: like semantic navigator but in markdown
5. Portable: works in any text editor or viewer

## Structure

```
kb/
├── notes/          # Flat directory of all notes
├── atlas.md        # Generated semantic map (entry point)
├── templates/      # Note templates
└── scripts/        # Generation tools
```

## The Atlas

The `atlas.md` is the entry point. It:

- Clusters notes by semantic similarity
- Shows hierarchical tree view
- Lists recent additions
- Shows orphaned notes (unlinked)

## Clustering Approach

Since we're using pure markdown without a database:

- Store cluster hints in YAML frontmatter
- Use tags and keywords for initial grouping
- Generate the atlas by clustering at build time
- Manual refinement of clusters over time

## Comparison to Semantic Navigator

Gabriel Gonzalez's tool uses embeddings for perfect semantic clustering. Our
pure-markdown approach:

- Uses metadata and tags (heuristic clustering)
- Could use embeddings stored in frontmatter
- Generates static atlas file
- No runtime dependencies to browse

## Backlinks

- [[Semantic Navigation]] ([Semantic Navigation](semantic-navigation.md))
- [[Knowledge Organization]]
  ([Knowledge Organization](knowledge-organization.md))
