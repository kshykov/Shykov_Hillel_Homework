import csv
import json
from Shykov_Homework.hw_lesson_20.adapter.json_to_csv import JSONConverter


class TestJSONToCsv:

    def test_add_row(self):
        convert = JSONConverter()
        convert.read_file('example_test.json')
        convert.write_file('example_test.csv')
        test_row = ["Test", "Testovcih", 99, "TEST", 9999]
        row_to_assert = ["Test", "Testovcih", "99", "TEST", "9999"]

        with open('example_test.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            rows = [row for row in reader]
            rows_before = len(rows)


        convert.add_row('example_test.csv', test_row)

        with open('example_test.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            rows = [row for row in reader]
            rows_after = len(rows)

        assert rows_after > rows_before
        assert rows[-1] == row_to_assert

    def test_remove_row(self):
        convert = JSONConverter()
        with open('example_test.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            rows = [row for row in reader]
            rows_before = len(rows)

        convert.remove_row('example_test.csv', len(rows) - 1)

        with open('example_test.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            rows = [row for row in reader]
            rows_after = len(rows)

        assert rows_after < rows_before