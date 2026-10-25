# Domain — academic & application writing

Covers four document shapes, in Traditional Chinese or English:

| Shape | Examples | Weighting (`professional-pass.md`) |
|---|---|---|
| A. Plans | 研究計畫, 讀書計畫, research proposal, grant-style aims | Article-like; also run `discourse-pass.md` §1–3 |
| B. Personal accounts | 自傳, personal statement, statement of purpose, motivation letter | Article-like; also run `discourse-pass.md` §1–3 |
| C. Scholarly text | thesis chapters, journal or conference manuscripts, abstracts, 摘要 | Article-like; §1–3 on whole sections, not on an abstract alone |
| D. Correspondence | emails to a prospective advisor, lab inquiries, recommendation requests | Short answer: factuality, specificity, templatedness first |

Evidence. On academic prose the measured findings are about vocabulary at corpus scale: an excess-vocabulary analysis of more than 15 million PubMed abstracts (2010–2024) put a lower bound of 13.5% on 2024 abstracts processed with LLMs, reaching 40% in some subcorpora, carried by style words rather than content words (`KOBAK-2025`); across about 950,000 arXiv, bioRxiv and Nature-portfolio papers, an estimated 17.5% of computer-science abstract sentences were LLM-modified by February 2024, with *realm, intricate, showcasing, pivotal* among the marker words, and higher rates in crowded subfields and shorter papers (`LIANG-MAP-2024`); the same group found the same kind of shift in AI-conference peer reviews (`LIANG-REVIEW-2024`). Expert readers reward within-text sentence-length spread in ICLR submissions while a frozen LLM rater does not (`ZHENG-2026`, `style-pass.md` §5). Perplexity detectors flag most TOEFL essays by non-native writers as AI (`LIANG-BIAS-2023`), which is why plain second-language English is whitelisted below. These studies measured populations, not any fix. Every rule in this file is a Sepia inference or an editorial heuristic; the shape-specific tells are what Taiwanese reviewers and advisors report reading, not measured rates. Sources: `research/academic-sources.md`.

> Goal: a reviewer who reads forty of these in an afternoon should meet a specific person with a specific problem. This route writes for that reader. It aims at no detector, and it changes nothing that a school's or journal's AI-use policy asks of the author.

## Guardrails that tighten on this route

1. **Never invent a credential.** Grades, ranks, awards, publications, conference names, competition results, years, course names, lab names, professors' names and their papers, datasets, sample sizes, metrics, p-values, citations: all come from the user. A missing one becomes a visible placeholder — 「【待補：修課成績】」 or `[TODO: GPA]` — never a plausible guess. A fabricated reference or an inflated result is the single most damaging thing this route can produce: reviewers check, and it reads as dishonesty, not as AI.
2. **Contribution boundary.** Keep the author's verb exactly as strong as the facts. "Helped evaluate", 「協助跑效能評估」, "maintained the pipeline", "was second author" stay what they are; never upgrade them to "developed", 「主導」「提出」, "first-authored". Shared lab tools, an advisor's idea, a teammate's model are named as theirs. "We" in a paper is the author team; "I" in a statement is the applicant alone — do not let one slide into the other. This is the academic form of *no register drift* in `SKILL.md`.
3. **Citations are quoted material.** Do not correct an author name, year, venue or title from memory; if it looks wrong, report it as 「【待查】」 and leave it. Do not add citations. Do not add a claim that would need one.
4. **Personal accounts are the author's own account.** On shape B the memoir clause of `SKILL.md` (*Respect the author's voice*) applies in full: what the applicant reports feeling, deciding or realizing is theirs; ask before cutting or recasting it.
5. **Recreate adds no science.** On recreate, no new limitation, hypothesis, expected result, significance claim or future-work item that neither the source nor the user states (`SKILL.md` Operations, recreate). Repeating a number the source reports is fine; a conclusion drawn from it is an addition.

## Human baseline

Specific before general. The first paragraph names a concrete problem, gap, result or episode. Unevenness: depth where the author actually did the work, a line where they did not. One position the reader could disagree with (a method choice defended, a prior approach judged insufficient, a reason for this lab and not another). Hedging sits on the claims the evidence leaves fragile and nowhere else. Numbers carry their conditions.

## Tells by shape

### A. 研究計畫 / 讀書計畫 / research proposals

| Tell | Fix |
|---|---|
| The era opening: 「隨著人工智慧的快速發展」「近年來，X 受到廣泛關注」 / "In recent years, X has attracted increasing attention" | Open at the gap: the named method, its named limitation, the number that shows it. If no such gap is in the source, ask — do not write a generic one |
| Buzzword stacking: 「結合深度學習、強化學習與大型語言模型等前沿技術」 | Name the one technique the plan actually uses and what it does here |
| Goal inflation: 「徹底解決」「革命性」「填補此領域之空白」, "novel framework", "first to" | State the deliverable and how it would be measured; "first" only with the user's evidence |
| Aims that restate the motivation; methods that restate the aims | Each aim → method → success measure → one risk and its fallback. A plan with no possible failure reads as unplanned |
| Symmetric literature review: every prior work one paragraph, no verdict | Organize by the gap; say which work the plan builds on and which it departs from, and why |
| Even timeline: identical phases, every milestone 「完成」 | Phase lengths follow the work; name the first concrete milestone |
| 預期成果 / expected contributions as a generic list: 「對學術與產業皆有重大貢獻」 | One or two outcomes a committee could check a year from now |
| 讀書計畫 contents that fit any applicant: 「精進專業知識、培養獨立研究能力」 | Named courses, techniques, a lab or core facility, a first-year target — from the user; placeholder if missing |

