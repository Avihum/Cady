from dataclasses import dataclass
from temperature import temperature
from voltage import voltage


@dataclass
class component:
    model: str
    temp: temperature
    voltage: voltage

    # manufacturer: str

    def __post_init__(self):
        if self.temp:
            self.temp = temperature(self.temp[0], self.temp[1], self.temp[2])
        if self.voltage:
            self.voltage = voltage(self.voltage[0], self.voltage[1], self.voltage[2])

    def __repr__(self):
        return f"Component:\n\tModel: {self.model}\n\tTemperature: {self.temp}\n\tVoltage: {self.voltage}\n"

    def is_safe_to_use_temp(self, working_temperature: float) -> tuple[bool, str]:
        result = False
        cause = "Feature not supported yet, thank you for your patience! "
        if working_temperature and self.temp:
            result = self.temp.lower_bound <= working_temperature <= self.temp.higher_bound
            cause = 'Valid check'
        return result, cause

    def is_safe_to_use_voltage(self, working_voltage: float) -> tuple[bool, str]:
        result = False
        cause = "Feature not supported yet, thank you for your patience! "
        if working_voltage and self.voltage:
            result = self.voltage.lower_bound <= working_voltage <= self.voltage.higher_bound
            cause = 'Valid check'
        return result, cause


if __name__ == '__main__':
    temporary_temperature = [-40, 125, "celsius"]
    temporary_voltage = [2.4, 5.1, "volt"]

    component_1 = component(model="some_model", temp=temporary_temperature, voltage=temporary_voltage)
    component_2 = component(model="some_model", temp=None, voltage=None)

    print(component_1.is_safe_to_use_temp(10))
    print(component_1.is_safe_to_use_temp(125))
    print(component_1.is_safe_to_use_temp(126))
    print(component_1.is_safe_to_use_voltage(3))
    print(component_1.is_safe_to_use_voltage(2.4))
    print(component_1.is_safe_to_use_voltage(2))
    print(component_2)
    try:
        assert component_1.temp.in_range(60), "out of range"
    except Exception as e:
        print(e)
