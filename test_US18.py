import unittest
import parse
import datetime

families = {'F1': [('HUSB', 'I3'), ('WIFE', 'I2'), ('CHIL', 'I1'), ('CHIL', 'I4'), ('MARR', '12 JAN 1995')], 'F2': [('HUSB', 'I7'), ('WIFE', 'I5'), ('CHIL', 'I2'), ('CHIL', 'I8'), ('MARR', '12 SEP 1968')], 'F3': [('HUSB', 'I10'), ('WIFE', 'I9'), ('CHIL', 'I3'), ('MARR', '12 FEB 1970')], 'F4': [('HUSB', 'I6'), ('WIFE', 'I5'), ('CHIL', 'I11'), ('MARR', '12 SEP 1980')], 'F5': [('HUSB', 'I12'), ('WIFE', 'I13'), ('CHIL', 'I5'), ('MARR', '2 FEB 1948')], 'F6': [('HUSB', 'I15'), ('WIFE', 'I14'), ('CHIL', 'I10'), ('MARR', '12 SEP 1950')]}
families2 = {'F2': [('HUSB', 'I7'), ('WIFE', 'I5'), ('CHIL', 'I2'), ('CHIL', 'I8'), ('MARR', '12 SEP 1968')], 'F3': [('HUSB', 'I10'), ('WIFE', 'I9'), ('CHIL', 'I3'), ('MARR', '12 FEB 1970')], 'F4': [('HUSB', 'I6'), ('WIFE', 'I5'), ('CHIL', 'I11'), ('MARR', '12 SEP 1980')], 'F5': [('HUSB', 'I12'), ('WIFE', 'I13'), ('CHIL', 'I5'), ('MARR', '2 FEB 1948')], 'F6': [('HUSB', 'I15'), ('WIFE', 'I14'), ('CHIL', 'I10'), ('MARR', '12 SEP 1950')]}
families3 = {
    'F1': [('HUSB', 'I3'), ('WIFE', 'I2'), ('CHIL', 'I1'), ('CHIL', 'I4'), ('MARR', '12 JAN 1995')],
    'F2': [('HUSB', 'I7'), ('WIFE', 'I5'), ('CHIL', 'I2'), ('CHIL', 'I8'), ('MARR', '12 SEP 1968')],
    'F3': [('HUSB', 'I10'), ('WIFE', 'I9'), ('CHIL', 'I3'), ('MARR', '12 FEB 1970')],
    'F4': [('HUSB', 'I6'), ('WIFE', 'I5'), ('CHIL', 'I11'), ('MARR', '12 SEP 1980')],
    'F5': [('HUSB', 'I12'), ('WIFE', 'I13'), ('CHIL', 'I5'), ('MARR', '2 FEB 1948')],
    'F6': [('HUSB', 'I1'), ('WIFE', 'I4'), ('CHIL', 'I10'), ('MARR', '12 SEP 1950')]
}
families4 = {'F2': [('HUSB', 'I7'), ('WIFE', 'I5'), ('CHIL', 'I2'), ('CHIL', 'I8'), ('MARR', '12 SEP 1968')], 'F3': [('HUSB', 'I10'), ('WIFE', 'I9'), ('CHIL', 'I3'), ('MARR', '12 FEB 1970')], 'F4': [('HUSB', 'I6'), ('WIFE', 'I5'), ('CHIL', 'I11'), ('MARR', '12 SEP 1980')], 'F5': [('HUSB', 'I12'), ('WIFE', 'I13'), ('CHIL', 'I5'), ('MARR', '2 FEB 1948')], 'F6': [('HUSB', 'I15'), ('WIFE', 'I14'), ('CHIL', 'I10'), ('MARR', '12 SEP 1950')]}
families5 = {
    'F1': [('HUSB', 'I3'), ('WIFE', 'I2'), ('CHIL', 'I1'), ('CHIL', 'I4'), ('MARR', '12 JAN 1995')],
    'F3': [('HUSB', 'I10'), ('WIFE', 'I9'), ('CHIL', 'I3'), ('MARR', '12 FEB 1970')],
    'F4': [('HUSB', 'I6'), ('WIFE', 'I5'), ('CHIL', 'I11'), ('MARR', '12 SEP 1980')],
    'F5': [('HUSB', 'I12'), ('WIFE', 'I13'), ('CHIL', 'I5'), ('MARR', '2 FEB 1948')],
    'F6': [('HUSB', 'I1'), ('WIFE', 'I4'), ('CHIL', 'I10'), ('MARR', '12 SEP 1950')]
}

class MyTestCase(unittest.TestCase):
    def test_US18_1(self):
        self.assertEqual(parse.sibling_should_not_marry(families), False)
        print('US18 Test Case 1 Passed: No siblings are married')

    def test_US18_2(self):
        self.assertEqual(parse.sibling_should_not_marry(families2), False)
        print('US18 Test Case 2 Passed: No siblings are married')

    def test_US18_3(self):
        print(parse.sibling_should_not_marry(families3))
        self.assertEqual(parse.sibling_should_not_marry(families3), True)
        print('US18 Test Case 3 Passed: Siblings are married')

    def test_US18_4(self):
        self.assertEqual(parse.sibling_should_not_marry(families4), False)
        print('US18 Test Case 4 Passed: Sibling are not married')

    def test_US18_5(self):
        parse.sibling_should_not_marry(families5)
        self.assertEqual(parse.sibling_should_not_marry(families5), True)
        print('US18 Test Case 5 Passed: Sibling are married')

        
if __name__ == '__main__':
    unittest.main()


