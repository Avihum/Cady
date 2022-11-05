import file_reader
import os

if __name__ == '__main__':
    dir_path = "C:\\Cady\\Task example files\\Task example files"
    files = os.listdir(dir_path)
    components = []
    for file in files:
        components.append(file_reader.component_generator(os.path.join(dir_path, file)))
    for component in components:
        print(component)

