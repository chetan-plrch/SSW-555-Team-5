import unittest
import parse
import datetime

class MyTestCase(unittest.TestCase):
    def test_US39_1(self):
        # Test case: No upcoming anniversaries
        families = {
            'F1': [('HUSB', 'I1'), ('WIFE', 'I2'), ('MARR', '12 JAN 2020')],
            'F2': [('HUSB', 'I3'), ('WIFE', 'I4'), ('MARR', '15 FEB 2018')],
            'F3': [('HUSB', 'I5'), ('WIFE', 'I6'), ('MARR', '21 MAY 2019')],
        }
        individuals = {
            'I1': [('DEAT', '1 JAN 2023')],
            'I2': [('DEAT', '1 JAN 2022')],
            'I3': [('DEAT', '1 JAN 2022')],
            'I4': [('DEAT', '1 JAN 2022')],
            'I5': [('DEAT', '1 JAN 2022')],
            'I6': [('DEAT', '1 JAN 2022')],
        }
        result = parse.upcomingAnniversaries(families, individuals)
        self.assertEqual(result, None)
        print('US39 Test Case 1 Passed')

    def test_US39_2(self):
        # Test case: Upcoming anniversaries within 30 days
        families = {
            'F1': [('HUSB', 'I1'), ('WIFE', 'I2'), ('MARR', '12 AUG 2023')],
            'F2': [('HUSB', 'I3'), ('WIFE', 'I4'), ('MARR', '15 JUL 2023')],
            'F3': [('HUSB', 'I5'), ('WIFE', 'I6'), ('MARR', '21 SEP 2023')],
        }
        individuals = {
            'I1': [('DEAT', None)],
            'I2': [('DEAT', None)],
            'I3': [('DEAT', None)],
            'I4': [('DEAT', None)],
            'I5': [('DEAT', None)],
            'I6': [('DEAT', None)],
        }
        result = parse.upcomingAnniversaries(families, individuals)
        print("Result")
        print(result)
        expected_anniversaries = [
            datetime.datetime.strptime('12 AUG 2023', "%d %b %Y")
        ]
        self.assertEqual(result, expected_anniversaries)
        print('US39 Test Case 2 Passed')

    def test_US39_3(self):
        # Test case: No husband and wife alive in the family
        families = {
            'F1': [('HUSB', 'I1'), ('WIFE', 'I2'), ('MARR', '12 JAN 2019')],
            'F2': [('HUSB', 'I3'), ('WIFE', 'I4'), ('MARR', '15 FEB 2017')],
            'F3': [('HUSB', 'I5'), ('WIFE', 'I6'), ('MARR', '21 MAR 2020')],
        }
        individuals = {
            'I1': [('DEAT', '1 JAN 2022')],
            'I2': [('DEAT', '1 JAN 2022')],
            'I3': [('DEAT', '1 JAN 2022')],
            'I4': [('DEAT', '1 JAN 2022')],
            'I5': [('DEAT', '1 JAN 2022')],
            'I6': [('DEAT', '1 JAN 2022')],
        }
        result = parse.upcomingAnniversaries(families, individuals)
        self.assertEqual(result, None)
        print('US39 Test Case 3 Passed')

    def test_US39_4(self):
        # Test case: Multiple families with anniversaries on the same day
        families = {
            'F1': [('HUSB', 'I1'), ('WIFE', 'I2'), ('MARR', '05 SEP 2023')],
            'F2': [('HUSB', 'I3'), ('WIFE', 'I4'), ('MARR', '05 SEP 2018')],
            'F3': [('HUSB', 'I5'), ('WIFE', 'I6'), ('MARR', '05 SEP 2022')],
        }
        individuals = {
            'I1': [('DEAT', None)],
            'I2': [('DEAT', None)],
            'I3': [('DEAT', None)],
            'I4': [('DEAT', None)],
            'I5': [('DEAT', None)],
            'I6': [('DEAT', None)],
        }
        result = parse.upcomingAnniversaries(families, individuals)
        expected_anniversaries = [
            datetime.datetime.strptime('05 SEP 2023', "%d %b %Y"),
            datetime.datetime.strptime('05 SEP 2018', "%d %b %Y"),
            datetime.datetime.strptime('05 SEP 2022', "%d %b %Y")
        ]
        self.assertEqual(result, expected_anniversaries)
        print('US39 Test Case 4 Passed')

    def test_US39_5(self):
        # Test case: No anniversaries in any family
        families = {
            'F1': [('HUSB', 'I1'), ('WIFE', 'I2')],
            'F2': [('HUSB', 'I3'), ('WIFE', 'I4')],
            'F3': [('HUSB', 'I5'), ('WIFE', 'I6')],
        }
        individuals = {
            'I1': [('DEAT', None)],
            'I2': [('DEAT', None)],
            'I3': [('DEAT', None)],
            'I4': [('DEAT', None)],
            'I5': [('DEAT', None)],
            'I6': [('DEAT', None)],
        }
        result = parse.upcomingAnniversaries(families, individuals)
        self.assertEqual(result, None)
        print('US39 Test Case 5 Passed')
    
    def test_US39_6(self):
        # Test case: Anniversaries with different years
        families = {
            'F1': [('HUSB', 'I1'), ('WIFE', 'I2'), ('MARR', '12 AUG 2023')],
            'F2': [('HUSB', 'I3'), ('WIFE', 'I4'), ('MARR', '18 AUG 2022')],
            'F3': [('HUSB', 'I5'), ('WIFE', 'I6'), ('MARR', '01 SEP 2024')],
        }
        individuals = {
            'I1': [('DEAT', None)],
            'I2': [('DEAT', None)],
            'I3': [('DEAT', None)],
            'I4': [('DEAT', None)],
            'I5': [('DEAT', None)],
            'I6': [('DEAT', None)],
        }
        result = parse.upcomingAnniversaries(families, individuals)
        expected_anniversaries = [
            datetime.datetime.strptime('12 AUG 2023', "%d %b %Y"),
            datetime.datetime.strptime('18 AUG 2022', "%d %b %Y"),
            datetime.datetime.strptime('01 SEP 2024', "%d %b %Y")]
        self.assertEqual(result, expected_anniversaries)
        print('US39 Test Case 6 Passed')

    def test_US39_7(self):
        # Test case: Anniversaries with no death dates
        families = {
            'F1': [('HUSB', 'I1'), ('WIFE', 'I2'), ('MARR', '15 AUG 2023')],
            'F2': [('HUSB', 'I3'), ('WIFE', 'I4'), ('MARR', '05 JUN 2023')],
            'F3': [('HUSB', 'I5'), ('WIFE', 'I6'), ('MARR', '22 DEC 2023')],
        }
        individuals = {
            'I1': [('DEAT', None)],
            'I2': [('DEAT', None)],
            'I3': [('DEAT', None)],
            'I4': [('DEAT', None)],
            'I5': [('DEAT', None)],
            'I6': [('DEAT', None)],
        }
        result = parse.upcomingAnniversaries(families, individuals)
        expected_anniversaries = [
            datetime.datetime.strptime('15 AUG 2023', "%d %b %Y"),
        ]
        self.assertEqual(result, expected_anniversaries)
        print('US39 Test Case 7 Passed')

if __name__ == '__main__':
    unittest.main()