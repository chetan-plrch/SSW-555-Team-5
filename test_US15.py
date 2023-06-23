import unittest
import parse
import datetime

families = {'F1': [('HUSB', 'I3'), ('WIFE', 'I2'), ('CHIL', 'I1'), ('CHIL', 'I4'), ('MARR', '12 JAN 1995')]}
families2 = {'F2': [
                ('HUSB', 'I7'), ('WIFE', 'I5'),
                ('CHIL', 'I2'), ('CHIL', 'I8'), ('MARR', '12 SEP 1968'),
                ('CHIL', 'I3'), ('CHIL', 'I11'), ('CHIL', 'I9'), ('CHIL', 'I10'),
                ('CHIL', 'I13'), ('CHIL', 'I12'), ('CHIL', 'I4'), ('CHIL', 'I15'),
                ('CHIL', 'I16'), ('CHIL', 'I17'), ('CHIL', 'I18'), ('CHIL', 'I19'),
                ('CHIL', 'I20'), ('CHIL', 'I21'), ('CHIL', 'I22'), ('CHIL', 'I23'),
            ]}
families3 = {'F6': [('HUSB', 'I31'), ('WIFE', 'I21'), ('CHIL', 'I11'), ('CHIL', 'I41'), ('MARR', '18 JAN 1998')]}
families4 = {'F5': [
                ('HUSB', 'I34'), ('WIFE', 'I35'),
                ('CHIL', 'I2'), ('CHIL', 'I8'), ('MARR', '12 SEP 1968'),
                ('CHIL', 'I9'), ('CHIL', 'I10'),
                ('CHIL', 'I13'), ('CHIL', 'I12'), ('CHIL', 'I4'), ('CHIL', 'I15'),
                ('CHIL', 'I16'), ('CHIL', 'I17'), ('CHIL', 'I18'), ('CHIL', 'I19'),
                ('CHIL', 'I20'), ('CHIL', 'I21'), ('CHIL', 'I22'), ('CHIL', 'I23'),
            ]}
families5 = {'F9': [('HUSB', 'I13'), ('WIFE', 'I12'), ('CHIL', 'I11'), ('CHIL', 'I14'), ('MARR', '24 JAN 2000')]}

class MyTestCase(unittest.TestCase):
    def test_US15_1(self):
        self.assertEqual(parse.fewer_than_15_siblings(families), False)
        print('US15 Test Case 1 Passed: Siblings are under 15')

    def test_US15_2(self):
        self.assertEqual(parse.fewer_than_15_siblings(families2), True)
        print('US15 Test Case 2 Passed: Siblings exceed 15')

    def test_US15_3(self):
        self.assertEqual(parse.fewer_than_15_siblings(families), False)
        print('US15 Test Case 1 Passed: Siblings are under 15')

    def test_US15_4(self):
        self.assertEqual(parse.fewer_than_15_siblings(families2), True)
        print('US15 Test Case 2 Passed: Siblings exceed 15')

    def test_US15_5(self):
        self.assertEqual(parse.fewer_than_15_siblings(families), False)
        print('US15 Test Case 1 Passed: Siblings are under 15')




if __name__ == '__main__':
    unittest.main()


