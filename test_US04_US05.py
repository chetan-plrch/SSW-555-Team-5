import unittest
import parse
import datetime


class MyTestCase(unittest.TestCase):
    # US04: Marriage date before divorce date
    def test_US04_1(self):
        self.assertIsNone(parse.check_if_married_before_divorce('-', '-'))
        print('US04 Test Case #1 - Passed: Marriage date and divorce date are not present')

    def test_US04_2(self):
        self.assertEqual(parse.check_if_married_before_divorce('-', '1995-01-12'), 'ERROR: US04: Marriage date needs to be present if divorce date is present')
        print('US04 Test Case #2 - Passed: Marriage date is not present and divorce date is present')

    def test_US04_3(self):
        self.assertIsNone(parse.check_if_married_before_divorce('1995-01-12', '-'))
        print('US04 Test Case #3 - Passed: Marriage date is present and divorce date is not present')

    def test_US04_4(self):
        self.assertEqual(parse.check_if_married_before_divorce('1995-01-12', '1990-01-12'), 'ERROR: US04: Marriage date cannot be after divorce date')
        print('US04 Test Case #4 - Passed: Valid Scenario -  Marriage date is greater than divorce date')

    def test_US04_5(self):
        self.assertEqual(parse.check_if_married_before_divorce('1995-01-12', '1995-01-12'), 'ERROR: US04: Marriage date cannot be equal to divorce date')
        print('US04 Test Case #5 - Passed: Invalid Scenario - Marriage date is lesser than divorce date')


    # US05: Marriage date before death date
    def test_US05_1(self):
        self.assertIsNone(parse.check_if_married_before_death('-', '-'))
        print('US05 Test Case #1 - Passed: Marriage date and death date are not present')

    def test_US05_2(self):
        self.assertIsNone(parse.check_if_married_before_death(datetime.datetime.strptime('1995-01-12', '%Y-%d-%m').date(), '-'))
        print('US05 Test Case #3 - Passed: Marriage date is present and death date is not present')

    def test_US05_3(self):
        self.assertIsNone(parse.check_if_married_before_death('-', '01 FEB 1995'))
        print('US05 Test Case #2 - Passed: Marriage date is present and divorce date is not present')

    def test_US05_4(self):
        self.assertEqual(parse.check_if_married_before_death(datetime.datetime.strptime('1995-01-12', '%Y-%d-%m').date(), '01 JAN 1995'),
                         'ERROR: US05: Marriage date cannot be after death date')
        print('US05 Test Case #4 - Passed: Marriage date cannot be after death date')

    def test_US05_5(self):
        self.assertEqual(parse.check_if_married_before_death(datetime.datetime.strptime('1995-01-12', '%Y-%d-%m').date(), '01 DEC 1995'),
                         'ERROR: US05: Marriage date cannot be equal to death date')
        print('US05 Test Case #5 - Passed: Invalid Scenario - ERROR: US04: Marriage date cannot be equal to death date')

    def test_US05_6(self):
        self.assertIsNone(parse.check_if_married_before_death(datetime.datetime.strptime('1995-01-12', '%Y-%d-%m').date(), '12 FEB 1996'))
        print('US05 Test Case #6 - Passed: Valid Scenario - Marriage date is before death date')

if __name__ == '__main__':
    unittest.main()