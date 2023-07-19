import csv
import sys
import os


class CSVReader:
    def __init__(self, input_file_path, output_file_path):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.data = self.read_csv_file()

    def read_csv_file(self):
        if not os.path.isfile(self.input_file_path):
            self.create_input_file([])
        with open(self.input_file_path, 'r') as file:
            data = list(csv.reader(file))
        return data

    def modify_csv_file(self, changes, new_values):
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
            if len(value) < 3:
                continue
            x, y, value = value[0], value[1], value[2]
            if not x.isdigit():
                continue
            x = int(x)
            if not y.isdigit():
                continue
            y = int(y)
            if y >= len(self.data):
                while y >= len(self.data):
                    self.data.append([])
            if x >= len(self.data[y]):
                while x >= len(self.data[y]):
                    self.data[y].append('')
            self.data[y][x] = value

    def display_csv_file(self):
        for row in self.data:
            print(','.join(row))

    def write_csv_file(self):
        with open(self.output_file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(self.data)

    def create_input_file(self, values):
        if not os.path.isfile(self.input_file_path):
            with open(self.input_file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(values)
        else:
            print(f"Plik wejściowy '{self.input_file_path}' już istnieje. "
                  f"Nie tworzę nowego")


if __name__ == '__main__':
    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]
    changes = sys.argv[3:]
    new_values = [value.split(',') for value in sys.argv[4:]]

    csv_reader = CSVReader(input_file_path, output_file_path)
    csv_reader.create_input_file(new_values)
    csv_reader.modify_csv_file(changes, new_values)
    csv_reader.display_csv_file()
    csv_reader.write_csv_file()
