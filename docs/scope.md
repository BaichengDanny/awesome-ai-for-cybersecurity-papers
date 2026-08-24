# Scope

## Mission

Awesome AI for Cybersecurity Papers is a curated research map for work that uses artificial intelligence to understand, assess, attack, or defend computer systems. It aims to help researchers identify foundational papers, strong representative methods, realistic benchmarks, and important emerging work.

The list prioritizes intellectual structure and reading value over exhaustive coverage.

## In Scope

A work is in scope when all of the following hold:

1. AI is a substantive part of the method, system, or object of capability evaluation. This includes classical machine learning, deep learning, graph learning, reinforcement learning, large language models, and autonomous agents.
2. The primary research question concerns a concrete cybersecurity task.
3. A public research paper or archival technical report describes the work in enough detail to evaluate its contribution.

Representative topics include:

- Vulnerability discovery, localization, explanation, reproduction, and prioritization
- Fuzzing, test generation, exploit generation, and penetration testing
- Program understanding, binary analysis, and reverse engineering
- Cryptographic reasoning, cryptanalysis, solver guidance, and cryptographic implementation analysis
- Security patch generation and validation
- Malware, phishing, fraud, and malicious infrastructure analysis
- Intrusion detection, telemetry analysis, threat hunting, and incident response
- Threat intelligence extraction and security knowledge representation
- Autonomous agents evaluated on cybersecurity tasks
- Detection, deception, containment, and response techniques for AI-enabled or autonomous cyber attackers
- Benchmarks, datasets, cyber ranges, and execution environments for the above tasks

Defending conventional software, networks, or infrastructure against an attacker that uses an AI model or autonomous agent is explicitly in scope. The protected object is the cyber system, not the attacker's AI model.

## Dual-use Research

Offensive and dual-use research is in scope because exploit generation, penetration testing, and adversarial evaluation are important scientific areas. Inclusion is descriptive, not an endorsement of deployment against systems without authorization.

The catalog may link to an authors' official paper, project, benchmark, and repository. It will not reproduce weaponized payloads, credentials, private answer keys, or targeting instructions. Where appropriate, entries should note access controls, containment requirements, and responsible-use restrictions.

## Unit of Inclusion

The primary unit of the canonical catalog is a research paper. A benchmark, dataset, code repository, leaderboard, blog post, or social-media thread is normally metadata attached to that paper rather than an independent paper entry.

The README contains one deliberately separate exception: `Frontier Lab Reports and Briefings`. An item may appear there without an academic paper only when it is an official primary source from a frontier AI lab, its security or threat-intelligence team, an incident partner, or the host of a major technical briefing, and it documents at least one of the following:

- A real-world AI-enabled cyber incident or technical postmortem
- Observed malicious use of frontier models or AI-enabled attack tradecraft
- Empirical evidence about frontier cyber capabilities
- Concrete containment, monitoring, access-control, or defensive deployment practices

Marketing-only announcements, unsupported capability claims, and third-party news summaries are excluded. Supplementary items are presented only in the README and do not receive records in `data/papers.yaml`.
