# AI Agent Guidance for bioinformatics-challenges

## Repository purpose
This repository contains Rosalind-style bioinformatics exercises solved in Python. It is intended for practicing sequence analysis and simple algorithmic problems.

## Structure
- Each challenge lives in its own directory under the repository root.
- Typical files in a challenge directory:
  - `problem.txt`: problem description
  - `problem_input.txt`: input data for the problem
  - `problem_output.py`: Python solution script

## Conventions for changes
- Keep solutions simple and idiomatic Python.
- Use the local `problem_input.txt` file or a hard-coded string as the existing solutions do.
- Do not introduce a complex build system or external dependencies.
- Validate changes by running the Python script directly: `python3 <challenge_dir>/problem_output.py`.

## Notes for agents
- There is no existing test harness or CI configuration.
- Respect repository naming and file conventions, including directories with spaces (for example `Problem_Transcribing_DNA _into_RNA`).
- Prefer minimal edits that preserve the standalone nature of each solution file.

## Reference
See `README.md` for the repository description.
