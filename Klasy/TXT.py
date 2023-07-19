import os


class TXTReader:
    def __init__(self, input_file_path, output_file_path):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.data = self.read_txt_file()

    def read_txt_file(self):
        if not os.path.isfile(self.input_file_path):
            self.create_input_file('')
        with open(self.input_file_path, 'r') as file:
            data = file.readlines()
        self.data = [line.strip() for line in data]
        return self.data

    def modify_txt_file(self, changes, new_values):
        for change in changes:
            values = change.split(',')
            if len(values) != 3:
                print(f"Nieprawidłowa zmiana: {change}. Oczekiwane 3 wartości "
                      f"oddzielone przecinkami")
                continue
            x, y, value = values
            if not x.isdigit():
                print(f"Nieprawidłowa zmiana {change}. Pierwszy argument "
                      f"musi być cyfrą.")
                continue
            x = int(x)
            if not y.isdigit():
                print(f"Nieprawidłowa zmiana {change}. Drugi argument musi "
                      f"być cyfrą.")
                continue
            y = int(y)

            if y >= len(self.data):
                while y >= len(self.data):
                    self.data.append('')
            if x >= len(self.data[y]):
                while x >= len(self.data[y]):
                    self.data[y] += ' '
            self.data[y] = self.data[y][:x] + value + self.data[y][x + 1:]

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
                    self.data.append('')
            if x >= len(self.data[y]):
                while x >= len(self.data[y]):
                    self.data[y] += ' '
            self.data[y] = self.data[y][:x] + value + self.data[y][x + 1:]

    def display_txt_file(self):
        for line in self.data:
            print(line)

    def write_txt_file(self):
        with open(self.output_file_path, 'w') as file:
            file.write('\n'.join(self.data))

    def create_input_file(self, value):
        if not os.path.isfile(self.input_file_path):
            with open(self.input_file_path, 'w') as file:
                file.write(value)
        else:
            print(f"Plik wejściowy '{self.input_file_path}' już istnieje. "
                  f"Nie tworzę nowego")
