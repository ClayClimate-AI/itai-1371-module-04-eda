# Reuse Module 3 structure for Lab 04

Joseph note: Grok (in app) said some Module 3 structure can be reused or cloned for Module 4. Saved 2026 09 13.

## Plain meaning of "clone"

Two options. Neither starts until Joseph says yes to that exact step.

1. `git clone` the L03 repo, create a new branch or new repo for Lab 04, then replace Wine / model cells with the Lab 04 Titanic notebook path.
2. Copy only the folder skeleton (README, requirements, CI, specs, journals templates) into a new Lab 04 repo and drop in `Module_04_Lab_Exploratory_Data_Analysis.ipynb`.

## Reuse (keep)

```text
Keep from Module 3
├── repo layout: README, requirements.txt, scripts/setup_gate, .github CI
├── process docs: checkpoints, progress, reflections, specs, ADRs
├── engineering gates: run all top to bottom, integrity asserts, no out of order cells
├── deliverable pattern: executed notebook PDF + reflective journal PDF + contribution journal PDF
└── Zero Defect rules: fight State Drift, Data Rot, Scope Creep
```

## Do not reuse as the Lab 04 core

```text
Replace for Lab 04
├── Wine dataset and cultivar classifiers
├── learning curve as the main proof artifact
├── L03 file names (use L04_* names)
└── Module 03 acceptance criteria text
```

Lab 04 acceptance criteria stay Titanic EDA: run the Module 04 notebook, explanations, experimentation, three PDFs, due Tue 15 Sep 2026 11:59 PM CT. RCA intent still maps here.

## Suggested next action (needs Joseph yes)

```text
If yes to scaffold
├── new public repo name, e.g. itai-1371-module-04-eda
├── copy skeleton from L03 (not the Wine notebook)
├── add Module_04_Lab_Exploratory_Data_Analysis.ipynb as the main notebook
├── rewrite README for EDA goals + RCA notes in explanation cells
└── keep journals and PDF export process
```

## Resolved (2026-09-14)

Joseph provided the Lab 04 GitHub remote:
`https://github.com/ClayClimate-AI/itai-1371-module-04-eda.git`

Done: `git init` in this folder, `git remote add origin <link>`.
Not done yet (needs separate yes): commit, push. The skeleton was not copied via
`git clone` of L03 — this folder already had its own scaffold, so option 2 (copy
skeleton only) is effectively how it happened, just done manually earlier rather
than via clone.
