# Awesome AI for Cybersecurity Papers

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Validate catalog](https://github.com/BaichengDanny/awesome-ai-for-cybersecurity-papers/actions/workflows/validate.yml/badge.svg)](https://github.com/BaichengDanny/awesome-ai-for-cybersecurity-papers/actions/workflows/validate.yml)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-orange.svg)](CONTRIBUTING.md)

> A curated, taxonomy-driven reading list on using AI to understand, assess, attack, and defend cyber systems.

This list covers **AI for cybersecurity** research in which machine learning, large language models, or autonomous agents perform or support a cybersecurity task.

## Contents

Use this index to navigate the reading guide, benchmark section, and task taxonomy.

- [Start Here](#start-here)
- [Frontier Lab Reports and Briefings](#frontier-lab-reports-and-briefings)
- [Research Map](#research-map)
- [Surveys, SoKs, and Perspectives](#surveys-soks-and-perspectives)
- [Benchmark Papers](#benchmark-papers)
- [Papers by Security Task](#papers-by-security-task)
  - [Vulnerability Discovery and Analysis](#vulnerability-discovery-and-analysis)
  - [Program Understanding and Reverse Engineering](#program-understanding-and-reverse-engineering)
  - [AI for Cryptography and Cryptanalysis](#ai-for-cryptography-and-cryptanalysis)
  - [Exploitation and Offensive Security](#exploitation-and-offensive-security)
  - [Remediation and Secure Software Engineering](#remediation-and-secure-software-engineering)
  - [Malware and Unwanted Software](#malware-and-unwanted-software)
  - [Network, Host, and Infrastructure Defense](#network-host-and-infrastructure-defense)
  - [Social Engineering, Identity, and Abuse](#social-engineering-identity-and-abuse)
  - [Threat Intelligence, SOC, and Incident Response](#threat-intelligence-soc-and-incident-response)
- [Defending Against AI-Enabled Cyber Attacks](#defending-against-ai-enabled-cyber-attacks)
- [Curation Statement](#curation-statement)
- [Contributing](#contributing)
- [License and Citation](#license-and-citation)

## Start Here

Each paper has one canonical security-task path in the machine-readable catalog. A paper may also appear once in a specialized section, such as `Benchmark Papers` or `Defending Against AI-Enabled Cyber Attacks`, because these complement the task-oriented view. Properties such as `llm`, `agent`, `binary`, `offensive`, and `execution-grounded` are represented as tags.

README author names follow one display rule: papers with up to three authors list every author, while papers with four or more authors list the first author followed by `et al.`. The canonical YAML record always preserves the complete author list.

Each paper entry uses five lines in this order: title, authors and venue, links, description, and editorial label plus controlled tags. Within every paper section, entries are ordered by publication year from newest to oldest.

- Read the project boundaries in [Scope](docs/scope.md).
- Read category definitions and controlled tags in [Taxonomy](docs/taxonomy.md).
- Read the editorial rubric in [Inclusion Criteria](docs/inclusion-criteria.md).
- Use [data/papers.yaml](data/papers.yaml) as the canonical machine-readable catalog.

Reading priority is editorial, not a paper ranking:

- **Essential**: defines an important problem, method, system, or benchmark.
- **Recommended**: a strong representative work with lasting reference value.
- **Emerging**: recent and promising, but its long-term impact is not yet clear.

## Frontier Lab Reports and Briefings

This section tracks primary-source incident disclosures, threat-intelligence reports, and major public briefings from frontier AI labs and their security partners.

- **OpenAI – Hugging Face Incident Technical Report**  
  OpenAI. *August 26, 2026*.  
  [Technical Report](https://cdn.openai.com/pdf/67869394-cb91-4c12-888c-5cbd85c7814c/OpenAI-Hugging-Face%20Incident-Technical-Report.pdf) · [Overview](https://openai.com/index/hugging-face-incident-and-the-road-ahead/)  
  Reconstructs how evaluation agents escaped isolated environments, formed an unauthorized inter-agent communication network, chained zero-day vulnerabilities into OpenAI and Hugging Face infrastructure, and motivates stronger containment, monitoring, alignment, and incident response.  
  **Technical Incident Report**

- **Pacing model development in an era of cyber-critical capabilities**  
  OpenAI. *August 18, 2026*.  
  [Report](https://openai.com/index/pacing-model-development-cyber-capabilities/)  
  Describes the training pause, stronger workload and network isolation, expanded monitoring, and alignment measures adopted after the OpenAI–Hugging Face incident and evidence of critical cyber capability in an upcoming model.  
  **Safeguards Update**

- **The “Breaking” News: The OpenAI–Hugging Face Incident — A Technical Reconstruction and Its Implications for AI**  
  Michael Dalton and Eric Wallace, OpenAI. *Black Hat USA, August 5, 2026*.  
  [Black Hat Briefing](https://blackhat.com/us-26/briefings/schedule/index.html#the-breaking-news--the-openaihugging-face-incident---a-technical-reconstruction-and-its-implications-for-ai-57401) · [Video](https://www.youtube.com/watch?v=87DyyMV0kCY)  
  Reconstructs how model instances used a shared message board across evaluation runs, escaped constrained infrastructure, and carried out multi-stage intrusions involving OpenAI and Hugging Face systems.  
  **Conference Briefing**

- **Investigating three real-world incidents in our cybersecurity evaluations**  
  Anthropic. *July 30, 2026*.  
  [Incident Report](https://www.anthropic.com/news/investigating-incidents-cybersecurity-evals)  
  Reports three cases found across 141,006 reviewed evaluation runs in which Claude reached real systems through misconfigured evaluation infrastructure, including a malicious PyPI package that was executed on external systems.  
  **Incident Disclosure**

- **Anatomy of a Frontier Lab Agent Intrusion: A Technical Timeline of the July 2026 Incident**  
  Hugging Face. *July 27, 2026*.  
  [Technical Postmortem](https://huggingface.co/blog/agent-intrusion-technical-timeline)  
  Reconstructs approximately 17,600 agent actions across initial access, code execution, command and control, Kubernetes escalation, credential access, lateral movement, and attempted supply-chain compromise.  
  **Technical Postmortem**

- **OpenAI and Hugging Face partner to address security incident during model evaluation**  
  OpenAI. *July 21, 2026; updated July 29, 2026*.  
  [Incident Disclosure](https://openai.com/index/hugging-face-model-evaluation-security-incident/) · [Hugging Face Disclosure](https://huggingface.co/blog/security-incident-july-2026)  
  Provides the initial joint account of OpenAI models exploiting a previously unknown path out of a constrained evaluation environment and chaining vulnerabilities into Hugging Face production infrastructure.  
  **Incident Disclosure**

- **What we learned mapping a year’s worth of AI-enabled cyber threats**  
  Anthropic Frontier Red Team. *June 3, 2026*.  
  [Report](https://www.anthropic.com/news/AI-enabled-cyber-threats-mitre-attack) · [Interactive Analysis](https://www.anthropic.com/research/attack-navigator)  
  Maps 832 accounts banned for malicious cyber activity to MITRE ATT&CK and finds increasing use of AI in later attack stages, greater autonomy, and attacker behaviors not represented by existing ATT&CK techniques.  
  **Threat Intelligence Report**

- **Cybersecurity in the Intelligence Age**  
  OpenAI. *April 29, 2026*.  
  [Overview](https://openai.com/index/cybersecurity-in-the-intelligence-age/) · [Action Plan](https://cdn.openai.com/pdf/7ca95dce-4424-4b62-9eab-89233bb38f82/oai-cybersecurity-action-plan.pdf)  
  Proposes five pillars for AI-powered cyber defense: broader defensive access, government–industry coordination, protection of frontier capabilities, deployment visibility and control, and user enablement.  
  **Policy and Strategy**

- **Disrupting the first reported AI-orchestrated cyber espionage campaign**  
  Anthropic Threat Intelligence. *November 13, 2025*.  
  [Report](https://www.anthropic.com/news/disrupting-AI-espionage) · [Full Report](https://assets.anthropic.com/m/ec212e6566a0d47/original/Disrupting-the-first-reported-AI-orchestrated-cyber-espionage-campaign.pdf)  
  Documents a state-sponsored campaign that used Claude Code across reconnaissance, exploitation, credential harvesting, lateral movement, data analysis, and exfiltration with relatively limited human intervention.  
  **Threat Intelligence Report**

- **GTIG AI Threat Tracker: Advances in Threat Actor Usage of AI Tools**  
  Google Threat Intelligence Group. *November 5, 2025*.  
  [Report](https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools)  
  Reports movement from general productivity assistance toward AI-enabled malware, including experimental runtime code generation and observed use of AI throughout intrusion lifecycles.  
  **Threat Intelligence Report**

- **Detecting and countering misuse of AI: August 2025**  
  Anthropic Threat Intelligence. *August 27, 2025*.  
  [Report](https://www.anthropic.com/news/detecting-countering-misuse-aug-2025)  
  Presents cases involving Claude-assisted data theft and extortion, North Korean fraudulent employment, and ransomware development by an actor with limited technical expertise.  
  **Threat Intelligence Report**

- **Adversarial Misuse of Generative AI**  
  Google Threat Intelligence Group. *January 29, 2025*.  
  [Report](https://cloud.google.com/blog/topics/threat-intelligence/adversarial-misuse-generative-ai)  
  Analyzes how government-backed APT and information-operations actors used Gemini for research, reconnaissance, scripting, payload support, phishing, translation, and content generation.  
  **Threat Intelligence Report**

- **Disrupting malicious uses of AI by state-affiliated threat actors**  
  OpenAI and Microsoft Threat Intelligence. *February 14, 2024*.  
  [OpenAI Report](https://openai.com/index/disrupting-malicious-uses-of-ai-by-state-affiliated-threat-actors/) · [Microsoft Analysis](https://www.microsoft.com/en-us/security/blog/2024/02/14/staying-ahead-of-threat-actors-in-the-age-of-ai/)  
  Documents the disruption of five state-affiliated actors using LLMs for reconnaissance, translation, phishing content, scripting, debugging, and other incremental support to existing cyber operations.  
  **Threat Intelligence Report**

## Research Map

This map summarizes the canonical security tasks and dedicated reading views covered below.

| Section | Representative questions |
| --- | --- |
| Frontier lab reports and briefings | What are frontier labs and their security partners observing in real-world AI-enabled attacks, capability evaluations, incidents, and defensive deployments? |
| Surveys, SoKs, and perspectives | Which works synthesize evidence, systematize methods and limitations, or assess developments spanning multiple security tasks? |
| Benchmark papers | Which reusable tasks, datasets, environments, and evaluation protocols measure progress in AI for cybersecurity? |
| Vulnerability discovery and analysis | Can AI find, localize, explain, reproduce, or prioritize vulnerabilities? |
| Program understanding and reverse engineering | Can AI recover semantics from source, bytecode, binaries, or protocols? |
| AI for cryptography and cryptanalysis | Can AI reason about cryptographic constructions, discover attacks, guide cryptanalytic solvers, or recover cryptographic semantics from implementations? |
| Exploitation and offensive security | Can AI turn weaknesses into concrete impact or execute multi-step attacks? |
| Remediation and secure software engineering | Can AI generate, validate, or prioritize security fixes? |
| Malware and unwanted software | Can AI detect, classify, reverse engineer, or explain malicious software? |
| Network, host, and infrastructure defense | Can AI detect malicious behavior in traffic, hosts, cloud systems, or logs? |
| Social engineering, identity, and abuse | Can AI detect or analyze phishing, fraud, credential abuse, and manipulation? |
| Threat intelligence, SOC, and incident response | Can AI help analysts understand threats, triage alerts, hunt, and respond? |
| Defending against AI-enabled cyber attacks | How can conventional software, networks, and infrastructure detect, delay, deceive, or stop AI-powered attackers and autonomous attack agents? |

## Surveys, SoKs, and Perspectives

This section is reserved for work that synthesizes multiple primary security tasks. A survey focused on one task remains in that task's canonical section.

- **SoK: The Pitfalls of Deep Reinforcement Learning for Cybersecurity**  
  Shae McFadden et al. *USENIX Security 2026*.  
  [Paper](https://www.usenix.org/conference/usenixsecurity26/presentation/mcfadden)  
  Systematizes eleven recurring methodological pitfalls across 66 deep-reinforcement-learning-for-cybersecurity papers and demonstrates their effects in autonomous defense, malware creation, and web testing environments.  
  **Emerging · SoK** · `reinforcement-learning` `network-anomaly-detection` `malware-detection` `web-exploitation` `dual-use` `execution-grounded`

- **Frontier AI's Impact on the Cybersecurity Landscape**  
  Yujin Potter et al. *arXiv 2025*.  
  [Paper](https://arxiv.org/abs/2504.05408) · [Project](https://rdi.berkeley.edu/frontier-ai-impact-on-cybersecurity/)  
  Combines benchmark evidence, literature synthesis, empirical agent evaluation, and an expert survey to assess how frontier AI is changing cyber offense and defense.  
  **Recommended · SoK** · `llm` `agent` `dual-use` `ai-agent-defense` `exploit-generation` `patch-generation` `curated-real-data`

- **SoK: Automated TTP Extraction from CTI Reports – Are We There Yet?**  
  Marvin Büchel et al. *USENIX Security 2025*.  
  [Paper](https://www.usenix.org/conference/usenixsecurity25/presentation/buechel)  
  Unifies and reevaluates more than forty NLP-based approaches to extracting ATT&CK tactics, techniques, and procedures from threat reports, exposing dataset, ontology, and comparability problems.  
  **Essential · SoK** · `language-model` `llm` `threat-intelligence` `attack-technique-mapping` `real-world`

## Benchmark Papers

This section collects benchmark and dataset papers that define reusable tasks, environments, corpora, or evaluation protocols for AI for cybersecurity research.

- **AICrypto: Evaluating Cryptography Capabilities of Large Language Models**  
  Yu Wang et al. *ICML 2026*.  
  [Paper](https://icml.cc/virtual/2026/poster/63082) · [arXiv](https://arxiv.org/abs/2507.09580) · [Code](https://github.com/wangyu-ovo/aicrypto-agent) · [Dataset](https://huggingface.co/datasets/yuuwwang/aicrypto) · [Project](https://aicryptobench.github.io/)  
  Evaluates cryptographic knowledge, practical vulnerability exploitation, and proof reasoning with 135 multiple-choice questions, 150 CTF challenges, and 30 proof problems reviewed or constructed by cryptography experts.  
  **Emerging · Benchmark** · `llm` `agent` `cryptographic-reasoning` `cryptanalysis` `cryptography` `ctf-style` `human-baseline`

- **AutoBaxBuilder: Bootstrapping Code Security Benchmarking**  
  Tobias von Arx et al. *ICML 2026*.  
  [Paper](https://icml.cc/virtual/2026/poster/64856)  
  Automates the construction of code-security tasks with functional tests and executable exploits while reducing dependence on reusable, contamination-prone benchmark instances.  
  **Emerging · Benchmark** · `llm` `agent` `secure-code-generation` `vulnerability-detection` `execution-grounded` `contamination-controlled`

- **CrackMeBench: Binary Reverse Engineering for Agents**  
  Ilia David and Arthur Gervais. *arXiv 2026*.  
  [Paper](https://arxiv.org/abs/2605.10597)  
  Evaluates tool-using agents on clean-room binary reverse-engineering challenges with deterministic grading.  
  **Emerging · Benchmark** · `llm` `agent` `malware-reverse-engineering` `decompilation` `binary` `dual-use` `execution-grounded` `contamination-controlled`

- **CREBench: Evaluating Large Language Models in Cryptographic Binary Reverse Engineering**  
  Baicheng Chen et al. *COLM 2026*.  
  [Paper](https://arxiv.org/abs/2604.03750) · [Code](https://github.com/wangyu-ovo/CREBench) · [Dataset](https://huggingface.co/datasets/Danny-1223/CREBench) · [Project](https://jams-zhou-james.github.io/CREBench/)  
  Evaluates LLMs across four levels of cryptographic binary reverse engineering, from algorithm identification to flag recovery.  
  **Emerging · Benchmark** · `llm` `binary` `cryptographic-reverse-engineering` `cryptography` `ctf-style` `execution-grounded`

- **CryptanalysisBench: Can LLMs do Cryptanalysis?**  
  Lukas Fluri et al. *arXiv 2026*.  
  [Paper](https://arxiv.org/abs/2607.18538) · [Code](https://github.com/ethz-spylab/cryptanalysis-benchmark) · [Project](https://cryptanalysis-bench.com/)  
  Evaluates agents on 191 real cryptographic schemes across six primitive families using formal security games and fresh-randomness verification of submitted attack programs.  
  **Emerging · Benchmark** · `llm` `agent` `cryptanalysis` `cryptography` `dual-use` `execution-grounded` `adaptive-adversary`

- **CTIConnect: A Benchmark for Retrieval-Augmented LLMs over Heterogeneous Cyber Threat Intelligence**  
  Yutong Cheng et al. *ACM SIGKDD 2026*.  
  [Paper](https://arxiv.org/abs/2510.11974) · [Code](https://github.com/peng-gao-lab/CTIConnect) · [Dataset](https://github.com/peng-gao-lab/CTIConnect/tree/main/data) · [Project](https://cticonnect.github.io/)  
  Evaluates retrieval and reasoning across 1,859 expert-verified questions, nine tasks, and five heterogeneous cyber-threat-intelligence sources.  
  **Emerging · Benchmark** · `llm` `retrieval-augmented` `threat-intelligence` `attack-technique-mapping` `curated-real-data` `temporal`

- **CVE-Factory: Scaling Expert-Level Agentic Tasks for Code Security Vulnerability**  
  Xianzhen Luo et al. *ICML 2026 Oral*.  
  [Paper](https://icml.cc/virtual/2026/poster/65622)  
  Builds executable environments from sparse CVE records and introduces LiveCVEBench with 190 tasks spanning 153 repositories and 14 programming languages.  
  **Emerging · Benchmark** · `llm` `agent` `multi-agent` `vulnerability-reproduction` `repository-scale` `execution-grounded`

- **CyberGym-E2E: Scalable Real-World Benchmark for AI Agents' End-to-End Cybersecurity Capabilities**  
  Tianneng Shi et al. *ICML 2026*.  
  [Paper](https://icml.cc/virtual/2026/poster/62134)  
  Evaluates discovery, proof-of-concept generation, and patching across 920 vulnerabilities from 139 real open-source projects.  
  **Emerging · Benchmark** · `llm` `agent` `vulnerability-detection` `poc-generation` `patch-generation` `repository-scale` `execution-grounded`

- **CyberGym: Evaluating AI Agents' Real-World Cybersecurity Capabilities at Scale**  
  Zhun Wang et al. *ICLR 2026*.  
  [Paper](https://openreview.net/forum?id=2YvbLQEdYt) · [arXiv](https://arxiv.org/abs/2506.02548) · [Code](https://github.com/sunblaze-ucb/cybergym) · [Dataset](https://huggingface.co/datasets/sunblaze-ucb/cybergym) · [Project](https://www.cybergym.io/cybergym/)  
  Evaluates agents on generating executable PoCs that reproduce historical vulnerabilities in real, repository-scale software.  
  **Essential · Benchmark** · `llm` `agent` `source-code` `vulnerability-reproduction` `poc-generation` `dual-use` `real-world` `execution-grounded`

- **ExploitBench: A Capability Ladder Benchmark for LLM Cybersecurity Agents**  
  Seunghyun Lee and David Brumley. *arXiv 2026*.  
  [Paper](https://arxiv.org/abs/2605.14153)  
  Grades sixteen progressive exploitation capabilities on 41 V8 bugs rather than equating a crash with code execution.  
  **Emerging · Benchmark** · `llm` `agent` `exploit-generation` `exploit-adaptation` `binary` `web` `offensive` `real-world`

- **ExploitGym: Can AI Agents Turn Security Vulnerabilities into Real Attacks?**  
  Zhun Wang et al. *arXiv 2026*.  
  [Paper](https://arxiv.org/abs/2605.11086) · [Code](https://github.com/sunblaze-ucb/exploitgym) · [Project](https://www.cybergym.io/exploitgym/)  
  Evaluates whether agents can extend vulnerability-triggering inputs into working exploits across userspace programs, V8, and the Linux kernel.  
  **Emerging · Benchmark** · `llm` `agent` `binary` `exploit-generation` `dual-use` `real-world` `execution-grounded`

- **Is Vibe Coding Safe? Benchmarking Vulnerability of Agent-Generated Code in Real-World Tasks**  
  Songwen Zhao et al. *ICML 2026*.  
  [Paper](https://icml.cc/virtual/2026/poster/61427) · [Code](https://github.com/LeiLiLab/susvibes) · [Leaderboard](https://leililab.github.io/susvibes-leaderboard)  
  Introduces SUSVIBES, 186 real feature-request tasks that jointly test the functionality and security of coding-agent changes to open-source repositories.  
  **Emerging · Benchmark** · `llm` `agent` `secure-code-generation` `vulnerability-detection` `repository-scale` `unit-tested`

- **REBENCH: A Procedural, Fair-by-Construction Benchmark for LLMs on Stripped-Binary Types and Names**  
  Jun Yeon Won et al. *AIWare 2026*.  
  [Paper](https://arxiv.org/abs/2604.27319)  
  Builds byte-aligned ground truth for fair evaluation of type and name recovery across architectures and optimization levels.  
  **Emerging · Benchmark** · `llm` `type-recovery` `function-naming` `binary` `dual-use` `real-world` `contamination-controlled`

- **REFORGE: A Method for Benchmarking LLMs' Reverse Engineering Capabilities in Decompiled Binary Function Naming**  
  Nicolas Koller and Andreas U. Schmidt. *Applied Computing 2026*.  
  [Paper](https://arxiv.org/abs/2607.07738)  
  Makes binary-to-source alignment uncertainty explicit when benchmarking LLM-based function naming.  
  **Emerging · Benchmark** · `llm` `function-naming` `decompilation` `binary` `dual-use` `synthetic` `contamination-controlled`

- **SEC-bench Pro: Can Language Models Solve Long-Horizon Software Security Tasks?**  
  Hwiwon Lee et al. *arXiv 2026*.  
  [Paper](https://arxiv.org/abs/2605.26548)  
  Benchmarks long-horizon PoC reproduction on 344 validated V8, SpiderMonkey, and Linux-kernel vulnerabilities.  
  **Emerging · Benchmark** · `llm` `agent` `vulnerability-reproduction` `poc-generation` `source-code` `repository` `dual-use` `real-world`

- **The Next Challenge for Agentic Cybersecurity: A Realistic, Contamination-Free Reverse Engineering Benchmark**  
  Jeremy Spence et al. *arXiv 2026*.  
  [Paper](https://arxiv.org/abs/2608.11469)  
  Introduces 262 contamination-controlled binary instances from 19 private, real-world-scale programs with layered anti-analysis protections.  
  **Emerging · Benchmark** · `llm` `agent` `malware-reverse-engineering` `protocol-reverse-engineering` `decompilation` `binary` `firmware` `network`

- **Towards Effective Offensive Security LLM Agents: Hyperparameter Tuning, LLM as a Judge, and a Lightweight CTF Benchmark**  
  Minghao Shao et al. *AAAI 2026*.  
  [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/40210) · [arXiv](https://arxiv.org/abs/2508.05674) · [Code](https://github.com/NYU-LLM-CTF/CTFTiny)  
  Introduces CTFTiny, CTFJudge, and the CTF Competency Index for low-cost, fine-grained evaluation of offensive-security agents across fifty CTF challenges.  
  **Emerging · Benchmark** · `llm` `agent` `multi-agent` `ctf-solving` `attack-planning` `binary` `web` `cryptography` `offensive` `ctf-style` `model-graded`

- **Training Language Model Agents to Find Vulnerabilities with CTF-Dojo**  
  Terry Yue Zhuo et al. *ICML 2026*.  
  [Paper](https://icml.cc/virtual/2026/poster/61783) · [arXiv](https://arxiv.org/abs/2508.18370)  
  Provides an interactive CTF environment and training recipe for agents that learn from executable security feedback.  
  **Emerging · Benchmark** · `llm` `agent` `reinforcement-learning` `ctf-solving` `vulnerability-detection` `binary` `web` `source-code`

- **BaxBench: Can LLMs Generate Correct and Secure Backends?**  
  Mark Vero et al. *ICML 2025*.  
  [Paper](https://proceedings.mlr.press/v267/vero25a.html) · [Preprint](https://arxiv.org/abs/2502.11844) · [Code](https://github.com/logic-star-ai/baxbench) · [Dataset](https://huggingface.co/datasets/LogicStar/BaxBench) · [Leaderboard](https://baxbench.com/)  
  Evaluates secure backend generation across 392 tasks using comprehensive functional tests and executable end-to-end security exploits.  
  **Essential · Benchmark** · `llm` `secure-code-generation` `source-code` `web` `unit-tested` `execution-grounded`

- **Benchmarking LLMs and LLM-Based Agents in Practical Vulnerability Detection for Code Repositories**  
  Alperen Yildiz et al. *ACL 2025*.  
  [Paper](https://aclanthology.org/2025.acl-long.1490/)  
  Measures practical repository-level vulnerability detection beyond isolated-function classification.  
  **Recommended · Benchmark** · `llm` `agent` `vulnerability-detection` `vulnerability-localization` `source-code` `repository` `defensive` `real-world`

- **BountyBench: Dollar Impact of AI Agent Attackers and Defenders on Real-World Cybersecurity Systems**  
  Andy Zhang et al. *NeurIPS 2025 Datasets and Benchmarks*.  
  [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/faed4276b52ef762879db4142655c699-Abstract-Datasets_and_Benchmarks_Track.html) · [arXiv](https://arxiv.org/abs/2505.15216) · [Code](https://github.com/bountybench/bountybench)  
  Measures Detect, Exploit, and Patch capabilities on forty real bug bounties in twenty-five deployable systems and reports their historical dollar impact.  
  **Essential · Benchmark** · `llm` `agent` `vulnerability-detection` `exploit-generation` `patch-generation` `dual-use` `real-world` `execution-grounded`

- **Bridging Crypto with ML-based Solvers: the SAT Formulation and Benchmarks**  
  Xinhao Zheng et al. *NeurIPS 2025 Datasets and Benchmarks*.  
  [Paper](https://papers.neurips.cc/paper_files/paper/2025/hash/69d97a6493fbf016fff0a751f253ad18-Abstract-Datasets_and_Benchmarks_Track.html) · [Code](https://github.com/void-zxh/SAT4CryptoBench)  
  Introduces SAT4CryptoBench for comparing standalone learned distinguishers, ML-guided solver heuristics, and hyperparameter optimization on cryptographic ANF and CNF instances.  
  **Recommended · Benchmark** · `classical-ml` `deep-learning` `neuro-symbolic` `cryptanalysis` `cryptography` `execution-grounded`

- **CVE-Bench: A Benchmark for AI Agents' Ability to Exploit Real-World Web Application Vulnerabilities**  
  Yuxuan Zhu et al. *ICML 2025 Spotlight*.  
  [Paper](https://proceedings.mlr.press/v267/zhu25i.html) · [arXiv](https://arxiv.org/abs/2503.17332) · [Code](https://github.com/uiuc-kang-lab/cve-bench)  
  Provides reproducible sandboxes and automatic outcome checks for forty critical-severity web CVEs under zero-day and one-day information settings.  
  **Essential · Benchmark** · `llm` `agent` `web` `web-exploitation` `offensive` `real-world` `execution-grounded`

- **Cybench: A Framework for Evaluating Cybersecurity Capabilities and Risks of Language Models**  
  Andy K. Zhang et al. *ICLR 2025 Oral*.  
  [Paper](https://openreview.net/forum?id=c9OLV0yRL) · [arXiv](https://arxiv.org/abs/2408.08926) · [Code](https://github.com/andyzorigin/cybench) · [Project](https://cybench.github.io/)  
  Evaluates agents on forty professional CTF tasks from four recent competitions and adds expert-written subtasks for measuring partial progress on unsolved challenges.  
  **Essential · Benchmark** · `llm` `agent` `ctf-solving` `offensive` `ctf-style` `execution-grounded`

- **Decompile-Bench: Million-Scale Binary-Source Function Pairs for Real-World Binary Decompilation**  
  Hanzhuo Tan et al. *NeurIPS 2025 Datasets and Benchmarks*.  
  [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/079cf13ae174c31f148207d94d213bdc-Abstract-Datasets_and_Benchmarks_Track.html) · [Preprint](https://arxiv.org/abs/2505.12668) · [Code](https://github.com/albertan017/LLM4Decompile)  
  Releases two million matched binary-source function pairs plus execution-oriented evaluation sets for training and comparing neural decompilers.  
  **Recommended · Benchmark** · `llm` `decompilation` `binary` `source-code` `repository-scale` `execution-grounded` `temporal`

- **DecompileBench: A Comprehensive Benchmark for Evaluating Decompilers in Real-World Scenarios**  
  Zeyu Gao et al. *ACL Findings 2025*.  
  [Paper](https://aclanthology.org/2025.findings-acl.1194/)  
  Evaluates neural and traditional decompilers with semantic and execution-aware criteria on real programs.  
  **Recommended · Benchmark** · `llm` `decompilation` `binary` `source-code` `dual-use` `real-world` `execution-grounded`

- **JsDeObsBench: Measuring and Benchmarking LLMs for JavaScript Deobfuscation**  
  Guoqiang Chen, Xin Jin, and Zhiqiang Lin. *ACM CCS 2025*.  
  [Paper](https://dl.acm.org/doi/10.1145/3719027.3744871)  
  Introduces an execution-aware benchmark for measuring whether LLMs recover readable and behaviorally correct JavaScript from obfuscated programs.  
  **Recommended · Benchmark** · `llm` `decompilation` `source-code` `web` `execution-grounded`

- **SEC-bench: Automated Benchmarking of LLM Agents on Real-World Software Security Tasks**  
  Hwiwon Lee et al. *NeurIPS 2025*.  
  [Paper](https://arxiv.org/abs/2506.11791)  
  Evaluates agents across real software-security workflows with automated, execution-grounded grading.  
  **Recommended · Benchmark** · `llm` `agent` `vulnerability-reproduction` `poc-generation` `patch-generation` `source-code` `repository` `dual-use`

- **SECODEPLT: A Unified Benchmark for Evaluating the Security Risks and Capabilities of Code GenAI**  
  Yuzhou Nie et al. *NeurIPS 2025 Datasets and Benchmarks*.  
  [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/13d0a982aae786d473f6949b734e2720-Abstract-Datasets_and_Benchmarks_Track.html) · [Code](https://github.com/ucsb-mlsec/SeCodePLT) · [Dataset](https://huggingface.co/datasets/UCSB-SURFI/SeCodePLT)  
  Unifies insecure code generation, vulnerability detection, and patch generation across more than 5,900 examples, 44 CWE types, and four programming languages.  
  **Recommended · Benchmark** · `llm` `secure-code-generation` `vulnerability-detection` `patch-generation` `execution-grounded`

- **CTIBench: A Benchmark for Evaluating LLMs in Cyber Threat Intelligence**  
  Md Tanvirul Alam et al. *NeurIPS 2024 Datasets and Benchmarks Spotlight*.  
  [Paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/5acd3c628aa1819fbf07c39ef73e7285-Abstract-Datasets_and_Benchmarks_Track.html) · [Code](https://github.com/maveryn/cti-bench) · [Dataset](https://huggingface.co/datasets/AI4Sec/cti-bench)  
  Evaluates CTI knowledge, CWE mapping, CVSS prediction, ATT&CK extraction, and threat-actor attribution rather than generic cybersecurity question answering.  
  **Recommended · Benchmark** · `llm` `threat-intelligence` `attack-technique-mapping` `curated-real-data`

- **NYU CTF Bench: A Scalable Open-Source Benchmark Dataset for Evaluating LLMs in Offensive Security**  
  Minghao Shao et al. *NeurIPS 2024 Datasets and Benchmarks*.  
  [Paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/69d97a6493fbf016fff0a751f253ad18-Abstract-Datasets_and_Benchmarks_Track.html) · [Code](https://github.com/NYU-LLM-CTF/NYU_CTF_Bench)  
  Provides 200 validated CSAW CTF challenges across six categories and an automated tool-using evaluation framework.  
  **Essential · Benchmark** · `llm` `agent` `ctf-solving` `offensive` `ctf-style` `execution-grounded`

- **VulDetectBench: Evaluating the Deep Capability of Vulnerability Detection with Large Language Models**  
  Yue Liu et al. *arXiv 2024*.  
  [Paper](https://arxiv.org/abs/2406.07595)  
  Separates shallow pattern matching from deeper vulnerability reasoning in LLM evaluation.  
  **Emerging · Benchmark** · `llm` `vulnerability-detection` `vulnerability-localization` `source-code` `defensive` `curated-real-data`

- **DiverseVul: A New Vulnerable Source Code Dataset for Deep Learning Based Vulnerability Detection**  
  Yizheng Chen et al. *RAID 2023*.  
  [Paper](https://doi.org/10.1145/3607199.3607242)  
  Builds a broad real-world vulnerable-function dataset and exposes generalization limits in learned detectors.  
  **Recommended · Dataset** · `deep-learning` `representation-learning` `vulnerability-detection` `source-code` `defensive` `real-world`

- **MOTIF: A Malware Reference Dataset with Ground Truth Family Labels**  
  Robert J. Joyce et al. *Computers & Security 2022*.  
  [Paper](https://doi.org/10.1016/j.cose.2022.102921)  
  Provides expert-vetted malware-family labels to reduce noise in family-classification evaluation.  
  **Recommended · Dataset** · `classical-ml` `deep-learning` `family-attribution` `malware-classification` `binary` `defensive` `real-world`

- **SOREL-20M: A Large Scale Benchmark Dataset for Malicious PE Detection**  
  Richard Harang and Ethan M. Rudd. *arXiv 2020*.  
  [Paper](https://arxiv.org/abs/2012.07634) · [Code and Data](https://github.com/sophos/SOREL-20M)  
  Releases metadata, labels, behavioral tags, features, and baselines for twenty million Windows PE files, with disarmed malware binaries available under controlled terms.  
  **Recommended · Dataset** · `classical-ml` `deep-learning` `binary` `malware-detection` `real-world`

- **EMBER: An Open Dataset for Training Static PE Malware Machine Learning Models**  
  Hyrum S. Anderson and Phil Roth. *arXiv 2018*.  
  [Paper](https://arxiv.org/abs/1804.04637)  
  Releases a standard feature set, labels, and baseline for reproducible static Windows PE malware detection.  
  **Essential · Dataset** · `classical-ml` `malware-detection` `malware-classification` `binary` `defensive` `real-world`

## Papers by Security Task

This is the primary task-oriented view of the catalog: every paper has one canonical security-task placement even when it also appears in the benchmark section.

### Vulnerability Discovery and Analysis

Papers in this section use AI to find, localize, classify, reproduce, prioritize, or dynamically uncover software vulnerabilities.

- **BACAgent: LLM-Powered Detection of Broken-Access-Control Vulnerabilities in Web Applications**  
  Fengyu Liu et al. *ACM CCS 2026*.  
  [Paper](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html)  
  Uses an LLM-powered agent to detect broken-access-control vulnerabilities in web applications.  
  **Emerging · System** · `llm` `agent` `vulnerability-detection` `web-exploitation` `web` `execution-grounded`

- **Cottontail: Large Language Model-Driven Concolic Execution for Highly Structured Test Input Generation**  
  Haoxin Tu et al. *IEEE S&P 2026*.  
  [Paper](https://arxiv.org/abs/2504.17542) · [Code](https://github.com/Cottontail-Proj/cottontail)  
  Combines concolic execution with LLM constraint solving and history-guided seed acquisition to generate highly structured test inputs.  
  **Emerging · System** · `llm` `neuro-symbolic` `test-generation` `dynamic-analysis` `fuzzing` `execution-grounded`

- **CTX-Coder: Cross-Attention Architectures Empower LLMs for Long-Context Vulnerability Detection**  
  Jujie Wang et al. *AAAI 2026*.  
  [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/37087)  
  Uses cross-attention over contextual functions and introduces CTX-VUL for repository-context vulnerability detection.  
  **Emerging · Method** · `llm` `vulnerability-detection` `vulnerability-localization` `source-code` `repository-scale`

- **CVE-Factory: Scaling Expert-Level Agentic Tasks for Code Security Vulnerability**  
  Xianzhen Luo et al. *ICML 2026 Oral*.  
  [Paper](https://icml.cc/virtual/2026/poster/65622)  
  Builds executable vulnerability environments from CVE records and introduces LiveCVEBench across 153 repositories and 14 languages.  
  **Emerging · Benchmark** · `llm` `agent` `vulnerability-reproduction` `poc-generation` `repository-scale` `execution-grounded`

- **CyberGym-E2E: Scalable Real-World Benchmark for AI Agents' End-to-End Cybersecurity Capabilities**  
  Tianneng Shi et al. *ICML 2026*.  
  [Paper](https://icml.cc/virtual/2026/poster/62134)  
  Evaluates discovery, proof-of-concept generation, and patching across 920 vulnerabilities from 139 real open-source projects.  
  **Emerging · Benchmark** · `llm` `agent` `vulnerability-detection` `vulnerability-reproduction` `patch-generation` `execution-grounded`

- **CyberGym: Evaluating AI Agents' Real-World Cybersecurity Capabilities at Scale**  
  Zhun Wang et al. *ICLR 2026*.  
  [Paper](https://openreview.net/forum?id=2YvbLQEdYt) · [arXiv](https://arxiv.org/abs/2506.02548) · [Code](https://github.com/sunblaze-ucb/cybergym) · [Dataset](https://huggingface.co/datasets/sunblaze-ucb/cybergym) · [Project](https://www.cybergym.io/cybergym/)  
  Evaluates agents on generating executable PoCs that reproduce historical vulnerabilities in real, repository-scale software.  
  **Essential · Benchmark** · `llm` `agent` `source-code` `vulnerability-reproduction` `poc-generation` `dual-use` `real-world` `execution-grounded`

- **deepSURF: Detecting Memory Safety Vulnerabilities in Rust Through Fuzzing LLM-Augmented Harnesses**  
  Georgios C. Androutsopoulos and Antonio Bianchi. *IEEE S&P 2026*.  
  [Paper](https://arxiv.org/abs/2506.15648) · [Code](https://github.com/purseclab/deepSURF)  
  Combines static analysis and LLM-augmented fuzz harnesses for unsafe Rust, rediscovering 20 known bugs and finding six new vulnerabilities.  
  **Emerging · System** · `llm` `fuzzing` `test-generation` `source-code` `execution-grounded`

- **FirmAgent: Leveraging Fuzzing to Assist LLM Agents with IoT Firmware Vulnerability Discovery**  
  Jiangan Ji et al. *NDSS 2026*.  
  [Paper](https://www.ndss-symposium.org/ndss-paper/firmagent-leveraging-fuzzing-to-assist-llm-agents-with-iot-firmware-vulnerability-discovery/)  
  Grounds LLM-agent taint analysis and PoC refinement in fuzzing evidence, finding 182 vulnerabilities in 14 firmware images.  
  **Emerging · System** · `llm` `agent` `fuzzing` `firmware` `iot` `poc-generation` `execution-grounded`

- **From Documentation to Zero-day Vulnerabilities: LLM-Driven Fuzzing of JavaScript Engines in PDF Readers**  
  Suyue Guo et al. *ACM CCS 2026*.  
  [Paper](https://arxiv.org/abs/2608.06641) · [Code](https://github.com/ucsb-seclab/PDFuzzer)  
  Uses LLM-derived grammars and API relationships plus constraint solving to generate complex JavaScript call sequences, finding 31 zero-day flaws in three PDF readers.  
  **Emerging · System** · `llm` `neuro-symbolic` `fuzzing` `test-generation` `source-code` `real-world` `execution-grounded`

- **MulVul: Retrieval-augmented Multi-Agent Code Vulnerability Detection via Cross-Model Prompt Evolution**  
  Zihan Wu et al. *ACL 2026*.  
  [Paper](https://aclanthology.org/events/acl-2026/)  
  Combines CWE-specialized detector agents, vulnerability-knowledge retrieval, and cross-model prompt evolution across 130 weakness types.  
  **Emerging · System** · `llm` `multi-agent` `retrieval-augmented` `vulnerability-detection` `source-code`

- **PILOT: Command-line Interface Fuzzing via Path-Guided, Iterative Large Language Model Prompting**  
  Momoko Shiraishi, Yinzhi Cao, and Takahiro Shinagawa. *IEEE S&P 2026*.  
  [Paper](https://www.os.is.s.u-tokyo.ac.jp/en/publication/conference/2026-sp-shiraishi/)  
  Uses static call paths, iterative LLM prompting, and coverage feedback to generate meaningful option and file combinations for CLI fuzzing.  
  **Emerging · System** · `llm` `fuzzing` `test-generation` `vulnerability-detection` `real-world` `execution-grounded`

- **Revelio: Cost-Efficient Agentic Memory Safety Vulnerability Detection For Repository-Scale Codebases**  
  Yiwei Hou et al. *arXiv 2026*.  
  [Paper](https://arxiv.org/abs/2606.22263)  
  Combines inexpensive LLM-based triage, lightweight static analysis, and sanitizer-validated executable proofs to discover memory-safety vulnerabilities at repository scale.  
  **Emerging · System** · `llm` `agent` `vulnerability-detection` `vulnerability-reproduction` `poc-generation` `repository-scale` `real-world` `execution-grounded`

- **SEC-bench Pro: Can Language Models Solve Long-Horizon Software Security Tasks?**  
  Hwiwon Lee et al. *arXiv 2026*.  
  [Paper](https://arxiv.org/abs/2605.26548)  
  Benchmarks long-horizon PoC reproduction on 344 validated V8, SpiderMonkey, and Linux-kernel vulnerabilities.  
  **Emerging · Benchmark** · `llm` `agent` `vulnerability-reproduction` `poc-generation` `source-code` `repository` `dual-use` `real-world`

- **SpecAuditor: Generating Audit Specifications for LLM-Driven Bug Detection**  
  Miaoqian Lin and Hao Chen. *IEEE S&P 2026*.  
  [Paper](https://www.ieee-security.org/TC/SP2026/accepted-papers.html) · [Code](https://github.com/Yuuoniy/SpecAuditor)  
  Extracts, generalizes, and retrieves project-specific audit specifications to guide LLM-based bug detection.  
  **Emerging · System** · `llm` `retrieval-augmented` `static-analysis` `vulnerability-detection` `repository-scale`

- **Specializing Language Models for Textual Fuzzing via Reinforcement Learning**  
  Jiayi Lin et al. *IEEE S&P 2026*.  
  [Paper](https://arxiv.org/abs/2509.20384)  
  Trains R1-Fuzz with coverage-derived questions and distance-based rewards, reporting higher coverage and 29 previously unknown vulnerabilities.  
  **Emerging · System** · `language-model` `reinforcement-learning` `fuzzing` `test-generation` `execution-grounded`

- **The Illusion of Rust Safety: Detecting Modular Unsafe Functions with LLMs**  
  Xiang Cheng et al. *ACM CCS 2026*.  
  [Paper](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html)  
  Defines modular unsafe functions in Rust and uses fine-tuned LLMs to detect them and generate proof-of-concept witnesses.  
  **Emerging · System** · `llm` `vulnerability-detection` `poc-generation` `source-code` `repository-scale` `real-world`

- **VulAgent: Hypothesis-Validation Driven Multi-Agent Architecture for Vulnerability Detection**  
  Ziliang Wang et al. *Findings of ACL 2026*.  
  [Paper](https://aclanthology.org/2026.findings-acl.928/)  
  Structures auditing as explicit vulnerability hypotheses, trigger paths, and project-context validation to reduce speculative reports.  
  **Emerging · System** · `llm` `multi-agent` `vulnerability-detection` `vulnerability-localization` `repository`

- **Benchmarking LLMs and LLM-Based Agents in Practical Vulnerability Detection for Code Repositories**  
  Alperen Yildiz et al. *ACL 2025*.  
  [Paper](https://aclanthology.org/2025.acl-long.1490/)  
  Measures practical repository-level vulnerability detection beyond isolated-function classification.  
  **Recommended · Benchmark** · `llm` `agent` `vulnerability-detection` `vulnerability-localization` `source-code` `repository` `defensive` `real-world`

- **LLMxCPG: Context-Aware Vulnerability Detection Through Code Property Graph-Guided Large Language Models**  
  Ahmed Lekssays et al. *USENIX Security 2025*.  
  [Paper](https://www.usenix.org/conference/usenixsecurity25/presentation/lekssays)  
  Uses code-property-graph slices to preserve vulnerability-relevant interprocedural context while reducing the amount of code presented to an LLM.  
  **Recommended · Method** · `llm` `graph-learning` `source-code` `vulnerability-detection` `static`

- **PromeFuzz: A Knowledge-Driven Approach to Fuzzing Harness Generation with Large Language Models**  
  Yuwei Liu et al. *ACM CCS 2025*.  
  [Paper](https://dl.acm.org/doi/10.1145/3719027.3765222)  
  Grounds LLM fuzz-harness generation in target-library knowledge and validates generated harnesses through execution.  
  **Recommended · System** · `llm` `retrieval-augmented` `fuzzing` `test-generation` `execution-grounded`

- **SEC-bench: Automated Benchmarking of LLM Agents on Real-World Software Security Tasks**  
  Hwiwon Lee et al. *NeurIPS 2025*.  
  [Paper](https://arxiv.org/abs/2506.11791)  
  Evaluates agents across real software-security workflows with automated, execution-grounded grading.  
  **Recommended · Benchmark** · `llm` `agent` `vulnerability-reproduction` `poc-generation` `patch-generation` `source-code` `repository` `dual-use`

- **VulnLLM-R: Specialized Reasoning LLM with Agent Scaffold for Vulnerability Detection**  
  Yuzhou Nie et al. *arXiv 2025*.  
  [Paper](https://arxiv.org/abs/2512.07533) · [Code](https://github.com/ucsb-mlsec/VulnLLM-R) · [Model](https://huggingface.co/UCSB-SURFI/VulnLLM-R-7B)  
  Trains a compact security reasoning model and wraps it in an agent scaffold for project-level vulnerability detection across Python, C, C++, and Java.  
  **Emerging · Method** · `llm` `agent` `vulnerability-detection` `vulnerability-localization` `source-code` `repository-scale` `real-world`

- **YuraScanner: Leveraging LLMs for Task-driven Web App Scanning**  
  Aleksei Stafeev et al. *NDSS 2025*.  
  [Paper](https://www.ndss-symposium.org/ndss-paper/yurascanner-leveraging-llms-for-task-driven-web-app-scanning/)  
  Uses task-driven LLM reasoning to steer dynamic web-application scanning toward security-relevant behavior.  
  **Recommended · System** · `llm` `agent` `dynamic-analysis` `vulnerability-detection` `web` `dual-use` `real-world` `execution-grounded`

- **Fuzz4All: Universal Fuzzing with Large Language Models**  
  Chunqiu Steven Xia et al. *ICSE 2024*.  
  [Paper](https://doi.org/10.1145/3597503.3639121)  
  Introduces a language-agnostic LLM fuzzing loop that generates and mutates inputs from natural-language specifications.  
  **Essential · System** · `llm` `fuzzing` `test-generation` `source-code` `dual-use` `execution-grounded`

- **Large Language Model Guided Protocol Fuzzing**  
  Ruijie Meng et al. *NDSS 2024*.  
  [Paper](https://www.ndss-symposium.org/ndss-paper/large-language-model-guided-protocol-fuzzing/) · [Code](https://github.com/ChatAFLndss/ChatAFL)  
  Introduces ChatAFL, which extracts protocol grammars and state information from natural-language specifications and uses an LLM to enrich seeds and escape coverage plateaus.  
  **Essential · System** · `llm` `network` `fuzzing` `protocol-reverse-engineering` `execution-grounded` `real-world`

- **Large Language Models Are Edge-Case Generators: Crafting Unusual Programs for Fuzzing Deep Learning Libraries**  
  Yinlin Deng et al. *ICSE 2024*.  
  [Paper](https://doi.org/10.1145/3597503.3623343)  
  Uses historical bug-triggering programs and LLM prompting to generate unusual tests for deep-learning libraries.  
  **Recommended · System** · `llm` `fuzzing` `test-generation` `source-code` `dual-use` `execution-grounded`

- **ProphetFuzz: Fully Automated Prediction and Fuzzing of High-Risk Option Combinations with Only Documentation via Large Language Model**  
  Dawei Wang et al. *ACM CCS 2024*.  
  [Paper](https://doi.org/10.1145/3658644.3690231) · [Preprint](https://arxiv.org/abs/2409.00922) · [Code](https://github.com/NASP-THU/ProphetFuzz)  
  Predicts high-risk command-line option combinations from documentation and turns them into fully automated fuzzing campaigns.  
  **Recommended · System** · `llm` `fuzzing` `test-generation` `source-code` `real-world` `execution-grounded`

- **VulDetectBench: Evaluating the Deep Capability of Vulnerability Detection with Large Language Models**  
  Yue Liu et al. *arXiv 2024*.  
  [Paper](https://arxiv.org/abs/2406.07595)  
  Separates shallow pattern matching from deeper vulnerability reasoning in LLM evaluation.  
  **Emerging · Benchmark** · `llm` `vulnerability-detection` `vulnerability-localization` `source-code` `defensive` `curated-real-data`

- **DiverseVul: A New Vulnerable Source Code Dataset for Deep Learning Based Vulnerability Detection**  
  Yizheng Chen et al. *RAID 2023*.  
  [Paper](https://doi.org/10.1145/3607199.3607242)  
  Builds a broad real-world vulnerable-function dataset and exposes generalization limits in learned detectors.  
  **Recommended · Dataset** · `deep-learning` `representation-learning` `vulnerability-detection` `source-code` `defensive` `real-world`

- **Large Language Models Are Zero-Shot Fuzzers: Fuzzing Deep-Learning Libraries via Large Language Models**  
  Yinlin Deng et al. *ISSTA 2023*.  
  [Paper](https://doi.org/10.1145/3597926.3598067)  
  Shows that pretrained code models can synthesize and mutate valid tests for deep-learning libraries without task-specific training.  
  **Essential · System** · `llm` `fuzzing` `test-generation` `source-code` `dual-use` `execution-grounded`

- **LineVul: A Transformer-Based Line-Level Vulnerability Prediction**  
  Michael C. Fu and Chakkrit Tantithamthavorn. *MSR 2022*.  
  [Paper](https://doi.org/10.1145/3524842.3528452)  
  Applies Transformer representations and attention-based localization to function- and line-level vulnerability prediction.  
  **Recommended · Method** · `language-model` `representation-learning` `vulnerability-detection` `vulnerability-localization` `source-code` `defensive` `real-world` `static`

- **ReGVD: Revisiting Graph Neural Networks for Vulnerability Detection**  
  Van-Anh Nguyen et al. *ICSE Companion 2022*.  
  [Paper](https://doi.org/10.1109/ICSE-Companion55297.2022.9793807)  
  Revisits graph pooling and pretrained code representations for learned source-code vulnerability detection.  
  **Recommended · Method** · `graph-learning` `representation-learning` `vulnerability-detection` `source-code` `defensive` `static`

- **Montage: A Neural Network Language Model-Guided JavaScript Engine Fuzzer**  
  Suyoung Lee et al. *USENIX Security 2020*.  
  [Paper](https://www.usenix.org/conference/usenixsecurity20/presentation/lee-suyoung)  
  Learns fragment sequences from regression tests to generate semantically rich JavaScript-engine inputs.  
  **Essential · System** · `language-model` `deep-learning` `fuzzing` `test-generation` `source-code` `dual-use` `execution-grounded` `real-world`

- **Devign: Effective Vulnerability Identification by Learning Comprehensive Program Semantics via Graph Neural Networks**  
  Yaqin Zhou et al. *NeurIPS 2019*.  
  [Paper](https://proceedings.neurips.cc/paper_files/paper/2019/hash/49265d2447bc3bbfe9e76306ce40a31f-Abstract.html)  
  Combines syntax, control-flow, and data-flow relations in a graph neural network for function-level vulnerability classification on manually labeled real projects.  
  **Essential · Method** · `graph-learning` `representation-learning` `source-code` `vulnerability-detection` `static` `real-world`

- **NEUZZ: Efficient Fuzzing with Neural Program Smoothing**  
  Dongdong She et al. *IEEE S&P 2019*.  
  [Paper](https://arxiv.org/abs/1807.05620) · [Code](https://github.com/Dongdongshe/neuzz)  
  Learns a smooth neural approximation of branching behavior so gradients can guide mutations through the otherwise discrete fuzzing search space.  
  **Essential · Method** · `deep-learning` `source-code` `binary` `fuzzing` `execution-grounded`

- **Compiler Fuzzing through Deep Learning**  
  Chris Cummins et al. *ISSTA 2018*.  
  [Paper](https://doi.org/10.1145/3213846.3213848)  
  Learns a generative model of code to produce compiler test cases that resemble human-written programs.  
  **Recommended · System** · `language-model` `deep-learning` `fuzzing` `test-generation` `source-code` `dual-use` `execution-grounded`

- **VulDeePecker: A Deep Learning-Based System for Vulnerability Detection**  
  Zhen Li et al. *NDSS 2018*.  
  [Paper](https://www.ndss-symposium.org/ndss-program-2018-program/) · [PDF](https://www.ndss-symposium.org/wp-content/uploads/2018/02/ndss2018_03A-2_Li_paper.pdf)  
  Introduces code gadgets as a semantics-aware representation for learning vulnerability patterns and helped establish deep learning for source-code vulnerability detection.  
  **Essential · System** · `deep-learning` `source-code` `vulnerability-detection` `static`

- **Learn&Fuzz: Machine Learning for Input Fuzzing**  
  Patrice Godefroid, Hila Peleg, and Rishabh Singh. *ASE 2017*.  
  [Paper](https://doi.org/10.1109/ASE.2017.8115618)  
  Uses a learned generative model of structured inputs to seed and guide coverage-oriented fuzzing.  
  **Essential · Method** · `language-model` `fuzzing` `test-generation` `source-code` `dual-use` `execution-grounded`

### Program Understanding and Reverse Engineering

Papers in this section recover security-relevant semantics from source code, bytecode, binaries, firmware, or undocumented protocols.

- **CrackMeBench: Binary Reverse Engineering for Agents**  
  Ilia David and Arthur Gervais. *arXiv 2026*.  
  [Paper](https://arxiv.org/abs/2605.10597)  
  Evaluates tool-using agents on clean-room binary reverse-engineering challenges with deterministic grading.  
  **Emerging · Benchmark** · `llm` `agent` `malware-reverse-engineering` `decompilation` `binary` `dual-use` `execution-grounded` `contamination-controlled`

- **CREBench: Evaluating Large Language Models in Cryptographic Binary Reverse Engineering**  
  Baicheng Chen et al. *COLM 2026*.  
  [Paper](https://arxiv.org/abs/2604.03750) · [Code](https://github.com/wangyu-ovo/CREBench) · [Dataset](https://huggingface.co/datasets/Danny-1223/CREBench) · [Project](https://jams-zhou-james.github.io/CREBench/)  
  Evaluates LLMs across four levels of cryptographic binary reverse engineering, from algorithm identification to flag recovery.  
  **Emerging · Benchmark** · `llm` `binary` `cryptographic-reverse-engineering` `cryptography` `ctf-style` `execution-grounded`

- **Decompiling the Synergy: An Empirical Study of Human–LLM Teaming in Software Reverse Engineering**  
  Zion Leonahenahe Basque et al. *NDSS 2026*.  
  [Paper](https://www.ndss-symposium.org/ndss-paper/decompiling-the-synergy-an-empirical-study-of-human-llm-teaming-in-software-reverse-engineering/)  
  Combines a 153-practitioner survey with 109 hours of instrumented work from 48 participants to measure human–LLM reverse-engineering workflows.  
  **Emerging · Empirical Study** · `llm` `malware-reverse-engineering` `decompilation` `binary` `human-baseline`

- **Idioms: A Simple and Effective Framework for Turbo-Charging Local Neural Decompilation with Well-Defined Types**  
  Luke Dramko, Claire Le Goues, and Edward J. Schwartz. *NDSS 2026*.  
  [Paper](https://www.ndss-symposium.org/ndss-paper/idioms-a-simple-and-effective-framework-for-turbo-charging-local-neural-decompilation-with-well-defined-types/)  
  Fine-tunes local LLMs to emit decompiled code with user-defined type definitions and introduces the REALTYPE dataset.  
  **Emerging · Method** · `llm` `decompilation` `type-recovery` `binary` `execution-grounded`

- **REBENCH: A Procedural, Fair-by-Construction Benchmark for LLMs on Stripped-Binary Types and Names**  
  Jun Yeon Won et al. *AIWare 2026*.  
  [Paper](https://arxiv.org/abs/2604.27319)  
  Builds byte-aligned ground truth for fair evaluation of type and name recovery across architectures and optimization levels.  
  **Emerging · Benchmark** · `llm` `type-recovery` `function-naming` `binary` `dual-use` `real-world` `contamination-controlled`

- **REFORGE: A Method for Benchmarking LLMs' Reverse Engineering Capabilities in Decompiled Binary Function Naming**  
  Nicolas Koller and Andreas U. Schmidt. *Applied Computing 2026*.  
  [Paper](https://arxiv.org/abs/2607.07738)  
  Makes binary-to-source alignment uncertainty explicit when benchmarking LLM-based function naming.  
  **Emerging · Benchmark** · `llm` `function-naming` `decompilation` `binary` `dual-use` `synthetic` `contamination-controlled`

- **Selective Knowledge Distillation: Fusing LLM Semantic Strengths with DNN Efficiency for Binary Code Similarity Detection**  
  Shize Zhou et al. *ACL 2026*.  
  [Paper](https://aclanthology.org/2026.acl-long.1193/)  
  Distills LLM-derived program semantics into efficient binary-similarity models using selective targets and discrepancy-weighted sampling.  
  **Emerging · Method** · `llm` `deep-learning` `representation-learning` `binary-similarity` `binary`

- **The Next Challenge for Agentic Cybersecurity: A Realistic, Contamination-Free Reverse Engineering Benchmark**  
  Jeremy Spence et al. *arXiv 2026*.  
  [Paper](https://arxiv.org/abs/2608.11469)  
  Introduces 262 contamination-controlled binary instances from 19 private, real-world-scale programs with layered anti-analysis protections.  
  **Emerging · Benchmark** · `llm` `agent` `malware-reverse-engineering` `protocol-reverse-engineering` `decompilation` `binary` `firmware` `network`

- **Towards Generality: Task-Adaptive Binary Analysis via Semantic Retrieval and Verifiable Reasoning**  
  Yuzhe Liu et al. *USENIX Security 2026*.  
  [Paper](https://www.usenix.org/conference/usenixsecurity26/presentation/liu-yuzhe)  
  Introduces BINREX, which grounds intent through semantic retrieval and executes verifiable IDAPython subtasks for general static-binary analysis.  
  **Emerging · System** · `llm` `agent` `retrieval-augmented` `malware-reverse-engineering` `binary` `execution-grounded`

- **Beyond Classification: Inferring Function Names in Stripped Binaries via Domain Adapted LLMs**  
  Linxi Jiang, Xin Jin, and Zhiqiang Lin. *NDSS 2025*.  
  [Paper](https://www.ndss-symposium.org/ndss-paper/beyond-classification-inferring-function-names-in-stripped-binaries-via-domain-adapted-llms/)  
  Domain-adapts language models to infer meaningful names for functions in stripped binaries.  
  **Recommended · Method** · `llm` `function-naming` `decompilation` `binary` `dual-use` `real-world`

- **Decompile-Bench: Million-Scale Binary-Source Function Pairs for Real-World Binary Decompilation**  
  Hanzhuo Tan et al. *NeurIPS 2025 Datasets and Benchmarks*.  
  [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/079cf13ae174c31f148207d94d213bdc-Abstract-Datasets_and_Benchmarks_Track.html) · [Preprint](https://arxiv.org/abs/2505.12668) · [Code](https://github.com/albertan017/LLM4Decompile)  
  Releases two million matched binary-source function pairs plus execution-oriented evaluation sets for training and comparing neural decompilers.  
  **Recommended · Benchmark** · `llm` `decompilation` `binary` `source-code` `repository-scale` `execution-grounded` `temporal`

- **DecompileBench: A Comprehensive Benchmark for Evaluating Decompilers in Real-World Scenarios**  
  Zeyu Gao et al. *ACL Findings 2025*.  
  [Paper](https://aclanthology.org/2025.findings-acl.1194/)  
  Evaluates neural and traditional decompilers with semantic and execution-aware criteria on real programs.  
  **Recommended · Benchmark** · `llm` `decompilation` `binary` `source-code` `dual-use` `real-world` `execution-grounded`

- **Decompiling Smart Contracts with a Large Language Model**  
  Isaac David et al. *arXiv 2025*.  
  [Paper](https://arxiv.org/abs/2506.19624) · [Project](https://evmdecompiler.com/)  
  Combines static EVM analysis with a fine-tuned language model to translate bytecode into readable Solidity with recovered names, control flow, and function signatures.  
  **Emerging · System** · `llm` `neuro-symbolic` `decompilation` `type-recovery` `function-naming` `bytecode` `smart-contract` `dual-use`

- **JsDeObsBench: Measuring and Benchmarking LLMs for JavaScript Deobfuscation**  
  Guoqiang Chen, Xin Jin, and Zhiqiang Lin. *ACM CCS 2025*.  
  [Paper](https://dl.acm.org/doi/10.1145/3719027.3744871)  
  Evaluates whether LLMs recover readable and behaviorally correct JavaScript from obfuscated programs with execution-aware criteria.  
  **Recommended · Benchmark** · `llm` `decompilation` `source-code` `web` `execution-grounded`

- **Nova: Generative Language Models for Assembly Code with Hierarchical Attention and Contrastive Learning**  
  Nan Jiang et al. *ICLR 2025*.  
  [Paper](https://openreview.net/forum?id=4ytRL3HJrq) · [Code](https://github.com/lt-asset/nova)  
  Pretrains an assembly-language model with hierarchical attention and contrastive objectives over functions and compiler optimization levels.  
  **Recommended · Method** · `llm` `representation-learning` `binary-representation` `decompilation` `binary-similarity` `binary`

- **BinBert: Binary Code Understanding with a Fine-Tunable and Execution-Aware Transformer**  
  Fiorella Artuso et al. *IEEE TDSC 2024*.  
  [Paper](https://doi.org/10.1109/TDSC.2024.3397660)  
  Pretrains binary representations using execution-aware objectives and transfers them to multiple analysis tasks.  
  **Recommended · Method** · `language-model` `representation-learning` `binary-representation` `binary-similarity` `binary` `dual-use` `static`

- **LLM4Decompile: Decompiling Binary Code with Large Language Models**  
  Hanzhuo Tan et al. *EMNLP 2024*.  
  [Paper](https://aclanthology.org/2024.emnlp-main.203/) · [Code](https://github.com/albertan017/LLM4Decompile)  
  Introduces an open model family trained to translate binary code into readable and executable source code.  
  **Essential · Method** · `llm` `decompilation` `code-representation` `binary` `source-code` `execution-grounded`

- **Augmenting Decompiler Output with Learned Variable Names and Types**  
  Qibin Chen et al. *USENIX Security 2022 Distinguished Paper*.  
  [Paper](https://www.usenix.org/conference/usenixsecurity22/presentation/chen-qibin) · [Code](https://github.com/CMUSTRUDEL/DIRTY)  
  Introduces DIRTY, a Transformer that restores meaningful variable names and types to decompiler output, together with a large paired source/decompilation dataset.  
  **Essential · System** · `language-model` `binary` `decompilation` `function-naming` `type-recovery`

- **jTrans: Jump-Aware Transformer for Binary Code Similarity**  
  Hao Wang et al. *ISSTA 2022*.  
  [Paper](https://doi.org/10.1145/3533767.3534367)  
  Injects control-flow jump structure into Transformer pretraining for large-scale binary similarity search.  
  **Recommended · Method** · `language-model` `representation-learning` `binary-similarity` `binary-representation` `binary` `dual-use` `real-world` `static`

- **PalmTree: Learning an Assembly Language Model for Instruction Embedding**  
  Xuezixiang Li, Yu Qu, and Heng Yin. *ACM CCS 2021*.  
  [Paper](https://arxiv.org/abs/2103.03809) · [Code](https://github.com/palmtreemodel/PalmTree)  
  Pretrains a contextual assembly-language model with instruction, control-flow, and data-dependency objectives for reuse across binary-analysis tasks.  
  **Recommended · Method** · `language-model` `representation-learning` `binary` `binary-representation`

- **TREX: Learning Execution Semantics from Micro-Traces for Binary Similarity**  
  Kexin Pei et al. *IEEE TSE 2021*.  
  [Paper](https://arxiv.org/abs/2012.08680)  
  Uses micro-traces as self-supervision so binary embeddings capture execution semantics across compilers and architectures.  
  **Recommended · Method** · `language-model` `representation-learning` `binary-similarity` `binary-representation` `binary` `dual-use` `execution-grounded`

- **XDA: Accurate, Robust Disassembly with Transfer Learning**  
  Kexin Pei et al. *NDSS 2021*.  
  [Paper](https://www.ndss-symposium.org/ndss-paper/xda-accurate-robust-disassembly-with-transfer-learning/)  
  Treats disassembly and function-boundary recovery as transfer learning over raw binary bytes.  
  **Essential · Method** · `language-model` `representation-learning` `function-identification` `binary-representation` `binary` `dual-use` `real-world` `static`

- **DeepBinDiff: Learning Program-Wide Code Representations for Binary Diffing**  
  Yue Duan et al. *NDSS 2020*.  
  [Paper](https://www.ndss-symposium.org/ndss-paper/deepbindiff-learning-program-wide-code-representations-for-binary-diffing/)  
  Learns program-wide instruction embeddings and graph structure for cross-version binary diffing.  
  **Essential · System** · `graph-learning` `representation-learning` `binary-similarity` `software-provenance` `binary` `dual-use` `real-world` `static`

- **Asm2Vec: Boosting Static Representation Robustness for Binary Clone Search against Code Obfuscation and Compiler Optimization**  
  Steven H. H. Ding, Benjamin C. M. Fung, and Philippe Charland. *IEEE S&P 2019*.  
  [Paper](https://doi.org/10.1109/SP.2019.00003)  
  Learns assembly-function embeddings designed to remain useful across optimization and obfuscation.  
  **Essential · Method** · `representation-learning` `binary-similarity` `binary-representation` `binary` `dual-use` `static` `real-world`

- **Coda: An End-to-End Neural Program Decompiler**  
  Cheng Fu et al. *NeurIPS 2019*.  
  [Paper](https://proceedings.neurips.cc/paper_files/paper/2019/hash/093b60fd0557804c8ba0cbf1453da22f-Abstract.html)  
  Combines neural translation and error correction for end-to-end assembly-to-source decompilation.  
  **Essential · Method** · `deep-learning` `language-model` `decompilation` `binary` `source-code` `dual-use` `synthetic` `execution-grounded`

- **SAFE: Self-Attentive Function Embeddings for Binary Similarity**  
  Luca Massarelli et al. *DIMVA 2019*.  
  [Paper](https://doi.org/10.1007/978-3-030-22038-9_15)  
  Builds efficient self-attentive instruction-sequence embeddings for cross-architecture function similarity.  
  **Recommended · Method** · `deep-learning` `representation-learning` `binary-similarity` `binary-representation` `binary` `dual-use` `static`

- **DEBIN: Predicting Debug Information in Stripped Binaries**  
  Jingxuan He et al. *ACM CCS 2018*.  
  [Paper](https://doi.org/10.1145/3243734.3243866)  
  Uses probabilistic structured prediction to recover variable names and types from stripped binaries.  
  **Essential · System** · `structured-prediction` `representation-learning` `function-naming` `type-recovery` `binary` `dual-use` `real-world` `static`

- **EKLAVYA: Recovering Function Types in Stripped Binaries**  
  Zheng Leong Chua et al. *USENIX Security 2017*.  
  [Paper](https://www.usenix.org/conference/usenixsecurity17/technical-sessions/presentation/chua)  
  Learns function signatures from disassembly to improve indirect-call resolution in stripped binaries.  
  **Essential · System** · `deep-learning` `type-recovery` `function-identification` `binary` `dual-use` `real-world` `static`

- **Neural Network-Based Graph Embedding for Cross-Platform Binary Code Similarity Detection**  
  Xiaojun Xu et al. *ACM CCS 2017*.  
  [Paper](https://arxiv.org/abs/1708.06525) · [PDF](https://www.cs.ucr.edu/~heng/pubs/gemini-ccs17.pdf)  
  Introduces Gemini, a learned embedding of attributed control-flow graphs that made cross-architecture binary similarity substantially faster and more accurate than graph matching.  
  **Essential · Method** · `graph-learning` `representation-learning` `binary` `binary-similarity` `software-provenance`

### AI for Cryptography and Cryptanalysis

Papers in this section apply AI to cryptographic reasoning, cryptanalysis, solver guidance, side-channel analysis, and the recovery of cryptographic semantics from implementations.

- **AICrypto: Evaluating Cryptography Capabilities of Large Language Models**  
  Yu Wang et al. *ICML 2026*.  
  [Paper](https://icml.cc/virtual/2026/poster/63082) · [arXiv](https://arxiv.org/abs/2507.09580) · [Code](https://github.com/wangyu-ovo/aicrypto-agent) · [Dataset](https://huggingface.co/datasets/yuuwwang/aicrypto) · [Project](https://aicryptobench.github.io/)  
  Evaluates cryptographic knowledge, practical vulnerability exploitation, and proof reasoning with 135 multiple-choice questions, 150 CTF challenges, and 30 proof problems reviewed or constructed by cryptography experts.  
  **Emerging · Benchmark** · `llm` `agent` `cryptographic-reasoning` `cryptanalysis` `cryptography` `ctf-style` `human-baseline`

- **CREBench: Evaluating Large Language Models in Cryptographic Binary Reverse Engineering**  
  Baicheng Chen et al. *COLM 2026*.  
  [Paper](https://arxiv.org/abs/2604.03750) · [Code](https://github.com/wangyu-ovo/CREBench) · [Dataset](https://huggingface.co/datasets/Danny-1223/CREBench) · [Project](https://jams-zhou-james.github.io/CREBench/)  
  Evaluates LLMs across four levels of cryptographic binary reverse engineering, from algorithm identification to flag recovery.  
  **Emerging · Benchmark** · `llm` `binary` `cryptographic-reverse-engineering` `cryptography` `ctf-style` `execution-grounded`

- **CryptanalysisBench: Can LLMs do Cryptanalysis?**  
  Lukas Fluri et al. *arXiv 2026*.  
  [Paper](https://arxiv.org/abs/2607.18538) · [Code](https://github.com/ethz-spylab/cryptanalysis-benchmark) · [Project](https://cryptanalysis-bench.com/)  
  Evaluates agents on 191 real cryptographic schemes across six primitive families using formal security games and fresh-randomness verification of submitted attack programs.  
  **Emerging · Benchmark** · `llm` `agent` `cryptanalysis` `cryptography` `dual-use` `execution-grounded` `adaptive-adversary`

- **Deep Neural Cryptography**  
  David Gerault et al. *EUROCRYPT 2026*.  
  [Paper](https://eprint.iacr.org/2025/288) · [PDF](https://eprint.iacr.org/2025/288.pdf) · [DOI](https://doi.org/10.1007/978-3-032-25333-0_18)  
  Defines correctness and security for cryptographic primitives implemented as ReLU neural networks, breaks natural implementations using non-Boolean inputs, and gives a low-overhead provably secure construction.  
  **Recommended · Method** · `deep-learning` `cryptographic-implementation-analysis` `cryptographic-design-analysis` `cryptanalysis` `cryptography` `dual-use` `execution-grounded`

- **Halfspace Learning for Lattice Signature Key Recovery from Signs**  
  Marcus Brinkmann, Nicolai Kraus, and Alexander May. *CRYPTO 2026*.  
  [Paper](https://eprint.iacr.org/2026/1366) · [DOI](https://doi.org/10.1007/978-3-032-35377-1_12) · [Code](https://github.com/nicolkraus/halfspace)  
  Models sign leakage as halfspace learning to recover HAWK, Falcon, and ML-DSA signing keys with strong noise tolerance.  
  **Emerging · Method** · `classical-ml` `side-channel-analysis` `cryptanalysis` `cryptography` `execution-grounded`

- **Neural-Inspired Advances in Integral Cryptanalysis**  
  Liu Zhang et al. *EUROCRYPT 2026*.  
  [Paper](https://eprint.iacr.org/2025/852) · [DOI](https://doi.org/10.1007/978-3-032-25333-0_16)  
  Uses neural distinguishers to discover integral features, interprets them with Boolean analysis, and converts them into improved classical attacks on SKINNY.  
  **Emerging · Method** · `deep-learning` `neural-cryptanalysis` `cryptanalysis` `cryptography` `execution-grounded`

- **AI for Code-based Cryptography**  
  Mohamed Malhou, Ludovic Perret, and Kristin Lauter. *SAC 2025*.  
  [Paper](https://sacworkshop.org/SAC25/preproceedings/sac2025-2-paper16.pdf) · [Code](https://github.com/facebookresearch/ai4code-cryptanalysis)  
  Introduces a Transformer-based distinguisher for structured Goppa, MDPC, and QC-MDPC codes and studies whether learned representations expose structure relevant to post-quantum cryptanalysis.  
  **Recommended · Method** · `deep-learning` `language-model` `neural-cryptanalysis` `cryptographic-design-analysis` `cryptography` `dual-use`

- **Bridging Crypto with ML-based Solvers: the SAT Formulation and Benchmarks**  
  Xinhao Zheng et al. *NeurIPS 2025 Datasets and Benchmarks*.  
  [Paper](https://papers.neurips.cc/paper_files/paper/2025/hash/69d97a6493fbf016fff0a751f253ad18-Abstract-Datasets_and_Benchmarks_Track.html) · [Code](https://github.com/void-zxh/SAT4CryptoBench)  
  Introduces SAT4CryptoBench for comparing standalone learned distinguishers, ML-guided solver heuristics, and hyperparameter optimization on cryptographic ANF and CNF instances.  
  **Recommended · Benchmark** · `classical-ml` `deep-learning` `neuro-symbolic` `cryptanalysis` `cryptography` `execution-grounded`

- **Is ML-Based Cryptanalysis Inherently Limited? Simulating Cryptographic Adversaries via Gradient-Based Methods**  
  Avital Shafran et al. *CRYPTO 2024*.  
  [Paper](https://eprint.iacr.org/2024/1126) · [DOI](https://doi.org/10.1007/978-3-031-68391-6_2)  
  Formalizes sample- and gradient-based cryptanalytic adversaries and proves simulation results that clarify the expressive potential and limits of ML-based attacks.  
  **Recommended · Method** · `classical-ml` `deep-learning` `neural-cryptanalysis` `cryptanalysis` `cryptography`

- **SALSA VERDE: A Machine Learning Attack on Learning With Errors with Sparse Small Secrets**  
  Cathy Yuanchen Li et al. *NeurIPS 2023*.  
  [Paper](https://eprint.iacr.org/2023/968)  
  Extends Transformer-based LWE attacks to larger dimensions and sparse binary, ternary, and narrow-Gaussian secrets.  
  **Essential · Method** · `deep-learning` `language-model` `neural-cryptanalysis` `cryptanalysis` `cryptography` `dual-use` `execution-grounded` `synthetic`

- **An Assessment of Differential-Neural Distinguishers**  
  Aron Gohr, Gregor Leander, and Patrick Neumann. *IACR ePrint 2022*.  
  [Paper](https://eprint.iacr.org/2022/253)  
  Systematically reassesses what differential-neural distinguishers learn and corrects misleading multi-pair improvement claims.  
  **Recommended · Empirical Study** · `deep-learning` `neural-cryptanalysis` `cryptanalysis` `cryptography` `dual-use` `execution-grounded`

- **SALSA: Attacking Lattice Cryptography with Transformers**  
  Emily Wenger et al. *NeurIPS 2022*.  
  [Paper](https://proceedings.neurips.cc/paper_files/paper/2022/hash/e28b3369186459f57c94a9ec9137fac9-Abstract-Conference.html) · [Code](https://github.com/facebookresearch/SALSA)  
  Combines Transformer learning of modular arithmetic with statistical cryptanalysis to recover sparse binary secrets from small-to-medium LWE instances.  
  **Recommended · Method** · `deep-learning` `language-model` `neural-cryptanalysis` `cryptanalysis` `cryptography` `dual-use` `execution-grounded`

- **A Deeper Look at Machine Learning-Based Cryptanalysis**  
  Adrien Benamira et al. *EUROCRYPT 2021*.  
  [Paper](https://eprint.iacr.org/2021/287)  
  Analyzes the internal behavior of neural distinguishers and relates learned signals to classical differential cryptanalysis.  
  **Essential · Empirical Study** · `deep-learning` `neural-cryptanalysis` `cryptanalysis` `cryptography` `dual-use` `execution-grounded`

- **SCAUL: Power Side-Channel Analysis with Unsupervised Learning**  
  Keyvan Ramezanpour, Paul Ampadu, and William Diehl. *IEEE Transactions on Computers 2020*.  
  [Paper](https://arxiv.org/abs/2001.05951)  
  Uses unsupervised representation learning to recover leakage features and keys from power traces without profiling labels.  
  **Recommended · Method** · `deep-learning` `unsupervised-learning` `side-channel-analysis` `cryptanalysis` `cryptography` `dual-use` `execution-grounded` `real-world`

- **Improving Attacks on Round-Reduced Speck32/64 Using Deep Learning**  
  Aron Gohr. *CRYPTO 2019*.  
  [Paper](https://eprint.iacr.org/2019/037) · [PDF](https://eprint.iacr.org/2019/037.pdf) · [Code](https://github.com/agohr/deep_speck)  
  Introduces deep residual neural distinguishers and a Bayesian key-search strategy that improve differential attacks on round-reduced Speck32/64.  
  **Essential · Method** · `deep-learning` `neural-cryptanalysis` `cryptanalysis` `cryptography` `dual-use` `execution-grounded`

- **Breaking Cryptographic Implementations Using Deep Learning Techniques**  
  Houssem Maghrebi, Thibault Portigliatti, and Emmanuel Prouff. *SPACE 2016*.  
  [Paper](https://eprint.iacr.org/2016/921)  
  Demonstrates early deep-learning profiling attacks against masked cryptographic implementations.  
  **Essential · Method** · `deep-learning` `side-channel-analysis` `cryptanalysis` `cryptography` `dual-use` `execution-grounded` `real-world`

### Exploitation and Offensive Security

Papers in this section study AI systems that turn weaknesses into concrete impact or execute multi-step offensive workflows in controlled settings.

- **Co-RedTeam: Orchestrated Security Discovery and Exploitation with LLM Agents**  
  Pengfei He et al. *ICML 2026*.  
  [Paper](https://icml.cc/virtual/2026/poster/60747)  
  Orchestrates specialized agents for vulnerability discovery and exploitation with shared execution-grounded memory.  
  **Emerging · System** · `llm` `agent` `multi-agent` `automated-penetration-testing` `exploit-generation` `execution-grounded`

- **ExploitBench: A Capability Ladder Benchmark for LLM Cybersecurity Agents**  
  Seunghyun Lee and David Brumley. *arXiv 2026*.  
  [Paper](https://arxiv.org/abs/2605.14153)  
  Grades sixteen progressive exploitation capabilities on 41 V8 bugs rather than equating a crash with code execution.  
  **Emerging · Benchmark** · `llm` `agent` `exploit-generation` `exploit-adaptation` `binary` `web` `offensive` `real-world`

- **ExploitGym: Can AI Agents Turn Security Vulnerabilities into Real Attacks?**  
  Zhun Wang et al. *arXiv 2026*.  
  [Paper](https://arxiv.org/abs/2605.11086) · [Code](https://github.com/sunblaze-ucb/exploitgym) · [Project](https://www.cybergym.io/exploitgym/)  
  Evaluates whether agents can extend vulnerability-triggering inputs into working exploits across userspace programs, V8, and the Linux kernel.  
  **Emerging · Benchmark** · `llm` `agent` `binary` `exploit-generation` `dual-use` `real-world` `execution-grounded`

- **Patch-to-PoC: A Systematic Study of Agentic LLM Systems for Linux Kernel N-Day Reproduction**  
  Jiahao Pu et al. *arXiv 2026*.  
  [Paper](https://arxiv.org/abs/2602.07287)  
  Studies whether agents can turn Linux-kernel patches into working n-day proofs of concept.  
  **Emerging · Empirical Study** · `llm` `agent` `exploit-adaptation` `poc-generation` `source-code` `repository` `dual-use` `real-world`

- **Teams of LLM Agents Can Exploit Zero-Day Vulnerabilities**  
  Yuxuan Zhu et al. *EACL 2026*.  
  [Paper](https://aclanthology.org/2026.eacl-long.2/) · [arXiv](https://arxiv.org/abs/2406.01637)  
  Studies coordinated multi-agent exploitation of previously unseen vulnerabilities in sandboxed systems.  
  **Emerging · Empirical Study** · `llm` `agent` `exploit-chaining` `automated-penetration-testing` `web` `offensive` `execution-grounded`

- **Towards Effective Offensive Security LLM Agents: Hyperparameter Tuning, LLM as a Judge, and a Lightweight CTF Benchmark**  
  Minghao Shao et al. *AAAI 2026*.  
  [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/40210) · [arXiv](https://arxiv.org/abs/2508.05674) · [Code](https://github.com/NYU-LLM-CTF/CTFTiny)  
  Introduces CTFTiny, CTFJudge, and the CTF Competency Index for low-cost, fine-grained evaluation of offensive-security agents across fifty CTF challenges.  
  **Emerging · Benchmark** · `llm` `agent` `multi-agent` `ctf-solving` `attack-planning` `binary` `web` `cryptography` `offensive` `ctf-style` `model-graded`

- **Training Language Model Agents to Find Vulnerabilities with CTF-Dojo**  
  Terry Yue Zhuo et al. *ICML 2026*.  
  [Paper](https://icml.cc/virtual/2026/poster/61783) · [arXiv](https://arxiv.org/abs/2508.18370)  
  Provides an interactive CTF environment and training recipe for agents that learn from executable security feedback.  
  **Emerging · Benchmark** · `llm` `agent` `reinforcement-learning` `ctf-solving` `vulnerability-detection` `binary` `web` `source-code`

- **CVE-Bench: A Benchmark for AI Agents' Ability to Exploit Real-World Web Application Vulnerabilities**  
  Yuxuan Zhu et al. *ICML 2025 Spotlight*.  
  [Paper](https://proceedings.mlr.press/v267/zhu25i.html) · [Code](https://github.com/uiuc-kang-lab/cve-bench)  
  Provides reproducible sandboxes and automatic outcome checks for forty critical-severity web CVEs under zero-day and one-day information settings.  
  **Essential · Benchmark** · `llm` `agent` `web` `web-exploitation` `offensive` `real-world` `execution-grounded`

- **Cybench: A Framework for Evaluating Cybersecurity Capabilities and Risks of Language Models**  
  Andy K. Zhang et al. *ICLR 2025 Oral*.  
  [Paper](https://openreview.net/forum?id=c9OLV0yRL) · [arXiv](https://arxiv.org/abs/2408.08926) · [Code](https://github.com/andyzorigin/cybench) · [Project](https://cybench.github.io/)  
  Evaluates agents on forty professional CTF tasks from four recent competitions and adds expert-written subtasks for measuring partial progress on unsolved challenges.  
  **Essential · Benchmark** · `llm` `agent` `ctf-solving` `offensive` `ctf-style` `execution-grounded`

- **Dynamic Risk Assessments for Offensive Cybersecurity Agents**  
  Boyi Wei et al. *NeurIPS 2025 Datasets and Benchmarks*.  
  [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/4bc29e0822458441dc0ada00d1f53d3e-Abstract-Datasets_and_Benchmarks_Track.html)  
  Shows how offensive-agent risk estimates change under adversarial improvement and additional inference-time compute on InterCode CTF.  
  **Recommended · Empirical Study** · `llm` `agent` `ctf-solving` `attack-planning` `adaptive-adversary` `execution-grounded`

- **EnIGMA: Interactive Tools Substantially Assist LM Agents in Finding Security Vulnerabilities**  
  Talor Abramovich et al. *ICML 2025*.  
  [Paper](https://proceedings.mlr.press/v267/abramovich25a.html) · [arXiv](https://arxiv.org/abs/2409.16165) · [Project](https://enigma-agent.com/)  
  Shows that LM-friendly terminal interfaces, interactive debugger and connection tools, and output summarization materially improve agent performance across 390 CTF challenges.  
  **Essential · System** · `llm` `agent` `ctf-solving` `offensive` `ctf-style` `execution-grounded`

- **From Capabilities to Performance: Evaluating Key Functional Properties of LLM Architectures in Penetration Testing**  
  Lanxiao Huang et al. *EMNLP 2025*.  
  [Paper](https://aclanthology.org/2025.emnlp-main.802/)  
  Isolates how memory, coordination, tool selection, planning, and monitoring affect singular and modular penetration-testing agents.  
  **Recommended · Empirical Study** · `llm` `agent` `multi-agent` `automated-penetration-testing` `attack-planning` `execution-grounded`

- **Measuring and Augmenting Large Language Models for Solving Capture-the-Flag Challenges**  
  Zimo Ji et al. *ACM CCS 2025*.  
  [Paper](https://dl.acm.org/doi/10.1145/3719027.3744855)  
  Measures LLM performance on capture-the-flag challenges and studies augmentations that improve tool-assisted solution workflows.  
  **Recommended · Empirical Study** · `llm` `agent` `ctf-solving` `attack-planning` `execution-grounded`

- **A Preliminary Study on Using Large Language Models in Software Pentesting**  
  Kumar Shashwat et al. *WoS-CaD 2024*.  
  [Paper](https://doi.org/10.14722/wosoc.2024.23002)  
  Empirically probes how LLMs plan and execute multi-step software penetration-testing workflows.  
  **Emerging · Empirical Study** · `llm` `agent` `automated-penetration-testing` `attack-planning` `web` `host` `offensive` `execution-grounded`

- **LLM Agents Can Autonomously Exploit One-Day Vulnerabilities**  
  Richard Fang et al. *arXiv 2024*.  
  [Paper](https://arxiv.org/abs/2404.08144)  
  Measures autonomous exploitation when agents receive vulnerability descriptions for recently disclosed flaws.  
  **Emerging · Empirical Study** · `llm` `agent` `exploit-adaptation` `automated-penetration-testing` `web` `offensive` `execution-grounded` `synthetic`

- **LLM Agents Can Autonomously Hack Websites**  
  Richard Fang et al. *arXiv 2024*.  
  [Paper](https://arxiv.org/abs/2402.06664)  
  Provides an early execution-grounded evaluation of autonomous LLM agents attacking vulnerable web applications.  
  **Emerging · Empirical Study** · `llm` `agent` `web-exploitation` `automated-penetration-testing` `web` `offensive` `execution-grounded` `synthetic`

- **NYU CTF Bench: A Scalable Open-Source Benchmark Dataset for Evaluating LLMs in Offensive Security**  
  Minghao Shao et al. *NeurIPS 2024 Datasets and Benchmarks*.  
  [Paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/69d97a6493fbf016fff0a751f253ad18-Abstract-Datasets_and_Benchmarks_Track.html) · [Code](https://github.com/NYU-LLM-CTF/NYU_CTF_Bench)  
  Provides 200 validated CSAW CTF challenges across six categories and an automated tool-using evaluation framework.  
  **Essential · Benchmark** · `llm` `agent` `ctf-solving` `offensive` `ctf-style` `execution-grounded`

- **PentestGPT: Evaluating and Harnessing Large Language Models for Automated Penetration Testing**  
  Gelei Deng et al. *USENIX Security 2024, Distinguished Artifact Award*.  
  [Paper](https://www.usenix.org/conference/usenixsecurity24/presentation/deng) · [Code](https://github.com/GreyDGL/PentestGPT)  
  Introduces a penetration-testing task tree and a modular LLM system that separates reasoning, command generation, and output parsing to reduce context loss during long workflows.  
  **Essential · System** · `llm` `agent` `automated-penetration-testing` `offensive` `ctf-style` `execution-grounded`

### Remediation and Secure Software Engineering

Papers in this section use AI to generate, validate, or prioritize security patches and to improve secure software development.

- **AutoBaxBuilder: Bootstrapping Code Security Benchmarking**  
  Tobias von Arx et al. *ICML 2026*.  
  [Paper](https://icml.cc/virtual/2026/poster/64856)  
  Automates construction of code-security tasks with functional tests and executable exploits while reducing benchmark contamination.  
  **Emerging · Benchmark** · `llm` `agent` `secure-code-generation` `vulnerability-detection` `execution-grounded`

- **GoodVibe: Security-by-Vibe for LLM-Based Code Generation**  
  Maximilian Thang et al. *USENIX Security 2026*.  
  [Paper](https://www.usenix.org/conference/usenixsecurity26/presentation/thang)  
  Uses neuron attribution and selective fine-tuning to improve secure code generation across C++, Java, Swift, and Go.  
  **Emerging · Method** · `llm` `secure-code-generation` `security-code-review` `source-code` `unit-tested`

- **Is Vibe Coding Safe? Benchmarking Vulnerability of Agent-Generated Code in Real-World Tasks**  
  Songwen Zhao et al. *ICML 2026*.  
  [Paper](https://icml.cc/virtual/2026/poster/61427) · [Code](https://github.com/LeiLiLab/susvibes) · [Leaderboard](https://leililab.github.io/susvibes-leaderboard)  
  Jointly evaluates functionality and security on 186 real feature-request tasks with vulnerable human implementations.  
  **Emerging · Benchmark** · `llm` `agent` `secure-code-generation` `vulnerability-detection` `repository-scale`

- **Kintsugi: Empowering LLMs to Mitigate Web Vulnerabilities via Runtime Policy Injection**  
  Yihao Peng et al. *USENIX Security 2026*.  
  [Paper](https://www.usenix.org/conference/usenixsecurity26/presentation/peng-yihao)  
  Uses LLM-localized vulnerable code and differential syscall analysis to inject temporary least-privilege containment policies.  
  **Emerging · System** · `llm` `patch-generation` `patch-validation` `security-specification` `web` `execution-grounded`

- **PORTGPT: Towards Automated Backporting Using Large Language Models**  
  Zhaoyang Li et al. *IEEE S&P 2026*.  
  [Paper](https://arxiv.org/abs/2510.22396) · [Code](https://github.com/OS3Lab/patch-backporting)  
  Builds a tool-using agent that backports security patches using repository history and compiler feedback, including nine patches merged into Linux.  
  **Emerging · System** · `llm` `agent` `patch-generation` `patch-validation` `repository` `real-world` `execution-grounded`

- **SecCodePRM: A Process Reward Model for Code Security**  
  Weichen Yu et al. *ICML 2026*.  
  [Paper](https://icml.cc/virtual/2026/poster/64014)  
  Introduces step-level process rewards for identifying insecure reasoning trajectories and improving secure code generation.  
  **Emerging · Method** · `llm` `reinforcement-learning` `secure-code-generation` `security-code-review` `source-code`

- **SecPI: Secure Code Generation with Reasoning Models via Security Reasoning Internalization**  
  Hao Wang et al. *arXiv 2026*.  
  [Paper](https://arxiv.org/abs/2604.03587) · [Code](https://github.com/moogician/SecPI)  
  Fine-tunes reasoning models to internalize structured security analysis and generate safer code without requiring security instructions at inference time.  
  **Emerging · Method** · `llm` `secure-code-generation` `security-code-review` `source-code` `unit-tested` `execution-grounded`

- **APPATCH: Automated Adaptive Prompting Large Language Models for Real-World Software Vulnerability Patching**  
  Yu Nong et al. *USENIX Security 2025*.  
  [Paper](https://www.usenix.org/conference/usenixsecurity25/presentation/nong)  
  Combines semantics-aware scoping, adaptive exemplar selection, and cross-model validation to patch real vulnerabilities without requiring an exploit input or model fine-tuning.  
  **Recommended · System** · `llm` `source-code` `patch-generation` `real-world`

- **BaxBench: Can LLMs Generate Correct and Secure Backends?**  
  Mark Vero et al. *ICML 2025*.  
  [Paper](https://proceedings.mlr.press/v267/vero25a.html) · [Preprint](https://arxiv.org/abs/2502.11844) · [Code](https://github.com/logic-star-ai/baxbench) · [Dataset](https://huggingface.co/datasets/LogicStar/BaxBench) · [Leaderboard](https://baxbench.com/)  
  Evaluates secure backend generation across 392 tasks using comprehensive functional tests and executable end-to-end security exploits.  
  **Essential · Benchmark** · `llm` `secure-code-generation` `source-code` `web` `unit-tested` `execution-grounded`

- **BountyBench: Dollar Impact of AI Agent Attackers and Defenders on Real-World Cybersecurity Systems**  
  Andy Zhang et al. *NeurIPS 2025 Datasets and Benchmarks*.  
  [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/faed4276b52ef762879db4142655c699-Abstract-Datasets_and_Benchmarks_Track.html) · [Code](https://github.com/bountybench/bountybench)  
  Measures Detect, Exploit, and Patch capabilities on forty real bug bounties in twenty-five deployable systems and reports their historical dollar impact.  
  **Essential · Benchmark** · `llm` `agent` `vulnerability-detection` `exploit-generation` `patch-generation` `dual-use` `real-world` `execution-grounded`

- **Give LLMs a Security Course: Securing Retrieval-Augmented Code Generation via Knowledge Injection**  
  Bo Lin et al. *ACM CCS 2025*.  
  [Paper](https://dl.acm.org/doi/10.1145/3719027.3765049)  
  Injects security knowledge into retrieval-augmented code generation to reduce vulnerable outputs while retaining functional quality.  
  **Recommended · Method** · `llm` `retrieval-augmented` `secure-code-generation` `security-code-review` `source-code`

- **PATCHAGENT: A Practical Program Repair Agent Mimicking Human Expertise**  
  Zheng Yu et al. *USENIX Security 2025*.  
  [Paper](https://www.usenix.org/conference/usenixsecurity25/presentation/yu-zheng)  
  Integrates fault localization, patch generation, building, PoC validation, and regression testing in a tool-using repair agent evaluated on 178 real-world vulnerabilities.  
  **Essential · System** · `llm` `agent` `source-code` `patch-generation` `patch-validation` `real-world` `execution-grounded`

- **PurpCode: Reasoning for Safer Code Generation**  
  Jiawei Liu et al. *NeurIPS 2025*.  
  [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/4f697305ef1f868ad77c3c0027989a6f-Abstract-Conference.html)  
  Trains code models to reason over security rules and produce safer implementations while preserving general coding utility.  
  **Recommended · Method** · `llm` `reinforcement-learning` `secure-code-generation` `security-code-review` `unit-tested`

- **SECODEPLT: A Unified Benchmark for Evaluating the Security Risks and Capabilities of Code GenAI**  
  Yuzhou Nie et al. *NeurIPS 2025 Datasets and Benchmarks*.  
  [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/13d0a982aae786d473f6949b734e2720-Abstract-Datasets_and_Benchmarks_Track.html) · [Code](https://github.com/ucsb-mlsec/SeCodePLT) · [Dataset](https://huggingface.co/datasets/UCSB-SURFI/SeCodePLT)  
  Unifies insecure code generation, vulnerability detection, and patch generation with dynamic security artifacts across four languages.  
  **Recommended · Benchmark** · `llm` `secure-code-generation` `vulnerability-detection` `patch-generation` `execution-grounded`

- **A Case Study of LLM for Automated Vulnerability Repair: Assessing Impact of Reasoning and Patch Validation Feedback**  
  Ummay Kulsum et al. *AIware 2024*.  
  [Paper](https://doi.org/10.1145/3664646.3664770)  
  Combines LLM patch generation with program analysis and iterative validation for real vulnerabilities.  
  **Recommended · System** · `llm` `agent` `patch-generation` `patch-validation` `program-repair` `source-code` `defensive` `execution-grounded`

- **SecCoder: Towards Generalizable and Robust Secure Code Generation**  
  Boyu Zhang et al. *EMNLP 2024*.  
  [Paper](https://aclanthology.org/2024.emnlp-main.806/)  
  Trains code models to generate secure implementations that generalize across weakness patterns and prompts.  
  **Recommended · Method** · `llm` `secure-code-generation` `security-code-review` `source-code` `defensive` `static`

- **InferFix: End-to-End Program Repair with LLMs**  
  Matthew Jin et al. *ESEC/FSE 2023*.  
  [Paper](https://doi.org/10.1145/3611643.3613892)  
  Combines retrieval and a repair model to generate fixes for real-world defects and security vulnerabilities.  
  **Recommended · System** · `llm` `program-repair` `patch-generation` `source-code` `defensive` `real-world` `execution-grounded`

- **Neural Transfer Learning for Repairing Security Vulnerabilities in C Code**  
  Zimin Chen, Steve Kommrusch, and Martin Monperrus. *IEEE Transactions on Software Engineering 2023*.  
  [Paper](https://doi.org/10.1109/TSE.2022.3147265) · [arXiv](https://arxiv.org/abs/2104.08308) · [Code](https://github.com/ASSERT-KTH/VRepair)  
  Introduces VRepair, which transfers knowledge from a large bug-fix corpus to the smaller-data problem of generating security patches for C vulnerabilities.  
  **Recommended · Method** · `deep-learning` `language-model` `source-code` `patch-generation` `program-repair`

- **VulRepair: A T5-Based Automated Software Vulnerability Repair**  
  Michael C. Fu et al. *ESEC/FSE 2022*.  
  [Paper](https://doi.org/10.1145/3540250.3549098)  
  Fine-tunes T5 for vulnerability repair and evaluates exact and semantically equivalent fixes on real patches.  
  **Recommended · Method** · `language-model` `patch-generation` `program-repair` `source-code` `defensive` `real-world` `execution-grounded`

### Malware and Unwanted Software

Papers in this section use AI to detect, classify, attribute, understand, or explain malware and other unwanted software.

- **Beyond the TESSERACT: Trustworthy Dataset Curation for Sound Evaluations of Android Malware Classifiers**  
  Theo Chow et al. *IEEE SaTML 2026*.  
  [Paper](https://satml.org/2026/program/)  
  Identifies five overlooked dataset-curation factors that materially change evaluations of learning-based Android malware classifiers.  
  **Emerging · Empirical Study** · `classical-ml` `deep-learning` `malware-detection` `malware-classification` `mobile` `temporal`

- **MalTree: Tracing Malware Evolution using Embeddings at Scale**  
  Akash Amalan, Georgios Smaragdakis, and Tom Viering. *ICML 2026*.  
  [Paper](https://icml.cc/virtual/2026/poster/64032)  
  Builds phylogeny-inspired malware evolution trees from structural, behavioral, and image embeddings at a scale exceeding 100,000 samples.  
  **Emerging · Method** · `deep-learning` `representation-learning` `family-attribution` `behavior-analysis` `binary` `temporal`

- **Threat2Traffic: Multi-Agent Environment Synthesis for Malware Traffic Generation from Threat Intelligence**  
  Haoyang Chen et al. *ICML 2026*.  
  [Paper](https://icml.cc/virtual/2026/poster/64510) · [Code](https://github.com/apos3637/Threat2Traffic)  
  Synthesizes malware execution environments from threat reports to reproduce network traffic for eight malware families.  
  **Emerging · System** · `llm` `multi-agent` `sandbox-analysis` `traffic-classification` `threat-intelligence` `execution-grounded`

- **Beyond Raw Bytes: Towards Large Malware Language Models**  
  Luke Kurlandski et al. *NDSS 2025*.  
  [Paper](https://www.ndss-symposium.org/ndss-paper/beyond-raw-bytes-towards-large-malware-language-models/)  
  Pretrains large language-style models over semantically structured malware representations rather than raw bytes alone.  
  **Recommended · Method** · `language-model` `representation-learning` `malware-detection` `malware-classification` `binary` `defensive` `real-world`

- **FlowMalTrans: Unsupervised Binary Code Translation for Malware Detection Using Flow-Adapter Architecture**  
  Minghao Hu et al. *Findings of EMNLP 2025*.  
  [Paper](https://aclanthology.org/2025.findings-emnlp.173/)  
  Translates binary representations across instruction-set architectures so a malware detector trained on one architecture can transfer to another.  
  **Recommended · Method** · `deep-learning` `unsupervised-learning` `malware-detection` `binary` `iot`

- **MOTIF: A Malware Reference Dataset with Ground Truth Family Labels**  
  Robert J. Joyce et al. *Computers & Security 2022*.  
  [Paper](https://doi.org/10.1016/j.cose.2022.102921)  
  Provides expert-vetted malware-family labels to reduce noise in family-classification evaluation.  
  **Recommended · Dataset** · `classical-ml` `deep-learning` `family-attribution` `malware-classification` `binary` `defensive` `real-world`

- **Neurlux: Dynamic Malware Analysis without Feature Engineering**  
  Chani Jindal et al. *ACSAC 2021*.  
  [Paper](https://arxiv.org/abs/1910.11376)  
  Learns directly from tokenized sandbox reports for dynamic malware detection without hand-engineered features.  
  **Recommended · Method** · `language-model` `deep-learning` `behavior-analysis` `malware-detection` `binary` `security-telemetry` `defensive` `real-world`

- **SOREL-20M: A Large Scale Benchmark Dataset for Malicious PE Detection**  
  Richard Harang and Ethan M. Rudd. *arXiv 2020*.  
  [Paper](https://arxiv.org/abs/2012.07634) · [Code and Data](https://github.com/sophos/SOREL-20M)  
  Releases metadata, labels, behavioral tags, features, and baselines for twenty million Windows PE files, with disarmed malware binaries available under controlled terms.  
  **Recommended · Dataset** · `classical-ml` `deep-learning` `binary` `malware-detection` `real-world`

- **EMBER: An Open Dataset for Training Static PE Malware Machine Learning Models**  
  Hyrum S. Anderson and Phil Roth. *arXiv 2018*.  
  [Paper](https://arxiv.org/abs/1804.04637)  
  Releases a standard feature set, labels, and baseline for reproducible static Windows PE malware detection.  
  **Essential · Dataset** · `classical-ml` `malware-detection` `malware-classification` `binary` `defensive` `real-world`

- **Malware Detection by Eating a Whole EXE**  
  Edward Raff et al. *AAAI 2018 Workshop on Artificial Intelligence for Cyber Security*.  
  [Paper](https://cdn.aaai.org/ocs/ws/ws0432/16422-75958-1-PB.pdf)  
  Introduces MalConv and frames end-to-end learning directly from multi-million-byte Windows executables as a practical sequence-modeling problem.  
  **Essential · Method** · `deep-learning` `binary` `malware-detection` `static`

- **MaMaDroid: Detecting Android Malware by Building Markov Chains of Behavioral Models**  
  Enrico Mariconti et al. *NDSS 2017*.  
  [Paper](https://www.ndss-symposium.org/ndss2017/ndss-2017-programme/mamadroid-detecting-android-malware-building-markov-chains-behavioral-models/)  
  Models Android API-call abstractions as Markov chains for behavioral malware detection resilient to API evolution.  
  **Essential · System** · `classical-ml` `mobile-malware` `malware-detection` `behavior-analysis` `mobile` `bytecode` `defensive` `real-world`

- **Transcend: Detecting Concept Drift in Malware Classification Models**  
  Roberto Jordaney et al. *USENIX Security 2017*.  
  [Paper](https://www.usenix.org/conference/usenixsecurity17/technical-sessions/presentation/jordaney)  
  Uses conformal evaluation to identify when evolving malware distributions make a classifier unreliable.  
  **Essential · Method** · `classical-ml` `malware-detection` `binary` `defensive` `real-world` `temporal`

- **DREBIN: Effective and Explainable Detection of Android Malware in Your Pocket**  
  Daniel Arp et al. *NDSS 2014*.  
  [Paper](https://www.ndss-symposium.org/ndss2014/programme/drebin-effective-and-explainable-detection-android-malware-your-pocket/)  
  Introduces lightweight and explainable on-device Android malware detection over broad static features.  
  **Essential · System** · `classical-ml` `mobile-malware` `malware-detection` `mobile` `bytecode` `defensive` `real-world` `static`

### Network, Host, and Infrastructure Defense

Papers in this section apply AI to defensive analysis of network traffic, system logs, host activity, provenance, cloud systems, and other operational telemetry.

- **ConCap: Practical Network Traffic Generation for (ML- and) Flow-based Intrusion Detection Systems**  
  Miel Verkerken et al. *IEEE SaTML 2026*.  
  [Paper](https://satml.org/2026/program/)  
  Generates automatically labeled packets and flows in a configurable isolated network for reproducible intrusion-detection experiments.  
  **Emerging · System** · `classical-ml` `deep-learning` `intrusion-detection` `traffic-classification` `network` `real-world`

- **Cloak, Honey, Trap: Proactive Defenses Against LLM Agents**  
  Daniel Ayzenshteyn, Roy Weiss, and Yisroel Mirsky. *USENIX Security 2025*.  
  [Paper](https://www.usenix.org/conference/usenixsecurity25/presentation/ayzenshteyn) · [PDF](https://www.usenix.org/system/files/usenixsecurity25-ayzenshteyn.pdf) · [Code](https://github.com/Daniel-Ayz/CHeaT)  
  Introduces six strategies and fifteen techniques for detecting, delaying, and stopping LLM-powered attack agents through cloaking, honeytokens, traps, and deception, with an open-source implementation evaluated on CTF machines.  
  **Essential · System** · `llm` `agent` `defensive` `autonomous-ai-agent` `cyber-deception` `honeypot-and-honeytoken` `ctf-style` `execution-grounded`

- **Self-Supervised Learning of Graph Representations for Network Intrusion Detection**  
  Lorenzo Guerra et al. *NeurIPS 2025*.  
  [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/9ddb13ae9150f99298065d889f951014-Abstract-Conference.html)  
  Uses masked self-supervised graph representation learning to model flow context for network intrusion detection.  
  **Recommended · Method** · `graph-learning` `representation-learning` `unsupervised-learning` `intrusion-detection` `network`

- **DeepCASE: Semi-Supervised Contextual Analysis of Security Events**  
  Thijs van Ede et al. *IEEE S&P 2022*.  
  [Paper](https://doi.org/10.1109/SP46214.2022.9833671)  
  Learns contextual event sequences and analyst feedback to prioritize large volumes of security events.  
  **Essential · System** · `deep-learning` `semi-supervised-learning` `log-analysis` `alert-triage` `host` `security-telemetry` `defensive` `real-world`

- **ET-BERT: A Contextualized Datagram Representation with Pre-Training Transformers for Encrypted Traffic Classification**  
  Xinjie Lin et al. *The Web Conference 2022*.  
  [Paper](https://doi.org/10.1145/3485447.3512217)  
  Pretrains contextual datagram representations for encrypted-traffic classification with limited labels.  
  **Essential · Method** · `language-model` `representation-learning` `traffic-classification` `intrusion-detection` `network` `defensive` `real-world`

- **ShadeWatcher: Recommendation-Guided Cyber Threat Analysis Using System Audit Records**  
  Jun Zeng et al. *IEEE S&P 2022*.  
  [Paper](https://doi.org/10.1109/SP46214.2022.9833669)  
  Frames provenance-based threat analysis as recommendation over audit-record entities and behaviors.  
  **Essential · System** · `graph-learning` `representation-learning` `host-based-detection` `threat-hunting` `host` `security-telemetry` `defensive` `real-world`

- **UNICORN: Runtime Provenance-Based Detector for Advanced Persistent Threats**  
  Xueyuan Han et al. *NDSS 2020*.  
  [Paper](https://www.ndss-symposium.org/ndss-paper/unicorn-runtime-provenance-based-detector-for-advanced-persistent-threats/)  
  Builds streaming graph sketches of system provenance to detect long-running advanced persistent threats.  
  **Essential · System** · `graph-learning` `streaming-learning` `host-based-detection` `threat-hunting` `host` `security-telemetry` `defensive` `real-world`

- **Kitsune: An Ensemble of Autoencoders for Online Network Intrusion Detection**  
  Yisroel Mirsky et al. *NDSS 2018*.  
  [Paper](https://www.ndss-symposium.org/ndss2018/accepted-papers/) · [PDF](https://www.ndss-symposium.org/wp-content/uploads/2018/02/ndss2018_03A-3_Mirsky_paper.pdf) · [Code](https://github.com/ymirsky/Kitsune-py)  
  Uses an ensemble of small autoencoders for unsupervised, online network anomaly detection that can train and run on resource-constrained gateways.  
  **Essential · System** · `deep-learning` `network` `intrusion-detection` `network-anomaly-detection` `real-world`

- **DeepLog: Anomaly Detection and Diagnosis from System Logs through Deep Learning**  
  Min Du and Feifei Li. *ACM CCS 2017*.  
  [Paper](https://doi.org/10.1145/3133956.3134015)  
  Models log-key sequences with recurrent networks for online anomaly detection and workflow diagnosis.  
  **Essential · Method** · `deep-learning` `language-model` `log-analysis` `network-anomaly-detection` `host` `security-telemetry` `defensive` `real-world`

- **BotMiner: Clustering Analysis of Network Traffic for Protocol- and Structure-Independent Botnet Detection**  
  Guofei Gu et al. *USENIX Security 2008*.  
  [Paper](https://www.usenix.org/legacy/event/sec08/tech/full_papers/gu/gu.pdf)  
  Correlates communication and malicious-activity clusters to detect botnets independently of protocol structure.  
  **Essential · System** · `unsupervised-learning` `classical-ml` `botnet-detection` `traffic-classification` `network` `defensive` `real-world`

- **BotSniffer: Detecting Botnet Command and Control Channels in Network Traffic**  
  Guofei Gu, Junjie Zhang, and Wenke Lee. *NDSS 2008*.  
  [Paper](https://www.ndss-symposium.org/ndss2008/botsniffer-detecting-botnet-command-and-control-channels-in-network-traffic/)  
  Detects botnet command-and-control channels through spatial-temporal correlation in network behavior.  
  **Essential · System** · `classical-ml` `botnet-detection` `traffic-classification` `network` `defensive` `real-world`

### Social Engineering, Identity, and Abuse

Papers in this section analyze or detect phishing, malicious services, credential abuse, impersonation, fraud, and other attacks on people or online trust.

- **When LLMs Go Online: The Emerging Threat of Web-Enabled LLMs**  
  Hanna Kim et al. *USENIX Security 2025*.  
  [Paper](https://www.usenix.org/conference/usenixsecurity25/presentation/kim-hanna)  
  Studies malicious web-enabled LLM services and the risks created when models can browse and act online.  
  **Recommended · Empirical Study** · `llm` `agent` `online-abuse` `social-engineering` `web` `offensive` `real-world`

- **KnowPhish: Large Language Models Meet Multimodal Knowledge Graphs for Enhancing Reference-Based Phishing Detection**  
  Yuexin Li et al. *USENIX Security 2024*.  
  [Paper](https://www.usenix.org/conference/usenixsecurity24/presentation/li-yuexin)  
  Builds a multimodal knowledge base covering twenty thousand brands and uses an LLM to extract textual brand evidence, extending reference-based detectors beyond logo-only pages.  
  **Recommended · System** · `llm` `multimodal-model` `security-knowledge-graph` `web` `phishing-detection` `real-world`

- **Malla: Demystifying Real-World Large Language Model Integrated Malicious Services**  
  Zilong Lin et al. *USENIX Security 2024*.  
  [Paper](https://www.usenix.org/conference/usenixsecurity24/presentation/lin-zilong)  
  Measures how underground services operationalize LLMs for phishing, malware, and other malicious content.  
  **Essential · Empirical Study** · `llm` `online-abuse` `phishing-generation` `social-engineering` `web` `email` `offensive` `real-world`

- **Inferring Phishing Intention via Webpage Appearance and Dynamics: A Deep Vision Based Approach**  
  Ruofan Liu et al. *USENIX Security 2022*.  
  [Paper](https://www.usenix.org/conference/usenixsecurity22/presentation/liu-ruofan)  
  Combines visual brand recognition with active webpage interaction to infer credential-stealing intent.  
  **Essential · System** · `computer-vision` `deep-learning` `phishing-detection` `web` `defensive` `real-world` `execution-grounded`

- **Phishpedia: A Hybrid Deep Learning Based Approach to Visually Identify Phishing Webpages**  
  Yun Lin et al. *USENIX Security 2021*.  
  [Paper](https://www.usenix.org/conference/usenixsecurity21/presentation/lin) · [Code](https://github.com/lindsey98/Phishpedia)  
  Combines logo detection with Siamese similarity matching to identify the impersonated brand and provide a visual explanation without training on phishing samples.  
  **Essential · System** · `deep-learning` `multimodal-model` `web` `phishing-detection` `real-world`

- **URLNet: Learning a URL Representation with Deep Learning for Malicious URL Detection**  
  Hung Le et al. *arXiv 2018*.  
  [Paper](https://arxiv.org/abs/1802.03162)  
  Learns character- and word-level URL representations for scalable malicious-link detection.  
  **Essential · Method** · `deep-learning` `representation-learning` `malicious-url-detection` `phishing-detection` `web` `defensive` `real-world`

### Threat Intelligence, SOC, and Incident Response

Papers in this section help analysts extract threat intelligence, map adversary behavior, triage security events, hunt threats, investigate incidents, or coordinate response.

- **CTIConnect: A Benchmark for Retrieval-Augmented LLMs over Heterogeneous Cyber Threat Intelligence**  
  Yutong Cheng et al. *ACM SIGKDD 2026*.  
  [Paper](https://arxiv.org/abs/2510.11974) · [Code](https://github.com/peng-gao-lab/CTIConnect) · [Dataset](https://github.com/peng-gao-lab/CTIConnect/tree/main/data) · [Project](https://cticonnect.github.io/)  
  Evaluates retrieval and reasoning across 1,859 expert-verified questions, nine tasks, and five heterogeneous cyber-threat-intelligence sources.  
  **Emerging · Benchmark** · `llm` `retrieval-augmented` `threat-intelligence` `attack-technique-mapping` `curated-real-data` `temporal`

- **LLMs in the SOC: An Empirical Study of Human-AI Collaboration in Security Operations Centres**  
  Ronal Singh et al. *IEEE S&P 2026*.  
  [Paper](https://arxiv.org/abs/2508.18947)  
  Analyzes 3,090 queries from 45 analysts over ten months to characterize how LLMs are used in an operational security operations center.  
  **Emerging · Empirical Study** · `llm` `soc-assistance` `incident-response` `human-ai-collaboration` `security-telemetry` `defensive` `real-world`

- **RedSage: A Cybersecurity Generalist LLM**  
  Naufal Suryanto et al. *ICLR 2026*.  
  [Paper](https://openreview.net/forum?id=W4FAenIrQ2) · [Preprint](https://arxiv.org/abs/2601.22159)  
  Develops and evaluates a cybersecurity-specialized generalist language model across knowledge, reasoning, threat intelligence, and applied security tasks.  
  **Emerging · Model** · `llm` `security-foundation-model` `threat-intelligence` `security-question-answering` `defensive` `curated-real-data`

- **Toward Cybersecurity-Expert Small Language Models**  
  Matan Levi et al. *ICML 2026*.  
  [Paper](https://icml.cc/virtual/2026/poster/66378)  
  Introduces CyberPal 2.0, a family of compact cybersecurity-specialized language models trained and evaluated for practical expert-level security assistance.  
  **Emerging · Model** · `llm` `small-language-model` `security-foundation-model` `security-question-answering` `defensive` `curated-real-data`

- **TxRay: Agentic Postmortem of Live Blockchain Attacks**  
  Ziyue Wang et al. *SBC 2026*.  
  [Paper](https://arxiv.org/abs/2602.01317) · [Project](https://www.clarahacks.com/research)  
  Reconstructs real DeFi attack lifecycles from seed transactions, derives evidence-backed root causes, and generates self-validating executable proofs of concept.  
  **Emerging · System** · `llm` `agent` `multi-agent` `incident-investigation` `root-cause-analysis` `poc-generation` `blockchain` `dual-use` `execution-grounded`

- **CTINexus: Automatic Cyber Threat Intelligence Knowledge Graph Construction Using Large Language Models**  
  Yutong Cheng et al. *IEEE EuroS&P 2025*.  
  [Paper](https://doi.org/10.1109/EUROSP63326.2025.00057) · [arXiv](https://arxiv.org/abs/2410.21060) · [Code](https://github.com/peng-gao-lab/CTINexus) · [Project](https://ctinexus.github.io/)  
  Uses optimized in-context learning, hierarchical entity alignment, and relation prediction to construct cybersecurity knowledge graphs from unstructured threat reports.  
  **Recommended · System** · `llm` `nlp` `threat-intelligence-extraction` `entity-relation-extraction` `security-knowledge-graph` `curated-real-data`

- **OCR-APT: Reconstructing APT Stories from Audit Logs using Subgraph Anomaly Detection and LLMs**  
  Ahmed Aly, Essam Mansour, and Amr Youssef. *ACM CCS 2025*.  
  [Paper](https://dl.acm.org/doi/10.1145/3719027.3765219)  
  Combines anomalous provenance subgraphs with LLM reasoning to reconstruct coherent advanced-persistent-threat narratives from audit logs.  
  **Recommended · System** · `llm` `graph-learning` `incident-investigation` `threat-hunting` `host` `security-telemetry` `defensive` `real-world`

- **SoK: Automated TTP Extraction from CTI Reports – Are We There Yet?**  
  Marvin Büchel et al. *USENIX Security 2025*.  
  [Paper](https://www.usenix.org/conference/usenixsecurity25/presentation/buechel)  
  Unifies and reevaluates more than forty NLP-based approaches to extracting ATT&CK tactics, techniques, and procedures from threat reports, exposing dataset, ontology, and comparability problems.  
  **Essential · SoK** · `language-model` `llm` `threat-intelligence` `attack-technique-mapping` `real-world`

- **CTIBench: A Benchmark for Evaluating LLMs in Cyber Threat Intelligence**  
  Md Tanvirul Alam et al. *NeurIPS 2024 Datasets and Benchmarks Spotlight*.  
  [Paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/5acd3c628aa1819fbf07c39ef73e7285-Abstract-Datasets_and_Benchmarks_Track.html) · [Code](https://github.com/maveryn/cti-bench) · [Dataset](https://huggingface.co/datasets/AI4Sec/cti-bench)  
  Evaluates CTI knowledge, CWE mapping, CVSS prediction, ATT&CK extraction, and threat-actor attribution rather than generic cybersecurity question answering.  
  **Recommended · Benchmark** · `llm` `threat-intelligence` `attack-technique-mapping` `curated-real-data`

- **ThreatKG: An AI-Powered System for Automated Open-Source Cyber Threat Intelligence Gathering and Management**  
  Peng Gao et al. *LAMPS@ACM CCS 2024*.  
  [Paper](https://doi.org/10.1145/3689217.3690613) · [arXiv](https://arxiv.org/abs/2212.10388)  
  Automates collection of public threat reports, AI-based entity and relation extraction, and continuous integration into an extensible threat knowledge graph.  
  **Recommended · System** · `deep-learning` `nlp` `structured-prediction` `threat-intelligence-extraction` `entity-relation-extraction` `security-knowledge-graph` `real-world`

- **EXTRACTOR: Extracting Attack Behavior from Threat Reports**  
  Kiavash Satvat, Rigel Gjomemo, and V. N. Venkatakrishnan. *EuroS&P 2021*.  
  [Paper](https://doi.org/10.1109/EuroSP51992.2021.00046)  
  Extracts attack behaviors and causal provenance graphs from unstructured threat reports for threat hunting.  
  **Essential · System** · `language-model` `threat-intelligence-extraction` `entity-relation-extraction` `threat-hunting` `threat-intelligence` `security-telemetry` `defensive` `real-world`

- **TTPDrill: Automatic and Accurate Extraction of Threat Actions from Unstructured Text of CTI Sources**  
  Ghaith Husari et al. *ACSAC 2017*.  
  [Paper](https://doi.org/10.1145/3134600.3134646)  
  Introduces ontology-guided NLP for extracting threat actions and mapping them to tactics, techniques, and kill-chain phases.  
  **Essential · System** · `nlp` `classical-ml` `threat-intelligence-extraction` `attack-technique-mapping` `threat-intelligence` `defensive` `real-world`

## Defending Against AI-Enabled Cyber Attacks

This section covers defenses for conventional software, networks, and infrastructure when AI systems or autonomous agents act as attackers or attack tools. It does not cover protecting AI models or agents themselves, which remains outside the scope of this list.

- **Cloak, Honey, Trap: Proactive Defenses Against LLM Agents**  
  Daniel Ayzenshteyn, Roy Weiss, and Yisroel Mirsky. *USENIX Security 2025*.  
  [Paper](https://www.usenix.org/conference/usenixsecurity25/presentation/ayzenshteyn) · [PDF](https://www.usenix.org/system/files/usenixsecurity25-ayzenshteyn.pdf) · [Code](https://github.com/Daniel-Ayz/CHeaT)  
  Introduces six strategies and fifteen techniques for detecting, delaying, and stopping LLM-powered attack agents through cloaking, honeytokens, traps, and deception, with an open-source implementation evaluated on CTF machines.  
  **Essential · System** · `llm` `agent` `defensive` `autonomous-ai-agent` `cyber-deception` `honeypot-and-honeytoken` `ctf-style` `execution-grounded`

## Curation Statement

This section explains the evidence and editorial judgment used to decide which papers belong in the list.

Venue prestige, citation count, GitHub popularity, and social-media attention are useful signals, but none is sufficient on its own. Every entry must have a clear cybersecurity contribution and a documented reason to read it. Community attention is recorded only when it can be linked to an author thread, independent technical discussion, or another verifiable source.

## Contributing

Contributions are highly welcome, especially missing foundational papers, important recent work, corrected publication metadata, and stronger descriptions of a paper's contribution or limitations.

Before submitting, please read the [scope](docs/scope.md), [inclusion criteria](docs/inclusion-criteria.md), and [contribution guidelines](CONTRIBUTING.md). You can propose a paper through the paper-suggestion issue form or open a pull request that updates both the canonical YAML record and its README presentation.

## License and Citation

This repository is available under the [MIT License](LICENSE). If this catalog supports your research, please cite the repository using the metadata in [CITATION.cff](CITATION.cff).
