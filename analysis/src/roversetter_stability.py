"""RoverSetter educational retrospective model. NOT a heavy-lift machine specification.

All numerical parameters are hypothetical unless explicitly identified as a user
recollection. Stationary, level, rigid-body, gravity-only static equilibrium.
No dynamic, deflection, joint, traction or real-machine safety inference.
"""
from __future__ import annotations
from dataclasses import dataclass
import csv
import math
from pathlib import Path

G = 9.81
RECALLED_TEST_MASS_KG = 70 * 0.45359237  # from approximate 70 lb historical recollection

@dataclass(frozen=True)
class StaticModel:
    machine_mass_kg: float
    restoring_arm_m: float  # machine COM behind front wheel line
    load_mass_kg: float
    wheelbase_m: float
    g: float = G

    def __post_init__(self):
        for field in ('machine_mass_kg','restoring_arm_m','load_mass_kg','wheelbase_m','g'):
            if getattr(self,field) <= 0 or not math.isfinite(getattr(self,field)):
                raise ValueError(f'{field} must be positive and finite')

    def state(self, overhang_m: float) -> dict:
        """Signed unconstrained statics; negative reaction is NOT physical."""
        if overhang_m < 0 or not math.isfinite(overhang_m):
            raise ValueError('overhang_m must be finite and nonnegative')
        machine_moment = self.machine_mass_kg*self.g*self.restoring_arm_m
        load_moment = self.load_mass_kg*self.g*overhang_m
        net = machine_moment-load_moment
        rear_unconstrained = net/self.wheelbase_m
        front_unconstrained = (self.machine_mass_kg+self.load_mass_kg)*self.g-rear_unconstrained
        lam=load_moment/machine_moment
        return {'overhang_m': overhang_m,
                'restoring_Nm': machine_moment,'overturning_Nm':load_moment,
                'net_restoring_Nm':net,'lambda':lam,
                'rear_unconstrained_N':rear_unconstrained,
                'front_unconstrained_N':front_unconstrained,
                'rear_status':'positive' if rear_unconstrained>1e-8 else ('zero' if rear_unconstrained>=-1e-8 else 'infeasible_four_contact_static'),
                'historical':'NO - ASSUMED GEOMETRY AND MACHINE MASS'}

    def critical_overhang_m(self) -> float:
        """Mathematical zero-rear-reaction point; NOT safe travel or rated limit."""
        return self.machine_mass_kg*self.restoring_arm_m/self.load_mass_kg

    def slope_rear_force_per_m(self) -> float:
        return -self.load_mass_kg*self.g/self.wheelbase_m


def with_carriage(remaining_machine_mass_kg: float, machine_arm_m: float,
                 carriage_mass_kg: float, carriage_arm_at_zero_m: float,
                 suspended_mass_kg: float, initial_overhang_m: float,
                 travel_forward_m: float, wheelbase_m: float, g: float=G):
    """Illustrative carriage translating with suspended load.

    All positions relative to stationary chassis front wheel line.
    Assumes carriage COM travels forward by x and load line moves forward by x.
    Only a quasi-static gravity model. Not motor-startup dynamics.
    """
    values=[remaining_machine_mass_kg,machine_arm_m,carriage_mass_kg,
            suspended_mass_kg,wheelbase_m,g]
    if any(not math.isfinite(v) or v<=0 for v in values):
        raise ValueError('physical mass, restoring arm, wheelbase and g must be positive')
    if initial_overhang_m < 0 or travel_forward_m < 0 or not math.isfinite(travel_forward_m):
        raise ValueError('distances must be nonnegative')
    carriage_arm=carriage_arm_at_zero_m-travel_forward_m
    load_overhang=initial_overhang_m+travel_forward_m
    net = g*(remaining_machine_mass_kg*machine_arm_m+carriage_mass_kg*carriage_arm-suspended_mass_kg*load_overhang)
    return {'travel_forward_m':travel_forward_m,'carriage_arm_m':carriage_arm,
            'load_overhang_m':load_overhang, 'net_restoring_Nm':net,
            'rear_unconstrained_N':net/wheelbase_m,
            'rear_slope_N_per_m':-(carriage_mass_kg+suspended_mass_kg)*g/wheelbase_m}


def write_scenarios(destination: Path) -> None:
    model = StaticModel(40,0.5,RECALLED_TEST_MASS_KG,1.29)
    rows=[model.state(d) for d in (0.25,0.50,0.75)]
    with destination.open('w', newline='',encoding='utf-8') as handle:
        writer=csv.DictWriter(handle,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)

if __name__ == '__main__':
    base=Path(__file__).resolve().parents[1]
    write_scenarios(base/'data'/'hypothetical_v11_reproduced.csv')
    model=StaticModel(40,0.5,RECALLED_TEST_MASS_KG,1.29)
    for d in (0.25,0.50,0.75):
        z=model.state(d)
        print(f"d={d:.2f} m lambda={z['lambda']:.3f} signed rear={z['rear_unconstrained_N']:+.1f} N")
    print('No experimental measurements in this project package.')
