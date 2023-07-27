import unittest
import parse
import datetime

class MyTestCase(unittest.TestCase):
    def test_US16_1(self):
        individuals = {
            'I1': [('NAME', 'John /Doe/'), ('SEX', 'M')],
            'I4': [('NAME', 'James /Doe/'), ('SEX', 'M')],
        }

        families = {
            'F1': [('HUSB', 'I1'), ('CHIL', 'I4')],
        }

        self.assertEqual(parse.maleLastNames(families, individuals), True)
        print('US16 Test Case 1 Passed: All Males in the family have the same last name')

    def test_US16_2(self):
        families = {
            'F1': [('HUSB', 'I1'), ('CHIL', 'I4')],
        }

        individuals = {
            'I1': [('NAME', 'John /Doe/'), ('SEX', 'M')],
            'I4': [('NAME', 'Michael /Smith/'), ('SEX', 'M')],
        }

        result = parse.maleLastNames(families, individuals)
        self.assertFalse(result)
        print('US16 Test Case 2 Passed: All Males in the family do not have the same last name')

    def test_US16_3(self):
        families = {
            'F1': [('HUSB', 'I1'), ('CHIL', 'I4')],
            'F2': [('HUSB', 'I7'), ('CHIL', 'I10'), ('CHIL', 'I11')],
        }

        individuals = {
            'I1': [('NAME', 'John /Doe/'), ('SEX', 'M')],
            'I4': [('NAME', 'James /Doe/'), ('SEX', 'M')],
            'I7': [('NAME', 'Michael /Smith/'), ('SEX', 'M')],
            'I10': [('NAME', 'David /Smith/'), ('SEX', 'M')],
            'I11': [('NAME', 'Robert /Smith/'), ('SEX', 'M')],
        }

        result = parse.maleLastNames(families, individuals)
        self.assertTrue(result)
        print('US16 Test Case 3 Passed: All Males in the family have the same last name')

    def test_US16_4(self):
        families = {
            'F1': [('HUSB', 'I1'), ('CHIL', 'I4')],
            'F2': [('HUSB', 'I7'), ('CHIL', 'I10'), ('CHIL', 'I11')],
        }

        individuals = {
            'I1': [('NAME', 'John /Doe/'), ('SEX', 'M')],
            'I4': [('NAME', 'Michael /Smith/'), ('SEX', 'M')],
            'I7': [('NAME', 'Michael /Smith/'), ('SEX', 'M')],
            'I10': [('NAME', 'David /Johnson/'), ('SEX', 'M')],
            'I11': [('NAME', 'Robert /Brown/'), ('SEX', 'M')],
        }

        result = parse.maleLastNames(families, individuals)
        self.assertFalse(result)
        print('US16 Test Case 4 Passed: All Males in the family do not have the same last name')

    def test_US16_5(self):
        families = {
            'F1': [('HUSB', 'I1')],
        }

        individuals = {
            'I1': [('NAME', 'John /Doe/'), ('SEX', 'M')],
        }

        result = parse.maleLastNames(families, individuals)
        self.assertTrue(result)
        print('US16 Test Case 5 Passed: No child in the family')

    def test_US16_6(self):
        families = {
            'F1': [('HUSB', 'I1'), ('CHIL', 'I2')],
        }

        individuals = {
            'I1': [('NAME', 'John /Doe/'), ('SEX', 'M')],
            'I2': [('NAME', 'Jane /Doe/'), ('SEX', 'F')],
        }

        result = parse.maleLastNames(families, individuals)
        self.assertTrue(result)
        print('US16 Test Case 6 Passed: Only female child in the family')

if __name__ == '__main__':
    unittest.main()