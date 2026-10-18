# Engineering Notes

## Model scope

The Python model represents a rigid stationary chassis on level ground. It uses vertical forces and longitudinal moments about the front wheel-contact line. Lateral load sharing, suspension compliance, structural flexibility, swinging loads, drivetrain effects, and acceleration are outside this calculation.

### Reference calculation

| Quantity | Baseline | Source |
| --- | ---: | --- |
| Machine mass, `M` | 40 kg | Assumed example |
| Machine COM arm, `L` | 0.50 m | Assumed example |
| Front–rear support spacing, `B` | 1.29 m | Current CAD design dimension; physical contact spacing unmeasured |
| Suspended stone, `m` | ≈31.75 kg | Approximate conversion of the recalled 70 lb stone |
| Forward overhang, `d` | 0.25, 0.50, 0.75 m | Example positions, not test measurements |

The signed rear reaction is `N_rear = (M*g*L - m*g*d)/B`. Once it becomes negative, the original four-contact equilibrium assumed in the equation is infeasible. Individual wheel loads cannot be determined from this two-support model.

## Prototype 3 test record

**Conditions:** hard surface, approximately 70 lb suspended stone forward of the front wheels, wheels supporting the chassis.

**Observed:** both rear wheels rose nearly together, the chassis rocked and settled, and forward pitching increased during drive-motor startup.

**Measurements not retained:** machine weight and COM, actual hook overhang, wheel-force histories, motor torque, vehicle acceleration, and stone swing.

## Open engineering questions

- How did the actual center of mass shift between the prototype's operating positions?
- What was the load's horizontal offset during the test?
- How much of the startup response came from load motion, tire contact, frame compliance, and drivetrain reaction?
- How would uneven ground change the support conditions?

The 2,000 lb target remains a design objective, not a measured or rated capability. The existing records do not support using these models as operating limits for a real lifting machine.
