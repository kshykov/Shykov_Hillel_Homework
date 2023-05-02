import csv
import json


class JSONConverter:
    def __init__(self):
        self.__lines = []

    def read_file(self, filename:str):
        with open(filename, 'r') as json_file:
            cont = json_file.read()
            lines = json.loads(cont)
            for line in lines:
                self.__lines.append(line)


    def write_file(self, filename:str):
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            header = list(self.__lines[0].keys())
            writer.writerow(header)

            for line in self.__lines:
                data_row = list(line.values())
                writer.writerow(data_row)

    def add_row(self, filename:str, row):
        with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(row)

    def remove_row(self, filename:str, row_index):
        with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            rows = [row for row in reader]

        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            for index, row in enumerate(rows):
                if index != row_index:
                    writer.writerow(row)


# test_row = ["Test", "Testovcih", 99, "TEST", 9999]
# convert = JSONConverter()
# convert.read_file('example1.json')
# convert.write_file('example1.csv')
# convert.add_row('example1.csv', test_row)
# convert.remove_row('example1.csv', [-1])
# convert.remove_row('example1.csv', [-1])