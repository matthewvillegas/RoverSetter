# RoverSetter

**Mobile monument handling | Mechanical design · CAD · Longitudinal stability**

[![Python tests](https://github.com/matthewvillegas/RoverSetter/actions/workflows/python-tests.yml/badge.svg)](https://github.com/matthewvillegas/RoverSetter/actions/workflows/python-tests.yml)

I started RoverSetter after a difficult cemetery monument installation took roughly **three to four hours** and damaged a stone. I wanted to develop a compact machine that could move across cemetery grounds and help position monuments more precisely. The long-term design target was **2,000 lb**; the prototypes did not demonstrate that capacity.

![RoverSetter CAD assembly](images/roversetter-full-cad.png)

*RoverSetter CAD assembly, current design export.*

## Design development

I built three physical prototype iterations, revising the mechanical approach as the project developed.

| Iteration | Engineering focus | Result |
| --- | --- | --- |
| **Prototype 1** | Initial mechanical handling concept | Established a starting arrangement; the early configuration was unsatisfactory. |
| **Prototype 2** | Revised mechanical layout | Further changes led to an integrated mobile concept. Detailed records of the early modifications are incomplete. |
| **Prototype 3** | Motorized chassis and forward hoist/positioning mechanism | Testing revealed a longitudinal stability problem. |

The physical prototypes were later dismantled or discarded. The images here are CAD drawings, not build photographs. See [Design History](HISTORY.md) for the project timeline and file history.

## Prototype 3: stability problem

During a test on hard ground, I suspended an approximately **70 lb** rectangular stone beyond the front wheel-contact line. I recall dimensions of about **16 in transverse × 8 in front-to-back × 6 in high**. The chassis was supported by its wheels, without the stabilizers carrying the load.

At rest, both rear wheels lifted nearly together and the chassis rocked before settling. When the drive motors began accelerating the machine forward, the forward pitching became more pronounced.

![Prototype 3 frame and test stone](images/prototype-3-cad.png)

*CAD frame-and-stone view. The stone dimensions reflect the test account; its pictured position is not a measured test coordinate.*

## Longitudinal stability analysis

I revisited the original stability assumption because the positioning mechanism could move a load forward relative to the wheelbase. A single static load position does not describe the full range of configurations.

For a rigid machine on level ground, taking moments about the front contact line gives:

$$
N_{\mathrm{rear}}=\frac{MgL-mgd}{B}
$$

Here, `M` is machine mass, `L` is the machine center-of-mass distance behind the front support, `m` is the suspended load mass, `d` is the forward load overhang, and `B` is the front-to-rear support spacing. With other quantities fixed:

$$
\frac{dN_{\mathrm{rear}}}{dd}=-\frac{mg}{B}
$$

This gives a linear decrease in the predicted rear support reaction as the load moves forward.

### Numerical study

The Python model uses a **hypothetical 40 kg machine**, a **0.50 m restoring arm**, a **1.29 m wheelbase**, and a load mass of approximately **31.75 kg** based on the test recollection. These parameters are not a measurement of the original machine's complete mass distribution.

| Assumed forward overhang | Calculated rear reaction |
| --- | ---: |
| 0.25 m | +91.7 N |
| 0.50 m | +31.4 N |
| 0.75 m | −29.0 N |

A negative signed reaction means the assumed all-wheel static equilibrium cannot exist; it does not represent a wheel exerting a downward force on the ground.

![Rear reaction versus forward overhang](images/model-overhang-sensitivity.png)

*Static-model predictions, not measured wheel loads.*

The static model explains the effect of forward overhang but does not establish why pitching increased during motor startup. That remains a separate dynamics problem involving unmeasured motion and contact forces.

## Technical material

- [Engineering case study](docs/CASE_STUDY.md) — development, test observations, and findings
- [Two-page case study (PDF)](docs/RoverSetter_Two_Page_Case_Study.pdf)
- [Technical report (PDF)](docs/RoverSetter_Engineering_Research.pdf)
- [CAD views (PDF)](docs/RoverSetter_CAD_Views.pdf)
- [Engineering notes](docs/ENGINEERING_NOTES.md) — assumptions, test conditions, and open questions
- [Python analysis](analysis/README.md) — model, scenarios, and tests
- [Design history](HISTORY.md) — prototype evolution and current CAD files

### Run the analysis

Requires Python 3.11 or later; no external Python packages are required.

```bash
python -m unittest discover -s analysis/tests -v
python analysis/src/roversetter_stability.py
```

The repository includes **seven unit tests** and a GitHub Actions workflow that runs both commands.

## Project status

Three physical prototype iterations were completed. The third revealed a stability issue under a small suspended load. I subsequently developed a reproducible static model to investigate forward load position. The original machine's wheel reactions and startup dynamics were not measured, and a full-scale 2,000 lb system has not been validated.

The full CAD source and STEP archives are stored separately from this public technical summary. No commercial lifting rating is claimed for the design.
