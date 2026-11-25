"""InSAR phase-bias correction (Maghsoudi et al., 2022, RSE 275:113022).

Five-step pipeline:
  01 read data -> 02 loop closures -> 03 calibration pars -> 04 inversion -> 05 correction

Run the steps with the console entry points (``phasebias-01-read-data`` ...
``phasebias-05-correction``) from a working directory containing ``config.txt``.
"""

__version__ = "1.0.0"
