#!/usr/bin/env python3
"""Rebuild the sepia (tw) skill from an upstream sepia checkout plus this overlay.

Usage: python3 -I build.py <upstream-checkout> <overlay-dir> <out-dir>

Stops with exit code 2 and a plain message if any upstream anchor the patches rely on
has moved or changed, instead of guessing where the custom text should go.
"""
import json
import re
import shutil
import sys
from pathlib import Path

ADAPTATION_TAG = "tw.1"


def fail(msg):
    print(f"BUILD STOPPED: {msg}", file=sys.stderr)
    sys.exit(2)


def replace_once(text, pattern, repl, what, flags=0):
    matches = re.findall(pattern, text, flags)
    if len(matches) != 1:
        fail(f"anchor for {what} matched {len(matches)} times (expected 1): {pattern!r}")
    return re.sub(pattern, lambda m: repl(m), text, count=1, flags=flags)


def main():
    if len(sys.argv) != 4:
        fail("usage: build.py <upstream-checkout> <overlay-dir> <out-dir>")
    up, ov, out = (Path(p).resolve() for p in sys.argv[1:])
    src = up / "skills" / "sepia"
    if not (src / "SKILL.md").is_file():
        fail(f"{src}/SKILL.md not found; upstream layout changed")
    if out.exists():
        shutil.rmtree(out)

    # 1. Upstream canonical skill, research ledger, license, upstream evals.
    shutil.copytree(src, out)
    shutil.rmtree(out / "agents", ignore_errors=True)  # Codex-only metadata
    if (up / "research").is_dir():
        shutil.copytree(up / "research", out / "references" / "research", dirs_exist_ok=True)
    if (up / "LICENSE").is_file():
        shutil.copy2(up / "LICENSE", out / "LICENSE")
    if (up / "evals").is_dir():
        shutil.copytree(up / "evals", out / "evals", dirs_exist_ok=True)

    # 2. Overlay files (academic route, its ledger addendum, our test cases).
    shutil.copytree(ov / "files", out, dirs_exist_ok=True)

    # 3. Patch SKILL.md.
    p = json.loads((ov / "patches.json").read_text(encoding="utf-8"))
    skill = out / "SKILL.md"
    t = skill.read_text(encoding="utf-8")

    m = re.search(r'^  version: "([^"]+)"$', t, re.M)
    if not m:
        fail("frontmatter version line not found")
    upstream_version = m.group(1)

    t = replace_once(t, r"^description: .*$", lambda _: "description: " + p["description"], "description", re.M)
    t = replace_once(
        t,
        r'^  version: "[^"]+"$',
        lambda _: f'  version: "{upstream_version}-{ADAPTATION_TAG}"\n'
        '  adapted-from: "https://github.com/Nanako0129/sepia (MIT, Nanako Tsai)"',
        "version",
        re.M,
    )
    intro = p["intro"].replace("adapts sepia 0.12.4", f"adapts sepia {upstream_version}")
    intro = re.sub(r"adapts sepia [0-9][^ ]*", f"adapts sepia {upstream_version}", intro)
    t = replace_once(t, r"^# Sepia — de-AI writing\n\n", lambda m: m.group(0) + intro + "\n\n", "title heading", re.M)
    t = replace_once(t, r"^\| Long-form journalism:", lambda m: p["academic_row"] + "\n" + m.group(0), "routing table journalism row", re.M)
    t = replace_once(
        t,
        r"^The two-stage protocol is not optional",
        lambda m: p["selecting"] + m.group(0),
        "two-stage protocol paragraph",
        re.M,
    )
    skill.write_text(t, encoding="utf-8")

    # 4. Sanity: every reference path SKILL.md names must exist in the build.
    missing = [r for r in sorted(set(re.findall(r"`(references/[^`*]+?\.md)`", t))) if not (out / r).is_file()]
    if missing:
        fail("SKILL.md names reference files missing from the build: " + ", ".join(missing))

    print(json.dumps({"upstream_version": upstream_version, "built_version": f"{upstream_version}-{ADAPTATION_TAG}", "out": str(out)}))


if __name__ == "__main__":
    main()
