# Awesome Swarm Agentic Papers [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

![papers](https://img.shields.io/badge/papers-2187-blue) ![updated](https://img.shields.io/badge/updated-Oct%202026-green) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](#contributing) [![License: CC0](https://img.shields.io/badge/license-CC0-lightgrey.svg)](#license)

A curated list of papers on **multi-agent and swarm agentic systems**: many agents (LLM-based or not) that work together, argue, compete, or are trained as a group. It runs from early game theory, multi-agent systems and swarm intelligence to recent LLM agent societies, and covers **frameworks, orchestration, automated system design, debate, training (RL, fine-tuning, self-play), data synthesis, evaluation, simulation, safety and applications**.

- **2,187 papers** in total. 2,019 of them are from 2022 or later.
- Every paper link and code link was checked. arXiv IDs were checked against arXiv, DOIs against Crossref, other paper pages by loading them, and code links against GitHub.
- Each one-line note on an arXiv paper was written from, or checked against, that paper's abstract. Papers withdrawn on arXiv are left out.
- For arXiv papers, titles and dates come from arXiv. Titles are the current arXiv versions, so a few differ from the name a paper is best known by. Dates are the first arXiv version. Papers that are not on arXiv, or were posted there years after publication, show their publication year instead.
- The list has one page per topic (see [Contents](#contents)), because a single page with every paper would be over 500 KB, which GitHub may not render in full. To search all papers at once, search [`data/papers.yaml`](data/papers.yaml), which is the source for every page.

## Start Here

If you are new to the area, these papers give the shape of the field.

| Paper | Why read it |
|---|---|
| [Particle Swarm Optimization](https://doi.org/10.1109/ICNN.1995.488968) (1995) | A classic swarm-intelligence algorithm. Simple agents share their best positions to search a space. |
| [MADDPG](https://arxiv.org/abs/1706.02275) (2017) / [QMIX](https://arxiv.org/abs/1803.11485) (2018) | Centralized training with decentralized execution, a common pattern in multi-agent RL. |
| [Generative Agents](https://arxiv.org/abs/2304.03442) (2023) | 25 LLM agents with memory and reflection live in a sandbox town and show believable social behaviour. |
| [CAMEL](https://arxiv.org/abs/2303.17760) (2023) | An early role-playing LLM agent framework. Two agents cooperate through inception prompting. |
| [Multiagent Debate](https://arxiv.org/abs/2305.14325) (2023) | Several LLM copies debate over rounds, which improves reasoning and factuality. |
| [AutoGen](https://arxiv.org/abs/2308.08155) (2023) / [MetaGPT](https://arxiv.org/abs/2308.00352) (2023) | Two influential ways to build agent teams: conversation between agents, and SOP-driven assembly lines. |
| [GPTSwarm](https://arxiv.org/abs/2402.16823) (2024) | Treats an agent swarm as a graph whose prompts and connections can be optimized. |
| [Mixture-of-Agents](https://arxiv.org/abs/2406.04692) (2024) | Layers of LLM proposers and aggregators. A simple and strong multi-LLM ensemble. |
| [ADAS](https://arxiv.org/abs/2408.08435) (2024) / [AFlow](https://arxiv.org/abs/2410.10762) (2024) | Search over agentic systems and workflows instead of designing them by hand. |
| [Multiagent Finetuning](https://arxiv.org/abs/2501.05707) (2025) / [MAPoRL](https://arxiv.org/abs/2502.18439) (2025) | Training a group of LLMs together rather than only prompting them. |
| [Why Do Multi-Agent LLM Systems Fail?](https://arxiv.org/abs/2503.13657) (2025) | A taxonomy of how multi-agent systems break, built from annotated traces. |
| [Multi-Agent Risks from Advanced AI](https://arxiv.org/abs/2502.14143) (2025) | Miscoordination, conflict and collusion as distinct risk classes. |
| [Towards a Science of Scaling Agent Systems](https://arxiv.org/abs/2512.08296) (2025) | Controlled experiments on when adding agents helps and when it hurts. |

## Papers by Year

The table covers 2022 onward. The topic pages also hold 168 earlier papers, going back to 1950.

| Year | Papers |
|---|---|
| 2022 | 24 |
| 2023 | 162 |
| 2024 | 433 |
| 2025 | 834 |
| 2026 | 566 |

## Contents

- [Surveys & Position Papers](papers/surveys-and-position-papers.md) (57)
- [Multi-Agent Systems & Multi-Agent RL](papers/multi-agent-systems-and-multi-agent-rl.md) (201)
  - [Classic Multi-Agent Systems](papers/multi-agent-systems-and-multi-agent-rl.md#classic-multi-agent-systems) (38)
  - [Multi-Agent Reinforcement Learning & Emergent Communication](papers/multi-agent-systems-and-multi-agent-rl.md#multi-agent-reinforcement-learning--emergent-communication) (163)
- [Swarm Intelligence](papers/swarm-intelligence.md) (52)
  - [Classic Swarm Intelligence & Swarm Robotics](papers/swarm-intelligence.md#classic-swarm-intelligence--swarm-robotics) (25)
  - [LLM Agent Swarms & Swarm-Inspired Methods](papers/swarm-intelligence.md#llm-agent-swarms--swarm-inspired-methods) (27)
- [Frameworks & Architectures](papers/frameworks-and-architectures.md) (273)
  - [Multi-Agent Frameworks & Role-Playing](papers/frameworks-and-architectures.md#multi-agent-frameworks--role-playing) (37)
  - [Orchestration, Hierarchies & Agent Swarms](papers/frameworks-and-architectures.md#orchestration-hierarchies--agent-swarms) (75)
  - [Automated Design & Search of Agentic Systems](papers/frameworks-and-architectures.md#automated-design--search-of-agentic-systems) (59)
  - [Communication Topology, Protocols & Latent Communication](papers/frameworks-and-architectures.md#communication-topology-protocols--latent-communication) (72)
  - [Memory & Knowledge Sharing](papers/frameworks-and-architectures.md#memory--knowledge-sharing) (30)
- [Debate & Collaborative Reasoning](papers/debate-and-collaborative-reasoning.md) (229)
  - [Multi-Agent Debate](papers/debate-and-collaborative-reasoning.md#multi-agent-debate) (87)
  - [Debate for Scalable Oversight](papers/debate-and-collaborative-reasoning.md#debate-for-scalable-oversight) (27)
  - [Mixture-of-Agents & Multi-LLM Ensembles](papers/debate-and-collaborative-reasoning.md#mixture-of-agents--multi-llm-ensembles) (48)
  - [Collaborative Reasoning, Role-Play & Theory of Mind](papers/debate-and-collaborative-reasoning.md#collaborative-reasoning-role-play--theory-of-mind) (67)
- [Training Multi-Agent Systems](papers/training-multi-agent-systems.md) (191)
  - [Multi-Agent RL for LLM Agents](papers/training-multi-agent-systems.md#multi-agent-rl-for-llm-agents) (59)
  - [Multi-Agent Fine-Tuning & Self-Improvement](papers/training-multi-agent-systems.md#multi-agent-fine-tuning--self-improvement) (31)
  - [Self-Play, Adversarial Games & Co-Evolution](papers/training-multi-agent-systems.md#self-play-adversarial-games--co-evolution) (74)
  - [Parallel & Concurrent Reasoners](papers/training-multi-agent-systems.md#parallel--concurrent-reasoners) (27)
- [Data Synthesis with Multi-Agent Systems](papers/data-synthesis-with-multi-agent-systems.md) (49)
- [Evaluation](papers/evaluation.md) (196)
  - [Benchmarks & Environments](papers/evaluation.md#benchmarks--environments) (75)
  - [Failure Analysis & Attribution](papers/evaluation.md#failure-analysis--attribution) (47)
  - [Scaling Studies & When Multi-Agent Helps](papers/evaluation.md#scaling-studies--when-multi-agent-helps) (39)
  - [Multi-Agent Judges & Evaluators](papers/evaluation.md#multi-agent-judges--evaluators) (35)
- [Agent Societies & Simulation](papers/agent-societies-and-simulation.md) (390)
  - [Social Simulation](papers/agent-societies-and-simulation.md#social-simulation) (151)
  - [Emergent Behaviour, Conventions & Cooperation](papers/agent-societies-and-simulation.md#emergent-behaviour-conventions--cooperation) (54)
  - [Games](papers/agent-societies-and-simulation.md#games) (73)
  - [Economics, Negotiation & Markets](papers/agent-societies-and-simulation.md#economics-negotiation--markets) (52)
  - [Cooperative AI & Human-Agent Teaming](papers/agent-societies-and-simulation.md#cooperative-ai--human-agent-teaming) (60)
- [Safety & Security](papers/safety-and-security.md) (174)
  - [Attacks](papers/safety-and-security.md#attacks) (51)
  - [Defenses, Monitoring & Resilience](papers/safety-and-security.md#defenses-monitoring--resilience) (46)
  - [Collusion, Steganography & Deception](papers/safety-and-security.md#collusion-steganography--deception) (40)
  - [Risks, Agendas & Governance](papers/safety-and-security.md#risks-agendas--governance) (37)
- [Applications](papers/applications.md) (375)
  - [Software Engineering](papers/applications.md#software-engineering) (64)
  - [Science & Research Automation](papers/applications.md#science--research-automation) (74)
  - [Medicine & Healthcare](papers/applications.md#medicine--healthcare) (54)
  - [Embodied Agents & Robotics](papers/applications.md#embodied-agents--robotics) (61)
  - [Web, GUI, Tools & Deep Research](papers/applications.md#web-gui-tools--deep-research) (27)
  - [Finance, Law, Education & Other Domains](papers/applications.md#finance-law-education--other-domains) (95)

## Contributing

Missing a paper, or found a wrong link or category? Pull requests are welcome.

1. Add or edit an entry in [`data/papers.yaml`](data/papers.yaml). Each entry has these fields:
   - `title`
   - `arxiv` (the arXiv ID), or `url` if the paper is not on arXiv
   - `date`: `YYYY-MM` of the first arXiv version, or `YYYY` (the publication year) if the paper is not on arXiv
   - `authors`: `First et al.`, or `First & Second` for two authors
   - `venue` (optional)
   - `section`: one of the keys in [`scripts/build_readme.py`](scripts/build_readme.py)
   - `note`: one sentence on what the paper does or finds
   - `code` (optional, official repository only)
2. Regenerate the README and the topic pages: `pip install pyyaml && python scripts/build_readme.py`.
3. Open a pull request.

**What belongs here:** papers where several agents (or a population, team or swarm of them) interact, cooperate, compete or are trained together. That includes classic multi-agent systems and multi-agent RL, with or without LLMs. Work on a single model is in scope when the model plays several roles with or against itself (self-play, co-evolution, parallel reasoning threads), or when the work is about building, training or evaluating multi-agent systems.

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the contributors have waived all copyright and related rights to this list.
