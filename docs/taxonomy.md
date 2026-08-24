# Taxonomy

## Design Principles

The taxonomy separates four concepts that are often conflated:

1. **Security task**: what security outcome is being pursued.
2. **Target domain**: what artifact or system is being analyzed.
3. **AI paradigm**: what kind of AI method performs the work.
4. **Evaluation setting**: how capability is measured.

Every paper has exactly one canonical `primary` path. For method, system, benchmark, and dataset papers, that path is a security task. A survey, SoK, or perspective that genuinely spans several tasks may use the narrow `overview` exception below. Papers may have multiple controlled tags in all other dimensions. This prevents duplicate catalog records while allowing a paper to appear once in a specialized README section, such as `Benchmark Papers`, and once in its canonical security-task section without creating a second YAML record.

Editor can use AI agents to help with selecting labels.

## Cross-task Overviews

Use these primary paths only when assigning one security task would misrepresent the paper:

- `overview/survey`
- `overview/sok`
- `overview/perspective`

A survey of a single task, such as ML-based intrusion detection, should remain under that task and use `paper_type: survey`.

## Primary Security Tasks

### `vulnerability-analysis`

Finding, locating, understanding, reproducing, or prioritizing software vulnerabilities.

Controlled subcategories:

- `vulnerability-detection`
- `vulnerability-localization`
- `vulnerability-classification`
- `severity-and-prioritization`
- `static-analysis`
- `dynamic-analysis`
- `fuzzing`
- `test-generation`
- `root-cause-analysis`
- `vulnerability-reproduction`
- `poc-generation`

Boundary: a PoC demonstrates that a vulnerability can be triggered. Work whose primary goal is to convert a trigger into concrete security impact belongs under exploitation.

### `program-understanding`

Recovering security-relevant semantics from programs, binaries, bytecode, or protocol implementations.

Controlled subcategories:

- `code-representation`
- `binary-representation`
- `decompilation`
- `function-identification`
- `algorithm-identification`
- `function-naming`
- `code-summarization`
- `type-recovery`
- `binary-similarity`
- `software-provenance`
- `protocol-reverse-engineering`
- `malware-reverse-engineering`

Boundary: recovering general program semantics belongs here, while work whose central object is a cryptographic construction, attack, proof, or implementation belongs under `cryptography`.

### `cryptography`

Using AI to reason about cryptographic constructions, discover or reproduce cryptanalytic attacks, guide mathematical or symbolic solvers, assess designs, or recover cryptographic semantics from implementations.

Controlled subcategories:

- `cryptographic-capability-evaluation`
- `cryptographic-reasoning`
- `cryptanalysis`
- `neural-cryptanalysis`
- `solver-guided-cryptanalysis`
- `cryptographic-design-analysis`
- `cryptographic-implementation-analysis`
- `cryptographic-reverse-engineering`
- `side-channel-analysis`

Boundary: generic binary similarity, decompilation, and malware reverse engineering remain under `program-understanding`. Breaking or analyzing deployed cryptographic libraries may also enable exploitation, but the canonical path is `cryptography` when the main contribution concerns the cryptographic primitive, security game, proof, or cryptographic semantics rather than system compromise.

### `exploitation`

Turning a weakness into security impact or executing an offensive workflow.

Controlled subcategories:

- `exploit-generation`
- `exploit-adaptation`
- `exploit-chaining`
- `automated-penetration-testing`
- `ctf-solving`
- `web-exploitation`
- `service-exploitation`
- `privilege-escalation`
- `lateral-movement`
- `post-exploitation`
- `attack-planning`

### `remediation`

Repairing vulnerabilities or improving software-development security.

Controlled subcategories:

- `patch-generation`
- `patch-validation`
- `program-repair`
- `secure-code-generation`
- `security-code-review`
- `dependency-security`
- `supply-chain-security`
- `fix-prioritization`
- `security-specification`

### `malware-analysis`

Detecting, classifying, understanding, or attributing malicious and unwanted software.

Controlled subcategories:

- `malware-detection`
- `malware-classification`
- `family-attribution`
- `behavior-analysis`
- `sandbox-analysis`
- `malicious-document-detection`
- `ransomware-analysis`
- `mobile-malware`
- `malware-report-generation`

Malware reverse engineering may use `program-understanding` as its primary path when semantic recovery is the principal research contribution.

### `infrastructure-defense`

Detecting or analyzing malicious behavior in networks, hosts, cloud systems, and operational telemetry.

Controlled subcategories:

- `intrusion-detection`
- `network-anomaly-detection`
- `traffic-classification`
- `log-analysis`
- `host-based-detection`
- `cloud-security`
- `container-security`
- `iot-security`
- `cyber-physical-security`
- `authentication-anomaly`
- `ddos-detection`
- `botnet-detection`
- `ai-agent-defense`
- `cyber-deception`
- `honeypot-and-honeytoken`
- `moving-target-defense`

### `social-identity-abuse`

Analyzing attacks that primarily target people, identities, accounts, or online trust systems.

Controlled subcategories:

- `phishing-detection`
- `phishing-generation`
- `malicious-url-detection`
- `email-security`
- `social-engineering`
- `credential-abuse`
- `account-takeover`
- `fraud-detection`
- `online-abuse`
- `human-ai-security-interaction`

