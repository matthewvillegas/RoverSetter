# RoverSetter | Engineering Case Study

**Problem → prototype iterations → instability → investigation**

![RoverSetter CAD design](../images/roversetter-full-cad.png)

*CAD design view (not a photograph of a physical build).*

### Customer problem

In my monument business, a cemetery installation took approximately three to four hours using difficult-to-handle equipment, and a stone was damaged during the process. I began RoverSetter to investigate whether a compact mobile system could make handling and setting monuments more practical. The eventual 2,000 lb handling target was aspirational, not tested or certified.

### Three development iterations

**Prototype 1:** an initial mechanical proof of concept. **Prototype 2:** a revised arrangement after the initial mechanisms proved unsatisfactory. **Prototype 3:** an integrated mobile and positioning concept, including motorized chassis motion and forward hoist support. The exact mechanisms changed between the first two versions are not fully recoverable from surviving records, so I do not claim precise design modifications that I cannot substantiate.

### What happened during Prototype 3 testing

I recall testing with a roughly **70 lb** rectangular stone, approximately **16 in across**, **8 in front-to-back** and **6 in tall**. The stone was suspended beyond the front wheel line on a hard surface, with only the wheels bearing on the ground. Both rear wheels lifted nearly together while stationary, after which the chassis rocked and settled. Pitching became more pronounced immediately as the drive motors began accelerating the chassis forward.

![Prototype 3 CAD view](../images/prototype-3-cad.png)

*The test stone's approximate dimensions are recalled. Its position in this design view must not be treated as a recorded hook location or a measurement from the historical trial.*

This is a firsthand historical account. Original wheel forces, chassis mass distribution, acceleration history, suspension line, and video were not recovered.

### Engineering investigation

My later static analysis examined an assumption I had overlooked: a stone intended to move forward relative to the frame should be analyzed across its movement range, rather than at one fixed position. Under a simple rigid, level-ground, stationary model, the sum of rear support reactions follows

$$
N_{\mathrm{rear}} = \frac{MgL - mgd}{B}
$$

where `M` and `m` are machine and stone masses, `L` the machine restoring arm, `d` the stone's forward overhang, and `B` the front-rear wheel spacing. Keeping other assumptions constant gives `dN_rear/dd = -mg/B`: the calculated rear reaction declines as overhang grows.

![Free-body diagram](../images/free-body-diagram.png)

For **hypothetical**, not measured, `M=40 kg`, `L=0.50 m`, `B=1.29 m`, and `m≈31.75 kg`, the model produces:

| Assumed overhang | Predicted rear force |
| --- | ---: |
| 0.25 m | +91.7 N |
| 0.50 m | +31.4 N |
| 0.75 m | −29.0 N (assumed all-wheel static contact infeasible) |

![Theoretical overhang sensitivity](../images/model-overhang-sensitivity.png)

**The table and graph are theoretical outputs, not experimental records.** A negative signed force signifies that this assumed contact equilibrium is impossible; it is not an actual negative wheel contact force. The static analysis does not by itself explain the increased pitching at motor startup. That observation could involve additional transient or contact effects, but the original cause has not been established.

### Outcome

RoverSetter taught me to evaluate the **stability of the complete machine throughout its intended configurations**, rather than examining whether individual mechanisms move correctly. I can reproduce the mathematical sensitivity result and explain its assumptions. I cannot claim a measured historical tipping threshold, validated 2,000 lb capacity, or independent diagnosis of the original motor-startup event.

**Documentation:** [two-page PDF](RoverSetter_Two_Page_Case_Study.pdf) · [technical PDF](RoverSetter_Engineering_Research.pdf) · [CAD views](RoverSetter_CAD_Views.pdf) · [model code](../analysis/README.md) · [file history](../HISTORY.md).
