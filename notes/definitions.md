---
title: Definitions and Abbreviations
created: 2026-03-12
source:
visibility: public
semantic_cluster: meta
tags: [definitions, abbreviations, reference]
---

# Definitions and Abbreviations

Central glossary for terms, concepts, and abbreviations used across the
knowledge base.

## Format

Each entry follows this structure:

```markdown
### TERM (Abbreviation if applicable)

Definition in your own words.

- Category: #concept, #tool, #mathematics, etc.
- Related: [[Related Note 1]], [[Related Note 2]]
- Source: Where you encountered this term
```

## Core Concepts

### Zettelkasten

A note-taking and knowledge management system developed by Niklas Luhmann based
on atomic notes, unique identifiers, and heavy cross-referencing to create a
"web of thought" that enables emergent insight.

- Category: #methodology #note-taking
- Related: [[Knowledge Organization]], [[Obsidian]], [[Roam Research]]
- Source: https://en.wikipedia.org/wiki/Zettelkasten

### Semantic Clustering

Grouping information by meaning and conceptual similarity rather than arbitrary
categories or folder hierarchies.

- Category: #organization #navigation
- Related: [[Semantic Navigation]], [[Knowledge Organization]]
- Source: https://haskellforall.com/2026/02/browse-code-by-meaning

## Power Systems

### LMP (Locational Marginal Price)

The cost of supplying the next megawatt of load at a specific location,
considering generation marginal cost, transmission congestion, and marginal
losses.

- Category: #power-systems #economics
- Related: [[Energy System Reliability]],
  [[Attribute-Preserving Optimal Network Reductions]]
- Source: Litvinov et al., 2008

### REI (Radial Equivalent Independent)

A network reduction method that aggregates multiple buses into a single
equivalent bus while preserving the radial structure of the network.

- Category: #power-systems #network-reduction
- Related: [[Attribute-Preserving Optimal Network Reductions]]
- Source: Ward Reduction paper

### PTDF (Power Transfer Distribution Factor)

A linear sensitivity factor indicating how much power flows through each
transmission line when 1 MW is transferred between two buses.

- Category: #power-systems #mathematics
- Related: [[Attribute-Preserving Optimal Network Reductions]]
- Source: Power Systems Analysis textbooks

### HSM (Holomorphic Series Method)

A mathematical technique using power series expansions and Padé approximants to
solve nonlinear equations, particularly useful for voltage stability analysis.

- Category: #mathematics #power-systems #voltage-stability
- Related: [[Attribute-Preserving Optimal Network Reductions]]
- Source: Dan Tylavsky, CERTS R&M Cornell, 2015

## Tools and Systems

### Wiki-Link

Internal link syntax `[[Note Title]]` used to create explicit connections
between notes in a knowledge base.

- Category: #tools #notation
- Related: [[Zettelkasten]], [[Obsidian]], [[Roam Research]]
- Source: Common in modern note-taking tools

### Frontmatter

YAML metadata block at the beginning of a markdown file containing structured
information like title, date, tags, and visibility settings.

- Category: #tools #markdown
- Related: [[Knowledge Base Structure]]
- Source: Jekyll, Obsidian, and other markdown-based systems

## Backlinks

- [[Knowledge Base Structure]]
- [[Knowledge Organization]]
