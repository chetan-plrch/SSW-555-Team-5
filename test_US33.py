import unittest
import parse
import datetime

class MyTestCase(unittest.TestCase):
    def test_US33_1(self):
        # Test case with no orphaned children
        families = {
            'F1': [('HUSB', 'I3'), ('WIFE', 'I2'), ('CHIL', 'I1'), ('CHIL', 'I4'), ('MARR', '12 JAN 1995')],
            'F2': [('HUSB', 'I7'), ('WIFE', 'I5'), ('CHIL', 'I2'), ('CHIL', 'I8'), ('MARR', '12 SEP 1968')],
            'F3': [('HUSB', 'I10'), ('WIFE', 'I9'), ('CHIL', 'I3'), ('MARR', '12 FEB 1970')],
            'F4': [('HUSB', 'I6'), ('WIFE', 'I5'), ('CHIL', 'I11'), ('MARR', '12 SEP 1980')],
            'F5': [('HUSB', 'I12'), ('WIFE', 'I13'), ('CHIL', 'I5'), ('MARR', '2 FEB 1948')],
            'F6': [('HUSB', 'I15'), ('WIFE', 'I14'), ('CHIL', 'I10'), ('MARR', '12 SEP 1950')]
        }

        individuals = {
            'I1': [('NAME', 'Hamilton P /Kirk/'), ('SEX', 'M'), ('DATE', '29 DEC 1995'), ('FAMC', 'F1')],
            'I2': [('NAME', 'Elena /Golecha/'), ('SEX', 'F'), ('DATE', '1 JAN 1976'), ('DEAT', '1 JAN 2012'), ('FAMS', 'F1'), ('FAMC', 'F2')],
            'I3': [('NAME', 'Stevens /Krik/'), ('SEX', 'M'), ('DATE', '1 DEC 1969'), ('FAMS', 'F1'), ('FAMC', 'F3')],
            'I4': [('NAME', 'Kamala /Kirk/'), ('SEX', 'F'), ('DATE', '3 DEC 2005'), ('FAMC', 'F1')],
            'I5': [('NAME', 'Keerthi /Kirk/'), ('SEX', 'F'), ('DATE', '12 SEP 1950'), ('FAMS', 'F2'), ('FAMS', 'F4'), ('FAMC', 'F5')],
            'I6': [('NAME', 'Rex /Stevens/'), ('SEX', 'M'), ('DATE', '12 SEP 1951'), ('FAMS', 'F4')],
            'I7': [('NAME', 'Tom /Golecha/'), ('SEX', 'M'), ('DATE', '12 SEP 1950'), ('DEAT', '12 SEP 1979'), ('FAMS', 'F2')],
            'I8': [('NAME', 'Jared /Golecha/'), ('SEX', 'M'), ('DATE', '12 SEP 1978'), ('FAMC', 'F2')],
            'I9': [('NAME', 'Putli /Bafna/'), ('SEX', 'F'), ('DATE', '13 FEB 1952'), ('DEAT', '13 FEB 1985'), ('FAMS', 'F3')],
            'I10': [('NAME', 'Jasraj /Kirk/'), ('SEX', 'M'), ('DATE', '13 FEB 1950'), ('DEAT', '13 FEB 1975'), ('FAMS', 'F3'), ('FAMC', 'F6')],
            'I11': [('NAME', 'Felix /Stevens/'), ('SEX', 'M'), ('DATE', '12 SEP 1990'), ('FAMC', 'F4')],
            'I12': [('NAME', 'Manoj /Kirk/'), ('SEX', 'M'), ('DATE', '12 FEB 1930'), ('DEAT', '12 FEB 1980'), ('FAMS', 'F5')],
            'I13': [('NAME', 'Teena /Alma/'), ('SEX', 'F'), ('DATE', '1 MAR 1930'), ('DEAT', '12 FEB 1985'), ('FAMS', 'F5')],
            'I14': [('NAME', 'Anjali /Ambani/'), ('SEX', 'F'), ('DATE', '12 JUL 1925'), ('DEAT', '2 AUG 1999'), ('FAMS', 'F6')],
            'I15': [('NAME', 'James /Kirk/'), ('SEX', 'M'), ('DATE', '12 SEP 1930'), ('DEAT', '12 SEP 2000'), ('FAMS', 'F6')]
        }

        result = parse.listOrphans(families, individuals)
        self.assertIn(False, result) 
        print('US33 Test Case 1 Passed: No orphan children')

    def test_US33_2(self):
        families = {
            'F1': [('HUSB', 'I3'), ('WIFE', 'I2'), ('CHIL', 'I1'), ('CHIL', 'I4'), ('MARR', '12 JAN 1995')],
        }

        individuals = {
            'I1': [('NAME', 'Hamilton P /Kirk/'), ('SEX', 'M'), ('DATE', '29 DEC 1995'), ('FAMC', 'F1')],
            'I2': [('NAME', 'Elena /Golecha/'), ('SEX', 'F'), ('DATE', '1 JAN 1976'), ('DEAT', '1 JAN 2012'), ('FAMS', 'F1'), ('FAMC', 'F2')],
            'I3': [('NAME', 'Stevens /Krik/'), ('SEX', 'M'), ('DATE', '1 DEC 1969'), ('FAMS', 'F1'), ('FAMC', 'F3')],
            'I4': [('NAME', 'Kamala /Kirk/'), ('SEX', 'F'), ('DATE', '29 DEC 1997'), ('FAMC', 'F1')],
        }

        result = parse.listOrphans(families, individuals)
        self.assertIn(False, result)
        print('US33 Test Case 2 Passed')
    
    def test_US33_3(self):
        families = {
        'F1': [('HUSB', 'I3'), ('WIFE', 'I2'), ('CHIL', 'I1'), ('CHIL', 'I4'), ('MARR', '12 JAN 1995')],
        'F2': [('HUSB', 'I7'), ('WIFE', 'I5'), ('CHIL', 'I2'), ('CHIL', 'I8'), ('MARR', '12 SEP 1968')],
        'F3': [('HUSB', 'I10'), ('WIFE', 'I9'), ('CHIL', 'I3'), ('MARR', '12 FEB 1970')],
       }

        individuals = {
        'I1': [('NAME', 'Hamilton P /Kirk/'), ('SEX', 'M'), ('DATE', '29 DEC 1995'), ('FAMC', 'F1')],
        'I2': [('NAME', 'Elena /Golecha/'), ('SEX', 'F'), ('DATE', '1 JAN 1976'), ('DEAT', '1 JAN 2012'), ('FAMS', 'F1'), ('FAMC', 'F2')],
        'I3': [('NAME', 'Stevens /Krik/'), ('SEX', 'M'), ('DATE', '1 DEC 1969'), ('FAMS', 'F1'), ('FAMC', 'F3')],
        'I4': [('NAME', 'Kamala /Kirk/'), ('SEX', 'F'), ('DATE', '29 DEC 2007'), ('FAMC', 'F1')],
        'I5': [('NAME', 'Keerthi /Kirk/'), ('SEX', 'F'), ('DATE', '12 SEP 2010'), ('FAMS', 'F2'), ('FAMS', 'F4'), ('FAMC', 'F5')],
        'I6': [('NAME', 'Rex /Stevens/'), ('SEX', 'M'), ('DATE', '12 SEP 2012'), ('FAMS', 'F4')],
        'I7': [('NAME', 'Tom /Golecha/'), ('SEX', 'M'), ('DATE', '12 SEP 1950'), ('DEAT', '12 SEP 1979'), ('FAMS', 'F2')],
        'I8': [('NAME', 'Jared /Golecha/'), ('SEX', 'M'), ('DATE', '12 SEP 1978'), ('FAMC', 'F2')],
        'I9': [('NAME', 'Putli /Bafna/'), ('SEX', 'F'), ('DATE', '13 FEB 1952'), ('DEAT', '13 FEB 1985'), ('FAMS', 'F3')],
        'I10': [('NAME', 'Jasraj /Kirk/'), ('SEX', 'M'), ('DATE', '13 FEB 1950'), ('DEAT', '13 FEB 1975'), ('FAMS', 'F3'), ('FAMC', 'F6')],
        'I11': [('NAME', 'Felix /Stevens/'), ('SEX', 'M'), ('DATE', '12 SEP 1990'), ('FAMC', 'F4')],
    }

        result = parse.listOrphans(families, individuals)
        self.assertIn(False, result)
        print('US33 Test Case 3 Passed: Orphan children present')

    def test_US33_4(self):
        families = {
        'F1': [('HUSB', 'I3'), ('WIFE', 'I2'), ('MARR', '12 JAN 1995')],
        'F2': [('HUSB', 'I7'), ('WIFE', 'I5'), ('MARR', '12 SEP 1968')],
        'F3': [('HUSB', 'I10'), ('WIFE', 'I9'), ('MARR', '12 FEB 1970')],
        }

        individuals = {
            'I1': [('NAME', 'Hamilton P /Kirk/'), ('SEX', 'M'), ('DATE', '29 DEC 1995'), ('FAMC', 'F1')],
            'I2': [('NAME', 'Elena /Golecha/'), ('SEX', 'F'), ('DATE', '1 JAN 1976'), ('DEAT', '1 JAN 2012'), ('FAMS', 'F1'), ('FAMC', 'F2')],
            'I3': [('NAME', 'Stevens /Krik/'), ('SEX', 'M'), ('DATE', '1 DEC 1969'), ('FAMS', 'F1'), ('FAMC', 'F3')],
        }

        result = parse.listOrphans(families, individuals)
        self.assertIn(None, result)
        print('US33 Test Case 4 Passed: No children in any family')

    def test_US33_5(self):
        families = {
        'F1': [('HUSB', 'I3'), ('WIFE', 'I2'), ('CHIL', 'I1'), ('MARR', '12 JAN 1995')],
        }

        individuals = {
            'I1': [('NAME', 'Hamilton P /Kirk/'), ('SEX', 'M'), ('DATE', '29 DEC 1980'), ('FAMC', 'F1')],
            'I2': [('NAME', 'Elena /Golecha/'), ('SEX', 'F'), ('DATE', '1 JAN 1976'), ('DEAT', '1 JAN 2012'), ('FAMS', 'F1'), ('FAMC', 'F2')],
            'I3': [('NAME', 'Stevens /Krik/'), ('SEX', 'M'), ('DATE', '1 DEC 1969'), ('FAMS', 'F1'), ('FAMC', 'F3')],
        }

        result = parse.listOrphans(families, individuals)
        self.assertIn(False, result)
        print('US33 Test Case 5 Passed: No orphans')
    
    def test_US33_6(self):
        families = {
        'F1': [('HUSB', 'I3'), ('WIFE', 'I2'), ('CHIL', 'I1'), ('CHIL', 'I4'), ('MARR', '12 JAN 1995')],
        }

        individuals = {
            'I1': [('NAME', 'Hamilton P /Kirk/'), ('SEX', 'M'), ('DATE', '29 DEC 2005'), ('FAMC', 'F1')],
            'I2': [('NAME', 'Elena /Golecha/'), ('SEX', 'F'), ('DATE', '1 JAN 1976'), ('DEAT', '1 JAN 2012'), ('FAMS', 'F1'), ('FAMC', 'F2')],
            'I3': [('NAME', 'Stevens /Krik/'), ('SEX', 'M'), ('DATE', '1 DEC 1969'), ('FAMS', 'F1'), ('FAMC', 'F3')],
            'I4': [('NAME', 'Kamala /Kirk/'), ('SEX', 'F'), ('DATE', '3 DEC 2000'), ('FAMC', 'F1')],
        }

        result = parse.listOrphans(families, individuals)
        self.assertIn(False, result)
        print('US33 Test Case 6 Passed')
    
    def test_US33_7(self):
        families = {
        'F1': [('HUSB', 'I3'), ('WIFE', 'I2'), ('CHIL', 'I1'), ('CHIL', 'I4'), ('MARR', '12 JAN 1995')],
        }

        individuals = {
            'I1': [('NAME', 'Hamilton P /Kirk/'), ('SEX', 'M'), ('DATE', '29 DEC 2005'), ('FAMC', 'F1')],
            'I2': [('NAME', 'Elena /Golecha/'), ('SEX', 'F'), ('DATE', '1 JAN 1976'), ('DEAT', '1 JAN 2012'), ('FAMS', 'F1'), ('FAMC', 'F2')],
            'I3': [('NAME', 'Stevens /Krik/'), ('SEX', 'M'), ('DATE', '1 DEC 1969'), ('DEAT', '1 JAN 2012'), ('FAMS', 'F1'), ('FAMC', 'F3')],
            'I4': [('NAME', 'Kamala /Kirk/'), ('SEX', 'F'), ('DATE', '3 DEC 2007'), ('FAMC', 'F1')],
        }

        result = parse.listOrphans(families, individuals)
        self.assertIn(True, result)
        print('US33 Test Case 7 Passed')

if __name__ == '__main__':
    unittest.main()