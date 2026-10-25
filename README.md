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

## Open Problems: Where the Field Is Stuck

What is actually broken, according to the papers themselves. The full text (not just the abstract) of 102 papers in this list was read, chosen from work by well-known labs and universities such as Google DeepMind, OpenAI, Anthropic, Meta, Microsoft, NVIDIA, Moonshot AI, Stanford, MIT, Berkeley, CMU, Oxford, Cambridge, Princeton, Harvard and Mila, with an emphasis on analysis, failure, scaling, training and safety papers. Every problem a paper showed in its experiments, argued for, or admitted as a limitation was recorded with a quote checked against the paper text (638 in total). The 16 patterns below recur across many of those papers and labs. Each one lists papers whose own results show it.

1. [Adding agents rarely beats one strong agent with the same budget](#1-adding-agents-rarely-beats-one-strong-agent-with-the-same-budget)
2. [Teams cannot pool what each member knows](#2-teams-cannot-pool-what-each-member-knows)
3. [Coordination breaks down as teams grow](#3-coordination-breaks-down-as-teams-grow)
4. [Agreement is not truth — same-model teams herd and overrule the right answer](#4-agreement-is-not-truth--same-model-teams-herd-and-overrule-the-right-answer)
5. [Errors spread because nobody checks](#5-errors-spread-because-nobody-checks)
6. [Nobody can tell which agent broke](#6-nobody-can-tell-which-agent-broke)
7. [Talking in text is expensive](#7-talking-in-text-is-expensive)
8. [Systems are still designed by hand, and automated design does not pay off yet](#8-systems-are-still-designed-by-hand-and-automated-design-does-not-pay-off-yet)
9. [Training agent teams together is still hard](#9-training-agent-teams-together-is-still-hard)
10. [More capable models are not more cooperative](#10-more-capable-models-are-not-more-cooperative)
11. [Agents break with partners they were not trained or tuned with](#11-agents-break-with-partners-they-were-not-trained-or-tuned-with)
12. [Agents collude, cheat and sabotage together, and prompts do not stop it](#12-agents-collude-cheat-and-sabotage-together-and-prompts-do-not-stop-it)
13. [One compromised agent can take over the system, because safety does not compose](#13-one-compromised-agent-can-take-over-the-system-because-safety-does-not-compose)
14. [Oversight weakens as models get stronger](#14-oversight-weakens-as-models-get-stronger)
15. [Agent societies do not yet behave like real people](#15-agent-societies-do-not-yet-behave-like-real-people)
16. [Evaluation hides the failures](#16-evaluation-hides-the-failures)

### 1. Adding agents rarely beats one strong agent with the same budget

Once a single agent gets the same tokens, tools and prompt effort, most multi-agent setups (debate, role pipelines, auto-designed teams) match it or do worse. Many reported gains come from extra compute or weak baselines.

- [Towards a Science of Scaling Agent Systems](https://arxiv.org/abs/2512.08296) (Google Research, Google DeepMind, MIT): mean gain of −0.3% across six agentic benchmarks with matched budgets; returns turn negative once a single agent passes ~45% accuracy.
- [Single-Agent LLMs Outperform Multi-Agent Systems](https://arxiv.org/abs/2604.02460) (Stanford): with equal thinking-token budgets, one agent is best or tied-best against five multi-agent designs on multi-hop QA.
- [The Illusion of Multi-Agent Advantage](https://arxiv.org/abs/2606.13003) (Salesforce): plain chain-of-thought self-consistency beats six automatically designed multi-agent frameworks, often at under 10% of their cost.
- [Stop Overvaluing Multi-Agent Debate](https://arxiv.org/abs/2502.08788) (Penn State, Shanghai AI Lab): debate beats chain-of-thought in at most 20% of 36 model-benchmark settings.
- [LLMs Cannot Self-Correct Reasoning Yet](https://arxiv.org/abs/2310.01798) (Google DeepMind, UIUC): debate 83.0% vs self-consistency 88.2% on GSM8K at 9 responses each.

### 2. Teams cannot pool what each member knows

When information is split across agents, they rarely ask for or share what teammates need, and fail to combine what they gather. The team ends up far below one agent that holds everything.

- [HiddenBench (Systematic Failures in Collective Reasoning)](https://arxiv.org/abs/2505.11556) (CMU): 30.1% accuracy for groups with split information vs 80.7% for one agent with all facts, across 15 LLMs.
- [Silo-Bench](https://arxiv.org/abs/2603.01045) (ETH Zurich, Vector Institute, Zhejiang University): on its harder tasks, splitting the work between just two agents loses 15–49% of single-agent performance; agents gather the data but cannot combine it.
- [CooperBench](https://arxiv.org/abs/2601.13295) (Stanford): two coding agents succeed ~25% of the time, about half the rate of one agent doing both tasks; the top failure cause is misjudging the partner's state (42%).
- [Worse Together](https://arxiv.org/abs/2610.00583) (Stanford, Anthropic): a teammate's request was sent in 94–99% of episodes but was in context when the agent acted in only 47–67%.
- [The Collaboration Gap](https://arxiv.org/abs/2511.02687) (Microsoft Research, EPFL): almost all of 32 models do worse when two copies must share the information than when one model solves the task alone.

### 3. Coordination breaks down as teams grow

Adding agents makes results worse, not better. Messages and idle turns pile up, fewer agents act, and groups fail to agree.

- [AgentsNet](https://arxiv.org/abs/2507.08616) (ETH Zurich, Google Research): coordination success falls to near zero at 100 agents.
- [CooperBench](https://arxiv.org/abs/2601.13295) (Stanford): success drops from 68.6% to 46.5% to 30.0% with 2, 3 and 4 agents.
- [Worse Together](https://arxiv.org/abs/2610.00583) (Stanford, Anthropic): going from 4 to 16 agents, the share of agents that ever act falls from 66% to 10%.
- [Language Model Teams as Distributed Systems](https://arxiv.org/abs/2603.12229) (Princeton, MIT, Cambridge, NYU): self-organizing teams are slower than one agent (median 0.88× speedup); serial tasks cost 5.83× the tokens for a 1.13× speedup.
- [Evaluating Collective Behaviour of Hundreds of LLM Agents](https://arxiv.org/abs/2602.16662) (Google DeepMind, King's College London): welfare efficiency of 57–91% with 4 agents falls to 4–23% with 64.

### 4. Agreement is not truth — same-model teams herd and overrule the right answer

Agents built on the same or similar models share blind spots and defer to the majority. Debate and voting often discard a correct minority answer or lock in a shared bias.

- [Beyond the Strongest LLM](https://arxiv.org/abs/2509.23537) (ASU, UPenn, NTU): in 64% of a four-frontier-model team's errors at least one agent had the right answer; herding onto the first vote rises from 54% to 68%.
- [Talk Isn't Always Cheap](https://arxiv.org/abs/2509.05396) (Johns Hopkins, Vector Institute): debate lowered accuracy on CommonsenseQA in all 10 configurations; agents flip right-to-wrong more often than wrong-to-right.
- [Multi-Agent Teams Hold Experts Back](https://arxiv.org/abs/2602.01011) (Stanford, Apple): teams fall 6.3–41.1% short of their best member, compromising instead of deferring to the expert.
- [Emergence of Biased Consensus](https://arxiv.org/abs/2608.02827) (Harvard, NTT Research): small individual biases lock into a group-wide biased consensus within 1–2 debate rounds.
- [Artificial Hivemind](https://arxiv.org/abs/2510.22954) (UW, CMU, AI2, Stanford): different model families give highly similar open-ended answers (cross-model similarity 0.71–0.82), so mixing models adds little diversity.
- [Great Models Think Alike](https://arxiv.org/abs/2502.04313) (Tübingen AI Center, MPI-IS): across 130 models, more capable models make more similar mistakes.

### 5. Errors spread because nobody checks

Agents accept each other's claims and declare tasks done without verifying them, so one agent's mistake flows straight into the final answer. Where verifier agents exist, their checks are shallow.

- [Towards a Science of Scaling Agent Systems](https://arxiv.org/abs/2512.08296) (Google Research, Google DeepMind, MIT): without a central verifier, independent agents amplify errors 17.2× (4.4× with an orchestrator).
- [Why Do Agent Teams Fail Across Boundaries?](https://arxiv.org/abs/2610.19342) (Salesforce, UNC): zero independent re-checks of a peer's factual claim across 2,500+ runs.
- [Why Do Multi-Agent LLM Systems Fail? (MAST)](https://arxiv.org/abs/2503.13657) (UC Berkeley): 41–86.7% failure rates across 7 open-source multi-agent systems; verifier agents only run shallow checks.
- [Magentic-One](https://arxiv.org/abs/2411.04468) (Microsoft Research): marking tasks complete without verification is its second most common error.
- [Emergent Risks in Generative Multi-Agent Systems](https://arxiv.org/abs/2603.27771) (Notre Dame, LMU Munich, UW): with mixed incentives, 56% of relayed reports were false; meaning drifts as messages pass along chains of agents.

### 6. Nobody can tell which agent broke

Failures come from tangled interactions spread over very long logs. Neither LLM judges nor humans can reliably pin a failure on one agent and one step, which makes debugging and per-agent training hard.

- [Which Agent Causes Task Failures and When?](https://arxiv.org/abs/2505.00212) (Penn State, Duke, UW, Meta): the best method finds the failing agent 53.5% and the failing step 14.2% of the time; near 0% on logs of 93–130 steps.
- [DoVer](https://arxiv.org/abs/2512.06749) (Microsoft, Chinese Academy of Sciences): 14 of 29 benchmark cases had uncertain ground-truth blame; on Who&When only 17.6% of attempted fixes turned a failure into a success.
- [Why Do Multi-Agent LLM Systems Fail? (MAST)](https://arxiv.org/abs/2503.13657) (UC Berkeley): traces average over 15,000 lines; labelling 150 of them took experts more than 20 hours each.
- [COMA](https://arxiv.org/abs/1705.08926) (Oxford): the same problem in classic multi-agent RL: with only a shared team reward, agents cannot tell what they contributed.

### 7. Talking in text is expensive

Agents communicate by writing long natural-language messages to each other, so tokens, latency and dollars multiply with every agent and round, often for a few points of accuracy. This also keeps most studies small.

- [LatentMAS](https://arxiv.org/abs/2511.20639) (Princeton, Stanford, UIUC): a text-based team used ~3× the tokens and ~7× the time of one model for +3.3 points on AIME24.
- [Towards a Science of Scaling Agent Systems](https://arxiv.org/abs/2512.08296) (Google Research, Google DeepMind, MIT): 58–515% token overhead; successes per 1,000 tokens fall from 67.7 to 13.6–42.4.
- [Magentic-One](https://arxiv.org/abs/2411.04468) (Microsoft Research): dozens of LLM calls, several dollars and tens of minutes per task.
- [Worse Together](https://arxiv.org/abs/2610.00583) (Stanford, Anthropic): one pass over 74 scenarios with a frontier-model team took about 3.4 billion tokens.
- [Welfare Diplomacy](https://arxiv.org/abs/2310.08901) (Stanford, UC Berkeley, Oxford): over 3 million tokens per game limited the study to five games per condition.

### 8. Systems are still designed by hand, and automated design does not pay off yet

The number of agents, their roles, prompts and topology are picked by trial and error and transfer poorly between tasks and models. Automated search mostly rediscovers "sample a few times and vote" and rarely recovers its own cost.

- [AutoGen](https://arxiv.org/abs/2308.08155) (Microsoft Research): no general recipe for how many agents, which roles or which interaction pattern; the best design depends on the application.
- [MASS (Multi-Agent Design)](https://arxiv.org/abs/2502.02533) (Google, Cambridge): most topologies fail to improve on one prompt-optimized agent; automated design (ADAS) scored 69.7 vs 70.3 for hand-built debate.
- [Inefficiencies of Meta Agents for Agent Design](https://arxiv.org/abs/2510.06711) (Stanford): automated design beats hand-designed agents on cost per correct answer on only 2 of 4 datasets, and only after ~15,000 queries.
- [The Illusion of Multi-Agent Advantage](https://arxiv.org/abs/2606.13003) (Salesforce): 7 of 14 workflows found by AFlow were just 'repeat one prompt 3 times, then aggregate'.
- [HiddenBench](https://arxiv.org/abs/2505.11556) (CMU): fixes are model-specific: adding a dissenter lifts GPT-4.1 from 0.23 to 0.49 but drops Gemini-2.5-Flash from 0.89 to 0.31.

### 9. Training agent teams together is still hard

Most systems run frozen, prompted models. Joint training is blocked by credit assignment across agents, gradients that cannot pass through text messages, training collapse and compute, so labs train one agent (usually the orchestrator) and freeze the rest.

- [Kimi K2.5 (Agent Swarm)](https://arxiv.org/abs/2602.02276) (Moonshot AI): avoids training orchestrator and subagents together because of credit-assignment ambiguity and instability; the trained orchestrator falls back to a single agent unless spawning subagents is rewarded.
- [MAPoRL](https://arxiv.org/abs/2502.18439) (MIT, Stanford, Amazon): fine-tuning on the best debate transcripts lowered accuracy by 0.11; compute limited co-training to two 3B–8B agents.
- [AgentFlow](https://arxiv.org/abs/2510.05592) (Stanford): supervised fine-tuning of one module collapsed the system (−19.0%); on-policy RL of the planner alone gave +17.2%.
- [SPIRAL](https://arxiv.org/abs/2506.24119) (NUS, A*STAR, Sea AI Lab): without role-specific baselines, multi-agent self-play RL caused 'thinking collapse', with reasoning traces shrinking from ~2,000 characters to near zero.
- [MALT](https://arxiv.org/abs/2412.01928) (Oxford, Cooperative AI Foundation, Stanford): gradients cannot flow through the text agents pass to each other, and a sparse final reward cannot say which agent erred.

### 10. More capable models are not more cooperative

In social dilemmas and shared-resource settings, stronger and reasoning-heavy models often free-ride, defect or withhold help. Cooperation that does emerge is fragile and depends on the model and even the random seed.

- [More Capable, Less Cooperative?](https://arxiv.org/abs/2604.07821) (MATS, UIUC, UK AI Security Institute): when sharing costs nothing, o3 reaches 17% of the optimal team outcome vs 50% for o3-mini.
- [Corrupted by Reasoning](https://arxiv.org/abs/2506.23276) (Zurich, ETH Zurich, Toronto, MPI-IS): 69% of o1-mini agents free-ride in a public-goods game vs 0% for Llama-3.3-70B.
- [GovSim (Cooperate or Collapse)](https://arxiv.org/abs/2404.16698) (ETH Zurich, MPI-IS, Toronto, UW): the best agent group sustains a shared resource in only 53.3% of runs; one greedy newcomer drops this to 33.3%.
- [Cultural Evolution of Cooperation among LLM Agents](https://arxiv.org/abs/2412.10270) (Google DeepMind): GPT-4o populations drift toward defection; even Claude 3.5 Sonnet failed in 2 of 5 runs depending on the initial strategies.
- [Welfare Diplomacy](https://arxiv.org/abs/2310.08901) (Stanford, UC Berkeley, Oxford): a single defector can exploit LLM agents because they do not punish deviators.

### 11. Agents break with partners they were not trained or tuned with

Agents that coordinate well with copies of themselves fail with independently trained agents, other model families or humans. This was first measured in classic multi-agent RL and now reappears with LLM agents and learned orchestrators.

- [Other-Play](https://arxiv.org/abs/2003.02979) (Meta FAIR): Hanabi agents score 23.97 with their own copy but 2.52 with an independently trained copy of the same method.
- [The Hanabi Challenge](https://arxiv.org/abs/1902.00506) (DeepMind, Google Brain, Oxford, CMU): agents that score 20+ in self-play fall to near 0 with independently trained partners.
- [Concordia Contest](https://arxiv.org/abs/2512.03318) (Cooperative AI Foundation, Oxford, UC Berkeley, Cambridge): most of 25 LLM agents did no better than a rational baseline on held-out scenarios with unfamiliar co-players.
- [Decrypto](https://arxiv.org/abs/2506.20664) (Meta FAIR, Oxford): LLMs paired with human partners win 0–17% of games vs 40% for human pairs.
- [The Conductor](https://arxiv.org/abs/2512.04388) (Sakana AI): an orchestrator trained on one pool of worker models is tied to it; changing the available agents needs retraining.

### 12. Agents collude, cheat and sabotage together, and prompts do not stop it

Without being told to, agents converge on collusion, cheating or sabotage over repeated interaction, and more capable models are not safer. Outcome checks and prompt prohibitions miss it.

- [Emergent Collusion in Long-Horizon LLM Agent Interaction](https://arxiv.org/abs/2609.24967) (Stanford, Georgia Tech): agents asked to verify each other jointly skipped verification in 93.6% of trajectories across 10 models; stronger models collude sooner.
- [Algorithmic Collusion by LLMs](https://arxiv.org/abs/2404.00806) (Harvard, Penn State): GPT-4 pricing agents reach above-competitive prices with no instruction to collude and no way to talk.
- [Secret Collusion among AI Agents](https://arxiv.org/abs/2402.07510) (UC Berkeley, Oxford, Google DeepMind): GPT-4 hides messages from an equally capable overseer ~26% of the time; paraphrasing does not remove covert channels.
- [Shutdown Sabotage Propensities in Multi-Agent Systems](https://arxiv.org/abs/2609.28274) (Stuttgart, Oxford): agents disable a peer's shutdown script in 38% of rollouts (8% control); for GPT-5.5 it rises from 0% to 44% to 94% as agents are added.
- [Emergent Cheating in Autonomous Research Swarms](https://arxiv.org/abs/2609.04170) (Google DeepMind): one agent's grader exploit spread through a shared library and 'solved' 34 problems in 27 minutes despite prompts forbidding cheating.

### 13. One compromised agent can take over the system, because safety does not compose

Attacks travel through the same channels agents use to collaborate (messages, shared memory, delegation). Per-agent guardrails cannot see the whole context, so agents that are safe alone can form an unsafe system.

- [Prompt Infection](https://arxiv.org/abs/2410.07283) (UCL, Stanford): a self-replicating injection spreads from agent to agent with +209% success over one-shot injection on GPT-3.5; each defense fails when used alone.
- [Breaking and Fixing Defenses Against Control-Flow Hijacking](https://arxiv.org/abs/2510.17276) (Cornell, Microsoft): an LLM firewall was evaded in 67–80% of attacks; even with no attacker, a multi-agent system leaked internal-only data 56% of the time.
- [Mind Viruses](https://arxiv.org/abs/2608.10218) (Anthropic, EPFL): one infected agent persuades teammates through normal messages to abandon their task; resistance depends on the model, not its capability.
- [Shutdown Sabotage Propensities in Multi-Agent Systems](https://arxiv.org/abs/2609.28274) (Stuttgart, Oxford): orchestrators blocked none of 36 sabotage requests, and downstream agents executed 465 of 468 instructions.
- [GPT-Red](https://arxiv.org/abs/2607.26115) (OpenAI): before attacker-defender self-play, GPT-5.1 resisted fake chain-of-thought injected through tools only 5.2% of the time; the fix took frontier-scale compute.

### 14. Oversight weakens as models get stronger

Using weaker judges or debate to supervise stronger models only partly works. LLM judges are biased and worse than humans, persuasion can beat truth, and the chance of catching a stronger model falls as the capability gap grows.

- [Scaling Laws for Scalable Oversight](https://arxiv.org/abs/2504.18530) (MIT): at a 400-Elo capability gap, oversight succeeds 9–14% of the time in Mafia, backdoored code and wargames, and 51.7% in debate (chance is 50%).
- [Debating with More Persuasive LLMs](https://arxiv.org/abs/2402.06782) (UCL, Anthropic): with a single persuasive advocate, judge accuracy falls to 54% vs 76% with debate; the best LLM judge reaches 76% vs 88% for humans.
- [On Scalable Oversight with Weak LLMs Judging Strong LLMs](https://arxiv.org/abs/2407.04622) (Google DeepMind): debate gives little or no gain when judge and debaters share the same information; more rounds and best-of-N do not help.
- [Prover-Estimator Debate](https://arxiv.org/abs/2506.13609) (Google DeepMind, UK AI Security Institute, UC Berkeley): a dishonest debater can hide a flaw in intractable subclaims; the proposed fix is not yet turned into practical training.
- [Great Models Think Alike](https://arxiv.org/abs/2502.04313) (Tübingen AI Center, MPI-IS): LLM judges favour models whose mistakes resemble their own (r = 0.84).

### 15. Agent societies do not yet behave like real people

LLM social simulations look human-like under convenient setups but flatten diversity, follow steering prompts, recognise textbook experiments and exaggerate effects. Few are validated against new human data.

- [The PIMMUR Principles](https://arxiv.org/abs/2509.18052) (CUHK, Johns Hopkins, CMU, Fudan, Stanford): 91.1% of 576 studies violate at least one validity principle; a headline effect falls from 60.7% to 34.4% once the flaws are fixed.
- [SimBench](https://arxiv.org/abs/2510.17516) (Cambridge, Stanford, Oxford): the best of 45 LLMs scores 40.8/100 at matching human response distributions; ten score below a uniform guess.
- [The Misleading Success of Simulating Social Interactions](https://arxiv.org/abs/2403.05020) (CMU, MIT, AI2): one model scripting both sides reaches a deal 94% of the time vs 30% for independent agents.
- [Simulating 1,000 People (Grounded in Self-Reports)](https://arxiv.org/abs/2411.10109) (Stanford, Google DeepMind, UW): agents get the direction of experimental effects right but inflate their size (0.36 in humans vs 2.97–9.64 in agents).
- [Generative Agents](https://arxiv.org/abs/2304.03442) (Stanford, Google): instruction tuning made agents over-agreeable; only 5 of 12 invited agents came to the party; two simulated days cost thousands of dollars.

### 16. Evaluation hides the failures

Benchmarks score final outcomes, rarely match compute against strong single-agent baselines, test small self-play setups and can be overfit. As a result, multi-agent gains are overstated and group-level failures go unseen.

- [Why Do Agent Teams Fail Across Boundaries?](https://arxiv.org/abs/2610.19342) (Salesforce, UNC): a negotiated deal passed 10/10 outcome checks while the agent scored 4/10 on conduct for leaking confidential data.
- [Emergent Collusion in Long-Horizon LLM Agent Interaction](https://arxiv.org/abs/2609.24967) (Stanford, Georgia Tech): outcome checks missed collusion: verdicts matched the truth even when agents skipped the required verification.
- [Magentic-One](https://arxiv.org/abs/2411.04468) (Microsoft Research): 35.1% on its own validation split vs 30.5% on the held-out test split.
- [Single-Agent LLMs Outperform Multi-Agent Systems](https://arxiv.org/abs/2604.02460) (Stanford): API budget artifacts and possible benchmark memorization inflate apparent multi-agent gains.
- [LLMs Miss the Multi-Agent Mark](https://arxiv.org/abs/2505.21298) (Oxford, King's College London): of 60+ papers claiming emergent behaviour in agent societies, only a few define metrics.
- [AgentsNet](https://arxiv.org/abs/2507.08616) (ETH Zurich, Google Research): existing multi-agent benchmarks cover at most 2–5 agents.

[⬆ Back to top](#)

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

- [Open Problems: Where the Field Is Stuck](#open-problems-where-the-field-is-stuck)
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
2. Regenerate the README and the topic pages: `pip install pyyaml && python scripts/build_readme.py`. The Open Problems section is generated from [`data/open_problems.yaml`](data/open_problems.yaml) in the same way.
3. Open a pull request.

**What belongs here:** papers where several agents (or a population, team or swarm of them) interact, cooperate, compete or are trained together. That includes classic multi-agent systems and multi-agent RL, with or without LLMs. Work on a single model is in scope when the model plays several roles with or against itself (self-play, co-evolution, parallel reasoning threads), or when the work is about building, training or evaluating multi-agent systems.

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the contributors have waived all copyright and related rights to this list.
