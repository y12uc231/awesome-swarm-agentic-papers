"""Regenerate README.md and the per-topic pages in papers/ from data/papers.yaml.

Usage: python scripts/build_readme.py
"""
import re
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent

# (group title, intro, [(section key, section title), ...]) in README order.
SECTIONS = [
    ("Surveys & Position Papers", "Overviews of LLM-based multi-agent systems, agent protocols, simulation, training and safety.", [
        ("surveys", None),
    ]),
    ("Multi-Agent Systems & Multi-Agent RL", "Agent theory, coordination protocols and multi-agent reinforcement learning, from the classics to current (non-LLM) MARL.", [
        ("classic_mas", "Classic Multi-Agent Systems"),
        ("marl", "Multi-Agent Reinforcement Learning & Emergent Communication"),
    ]),
    ("Swarm Intelligence", "Collective behaviour from simple local rules, and recent work that brings swarm ideas to LLM agents, robot swarms and model weights.", [
        ("swarm_classic", "Classic Swarm Intelligence & Swarm Robotics"),
        ("swarm_llm", "LLM Agent Swarms & Swarm-Inspired Methods"),
    ]),
    ("Frameworks & Architectures", "How LLM agents are organized, connected and coordinated.", [
        ("frameworks", "Multi-Agent Frameworks & Role-Playing"),
        ("orchestration", "Orchestration, Hierarchies & Agent Swarms"),
        ("auto_design", "Automated Design & Search of Agentic Systems"),
        ("topology_comm", "Communication Topology, Protocols & Latent Communication"),
        ("memory_knowledge", "Memory & Knowledge Sharing"),
    ]),
    ("Debate & Collaborative Reasoning", "Agents that argue, critique, vote and aggregate to reason better.", [
        ("debate", "Multi-Agent Debate"),
        ("debate_oversight", "Debate for Scalable Oversight"),
        ("ensembles_moa", "Mixture-of-Agents & Multi-LLM Ensembles"),
        ("collab_reasoning", "Collaborative Reasoning, Role-Play & Theory of Mind"),
    ]),
    ("Training Multi-Agent Systems", "Learning the agents (not only prompting them): RL, fine-tuning, self-play and parallel reasoning.", [
        ("marl_llm", "Multi-Agent RL for LLM Agents"),
        ("multiagent_finetune", "Multi-Agent Fine-Tuning & Self-Improvement"),
        ("self_play", "Self-Play, Adversarial Games & Co-Evolution"),
        ("parallel_reasoning", "Parallel & Concurrent Reasoners"),
    ]),
    ("Data Synthesis with Multi-Agent Systems", "Agent teams and simulations that generate training data.", [
        ("data_synthesis", None),
    ]),
    ("Evaluation", "Benchmarks, failure analysis, scaling studies and multi-agent judges.", [
        ("benchmarks", "Benchmarks & Environments"),
        ("failure_analysis", "Failure Analysis & Attribution"),
        ("scaling_analysis", "Scaling Studies & When Multi-Agent Helps"),
        ("llm_judges", "Multi-Agent Judges & Evaluators"),
    ]),
    ("Agent Societies & Simulation", "Populations of agents: social simulation, emergent behaviour, games, markets and cooperation.", [
        ("social_sim", "Social Simulation"),
        ("emergence", "Emergent Behaviour, Conventions & Cooperation"),
        ("games", "Games"),
        ("economics_negotiation", "Economics, Negotiation & Markets"),
        ("cooperative_ai", "Cooperative AI & Human-Agent Teaming"),
    ]),
    ("Safety & Security", "New risks that appear when agents talk to, trust and depend on each other.", [
        ("attacks", "Attacks"),
        ("defenses", "Defenses, Monitoring & Resilience"),
        ("collusion_deception", "Collusion, Steganography & Deception"),
        ("risks_governance", "Risks, Agendas & Governance"),
    ]),
    ("Applications", "Domains where the multi-agent design is central.", [
        ("software", "Software Engineering"),
        ("science_research", "Science & Research Automation"),
        ("medicine", "Medicine & Healthcare"),
        ("embodied_robotics", "Embodied Agents & Robotics"),
        ("web_gui_tools", "Web, GUI, Tools & Deep Research"),
        ("finance_law_other", "Finance, Law, Education & Other Domains"),
    ]),
]


def anchor(title):
    a = title.strip().lower()
    a = re.sub(r"[^\w\- ]", "", a)
    return a.replace(" ", "-")


def link(p):
    if p.get("arxiv"):
        return f"https://arxiv.org/abs/{p['arxiv']}"
    return p["url"]


def md(text):
    return text.replace("*", "\\*")


def entry(p):
    parts = [f"`{p['date']}`", f"**[{md(p['title'])}]({link(p)})**"]
    meta = " · ".join(x for x in [p.get("authors"), f"*{p['venue']}*" if p.get("venue") else None] if x)
    line = "- " + " ".join(parts)
    if meta:
        line += f" — {meta}"
    if p.get("code"):
        line += f" · [[code]({p['code']})]"
    if p.get("note"):
        line += f"<br>{md(p['note'])}"
    return line


