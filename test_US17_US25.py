import unittest
import parse
import datetime

individuals = {'I1': [('NAME', 'Hamilton P /Kirk/'), ('SEX', 'M'), ('DATE', '29 DEC 1995'), ('FAMC', 'F1')], 'I2': [('NAME', 'Elena /Golecha/'), ('SEX', 'F'), ('DATE', '1 JAN 1976'), ('DEAT', '1 JAN 2012'), ('FAMS', 'F1'), ('FAMC', 'F2')], 'I3': [('NAME', 'Stevens /Krik/'), ('SEX', 'M'), ('DATE', '1 DEC 1969'), ('FAMS', 'F1'), ('FAMC', 'F3')], 'I4': [('NAME', 'Kamala /Kirk/'), ('SEX', 'F'), ('DATE', '3 DEC 2005'), ('FAMC', 'F1')], 'I5': [('NAME', 'Keerthi /Kirk/'), ('SEX', 'F'), ('DATE', '12 SEP 1959'), ('FAMS', 'F2'), ('FAMS', 'F4'), ('FAMC', 'F5')], 'I6': [('NAME', 'Rex /Stevens/'), ('SEX', 'M'), ('DATE', '12 SEP 1951'), ('FAMS', 'F4')], 'I7': [('NAME', 'Tom /Golecha/'), ('SEX', 'M'), ('DATE', '12 SEP 1950'), ('DEAT', '12 SEP 1979'), ('FAMS', 'F2')], 'I8': [('NAME', 'Jared /Golecha/'), ('SEX', 'M'), ('DATE', '12 SEP 1978'), ('FAMS', 'F6'), ('FAMS', 'F7'), ('FAMC', 'F2')], 'I9': [('NAME', 'Putli /Bafna/'), ('SEX', 'F'), ('DATE', '13 FEB 1952'), ('DEAT', '13 FEB 1985'), ('FAMS', 'F3')], 'I10': [('NAME', 'Jasraj /Kirk/'), ('SEX', 'M'), ('DATE', '13 FEB 1950'), ('DEAT', '13 FEB 1975'), ('FAMS', 'F3'), ('FAMC', 'F8')], 'I11': [('NAME', 'Felix /Stevens/'), ('SEX', 'M'), ('DATE', '12 SEP 1990'), ('FAMC', 'F4')], 'I12': [('NAME', 'Manoj /Kirk/'), ('SEX', 'M'), ('DATE', '12 FEB 1930'), ('DEAT', '12 FEB 1980'), ('FAMS', 'F5')], 'I13': [('NAME', 'Teena /Alma/'), ('SEX', 'F'), ('DATE', '1 MAR 1930'), ('DEAT', '12 FEB 1985'), ('FAMS', 'F5')], 'I14': [('NAME', 'Anjali /Ambani/'), ('SEX', 'F'), ('DATE', '12 JUL 1925'), ('DEAT', '2 AUG 1999'), ('FAMS', 'F8')], 'I15': [('NAME', 'James /Kirk/'), ('SEX', 'M'), ('DATE', '12 SEP 1930'), ('DEAT', '12 SEP 2000'), ('FAMS', 'F8')], 'I16': [('NAME', 'Jen /Folger/'), ('SEX', 'F'), ('DATE', '12 MAR 1979'), ('FAMS', 'F7')], 'I17': [('NAME', 'Kim /Smith/'), ('SEX', 'F'), ('DATE', '18 OCT 1985'), ('FAMS', 'F6')]}
families = {'F1': [('HUSB', 'I3'), ('WIFE', 'I2'), ('CHIL', 'I1'), ('CHIL', 'I4'), ('MARR', '12 JAN 1995')], 'F2': [('HUSB', 'I7'), ('WIFE', 'I5'), ('CHIL', 'I2'), ('CHIL', 'I8'), ('MARR', '12 SEP 1968')], 'F3': [('HUSB', 'I10'), ('WIFE', 'I9'), ('CHIL', 'I3'), ('MARR', '12 FEB 1970')], 'F4': [('HUSB', 'I8'), ('WIFE', 'I5'), ('CHIL', 'I11'), ('MARR', '12 SEP 1980')], 'F5': [('HUSB', 'I12'), ('WIFE', 'I13'), ('CHIL', 'I5'), ('MARR', '2 FEB 1948')], 'F6': [('HUSB', 'I8'), ('WIFE', 'I17'), ('MARR', '14 MAY 2005')], 'F7': [('HUSB', 'I8'), ('WIFE', 'I16'), ('MARR', '19 MAR 2002'), ('DIV', '14 JUL 2007')], 'F8': [('HUSB', 'I15'), ('WIFE', 'I14'), ('CHIL', 'I10'), ('MARR', '12 SEP 1950')]}

