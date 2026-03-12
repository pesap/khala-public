# Agent Guidelines for Knowledge Base

How to work with this semantic knowledge base.

## Adding Notes

### Use the script

```bash
python scripts/add_note.py "Note Title" \
  --source "URL or book citation" \
  --tags "comma,separated,tags"
```

### Manual creation (if script unavailable)

1. Create file in `notes/` with slugified name: `concept-name.md`
2. Use the template from `templates/note.md`
3. Required frontmatter: `title`, `created`, `visibility`, `semantic_cluster`,
   `tags`
4. Include `source` if applicable

### Visibility

- `visibility: private` stays only in this canonical repo
- `visibility: public` is eligible for export to the public mirror
- New notes should default to private unless there is a reason to publish them

## Semantic Organization

### Choosing a Cluster

Set `semantic_cluster` based on the note's primary nature:

- **concepts** - Ideas, theories, patterns, mental models
- **tools** - Software, frameworks, libraries, apps
- **people** - Individuals, companies, teams
- **sources** - Books, papers, articles, courses
- **projects** - Active work, repositories, initiatives
- **meta** - System documentation, templates, KB structure
- **uncategorized** - Temporary holding (move to proper cluster)

### Tagging Strategy

- First tag should refine the cluster (e.g., `semantic_cluster: concepts`, first
  tag: `programming`)
- Use lowercase, hyphenated tags: `machine-learning`, not `Machine Learning`
- 2-4 tags per note typically
- Tags can appear in body as `#tag` or only in frontmatter

## Linking

### Wiki-Links

- Use `[[Note Title]]` to reference other notes
- Must match the `title` field in target note's frontmatter
- Place context-relevant links in body content
- Update "Backlinks" section manually or regenerate via script

### When to Link

- Connect related concepts (bidirectional if possible)
- Link to prerequisite knowledge
- Link to contrasting/alternative approaches
- Link to tools that implement a concept
- Link to sources that inspired the note

### Broken Links

- The atlas generation will show orphaned notes
- If linking to a non-existent note, create it or remove the link

## Content Style

### Atomic Notes

- One primary concept per note
- Can be long if deep on one topic
- Split when covering multiple distinct ideas

### Structure

```markdown
# Title

Intro/context paragraph

## Key Ideas / Main Content

Body with [[links]] embedded naturally

## Related

- [[Note 1]]
- [[Note 2]]

## Backlinks

- [[Incoming 1]]
- [[Incoming 2]]
```

### Writing Tips

- Start with context: what is this and why does it matter?
- Include sources when applicable
- Write for your future self (what would you want to know?)
- Use code blocks for technical examples

## Maintenance

### After Adding Notes

Always regenerate the atlas:

```bash
uv run python scripts/generate_atlas.py
```

If you changed any public note, validate and export the public mirror as needed:

```bash
uv run python scripts/validate_public_notes.py
uv run python scripts/export_public.py ../khala-public
```

### Periodic Tasks

- Review orphaned notes section in atlas - connect them
- Check for notes with `semantic_cluster: uncategorized` - categorize them
- Look for clusters with >20 notes - they may need subcategorization
- Update backlinks sections (manual until automated)

## File Naming

- Slugify titles: lowercase, hyphens for spaces
- Example: "Rust Ownership Model" → `rust-ownership-model.md`
- Consistent naming helps wiki-links work reliably

## Metadata Standards

### Date Format

ISO 8601: `2026-03-11` or `2026-03-11T14:30:00`

### Source Field

- URLs: Full URL including https://
- Books: "Author, Title (Year)" or "Title by Author"
- Papers: "Title (Year) - Journal/Conference"
- Leave blank if original thought

### Visibility Field

- Use `private` by default for work-related or unpublished notes
- Use `public` only for notes safe to publish in `khala-public`
- Public notes must not link to private note titles
- Public and private notes must not reuse the same title or slug

### Cluster Evolution

It's okay to change `semantic_cluster` as your understanding evolves. The atlas
will reflect changes on next generation.

## Anti-Patterns

- Don't create folder hierarchies - flat structure in `notes/`
- Don't duplicate content across notes - link instead
- Don't leave notes orphaned - always try to connect to existing network
- Don't over-tag - too many tags dilute meaning
- Don't worry about perfect organization - the atlas helps you navigate
- Don't reference private note titles from public notes
- Don't publish by hand, always use the export script

## Quick Reference

| Task                  | Command                                                  |
| --------------------- | -------------------------------------------------------- |
| Add note              | `uv run python scripts/add_note.py "Title" --tags "a,b"` |
| Regenerate atlas      | `uv run python scripts/generate_atlas.py`                |
| Validate public notes | `uv run python scripts/validate_public_notes.py`         |
| Export public repo    | `uv run python scripts/export_public.py ../khala-public` |
| Browse                | Open `atlas.md`                                          |
| Find orphans          | Check atlas "Orphaned Notes" section                     |

Remember: **The goal is a web of connected ideas, not a rigid hierarchy.**

## Markdown Style

- No ASCII art for equations or symbols. Use LaTeX math notation: inline with
  `$...$`, block with `$$...$$` or fenced with ` ```math ` blocks
- No bold text (`**...**`). If emphasis is needed, make it a proper section
  heading or define it as a term
- No em dashes; use commas, parentheses, or periods instead

## Git Commits

- Use [Conventional Commits](https://www.conventionalcommits.org/):
  `type(scope): description`
- Common types: `feat`, `fix`, `docs`, `chore`, `refactor`
- No co-author lines in commit messages
