# Longitudinal Stability Model

This folder contains the Python calculations used to examine how moving a suspended load forward changes the total rear support reaction of a stationary, rigid machine on level ground.

## Run

From the repository root, using Python 3.11 or later:

```bash
python -m unittest discover -s analysis/tests -v
python analysis/src/roversetter_stability.py
```

The model uses only the Python standard library. Seven unit tests check equilibrium, load-position sensitivity, input validation, and selected reference scenarios. GitHub Actions runs the same commands.

## Baseline

| Parameter | Value |
| --- | ---: |
| Machine mass | 40 kg (assumed) |
| Machine center-of-mass arm | 0.50 m (assumed) |
| Front/rear wheel-contact spacing | 1.29 m (current CAD design value) |
| Suspended load | ≈31.75 kg (from recalled ~70 lb) |
| Load overhangs | 0.25, 0.50 and 0.75 m (assumed positions) |

Running the script writes `analysis/data/hypothetical_v11_reproduced.csv`. This file contains calculated forces, not field measurements. `analysis/data/blank_classroom_trials.csv` is a blank template for a possible teacher-supervised tabletop study.

The analysis does not include chassis acceleration or suspended-load dynamics; the motor-startup behavior observed during Prototype 3 testing remains outside the model.