individuals2 = {'I1': [('NAME', 'Hamilton P /Kirk/'), ('SEX', 'M'), ('DATE', '29 DEC 1995'), ('FAMC', 'F1')], 'I2': [('NAME', 'Elena /Golecha/'), ('SEX', 'F'), ('DATE', '1 JAN 1976'), ('DEAT', '1 JAN 2012'), ('FAMS', 'F1'), ('FAMC', 'F2')], 'I3': [('NAME', 'Stevens /Krik/'), ('SEX', 'M'), ('DATE', '1 DEC 1969'), ('FAMS', 'F1'), ('FAMC', 'F3')], 'I4': [('NAME', 'Kamala /Kirk/'), ('SEX', 'F'), ('DATE', '3 DEC 2005'), ('FAMC', 'F1')], 'I5': [('NAME', 'Keerthi /Kirk/'), ('SEX', 'F'), ('DATE', '12 SEP 1959'), ('FAMS', 'F2'), ('FAMS', 'F4'), ('FAMC', 'F5')], 'I6': [('NAME', 'Rex /Stevens/'), ('SEX', 'M'), ('DATE', '12 SEP 1951'), ('FAMS', 'F4')], 'I7': [('NAME', 'Tom /Golecha/'), ('SEX', 'M'), ('DATE', '12 SEP 1950'), ('DEAT', '12 SEP 1979'), ('FAMS', 'F2')], 'I8': [('NAME', 'Jared /Golecha/'), ('SEX', 'M'), ('DATE', '12 SEP 1978'), ('FAMS', 'F6'), ('FAMS', 'F7'), ('FAMC', 'F2')], 'I9': [('NAME', 'Putli /Bafna/'), ('SEX', 'F'), ('DATE', '13 FEB 1952'), ('DEAT', '13 FEB 1985'), ('FAMS', 'F3')], 'I10': [('NAME', 'Jasraj /Kirk/'), ('SEX', 'M'), ('DATE', '13 FEB 1950'), ('DEAT', '13 FEB 1975'), ('FAMS', 'F3'), ('FAMC', 'F8')], 'I11': [('NAME', 'Felix /Stevens/'), ('SEX', 'M'), ('DATE', '12 SEP 1990'), ('FAMC', 'F4')], 'I12': [('NAME', 'Manoj /Kirk/'), ('SEX', 'M'), ('DATE', '12 FEB 1930'), ('DEAT', '12 FEB 1980'), ('FAMS', 'F5')], 'I13': [('NAME', 'Teena /Alma/'), ('SEX', 'F'), ('DATE', '1 MAR 1930'), ('DEAT', '12 FEB 1985'), ('FAMS', 'F5')], 'I14': [('NAME', 'Anjali /Ambani/'), ('SEX', 'F'), ('DATE', '12 JUL 1925'), ('DEAT', '2 AUG 1999'), ('FAMS', 'F8')], 'I15': [('NAME', 'James /Kirk/'), ('SEX', 'M'), ('DATE', '12 SEP 1930'), ('DEAT', '12 SEP 2000'), ('FAMS', 'F8')], 'I16': [('NAME', 'Jen /Folger/'), ('SEX', 'F'), ('DATE', '12 MAR 1979'), ('FAMS', 'F7')], 'I17': [('NAME', 'Kim /Smith/'), ('SEX', 'F'), ('DATE', '18 OCT 1985'), ('FAMS', 'F6')]}
families2 = {'F1': [('HUSB', 'I3'), ('WIFE', 'I14'), ('CHIL', 'I1'), ('CHIL', 'I4'), ('MARR', '12 JAN 1995')], 'F2': [('HUSB', 'I7'), ('WIFE', 'I5'), ('CHIL', 'I2'), ('CHIL', 'I8'), ('MARR', '12 SEP 1968')], 'F3': [('HUSB', 'I10'), ('WIFE', 'I9'), ('CHIL', 'I3'), ('MARR', '12 FEB 1970')], 'F4': [('HUSB', 'I6'), ('WIFE', 'I5'), ('CHIL', 'I11'), ('MARR', '12 SEP 1980')], 'F5': [('HUSB', 'I12'), ('WIFE', 'I13'), ('CHIL', 'I5'), ('MARR', '2 FEB 1948')], 'F6': [('HUSB', 'I8'), ('WIFE', 'I17'), ('MARR', '14 MAY 2005')], 'F7': [('HUSB', 'I8'), ('WIFE', 'I16'), ('MARR', '19 MAR 2002'), ('DIV', '14 JUL 2007')], 'F8': [('HUSB', 'I15'), ('WIFE', 'I14'), ('CHIL', 'I10'), ('MARR', '12 SEP 1950')]}

