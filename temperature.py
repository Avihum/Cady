from dataclasses import dataclass
from ranged_property import ranged
from enum import Enum
from enum import unique


@unique
class temperature_units(Enum):
    celsius = "c"
    fahrenheit = "f"
    kelvin = "k"


@dataclass
class temperature(ranged):
    unit: str
    #
    # def __post_init__(self):
    #     self.unit = eval(f"temperature_units.{self.unit.lower()}")

    # TODO units conversions
    # def c_to_k(self):
    #     pass


@dataclass
class temperature_per_line:
    line_number: str
    values: [str]


if __name__ == '__main__':
    x = temperature(4, 5, "celsius")
    print(x)
