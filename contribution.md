# Contribution Journal — Lab 04

SingleEpoch | ITAI 1371 Module 04

## Individual contribution statement

This lab was completed as an individual effort in association with the
group SingleEpoch. There was no peer group to divide work with, so the
tasks below cover the full scope of the assignment.

**Environment and repo setup.** The project scaffold (`.venv`,
`requirements.txt`, `setup_gate.py`, tests, CI workflow) was set up, the
local gate was brought to passing, and the repo was initialized and
connected to the GitHub remote.

**A notebook defect surfaced before work could start.** Running the
first code cell produced a `SyntaxError: unterminated string literal`.
Tracing it back showed a notebook authoring defect: a `print()` string
had been split across two entries in the notebook's underlying source
data, which broke the string open when the cell ran. The same problem
turned up in a second cell. Every other code cell was checked to
confirm the defect was isolated to those two, and both were fixed. The
full RCA is documented in the reflective journal.

**Every cell was run and verified individually.** For each of the six
instructor-filled code cells and both experiment cells, the cell was
run and its output checked against a specific expectation before moving
on, rather than running everything at once and assuming it worked.

**Experiment code was written for the two student sections.** For
Experiment 1 (Embarked countplot) and Experiment 2 (Fare boxplot), the
plotting code was written by mirroring the pattern already used in the
instructor cells, and the resulting plots were read to answer what they
showed about survival.

**Knowledge check and reflections reflect direct observation.** The
knowledge check answers and the reflective journal are based on
observations from the plots that were run, not pulled from an outside
source.

**Data quality claims were checked against the source.** Where a
factual claim about the dataset appears (missing value counts for Age,
Cabin, Embarked), it was verified against the live dataset rather than
assumed.