individuals3 = {'I1': [('NAME', 'Hamilton P /Kirk/'), ('SEX', 'M'), ('DATE', '29 DEC 1995'), ('FAMC', 'F1')], 'I2': [('NAME', 'Elena /Golecha/'), ('SEX', 'F'), ('DATE', '1 JAN 1976'), ('DEAT', '1 JAN 2012'), ('FAMS', 'F1'), ('FAMC', 'F2')], 'I3': [('NAME', 'Stevens /Krik/'), ('SEX', 'M'), ('DATE', '1 DEC 1969'), ('FAMS', 'F1'), ('FAMC', 'F3')], 'I4': [('NAME', 'Kamala /Kirk/'), ('SEX', 'F'), ('DATE', '3 DEC 2005'), ('FAMC', 'F1')], 'I5': [('NAME', 'Keerthi /Kirk/'), ('SEX', 'F'), ('DATE', '12 SEP 1959'), ('FAMS', 'F2'), ('FAMS', 'F4'), ('FAMC', 'F5')], 'I6': [('NAME', 'Rex /Stevens/'), ('SEX', 'M'), ('DATE', '12 SEP 1951'), ('FAMS', 'F4')], 'I7': [('NAME', 'Tom /Golecha/'), ('SEX', 'M'), ('DATE', '12 SEP 1950'), ('DEAT', '12 SEP 1979'), ('FAMS', 'F2')], 'I8': [('NAME', 'Jared /Golecha/'), ('SEX', 'M'), ('DATE', '12 SEP 1978'), ('FAMS', 'F6'), ('FAMS', 'F7'), ('FAMC', 'F2')], 'I9': [('NAME', 'Putli /Bafna/'), ('SEX', 'F'), ('DATE', '13 FEB 1952'), ('DEAT', '13 FEB 1985'), ('FAMS', 'F3')], 'I10': [('NAME', 'Jasraj /Kirk/'), ('SEX', 'M'), ('DATE', '13 FEB 1950'), ('DEAT', '13 FEB 1975'), ('FAMS', 'F3'), ('FAMC', 'F8')], 'I11': [('NAME', 'Felix /Stevens/'), ('SEX', 'M'), ('DATE', '12 SEP 1990'), ('FAMC', 'F4')], 'I12': [('NAME', 'Manoj /Kirk/'), ('SEX', 'M'), ('DATE', '12 FEB 1930'), ('DEAT', '12 FEB 1980'), ('FAMS', 'F5')], 'I13': [('NAME', 'Teena /Alma/'), ('SEX', 'F'), ('DATE', '1 MAR 1930'), ('DEAT', '12 FEB 1985'), ('FAMS', 'F5')], 'I14': [('NAME', 'Anjali /Ambani/'), ('SEX', 'F'), ('DATE', '12 JUL 1925'), ('DEAT', '2 AUG 1999'), ('FAMS', 'F8')], 'I15': [('NAME', 'James /Kirk/'), ('SEX', 'M'), ('DATE', '12 SEP 1930'), ('DEAT', '12 SEP 2000'), ('FAMS', 'F8')], 'I16': [('NAME', 'Jen /Folger/'), ('SEX', 'F'), ('DATE', '12 MAR 1979'), ('FAMS', 'F7')], 'I17': [('NAME', 'Kim /Smith/'), ('SEX', 'F'), ('DATE', '18 OCT 1985'), ('FAMS', 'F6')]}
families3 = {'F1': [('HUSB', 'I3'), ('WIFE', 'I14'), ('CHIL', 'I1'), ('CHIL', 'I4'), ('MARR', '12 JAN 1995')], 'F2': [('HUSB', 'I7'), ('WIFE', 'I5'), ('CHIL', 'I2'), ('CHIL', 'I8'), ('MARR', '12 SEP 1968')], 'F3': [('HUSB', 'I10'), ('WIFE', 'I9'), ('CHIL', 'I3'), ('MARR', '12 FEB 1970')], 'F4': [('HUSB', 'I6'), ('WIFE', 'I5'), ('CHIL', 'I11'), ('MARR', '12 SEP 1980')], 'F5': [('HUSB', 'I12'), ('WIFE', 'I13'), ('CHIL', 'I5'), ('MARR', '2 FEB 1948')], 'F6': [('HUSB', 'I8'), ('WIFE', 'I17'), ('MARR', '14 MAY 2005')], 'F7': [('HUSB', 'I8'), ('WIFE', 'I16'), ('MARR', '19 MAR 2002'), ('DIV', '14 JUL 2007')], 'F8': [('HUSB', 'I15'), ('WIFE', 'I14'), ('CHIL', 'I10'), ('MARR', '12 SEP 1950')]}

