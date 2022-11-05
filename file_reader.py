import os
from string import punctuation
import value_and_unit_searcher
import temperature
import voltage
import component

v_word = "V"
c_word = "°C"


def component_generator(file_path):
    current_component = component.component(model=file_path.split("\\")[-1].split(".")[0], temp=None, voltage=None)
    temperatures, voltages = [], []

    with open(file_path, "r") as file:
        lines = file.readlines()

        if len(lines) < 1:
            return current_component

        for line_number, line in enumerate(lines):
            line_handling(line, line_number, temperatures, voltages)

    try:
        post_processing(current_component, temperatures, voltages)
    except Exception as e:
        print(e)

    return current_component


def post_processing(current_component, temperatures, voltages):
    if len(temperatures) == 1:
        if len(temperatures[0].values) == 2:
            current_component.temp = temperature.temperature(lower_bound=temperatures[0].values[0],
                                                                                                                higher_bound=temperatures[0].values[1],
                                                                                                                unit=c_word)
    if len(voltages) == 1:
        if len(voltages[0].values) == 2:
            current_component.voltage = voltage.voltage(lower_bound=voltages[0].values[0],
                                                                                                higher_bound=voltages[0].values[1],
                                                                                                unit=v_word)


def line_handling(line, line_number, temperatures, voltages):
    split_line = line.split()
    voltage_found = voltage.voltage_per_line(line_number=line_number, values=[])
    temperature_found = temperature.temperature_per_line(line_number=line_number, values=[])

    for position, word in enumerate(split_line):
        current_word = word.upper().translate(str.maketrans('', '', punctuation))

        if c_word in current_word:
            value_and_unit_searcher.value_processing(temperature_found, current_word[0:len(current_word) - 2])

        if v_word == current_word:
            value_and_unit_searcher.value_processing(voltage_found, split_line[position - 1])

    if len(temperature_found.values) > 0:
        temperatures.append(temperature_found)

    if len(voltage_found.values) > 0:
        voltages.append(voltage_found)


if __name__ == '__main__':
    dir_path = "C:\\Cady\\Task example files\\Task example files"
    files = os.listdir(dir_path)
    print(component_generator(os.path.join(dir_path, files[2])))
