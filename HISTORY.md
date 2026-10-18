# Design History

RoverSetter developed from a monument-handling problem I encountered through my business. I worked through three physical versions before returning to the stability calculations and documenting the results in this repository.

## Prototype development

| Stage | What I worked on |
| --- | --- |
| **Initial concept** | Explored a mechanical approach to transporting and positioning cemetery monuments after a difficult installation. |
| **Prototype 1** | Built an initial mechanical proof of concept. The arrangement did not meet what I wanted from the machine. |
| **Prototype 2** | Revised the mechanism and layout. I no longer have a reliable component-by-component record of those changes. |
| **Prototype 3** | Combined a motorized chassis with a forward hoist/positioning concept. The small-stone test revealed pitching instability. |
| **Follow-up analysis** | Revisited front/rear reactions using moment equilibrium and a Python model of load-position sensitivity. |

## Prototype 3 test

The test used an approximately 70 lb stone suspended forward of the front wheels on hard ground. With only the wheels supporting the machine, both rear wheels rose nearly together and the frame rocked and settled. The pitching increased when the chassis motors started accelerating forward.

I did not retain instrumented measurements of the wheel forces, chassis mass distribution, hook location, or motor-startup motion. The exact cause of the startup response remains open.

## CAD files

I continued working with the existing RoverSetter models, saving and exporting updated versions as I reorganized the project. I deleted an older project folder during that process. The available CAD drawings show the design as maintained in the current files; their export dates are not the dates of the first physical builds.

The current CAD is design documentation. It does not establish the exact stone position or hook geometry used in the physical test. I keep the larger original-file archive separately from this public repository.

## Engineering outcome

The analysis clarified a problem with evaluating stability at only one load position. In a gravity-only static model, advancing a suspended load beyond the front support decreases the calculated rear reaction. The separate motor-startup behavior needs dynamic measurements to investigate further.
