import unittest
from tests.part1_tests import Part1Tests

runner = unittest.TextTestRunner()

print("Running Tests...\n")
runner.run(unittest.TestSuite((unittest.makeSuite(Part1Tests))))
