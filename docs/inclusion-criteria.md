# Inclusion Criteria

## Editorial Goal

The list should answer a researcher's question: **Which papers are worth reading to understand the development, current capabilities, and open problems of AI for cybersecurity?** It is not intended to mirror every search result.

## Mandatory Gates

A candidate must pass every gate:

1. **Scope fit**: AI is substantive and the main research question is a concrete cybersecurity task defined in [Scope](scope.md).
2. **Readable research record**: a public paper or archival technical report is available.
3. **Identifiable contribution**: the entry can state what the work contributes and why that contribution matters in one or two precise sentences.
4. **Traceable metadata**: title, authors, year, publication status, and an official paper link can be verified.
5. **Responsible listing**: inclusion does not require mirroring weaponized payloads, leaked answers, private data, credentials, or instructions for unauthorized access.

Venue acceptance is not a mandatory gate. Strong preprints are eligible as `emerging`, especially in fast-moving areas such as autonomous cyber agents, but their status must be explicit.

## Quality Signals

Editors consider the following signals together:

### Research contribution

- Introduces an important task, method, benchmark, dataset, or system
- Provides a meaningful conceptual or empirical advance
- Clarifies a confused area through a survey, SoK, or careful negative result

### Evaluation quality

- Uses realistic inputs and threat models
- Compares against appropriate baselines
- Measures security outcomes rather than only proxy metrics
- Uses execution-grounded evaluation where the task permits it
- Reports limitations, failure modes, cost, variance, or uncertainty
- Includes human or expert baselines when they materially improve interpretation

### Reproducibility

- Releases code, data, prompts, traces, or an evaluation harness
- Documents environment versions and evaluation conditions
- Separates private evaluation material from public benchmark interfaces
- Makes benchmark contamination and answer leakage assessable

### Scholarly and community influence

- Appears at a respected security, software engineering, systems, AI, ML, NLP, or data-mining venue
- Is cited or built upon by later research
- Is adopted as a benchmark or comparison point
- Attracts substantive technical discussion from researchers or practitioners

No single proxy decides inclusion. Conference prestige, citation counts, GitHub stars, and social-media attention can all be noisy.

## Reading Priority

### `essential`

Use when a paper meets at least one of these conditions and remains a strong reading recommendation after editorial review:

- Defines a widely used research problem or benchmark
- Introduces a foundational method or system
- Provides the clearest authoritative synthesis of an important area
- Changes how later work evaluates or understands a capability

### `recommended`

Use for a high-quality representative work that advances an established area, offers a particularly strong evaluation, or is important for understanding a major branch of the taxonomy.

### `emerging`

Use for recent work with strong novelty, realism, artifacts, or community interest whose lasting influence cannot yet be judged. `Emerging` is not a lower quality label and should be revisited after publication or follow-on work.

## Community Signals

Social-media attention is evidence of reach, not scientific correctness. A community signal may be recorded only with a stable URL and one of these types:

- `author-thread`
- `independent-technical-discussion`
- `conference-talk`
- `research-blog`
- `practitioner-adoption`
- `github-activity`

An entry should briefly state what the signal demonstrates. Raw impression or like counts should not be stored because they are unstable and easy to game.

## Venue Signals

Relevant venue families include, but are not limited to:

- Security and privacy: IEEE S&P, USENIX Security, ACM CCS, NDSS
- Cryptography: CRYPTO, EUROCRYPT, ASIACRYPT
- Software engineering and testing: ICSE, FSE, ASE, ISSTA
- Systems and networking: SOSP, OSDI, NSDI, ASPLOS
- AI and machine learning: NeurIPS, ICML, ICLR, AAAI, IJCAI
- NLP and data mining: ACL, EMNLP, NAACL, KDD, The Web Conference

This is not a whitelist. Venue workshops, domain conferences, journals, and preprints may contain essential work.

## Review Workflow

For each proposed paper:

1. Verify the official paper and publication status.
2. Read at least the abstract, introduction, method overview, evaluation, and limitations.
3. Assign one canonical security-task path and the relevant controlled tags.
4. Verify official artifacts and distinguish the paper snapshot from later releases.
5. Write `contribution`, `why_read`, and `limitations`.
6. Record the verification date and evidence for any community signal.
7. Check for duplicate preprint, conference, or journal versions.

## Frontier Lab Reports and Briefings

The supplementary frontier-lab section follows the narrower exception defined in [Scope](scope.md). Prefer the lab's incident disclosure, technical postmortem, threat-intelligence report, or an official conference recording over press coverage or commentary. Each entry must identify the issuing organization, exact date, stable primary-source link, type of material, and the concrete evidence or operational lesson it contributes. These entries do not receive reading-priority labels, controlled paper tags, or YAML records.

## README Presentation

- List every author when a paper has one to three authors; for four or more authors, list the first author followed by `et al.`.
- Preserve the complete verified author list in `data/papers.yaml`, regardless of the abbreviated README display.
- Format each README paper entry as five physical lines: title; authors and venue; links; description; and editorial label plus controlled tags.
- Keep each YAML prose value quoted on one physical line; multiline indentation is reserved for structural sequences and mappings.

## Updating and Removal

Entries may be updated, demoted, or removed when:

- A preprint is superseded by a peer-reviewed version
- Official artifacts move or substantially change
- A benchmark is found to have leakage, invalid labels, or an unreliable judge
- Claims cannot be reproduced or are formally retracted
- The work is later found to fall outside scope
- A stronger paper makes an entry redundant in a deliberately curated section
