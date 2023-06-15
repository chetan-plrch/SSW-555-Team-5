import unittest
import parse
import datetime

class MyTestCase(unittest.TestCase):
    def test_US02_1(self):
        self.assertIsNone(parse.check_if_birth_before_marriage('-', '-'))
        print('US02 Test Case 1 Passed: Birth date and marriage date are not present')

    def test_US02_2(self):
        self.assertEqual(parse.check_if_birth_before_marriage('-', '1997-09-12'), 'Birth Date needs to be present if marriage date is present')
        print('US02 Test Case 2 Passed: Birth date is not present and marriage date is present')

    def test_US02_3(self):
        self.assertIsNone(parse.check_if_birth_before_marriage('2005-08-08', '-'))
        print('US02 Test Case 3 Passed: Birth date is present and marriage date is not present')

    def test_US02_4(self):
        self.assertEqual(parse.check_if_birth_before_marriage('1998-07-11', '1992-09-11'), 'Birth date cannot be after marriage date')
        print('US02 Test Case 4 Passed: Birth date should not be after marriage date')

    def test_US02_5(self):
        self.assertEqual(parse.check_if_birth_before_marriage('2005-09-01', '2005-09-01'), 'Birth date cannot be same as marriage date')
        print('US02 Test Case 5 Passed: Birth date should not be same as marriage date')


    def test_US03_1(self):
        self.assertIsNone(parse.check_if_birth_before_death('-', '-'))
        print('US03 Test Case 1 Passed: Birth date and death date are not present')

    def test_US03_2(self):
        self.assertIsNone(parse.check_if_birth_before_death(datetime.datetime.strptime('1998-29-06', '%Y-%d-%m').date(), '-'))
        print('US03 Test Case 2 Passed: Birth date is present and death date is not present')

    def test_US03_3(self):
        self.assertEqual(parse.check_if_birth_before_death('-', '01 FEB 1995'), 'Birth Date needs to be present if death date is present')
        print('US03 Test Case 3 Passed: Birth date is not present and death date is present')

    def test_US03_4(self):
        self.assertEqual(parse.check_if_birth_before_death(datetime.datetime.strptime('1998-15-08', '%Y-%d-%m').date(), '01 JAN 1995'),
                         'Birth date cannot be after death date')
        print('US03 Test Case 4 Passed: Birth date cannot be after death date')

    def test_US03_5(self):
        self.assertEqual(parse.check_if_birth_before_death(datetime.datetime.strptime('1999-14-11', '%Y-%d-%m').date(), '14 NOV 1999'),
                         'Birth date cannot be same as death date')
        print('US04 Test Case 5 Passed: Birth date cannot be same as death date')

    def test_US03_6(self):
        self.assertIsNone(parse.check_if_birth_before_death(datetime.datetime.strptime('1995-01-12', '%Y-%d-%m').date(), '12 FEB 2012'))
        print('US04 Test Case 6 Passed: Birth date is before death date')        
        
if __name__ == '__main__':
    unittest.main()


