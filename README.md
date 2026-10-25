# sepia-tw overlay

This branch holds only the customizations layered on top of upstream [Nanako0129/sepia](https://github.com/Nanako0129/sepia) (MIT). The `main` branch of this fork stays a plain mirror of upstream.

| Path | What it is |
|---|---|
| `files/references/domains/academic.md` | Academic and application route: 研究計畫, 讀書計畫, 自傳, SoP, theses, papers, abstracts, emails to professors |
| `files/references/research/academic-sources.md` | Ledger addendum for the sources the academic route cites |
| `files/evals/` | Test cases for the academic route |
| `patches.json` | Text inserted into upstream `SKILL.md`: description, intro note, routing row, "Selecting the operation" |
| `build.py` | Rebuilds the skill from an upstream checkout plus this overlay |
| `last-built-version` | Upstream version the last packaged build was made from |

## Build

```bash
git clone --depth 1 --branch v<VERSION> https://github.com/Nanako0129/sepia upstream
python3 -I build.py upstream . out/sepia
```

`build.py` copies upstream's `skills/sepia`, research ledger, license and evals, adds the overlay files, and patches `SKILL.md`. Each patch is anchored to one line of upstream text. If upstream moves or rewrites an anchor, the build stops with `BUILD STOPPED: …` naming the anchor instead of guessing.

To change the academic route, edit the files here; the next build picks them up.
