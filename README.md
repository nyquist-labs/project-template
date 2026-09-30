# Project template

Starting point for a new project in the [`projects`](https://github.com/nyquist-labs/projects) repository.
Every project follows **predict → measure → compare → explain** and documents itself in the standard below.

## Use it

1. Copy `project.py`, `figures/` and `data/` into `projects/<track>/<category>/<ID>-<short-slug>/` in the projects repository.
2. Fill in `META` (problem, prediction, method, data source) and `run(p)` (predict, measure, compare, figure, error analysis).
3. Run `python run_all.py --only <ID>` — this writes the project's `README.md`, `results.json`, figures and data.
4. Check the generated README against the standard, then open a pull request.

## Folder layout

```
<ID>-<short-slug>/
    project.py      the whole project: theory text (Prediction), method, measurement code, comparison, error analysis
    figures/        generated PNGs (and GIFs)
    data/           generated CSV files of every plotted or tabulated series
    README.md       generated — do not edit by hand
    results.json    generated — machine-readable results used by the website index
```

(Theory, simulation and analysis code live together in `project.py` so a single file reproduces every number; add a
`theory/` notes folder or extra modules only if a derivation needs more room than the README.)

## README standard (generated in this order)

```markdown
# <ID> · <Title>
> One-sentence summary
![main figure](figures/main.png)
**Track · Category · Level · Tools** — **Data:** <source and licence>

## Problem
## Prediction
## Method
## Measured results
| Quantity | Predicted | Measured | Error | Within tolerance |
## Error analysis
## Reproduce
    pip install -r requirements.txt
    python run_all.py --only <ID>
## License
MIT for code and text; datasets under their own licences.
---
How this was made (AI-assistance disclosure)
```

## License
MIT.
