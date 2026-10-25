# Academic route — ledger addendum

Sources cited by `references/domains/academic.md`, added in the sepia-tw adaptation. Same conventions as `sources.md`: stable IDs, what was measured, and the limit of each.

| ID | Source | Link | Kind | What it supports, and its limit |
|---|---|---|---|---|
| `KOBAK-2025` | Kobak, González-Márquez, Horvát, Lause — *Delving into LLM-assisted writing in biomedical publications through excess vocabulary*, Science Advances (2025) | [arXiv:2406.07016](https://arxiv.org/abs/2406.07016v5) · [code](https://github.com/berenslab/llm-excess-vocab) | measured corpus study | >15M PubMed abstracts 2010–2024; excess style words imply ≥13.5% of 2024 abstracts LLM-processed, up to 40% in some subcorpora. Population estimate; says nothing about any single text and tests no fix |
| `LIANG-MAP-2024` | Liang et al. — *Mapping the Increasing Use of LLMs in Scientific Papers* (COLM 2024) | [arXiv:2404.01268](https://arxiv.org/abs/2404.01268) | measured corpus study | ~950k arXiv/bioRxiv/Nature papers 2020–Feb 2024; CS abstracts 17.5% LLM-modified sentences (math 4.9%); higher in crowded areas and papers under 5,000 words; markers *realm, intricate, showcasing, pivotal*. Pre-ChatGPT baseline 2.3–3.1% is the false-positive floor |
| `LIANG-REVIEW-2024` | Liang et al. — *Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews* (ICML 2024) | [arXiv:2403.07183](https://arxiv.org/abs/2403.07183) | measured corpus study | Same distributional method on AI-conference peer reviews; adjective shift (e.g. *commendable, meticulous, intricate*). Reviews, not submissions |
| `LIANG-BIAS-2023` | Liang et al. — *GPT detectors are biased against non-native English writers*, Patterns 4(7) (2023) | listed in `sources.md` | measured | Perplexity detectors flagged 61.3% of TOEFL essays. Supports the whitelist for plain L2 English; a critique of detectors, no rhythm numbers |
| `ZHENG-2026` | Zheng — frozen-rater study of 124K ICLR reviews | listed in `sources.md` | measured | Expert reviewers reward within-text sentence-length spread; a frozen LLM rater does not. Reader preference, not a detector feature |
