import unittest
from part1 import process_weather, convert_f_to_c, calculate_mean


class Part1Tests(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.maxDiff = None
    
    def test_correct_output_5days_version_a(self):
        test_data = "data/forecast_5days_a.json"
        with open("tests/expected_output/forecast_5days_a_output.txt", encoding="utf8") as txt_file:
            expected_string = txt_file.read()
        result_string = process_weather(test_data)
        self.assertEqual(expected_string, result_string)

    def test_correct_output_5days_version_b(self):
        test_data = "data/forecast_5days_b.json"
        with open("tests/expected_output/forecast_5days_b_output.txt", encoding="utf8") as txt_file:
            expected_string = txt_file.read()
        result_string = process_weather(test_data)
        self.assertEqual(expected_string, result_string)

    def test_correct_output_10days(self):
        test_data = "data/forecast_8days.json"
        with open("tests/expected_output/forecast_8days_output.txt", encoding="utf8") as txt_file:
            expected_string = txt_file.read()
        result_string = process_weather(test_data)
        self.assertEqual(expected_string, result_string)

    def test_convert_f_to_c(self):
        self.assertEqual(convert_f_to_c(50), 10)
        self.assertEqual(convert_f_to_c(45), 7.2)
        self.assertEqual(convert_f_to_c(-2), -18.9)

    def test_calculate_mean(self):
        self.assertEqual(calculate_mean(50, 5), 10)
        self.assertEqual(calculate_mean(30, 9), 3.3)
        self.assertEqual(calculate_mean(32, 5), 6.4)
