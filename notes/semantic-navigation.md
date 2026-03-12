---
title: Semantic Navigation
created: 2026-03-11T10:00:00
source: https://haskellforall.com/2026/02/browse-code-by-meaning
visibility: public
semantic_cluster: concepts
tags: [navigation, meaning, organization, ai]
---

# Semantic Navigation

Browsing code (and knowledge) by meaning rather than by directory structure.
Gabriel Gonzalez's approach uses embeddings to cluster files semantically.

## Key Ideas

- Embeddings: convert content to vectors
- Clustering: group similar vectors (spectral clustering)
- Labeling: generate distinctive labels for clusters
- Tree View: present as browsable hierarchy

## Why This Matters

Traditional folder structures are arbitrary. They reflect the creator's mental
model at a point in time, not the semantic relationships between ideas.

[[Knowledge Organization]] shows alternative approaches.

## Implementation

The semantic navigator uses:

1. Vector embeddings (e.g., OpenAI embeddings)
2. Spectral clustering (tuning-free)
3. LLM-based cluster labeling (with "homework" prompting)
4. Pattern detection (common file prefixes/suffixes)

## Backlinks

- [[Knowledge Base Structure]]
- [[Semantic Clustering]]
