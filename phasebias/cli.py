"""Console-script entry points for the phase-bias pipeline.

Each entry point executes the corresponding top-level script as ``__main__``
(via ``runpy``), so the scripts keep their plain-script structure and
``--help`` behaviour.
"""

import runpy

_STEPS = {
    "p01": "PhaseBias_01_Read_Data",
    "p02": "PhaseBias_02_Loop_Closures",
    "p03": "PhaseBias_03_calibration_pars",
    "p04": "PhaseBias_04_Inversion",
    "p05": "PhaseBias_05_Correction",
}


def _run(module_name: str) -> None:
    runpy.run_module(f"phasebias.{module_name}", run_name="__main__")


def p01() -> None:
    """PhaseBias_01_Read_Data: read wrapped ifgs + coherence."""
    _run(_STEPS["p01"])


def p02() -> None:
    """PhaseBias_02_Loop_Closures: calculate loop closures."""
    _run(_STEPS["p02"])


def p03() -> None:
    """PhaseBias_03_calibration_pars: estimate calibration parameters a_n."""
    _run(_STEPS["p03"])


def p04() -> None:
    """PhaseBias_04_Inversion: invert base-ifg phase biases."""
    _run(_STEPS["p04"])


def p05() -> None:
    """PhaseBias_05_Correction: apply the correction, write GeoTIFFs."""
    _run(_STEPS["p05"])
