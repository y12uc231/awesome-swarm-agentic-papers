## Contributing

Missing a paper, or found a wrong link or category? Pull requests are welcome.

1. Add or edit an entry in [`data/papers.yaml`](data/papers.yaml). Fields: `title`, `arxiv` (or `url` if there is no arXiv version), `date` (`YYYY-MM`, first arXiv version or publication), `authors` (`First et al.`), `venue` (optional), `section` (one of the keys in [`scripts/build_readme.py`](scripts/build_readme.py)), `note` (one sentence on what the paper contributes) and `code` (optional, official repository only).
2. Regenerate the README and the topic pages: `pip install pyyaml && python scripts/build_readme.py`.
3. Open a pull request.

**What belongs here:** papers where several agents (or a population, team or swarm of them) interact, cooperate, compete or are trained together, plus the pre-LLM foundations and evaluations of such systems. Single-agent work is in scope only when it is about building, training or evaluating multi-agent systems.

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the contributors have waived all copyright and related rights to this list.
