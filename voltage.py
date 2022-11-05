from dataclasses import dataclass
from ranged_property import ranged
from enum import Enum
from enum import unique


@unique
class voltage_units(Enum):
    volt = "V"
    millivolt = "mV"


@dataclass
class voltage(ranged):
    unit: str
    #
    # def __post_init__(self):
    #     self.unit = eval(f"voltage_units.{self.unit.lower()}")


@dataclass
class voltage_per_line:
    line_number: str
    values: [str]


if __name__ == '__main__':
    x = voltage(4, 5, "volt")
    print(x)
