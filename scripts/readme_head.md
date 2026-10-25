# Awesome Swarm Agentic Papers [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

![papers](https://img.shields.io/badge/papers-{{N_PAPERS}}-blue) ![updated](https://img.shields.io/badge/updated-Oct%202026-green) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](#contributing) [![License: CC0](https://img.shields.io/badge/license-CC0-lightgrey.svg)](#license)

A curated list of papers on **multi-agent and swarm agentic systems**: many agents (LLM-based or not) that work together, argue, compete, or get trained as a group. It runs from early swarm intelligence and multi-agent RL to recent LLM agent societies, and covers **frameworks, orchestration, automated system design, debate, training (RL, fine-tuning, self-play), data synthesis, evaluation, simulation, safety and applications**.

- **{{N_PAPERS}} papers** in total, {{N_LLM}} of them from 2022 or later.
- Every link was checked. arXiv IDs were checked against arXiv (titles and dates come from arXiv itself), DOIs against Crossref, and code links against GitHub. Each one-line note on an arXiv paper was checked against that paper's abstract.
- Within each section, papers are listed newest first. The date is the first arXiv version (or the publication date if there is no arXiv version). Titles are the current arXiv titles, which are sometimes newer than the name the paper is known by.
- The data lives in [`data/papers.yaml`](data/papers.yaml), and the README is generated from it by [`scripts/build_readme.py`](scripts/build_readme.py).

## Start Here

If you are new to the area, these papers give the shape of the field.

| Paper | Why read it |
|---|---|
| [Particle Swarm Optimization](https://doi.org/10.1109/ICNN.1995.488968) (1995) | The classic swarm-intelligence algorithm. Simple agents share their best positions to search a space. |
| [MADDPG](https://arxiv.org/abs/1706.02275) (2017) / [QMIX](https://arxiv.org/abs/1803.11485) (2018) | Centralized training with decentralized execution, the standard pattern in cooperative multi-agent RL. |
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

## Papers by Year (2022 onward)

{{YEAR_TABLE}}