Conventional and not a tell: 近程／中程／遠程 sections, 研究背景／研究目的／研究方法／預期成果 headings, a Gantt-style table, 本研究／本計畫 as subject.

### B. 自傳 / personal statement / SoP

| Tell | Fix |
|---|---|
| The origin myth: 「從小我就對…充滿好奇」 / "Ever since I was a child" | Start at the decisive episode — the project, bug, result or course that changed direction |
| Trait lists: 「我具備積極、負責、善於團隊合作的特質」 | Delete the list; the one episode that shows the trait carries it |
| Resume in prose: every activity one paragraph of equal length | Two decisive episodes in depth, the rest a line or the CV |
| The lesson tail: every paragraph ends 「這段經歷讓我學到…」 / "This experience taught me" | Keep at most one, where the lesson is non-obvious; elsewhere end on the fact (discourse §1, reflection tail) |
| Program flattery: 「貴所師資優良、設備完善、學風自由」 / "your prestigious program" | The specific professor, lab, method or resource and the concrete reason — only if the user supplies it; else placeholder |
| Stacked commitment ending: a paragraph of 「定當全力以赴」「懇請教授給予機會」 | One closing line in the venue's convention is fine; cut the rest |

Conventional and not a tell: a single polite closing line, chronological order, 敬稱 for the committee, a formal register throughout.

### C. Theses, manuscripts, abstracts, 摘要

| Tell | Fix |
|---|---|
| Excess style vocabulary (`KOBAK-2025`, `LIANG-MAP-2024`): *delve, underscore, showcase, pivotal, intricate, realm, crucial, notably, comprehensive*; Chinese counterparts 「深入探討」「至關重要」「有效提升」「全面」「進一步」 in clusters | Plain verb, or delete; the style-pass §3 cluster rule decides |
| 「顯著」 / "significantly" with no statistical test behind it | Reserve for a reported test; otherwise give the number or say "larger"/「較高」 |
| Contribution bullets with inflated verbs: "We propose a novel, robust framework that significantly outperforms" | The bullet states what was done and the measured difference with its condition |
| Abstract with a generic-importance first sentence and results without numbers | One sentence of problem; the main result with its number, dataset and baseline |
| Fractal roadmaps: 「本章首先…接著…最後…」 at every section and subsection | One roadmap per chapter is a Taiwanese thesis convention; cut the rest |
| Generic limitations: "Future work could explore larger datasets and more models" | Name the limitation that actually bites this result — from the user or source only; on recreate, never added |
| Term drift: 強化學習 / 增強式學習 / RL alternating | Pick one per document; first mention 「強化學習（reinforcement learning, RL）」 with full-width parentheses (`languages/zh.md` §0) |

Conventional and not a tell: IMRaD or 緒論／文獻探討／研究方法／結果與討論／結論 structure, passive voice in methods, calibrated hedges on fragile claims ("may", "suggests", 「可能」「顯示」), dense terminology, 本研究 as subject.

### D. Emails to professors

| Tell | Fix |
|---|---|
| Stacked pleasantries: "I hope this email finds you well. I hope you are doing great." / 「久仰教授大名，拜讀您的大作深感敬佩」 | One conventional greeting; then who you are and why you are writing, in the first two sentences |
| Generic praise of "your groundbreaking work" | One sentence engaging a specific paper or project the user names — never one Claude picks from memory |
| Hedged-to-nothing ask: "I was wondering if perhaps you might possibly consider" | One direct, polite ask (a meeting, an opening, a reply by a date) |
| Essay length | Fits on one screen; detail goes in the attached CV or plan, listed by name |
| Vague subject line | Subject states who and what: 「申請逕讀博士班—詢問指導可能性（王○○，XX 大學碩士班）」 |

Conventional and not a tell: 「X 教授您好」, 「敬祝 研安」, 「學生 ○○○ 敬上」, "Dear Professor X", "Best regards".

## Whitelist specific to this route

| Do not flag | Why |
|---|---|
| Plain, correct second-language English | Non-native plainness is the population detectors misfire on (`LIANG-BIAS-2023`); simple is not machine |
| Formal 書面語 in Chinese academic text | Register match; restoring 語氣詞 (`languages/zh.md` §3) does not apply in shapes A–C, and only lightly in D |
| Hedges on genuinely fragile claims | Calibrated hedging is scientific practice; check 4 in `professional-pass.md` is about hedges with no fragile claim under them |
| Section templates required by the venue (a school's 書審 format, a journal's structured abstract) | The container is set by the venue |
| Lists of real items (courses, publications, skills with evidence) | Enumerable facts belong in lists |

## Rules

1. **Open at the specific.** First sentence of a plan, statement or abstract names the problem, gap, result or episode. If the source has none, ask.
2. **Evidence per claim.** Every claim of ability, novelty or result points to something checkable in the same document or the CV. Unbacked claims are cut or turned into placeholders, not softened.
3. **Depth by real work.** The part the author actually did gets the words. Setup, background and generic motivation get the least.
4. **One committed position** per plan or statement — a method choice, a judgment of prior work, a reason for this program — stated as the author's.
5. **Match the venue's template, not a generic one.** If the user shares the school's or journal's required sections or length, those win over everything here. Character or word limits are hard limits; report the count after editing.
6. **Bilingual pairs stay consistent.** When a Chinese and an English version of the same document exist, facts, numbers and claims match across them; flag any mismatch instead of resolving it.