individuals4 = {'I1': [('NAME', 'Hamilton P /Kirk/'), ('SEX', 'M'), ('DATE', '29 DEC 1995'), ('FAMC', 'F1')], 'I2': [('NAME', 'Elena /Golecha/'), ('SEX', 'F'), ('DATE', '1 JAN 1976'), ('DEAT', '1 JAN 2012'), ('FAMS', 'F1'), ('FAMC', 'F2')], 'I3': [('NAME', 'Stevens /Krik/'), ('SEX', 'M'), ('DATE', '1 DEC 1969'), ('FAMS', 'F1'), ('FAMC', 'F3')], 'I4': [('NAME', 'Kamala /Kirk/'), ('SEX', 'F'), ('DATE', '3 DEC 2005'), ('FAMC', 'F1')], 'I5': [('NAME', 'Keerthi /Kirk/'), ('SEX', 'F'), ('DATE', '12 SEP 1959'), ('FAMS', 'F2'), ('FAMS', 'F4'), ('FAMC', 'F5')], 'I6': [('NAME', 'Rex /Stevens/'), ('SEX', 'M'), ('DATE', '12 SEP 1951'), ('FAMS', 'F4')], 'I7': [('NAME', 'Tom /Golecha/'), ('SEX', 'M'), ('DATE', '12 SEP 1950'), ('DEAT', '12 SEP 1979'), ('FAMS', 'F2')], 'I8': [('NAME', 'Jared /Golecha/'), ('SEX', 'M'), ('DATE', '12 SEP 1978'), ('FAMS', 'F6'), ('FAMS', 'F7'), ('FAMC', 'F2')], 'I9': [('NAME', 'Putli /Bafna/'), ('SEX', 'F'), ('DATE', '13 FEB 1952'), ('DEAT', '13 FEB 1985'), ('FAMS', 'F3')], 'I10': [('NAME', 'Jasraj /Kirk/'), ('SEX', 'M'), ('DATE', '13 FEB 1950'), ('DEAT', '13 FEB 1975'), ('FAMS', 'F3'), ('FAMC', 'F8')], 'I11': [('NAME', 'Felix /Stevens/'), ('SEX', 'M'), ('DATE', '12 SEP 1990'), ('FAMC', 'F4')], 'I12': [('NAME', 'Manoj /Kirk/'), ('SEX', 'M'), ('DATE', '12 FEB 1930'), ('DEAT', '12 FEB 1980'), ('FAMS', 'F5')], 'I13': [('NAME', 'Teena /Alma/'), ('SEX', 'F'), ('DATE', '1 MAR 1930'), ('DEAT', '12 FEB 1985'), ('FAMS', 'F5')], 'I14': [('NAME', 'Anjali /Ambani/'), ('SEX', 'F'), ('DATE', '12 JUL 1925'), ('DEAT', '2 AUG 1999'), ('FAMS', 'F8')], 'I15': [('NAME', 'James /Kirk/'), ('SEX', 'M'), ('DATE', '12 SEP 1930'), ('DEAT', '12 SEP 2000'), ('FAMS', 'F8')], 'I16': [('NAME', 'Jen /Folger/'), ('SEX', 'F'), ('DATE', '12 MAR 1979'), ('FAMS', 'F7')], 'I17': [('NAME', 'Kim /Smith/'), ('SEX', 'F'), ('DATE', '18 OCT 1985'), ('FAMS', 'F6')]}
families4 = {'F1': [('HUSB', 'I3'), ('WIFE', 'I14'), ('CHIL', 'I1'), ('CHIL', 'I4'), ('MARR', '12 JAN 1995')], 'F2': [('HUSB', 'I7'), ('WIFE', 'I5'), ('CHIL', 'I2'), ('CHIL', 'I8'), ('MARR', '12 SEP 1968')], 'F3': [('HUSB', 'I10'), ('WIFE', 'I9'), ('CHIL', 'I3'), ('MARR', '12 FEB 1970')], 'F4': [('HUSB', 'I6'), ('WIFE', 'I5'), ('CHIL', 'I11'), ('MARR', '12 SEP 1980')], 'F5': [('HUSB', 'I12'), ('WIFE', 'I13'), ('CHIL', 'I5'), ('MARR', '2 FEB 1948')], 'F6': [('HUSB', 'I8'), ('WIFE', 'I17'), ('MARR', '14 MAY 2005')], 'F7': [('HUSB', 'I8'), ('WIFE', 'I16'), ('MARR', '19 MAR 2002'), ('DIV', '14 JUL 2007')], 'F8': [('HUSB', 'I15'), ('WIFE', 'I14'), ('CHIL', 'I10'), ('MARR', '12 SEP 1950')]}

