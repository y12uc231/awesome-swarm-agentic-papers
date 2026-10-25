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
