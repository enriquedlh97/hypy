# HyPy

HyPy is a general [hyper-heuristic](https://en.wikipedia.org/wiki/Hyper-heuristic)
package for solving [combinatorial optimization](https://en.wikipedia.org/wiki/Combinatorial_optimization)
problems by employing and developing hyper-heuristics.

## Installation and Set Up

- pyenv for python version
- poetry
- pre-commit
- tests
- remember to run mypy
- Automatic documentation
- Test docstrings examples (`poetry run python -m doctest hypy/problems/vrp/base_components.py`)
- Building and locally visualizing docs.
  - `poetry run mkdocs serve` for development.
  - `mkdocs build`
  - `mkdocs gh-deploy` for publishing documentation found [here](https://enriquedlh97.github.io/hypy/)
