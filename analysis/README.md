# Reproducible theoretical stability analysis

This folder contains a **stationary, gravity-only, level-ground** longitudinal model. It is not a real-machine load rating or a reconstruction of dynamic motor startup.

```bash
python -m unittest discover -s analysis/tests -v
python analysis/src/roversetter_stability.py
```

The script uses Python 3 standard library functions. It outputs `analysis/data/hypothetical_v11_reproduced.csv`, with signed rear reactions for three assumed overhangs. The `analysis/data/blank_classroom_trials.csv` is an intentionally empty log; no supervised experiment is claimed to have occurred.

| Assumption | Value | Evidence status |
| --- | --- | --- |
| Machine mass | 40 kg | Hypothetical |
| Machine center-of-mass arm | 0.50 m | Hypothetical |
| Fore-aft wheel spacing | 1.29 m | Digital design parameter, not as-built contact measurement |
| Stone mass | ≈31.75 kg | Approximation from recalled 70 lb |
| Overhangs | 0.25, 0.50, 0.75 m | Hypothetical scenarios |

The model predicts decreasing rear reaction with increasing suspended-load forward overhang. It **does not demonstrate** the original machine's static equilibrium or motor-startup mechanism.