individuals5 = {'I1': [('NAME', 'Hamilton P /Kirk/'), ('SEX', 'M'), ('DATE', '29 DEC 1995'), ('FAMC', 'F1')], 'I3': [('NAME', 'Stevens /Krik/'), ('SEX', 'M'), ('DATE', '1 DEC 1969'), ('FAMS', 'F1'), ('FAMC', 'F3')], 'I4': [('NAME', 'Kamala /Kirk/'), ('SEX', 'F'), ('DATE', '3 DEC 2005'), ('FAMC', 'F1')]}
families5 = {'F1': [('HUSB', 'I3'), ('WIFE', 'I14'), ('CHIL', 'I1'), ('CHIL', 'I4'), ('MARR', '12 JAN 1995')]}


class MyTestCase(unittest.TestCase):
    # US17: Parent is married to their descendant
    def test_US17_1(self):
        self.assertEqual(parse.user_story_17(individuals, families), True)
        print('US17 Test Case #1 - Passed: Parent is married to their child')

    def test_US17_2(self):
        self.assertEqual(parse.user_story_17(individuals2, families2), True)
        print('US17 Test Case #1 - Passed: Parent is married to their grand child')

    def test_US17_3(self):
        self.assertEqual(parse.user_story_17(individuals3, families3), True)
        print('US17 Test Case #1 - Passed: Parent is married to great grand child')

    def test_US17_4(self):
        self.assertEqual(parse.user_story_17(individuals4, families4), True)
        print('US17 Test Case #1 - Passed: Parent is married to great great grand child')

    def test_US17_5(self):
        self.assertEqual(parse.user_story_17(individuals5, families5), False)
        print('US17 Test Case #1 - Passed: Parent is not married their child')

    # US25: Child should not have same name and date of birth
    def test_US25_1(self):
        self.assertEqual(parse.user_story_25(individuals, families), False)
        print('US25 Test Case #1 - Passed: Child does not have same name and date of birth')

    def test_US25_2(self):
        self.assertEqual(parse.user_story_25(individuals2, families2), False)
        print('US25 Test Case #2 - Passed: Child does not have same name and date of birth')

    def test_US25_3(self):
        self.assertEqual(parse.user_story_25(individuals3, families3), False)
        print('US25 Test Case #3 - Passed: Child does have same name and date of birth')

    def test_US25_4(self):
        self.assertEqual(parse.user_story_25(individuals4, families4), False)
        print('US25 Test Case #4 - Passed: Child does have same name and date of birth')

    def test_US25_5(self):
        self.assertEqual(parse.user_story_25(individuals5, families5), False)
        print('US25 Test Case #5 - Passed: Child does not have same name and date of birth')


if __name__ == '__main__':
    unittest.main()