### `security-operations`

Supporting threat intelligence, security operations centers, threat hunting, investigation, and incident response.

Controlled subcategories:

- `threat-intelligence-extraction`
- `entity-relation-extraction`
- `attack-technique-mapping`
- `security-knowledge-graph`
- `alert-triage`
- `alert-correlation`
- `detection-rule-generation`
- `threat-hunting`
- `incident-investigation`
- `digital-forensics`
- `security-report-generation`

## Target Domains

The `domains` field accepts one or more of:

- `source-code`
- `repository`
- `binary`
- `bytecode`
- `firmware`
- `web`
- `network`
- `host`
- `cloud`
- `container`
- `mobile`
- `iot`
- `cyber-physical-system`
- `email`
- `identity`
- `blockchain`
- `smart-contract`
- `cryptography`
- `security-telemetry`
- `threat-intelligence`

New domains should be added only when at least several papers need the tag or when the domain implies a materially different evaluation setting.

## AI Paradigms

The `ai_paradigms` field accepts:

- `classical-ml`
- `deep-learning`
- `computer-vision`
- `representation-learning`
- `graph-learning`
- `reinforcement-learning`
- `language-model`
- `llm`
- `multimodal-model`
- `agent`
- `multi-agent`
- `neuro-symbolic`
- `retrieval-augmented`
- `structured-prediction`
- `unsupervised-learning`
- `semi-supervised-learning`
- `streaming-learning`
- `nlp`

`agent` indicates an iterative system that observes an environment, takes actions or invokes tools, and uses feedback. A one-shot LLM classifier or code generator should not receive the tag merely because the paper calls it an agent.

## Security Role

Use exactly one:

- `defensive`
- `offensive`
- `dual-use`

`dual-use` is preferred when the evaluated capability directly supports both authorized defense and realistic attack enablement. The label describes the capability, not the authors' intent.

## Adversary Model

The optional `adversary_models` field describes who or what executes the attack in defensive research. It accepts one or more of:

- `human`
- `automated-tool`
- `ai-assisted-human`
- `autonomous-ai-agent`
- `multi-agent-attacker`
- `mixed-or-unspecified`

Use `autonomous-ai-agent` when an AI system independently observes the environment, selects actions, invokes tools, and adapts based on feedback. Use `ai-assisted-human` when a human operator remains responsible for attack planning or action selection. This field describes the threat actor and is independent of `ai_paradigms`, which describes the AI technology studied by the paper.

## Evaluation Setting

Use one or more:

- `static`
- `dynamic`
- `human-graded`
- `model-graded`
- `unit-tested`
- `execution-grounded`
- `simulation`
- `ctf-style`
- `cyber-range`
- `synthetic`
- `curated-real-data`
- `real-world`
- `repository-scale`
- `live-system`
- `human-baseline`
- `adaptive-adversary`
- `contamination-controlled`
- `temporal`

Definitions:

- `execution-grounded`: success is checked by executing an artifact or action, rather than only comparing text.
- `real-world`: targets, vulnerabilities, or telemetry originate from deployed or historically deployed systems.
- `repository-scale`: the method must operate across a non-trivial software repository rather than an isolated function.
- `live-system`: evaluation interacts with an operational system. This tag requires a clear authorization and containment statement.

## Publication Status

Use exactly one:

- `peer-reviewed`
- `accepted`
- `preprint`
- `technical-report`

An accepted or peer-reviewed paper should record its archival venue. Do not label a paper by the venue to which it was merely submitted.

## Paper Type

Use exactly one:

- `method`
- `system`
- `benchmark`
- `dataset`
- `empirical-study`
- `survey`
- `sok`
- `perspective`

Choose the paper's main research contribution. For example, a paper that introduces a benchmark and evaluates several models is normally `benchmark`, not `empirical-study`.

## Artifact Types

Artifacts are recorded independently:

- `code`
- `dataset`
- `benchmark`
- `evaluation-harness`
- `reproducible-environment`
- `leaderboard`
- `model`
- `traces`

Availability should be verified from an official project or author-controlled repository and dated with `last_verified`.

## Example Placements

| Paper | Canonical primary path | Important tags |
| --- | --- | --- |
| CyberGym | `vulnerability-analysis/vulnerability-reproduction` | `llm`, `agent`, `source-code`, `real-world`, `execution-grounded` |
| ExploitGym | `exploitation/exploit-generation` | `llm`, `agent`, `binary`, `dual-use`, `real-world`, `execution-grounded` |
| CREBench | `cryptography/cryptographic-reverse-engineering` | `llm`, `binary`, `cryptography`, `ctf-style`, `execution-grounded` |
| AICrypto | `cryptography/cryptographic-capability-evaluation` | `llm`, `agent`, `cryptography`, `ctf-style`, `human-baseline` |
| CryptanalysisBench | `cryptography/cryptanalysis` | `llm`, `agent`, `cryptography`, `execution-grounded`, `adaptive-adversary` |
| Cloak, Honey, Trap | `infrastructure-defense/ai-agent-defense` | `llm`, `agent`, `defensive`, `autonomous-ai-agent`, `cyber-deception`, `execution-grounded` |
