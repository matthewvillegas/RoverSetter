# RoverSetter — Engineering Case Study

**Mobile monument handling: three prototypes and a longitudinal stability investigation**

![RoverSetter CAD assembly](../images/roversetter-full-cad.png)

*RoverSetter CAD design, current export.*

## The problem

A cemetery monument installation through my business took roughly three to four hours, and the stone was damaged during handling. I started RoverSetter to explore a smaller machine for monument transport and positioning, particularly where access and terrain make conventional equipment difficult to use. The long-term design target was 2,000 lb.

## Prototype development

I developed RoverSetter across three physical iterations:

- **Prototype 1 (Apr–May 2025):** Near the end of sophomore year, I built the first mechanical concept. The mechanisms felt awkward and were not as smooth in operation as I wanted.
- **Prototype 2 (Summer 2025):** I revised the mechanisms and layout. It operated better, but I was still dissatisfied with the build's strength and readiness for the intended application.
- **Prototype 3 (Summer 2026):** I further refined the mechanisms and overall construction, combining motorized chassis movement with forward load positioning. This was my most developed iteration, although its small-stone test exposed a longitudinal stability problem.

I no longer have a complete component-by-component record of the first two builds. The clearest test account I retained comes from Prototype 3.

## Prototype 3 test

I tested the machine on hard ground with a stone weighing approximately 70 lb. The stone was roughly 16 in across the chassis, 8 in front-to-back and 6 in high. It was suspended ahead of the front wheel-contact line, and the chassis was supported on its wheels.

Both rear wheels lifted almost together while stationary, and the chassis rocked before settling. When I started the drive motors and the machine accelerated forward, the pitching increased.

![Prototype 3 CAD view](../images/prototype-3-cad.png)

*CAD frame and stone geometry; the exact test overhang was not measured.*

The test did not include calibrated wheel-load measurements, motion tracking, or a measured machine center of mass. I therefore treated the physical behavior and the subsequent calculations as two separate sets of information.

## Static analysis

The machine was intended to move a suspended monument forward relative to the chassis. I had originally considered stability at a fixed load position; the follow-up investigation considered how the longitudinal reaction changes as the load advances.

Taking moments about the front wheel-contact line for a rigid stationary machine on level ground:

$$
N_{\mathrm{rear}}=\frac{MgL-mgd}{B}
$$

`M` is machine mass, `L` is its center-of-mass arm behind the front wheels, `m` is suspended load mass, `d` is forward overhang, and `B` is front-to-rear wheel-contact spacing.

The sensitivity is:

$$
\frac{dN_{\mathrm{rear}}}{dd}=-\frac{mg}{B}
$$

![Free-body diagram](../images/free-body-diagram.png)

For a sample calculation with **assumed** machine mass 40 kg, COM arm 0.50 m, and wheelbase 1.29 m, using approximately 31.75 kg as the test-load equivalent:

| Forward overhang | Calculated rear reaction |
| --- | ---: |
| 0.25 m | +91.7 N |
| 0.50 m | +31.4 N |
| 0.75 m | −29.0 N |

![Rear reaction from the static model](../images/model-overhang-sensitivity.png)

*Calculated scenario results. They are not force measurements from Prototype 3.*

At 0.75 m, the signed solution is negative. That indicates the assumed four-contact static state is no longer possible; it is not an actual negative normal force.

## What I learned

A working mechanism does not guarantee a stable machine across its full range of motion. Moving a suspended load forward changes the overall moment balance even if the chassis does not move. The gravity-only model explains that trend, but it does not explain the stronger pitching I observed at motor startup.

The next meaningful step is an independently reviewed, low-risk classroom mechanics experiment comparing measured support reactions with the model's predicted trend. It would test the statics calculation, not the original heavy equipment.

**Files:** [Technical report](RoverSetter_Engineering_Research.pdf) · [CAD drawings](RoverSetter_CAD_Views.pdf) · [Engineering notes](ENGINEERING_NOTES.md) · [Python model](../analysis/README.md)
