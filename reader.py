import sys


class FileProcessor:
    def __init__(self, file_path, output_file_path):
        self.file_path = file_path
        self.output_file_path = output_file_path

    def process_csv(self, changes, new_values):
        from Klasy.CSV import CSVReader

        csv_reader = CSVReader(self.file_path, self.output_file_path)
        csv_reader.modify_csv_file(changes, new_values)
        csv_reader.display_csv_file()
        csv_reader.write_csv_file()

    def process_json(self, changes, new_values):
        from Klasy.JSON import JSONReader

        json_reader = JSONReader(self.file_path, self.output_file_path)
        json_reader.modify_json_file(changes, new_values)
        json_reader.display_json_file()
        json_reader.write_json_file()

    def process_pickle(self, changes, new_values):
        from Klasy.Pickle import PickleReader

        pickle_reader = PickleReader(self.file_path, self.output_file_path)
        pickle_reader.modify_pickle_file(changes, new_values)
        pickle_reader.display_pickle_file()
        pickle_reader.write_pickle_file()

    def process_txt(self, changes, new_values):
        from Klasy.TXT import TXTReader

        txt_reader = TXTReader(self.file_path, self.output_file_path)
        txt_reader.modify_txt_file(changes, new_values)
        txt_reader.display_txt_file()
        txt_reader.write_txt_file()


if __name__ == '__main__':
    file_path = sys.argv[1]
    output_file_path = sys.argv[2]
    changes = sys.argv[3:]
    new_values = [value.split(',') for value in sys.argv[4:]]

    file_processor = FileProcessor(file_path, output_file_path)
    file_extension = file_path.split('.')[-1]

    if file_extension == 'csv':
        file_processor.process_csv(changes, new_values)
    elif file_extension == 'json':
        file_processor.process_json(changes, new_values)
    elif file_extension == 'pickle':
        file_processor.process_pickle(changes, new_values)
    elif file_extension == 'txt':
        file_processor.process_txt(changes, new_values)
    else:
        print(f"Nie osługiwany format pliku: {file_extension}")
