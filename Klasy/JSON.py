import json
import sys
import os



class JSONReader:
    def __init__(self, input_file_path, output_file_path):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.data = self.read_json_file()

    def read_json_file(self):
        if not os.path.isfile(self.input_file_path):
            self.create_input_file([])
        with open(self.input_file_path, 'r') as file:
            data = json.load(file)
        if isinstance(data, list):
            self.data = data
        else:
            self.data = [data]
        return self.data

    def modify_json_file(self, changes, new_values):
        for change in changes:
            values = change.split(',')
            if len(values) != 3:
                print(f"Nieprawidłowa zmiana: {change}. Oczekiwane 3 wartości"
                      f"oddzielone przecinkami")
                continue
            x, y, value = values
            if not x.isdigit():
                print(f"Nieprawidłowa zmiana {change}. Pierwszy argument musi"
                      f" być cyfrą.")
                continue
            x = int(x)
            if not y.isdigit():
                print(f"Nieprawidłowa zmiana {change}. Drugi argument musi"
                      f" być cyfrą.")
                continue
            y = int(y)

            if y >= len(self.data) or x >= len(self.data[y]):
                while y >= len(self.data):
                    self.data.append([])
                while x >= len(self.data[y]):
                    self.data[y].append('')
                self.data[y][x] = value
            else:
                self.data[y][x] = value

        for value in new_values:
            if len(value) >= 3:
                x, y, value = value
                if x.isdigit() and y.isdigit():
                    x = int(x)
                    y = int(y)
                    while y >= len(self.data):
                        self.data.append([])
                    while x >= len(self.data[y]):
                        self.data[y].append('')
                    self.data[y][x] = value

    def display_json_file(self):
        print(json.dumps(self.data, indent=4))

    def write_json_file(self):
        with open(self.output_file_path, 'w') as file:
            json.dump(self.data, file, indent=4)

    def create_input_file(self, values):
        if not os.path.isfile(self.input_file_path):
            with open(self.input_file_path, 'w') as file:
                json.dump(values, file, indent=4)
        else:
            print(f"Plik wejściowy '{self.input_file_path}' już istnieje. "
                  f"Nie tworzę nowego")


if __name__ == '__main__':
    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]
    changes = sys.argv[3:]
    new_values = [value.split(',') for value in sys.argv[4:]]

    csv_reader = JSONReader(input_file_path, output_file_path)
    csv_reader.create_input_file(new_values)
    csv_reader.modify_json_file(changes, new_values)
    csv_reader.display_json_file()
    csv_reader.write_json_file()