OPEN_PROBLEMS_INTRO = (
    "What is actually broken, according to the papers themselves. The full text (not just the abstract) of {n_read} papers "
    "in this list was read, chosen from work by well-known labs and universities such as Google DeepMind, OpenAI, Anthropic, "
    "Meta, Microsoft, NVIDIA, Moonshot AI, Stanford, MIT, Berkeley, CMU, Oxford, Cambridge, Princeton, Harvard and Mila, "
    "with an emphasis on analysis, failure, scaling, training and safety papers. Every problem a paper showed in its "
    "experiments, argued for, or admitted as a limitation was recorded with a quote checked against the paper text "
    "({n_items} in total). The {n_problems} patterns below recur across many of those papers and labs. Each one lists "
    "papers whose own results show it."
)


def render_open_problems(problems, papers_by_id):
    lines = ["## Open Problems: Where the Field Is Stuck", "",
             OPEN_PROBLEMS_INTRO.format(n_read=102, n_items=638, n_problems=len(problems)), ""]
    for i, prob in enumerate(problems, 1):
        lines.append(f"{i}. [{prob['title']}](#{anchor(f'{i}. ' + prob['title'])})")
    lines.append("")
    for i, prob in enumerate(problems, 1):
        lines += [f"### {i}. {prob['title']}", "", prob["problem"], ""]
        for ev in prob["evidence"]:
            assert ev["arxiv"] in papers_by_id, f"cited paper not in list: {ev['arxiv']}"
            lines.append(f"- [{md(ev['label'])}](https://arxiv.org/abs/{ev['arxiv']}) ({ev['lab']}): {md(ev['finding'])}.")
        lines.append("")
    lines.append("[⬆ Back to top](#)")
    return "\n".join(lines)


def main():
    papers = yaml.safe_load((ROOT / "data" / "papers.yaml").read_text())
    known = {k for _, _, subs in SECTIONS for k, _ in subs}
    unknown = {p["section"] for p in papers} - known
    assert not unknown, f"unknown sections: {unknown}"
    by_sec = {}
    for p in papers:
        by_sec.setdefault(p["section"], []).append(p)

    head = (ROOT / "scripts" / "readme_head.md").read_text()
    tail = (ROOT / "scripts" / "readme_tail.md").read_text()
    years = Counter(int(str(p["date"])[:4]) for p in papers)
    llm_era = sum(v for y, v in years.items() if y >= 2022)
    for k, v in {"{{N_PAPERS_PLAIN}}": str(len(papers)), "{{N_PAPERS}}": f"{len(papers):,}", "{{N_LLM}}": f"{llm_era:,}",
                 "{{N_PRE}}": f"{len(papers) - llm_era:,}", "{{MIN_YEAR}}": str(min(years))}.items():
        head = head.replace(k, v)

    toc = ["## Contents", "", "- [Open Problems: Where the Field Is Stuck](#open-problems-where-the-field-is-stuck)"]
    (ROOT / "papers").mkdir(exist_ok=True)
    for gtitle, intro, subs in SECTIONS:
        slug = anchor(gtitle.replace("&", "and"))
        gcount = sum(len(by_sec.get(k, [])) for k, _ in subs)
        toc.append(f"- [{gtitle}](papers/{slug}.md) ({gcount})")
        order = "newest first within each section" if any(t for _, t in subs) else "newest first"
        page = [f"# {gtitle}", "", f"[⬅ Back to the main list](../README.md) · {gcount:,} papers, {order}.", "", f"*{intro}*", ""]
        if any(t for _, t in subs):
            page += [f"- [{t}](#{anchor(t)}) ({len(by_sec.get(k, []))})" for k, t in subs] + [""]
        for key, stitle in subs:
            items = sorted(by_sec.get(key, []), key=lambda p: (str(p["date"]), p["title"]), reverse=True)
            if stitle:
                toc.append(f"  - [{stitle}](papers/{slug}.md#{anchor(stitle)}) ({len(items)})")
                page += [f"## {stitle}", ""]
            page += [entry(p) for p in items] + [""]
        page += ["[⬆ Back to top](#) · [⬅ Back to the main list](../README.md)", ""]
        (ROOT / "papers" / f"{slug}.md").write_text("\n".join(page))

    problems = yaml.safe_load((ROOT / "data" / "open_problems.yaml").read_text())
    head = head.replace("{{OPEN_PROBLEMS}}", render_open_problems(problems, {p.get("arxiv"): p for p in papers}))

    year_rows = ["| Year | Papers |", "|---|---|"] + [f"| {y} | {years[y]} |" for y in sorted(years) if y >= 2022]
    head = head.replace("{{YEAR_TABLE}}", "\n".join(year_rows))
    (ROOT / "README.md").write_text("\n".join([head.rstrip(), "", *toc, "", tail.strip(), ""]))
    print(f"README.md + {len(SECTIONS)} pages: {len(papers)} papers")


if __name__ == "__main__":
    main()
