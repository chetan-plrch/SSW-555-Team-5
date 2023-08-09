import unittest
import parse
import datetime

class MyTestCase(unittest.TestCase):
    def test_US38_1(self):
        # Test case: Upcoming birthdays within 30 days
        individuals = {
            'I1': [('DATE', '12 AUG 1985'), ('DEAT', None)],
            'I2': [('DATE', '05 SEP 1990'), ('DEAT', None)],
            'I3': [('DATE', '30 JUN 1978'), ('DEAT', '15 AUG 2010')],
        }
        result = parse.upcomingBirthdays(individuals)
        expected_birthdays = [
            datetime.datetime.strptime('12 AUG 1985', "%d %b %Y"),
            datetime.datetime.strptime('05 SEP 1990', "%d %b %Y"),
            None
        ]
        self.assertEqual(result, expected_birthdays)
        print('US39 Test Case 1 Passed')

    def test_US38_2(self):
        individuals = {
            'I1': [('DATE', '12 AUG 1985'), ('DEAT', None)],
            'I2': [('DATE', '05 JUL 1990'), ('DEAT', None)],
            'I3': [('DATE', '30 JUN 1978'), ('DEAT', '15 AUG 2010')],
        }
        result = parse.upcomingBirthdays(individuals)
        expected_birthdays = [
            datetime.datetime.strptime('12 AUG 1985', "%d %b %Y"),
            None, None
        ]
        self.assertEqual(result, expected_birthdays)
        print('US39 Test Case 2 Passed')

    def test_US38_3(self):
        # Test case: No upcoming birthdays
        individuals = {
            'I1': [('DATE', '12 JAN 1990'), ('DEAT', None)],
            'I2': [('DATE', '05 FEB 1985'), ('DEAT', None)],
            'I3': [('DATE', '30 MAR 1978'), ('DEAT', None)],
        }
        result = parse.upcomingBirthdays(individuals)
        expected_birthdays = [None] * len(individuals)
        self.assertEqual(result, expected_birthdays)
        print('US39 Test Case 3 Passed')

    def test_US38_4(self):
        # Test case: Upcoming birthdays of deceased individuals
        individuals = {
            'I1': [('DATE', '12 DEC 1980'), ('DEAT', '15 SEP 2010')],
            'I2': [('DATE', '05 JAN 1975'), ('DEAT', '30 JUN 2005')],
            'I3': [('DATE', '30 MAR 1992'), ('DEAT', '20 MAY 2020')],
        }
        result = parse.upcomingBirthdays(individuals)
        expected_birthdays = [None] * len(individuals)
        self.assertEqual(result, expected_birthdays)
        print('US39 Test Case 4 Passed')

    def test_US38_5(self):
        individuals = {
            'I1': [('DATE', '12 AUG 1985'), ('DEAT', None)],
            'I2': [('DATE', '05 JUL 1990'), ('DEAT', None)],
            'I3': [('DATE', '30 JUN 1978'), ('DEAT', '15 AUG 2010')],
        }
        result = parse.upcomingBirthdays(individuals)
        expected_birthdays = [
            datetime.datetime.strptime('12 AUG 1985', "%d %b %Y"),
            None, None
        ]
        self.assertEqual(result, expected_birthdays)
        print('US39 Test Case 5 Passed')

    def test_US38_6(self):
        # Test case: No upcoming birthdays
        individuals = {
            'I1': [('DATE', '12 JAN 1990'), ('DEAT', None)],
            'I2': [('DATE', '05 FEB 1985'), ('DEAT', None)],
            'I3': [('DATE', '30 MAR 1978'), ('DEAT', None)],
        }
        result = parse.upcomingBirthdays(individuals)
        expected_birthdays = [None] * len(individuals)
        self.assertEqual(result, expected_birthdays)
        print('US39 Test Case 6 Passed')

    def test_US38_7(self):
        # Test case: Upcoming birthdays of deceased individuals
        individuals = {
            'I1': [('DATE', '12 DEC 1980'), ('DEAT', '15 SEP 2010')],
            'I2': [('DATE', '05 JAN 1975'), ('DEAT', '30 JUN 2005')],
            'I3': [('DATE', '30 MAR 1992'), ('DEAT', '20 MAY 2020')],
        }
        result = parse.upcomingBirthdays(individuals)
        expected_birthdays = [None] * len(individuals)
        self.assertEqual(result, expected_birthdays)
        print('US39 Test Case 7 Passed')

    def test_US38_8(self):
        # Test case: Upcoming birthdays on the same day
        individuals = {
            'I1': [('DATE', '12 AUG 1990'), ('DEAT', None)],
            'I2': [('DATE', '25 AUG 1985'), ('DEAT', None)],
            'I3': [('DATE', '08 SEP 1970'), ('DEAT', None)],
        }
        result = parse.upcomingBirthdays(individuals)
        expected_birthdays = [
            datetime.datetime.strptime('12 AUG 1990', "%d %b %Y"),
            datetime.datetime.strptime('25 AUG 1985', "%d %b %Y"),
            datetime.datetime.strptime('08 SEP 1970', "%d %b %Y"),
        ]
        self.assertEqual(result, expected_birthdays)
        print('US39 Test Case 8 Passed')

if __name__ == '__main__':
    unittest.main()