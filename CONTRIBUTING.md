# Contributing

Thank you for helping improve Awesome AI for Cybersecurity Papers. Contributions may propose a paper, correct metadata, improve an annotation, update an artifact link, or refine the taxonomy.

## Before You Submit

Please read the project [scope](docs/scope.md), [taxonomy](docs/taxonomy.md), and [inclusion criteria](docs/inclusion-criteria.md), then search both [README.md](README.md) and [data/papers.yaml](data/papers.yaml) for the title, arXiv identifier, DOI, and earlier versions of the work.

A paper must make a substantive AI contribution to a concrete cybersecurity task. AI Security papers, traditional security papers without a substantive AI component, product announcements, and repositories without an associated research paper are outside scope.

## Ways to Contribute

- Use the paper-suggestion issue form for a candidate that still needs editorial review or metadata work.
- Open a pull request when you can provide a complete YAML record and the corresponding README entry.
- Open a regular issue for taxonomy discussions, repository-wide corrections, or questions that do not concern one paper.

## Information Required for a Paper Proposal

- Exact title and complete ordered author list.
- Publication year, venue, and status: `peer-reviewed`, `accepted`, `preprint`, or `technical-report`.
- Official paper page, DOI, proceedings page, or arXiv URL.
- One precise sentence describing the paper's contribution in your own words.
- A short explanation of why the paper is worth reading and its most important limitation.
- One canonical security-task path plus relevant controlled tags from the taxonomy.
- Official code, dataset, project, benchmark, leaderboard, or evaluation-harness links, when available.
- Stable evidence for any claimed community influence; raw view, like, or star counts are not sufficient.

## Frontier Lab Report Proposals

Use a regular issue to propose an official incident disclosure, technical postmortem, threat-intelligence report, or major conference briefing for `Frontier Lab Reports and Briefings`. Provide the exact title, issuing organization, publication date, primary-source URL, material type, and one sentence stating its concrete evidence or operational lesson. These supplementary entries update only the README and must satisfy the exception defined in the project [scope](docs/scope.md).

## Pull Request Format

The machine-readable record in [data/papers.yaml](data/papers.yaml) is canonical. Add exactly one YAML record per paper and preserve the complete verified author list there.

Add the paper to its canonical task section in [README.md](README.md). Benchmark and dataset papers may also appear once in `Benchmark Papers`; a directly relevant defense paper may also appear once in `Defending Against AI-Enabled Cyber Attacks`.

README entries must use exactly five physical lines:

```markdown
- **Paper Title**  
  First Author et al. *Venue Year*.  
  [Paper](https://example.org/paper) · [Code](https://example.org/code)  
  One-sentence description of the contribution.  
  **Priority · Type** · `controlled-tag` `controlled-tag`
```

List every author in the README when a paper has one to three authors. For four or more authors, display the first author followed by `et al.`. Keep YAML prose values quoted on one physical line, order entries from newest to oldest, and sort titles alphabetically within the same year.

## Local Validation

Install PyYAML and run the catalog validator before opening a pull request:

```bash
python -m pip install PyYAML==6.0.2
python scripts/validate.py
```

The same check runs automatically for pull requests and pushes to `main`.
