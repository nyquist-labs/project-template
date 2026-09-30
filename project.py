"""Project template for the Nyquist Labs `projects` repository.

Copy this folder to  projects/<track>/<category>/<ID>-<short-slug>/  in the projects repository, rename the ID,
fill in META and run(), then:  python run_all.py --only <ID>
The README.md in the project folder is generated from META and run(); do not edit it by hand.
"""
from eelab import *

META = dict(
    id="XX-000",                       # e.g. AM-219 (applied maths) or SL-215 (signal lab)
    title="Short descriptive title",
    level="M",                         # E (easy), M (moderate), H (hard)
    tools="Methods, solvers, simulators and libraries used — name the independent reference you compare against",
    summary="One or two sentences: what is predicted, how it is measured, and what the comparison shows.",
    problem="The engineering question, in one or two sentences.",
    theory=r"""PREDICTION — written before measuring. The formulas, assumptions and published values that give the expected result.
Use LaTeX in $…$. If you only have a guess, say "my guess" in the comparison label.""",
    method="""How the result is measured: model / simulator / dataset (with source), parameters, sample sizes, how errors are computed.""",
    data="Simulated (numerical model in this repo).",   # or: "Real: <dataset> (<source>, <licence>)"
)


def run(p):
    # 1. Predict (closed form)
    predicted = 1.0

    # 2. Measure (independent simulation / dataset) — every number comes from code, never typed in
    measured = 1.0 + 0.01 * p.rng.normal()

    # 3. Compare — relative tolerances are in PERCENT; kind="abs" for absolute differences
    p.compare("Quantity being checked (units)", predicted, measured, "", tol=5)
    p.metric("A related number worth reporting", measured, "")

    # 4. Figure(s)
    fig, ax = p.fig(1, 1)
    ax.bar(["predicted", "measured"], [predicted, measured], color=[C_PRED, C_MEAS])
    style_axes(ax, "", "value", "Predicted vs measured", legend=False)
    p.save(fig, "main", "Caption: what the figure shows.")

    # 5. Error analysis — explain every disagreement, including wrong predictions
    p.discuss(f"""State what agreed, what did not ({pct_err(predicted, measured):+.2f} %), and why.""")
