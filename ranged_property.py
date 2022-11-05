from dataclasses import dataclass


@dataclass
class ranged:
    lower_bound: float
    higher_bound: float

    def in_range(self, x):
        return self.lower_bound <= x <= self.higher_bound


