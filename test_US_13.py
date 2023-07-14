import unittest
import parse
import datetime

class MyTestCase(unittest.TestCase):
    def test_US13_1(self):
        individuals =  {
            'I1': [('NAME', 'Hamilton P /Kirk/'), ('SEX', 'M'), ('DATE', '29 DEC 1995'), ('FAMC', 'F1')], 
            'I2': [('NAME', 'Elena /Golecha/'), ('SEX', 'F'), ('DATE', '1 JAN 1976'), ('DEAT', '1 JAN 2012'), ('FAMS', 'F1'), ('FAMC', 'F2')], 
            'I3': [('NAME', 'Stevens /Krik/'), ('SEX', 'M'), ('DATE', '1 DEC 1969'), ('FAMS', 'F1'), ('FAMC', 'F3')], 
            'I4': [('NAME', 'Kamala /Kirk/'), ('SEX', 'F'), ('DATE', '3 DEC 2005'), ('FAMC', 'F1')]
        }

        families =  {
            'F1': [('HUSB', 'I3'), ('WIFE', 'I2'), ('CHIL', 'I1'), ('CHIL', 'I4'), ('MARR', '12 JAN 1995')]
        }
        self.assertEqual(parse.birth_dates_of_siblings_should_be_more_than_eight_months_apart(individuals, families), True)
        print('US13 Test Case 1 Passed: Birth Dates are more than 8 months apart')

    def test_US13_2(self):
        individuals =  {
            'I1': [('NAME', 'Hamilton P /Kirk/'), ('SEX', 'M'), ('DATE', '29 DEC 1995'), ('FAMC', 'F1')], 
            'I2': [('NAME', 'Elena /Golecha/'), ('SEX', 'F'), ('DATE', '1 JAN 1976'), ('DEAT', '1 JAN 2012'), ('FAMS', 'F1'), ('FAMC', 'F2')], 
            'I3': [('NAME', 'Stevens /Krik/'), ('SEX', 'M'), ('DATE', '1 DEC 1969'), ('FAMS', 'F1'), ('FAMC', 'F3')], 
            'I4': [('NAME', 'Kamala /Kirk/'), ('SEX', 'F'), ('DATE', '3 DEC 2005'), ('FAMC', 'F1')]
        }

        families =  {
            'F1': [('HUSB', 'I3'), ('WIFE', 'I2'), ('CHIL', 'I1'), ('CHIL', 'I4'), ('MARR', '12 JAN 1995')]
        }
        self.assertEqual(parse.birth_dates_of_siblings_should_be_more_than_eight_months_apart(individuals,families), True)
        print('US13 Test Case 2 Passed: Birth Dates are more than 8 months apart')

    def test_US13_3(self):
        individuals =  {
            'I1': [('NAME', 'Alan  /Smith/'), ('SEX', 'M'), ('DATE', '19 JAN 1995'), ('FAMC', 'F1')], 
            'I2': [('NAME', 'Elena /Smith/'), ('SEX', 'F'), ('DATE', '1 JAN 1976'), ('DEAT', '1 JAN 2012'), ('FAMS', 'F1'), ('FAMC', 'F2')], 
            'I3': [('NAME', 'Nathan /Smith/'), ('SEX', 'M'), ('DATE', '1 DEC 1969'), ('FAMS', 'F1'), ('FAMC', 'F3')], 
            'I4': [('NAME', 'Karen /Smith/'), ('SEX', 'F'), ('DATE', '20 JUN 1995'), ('FAMC', 'F1')]
        }

        families =  {
            'F1': [('HUSB', 'I3'), ('WIFE', 'I2'), ('CHIL', 'I1'), ('CHIL', 'I4'), ('MARR', '12 JAN 1995')]
        }
        self.assertEqual(parse.birth_dates_of_siblings_should_be_more_than_eight_months_apart(individuals,families), False)
        print('US13 Test Case 3 Passed: Birth Dates are not more than 8 months apart')

    def test_US13_4(self):
        individuals =  {
            'I1': [('NAME', 'Harry /Brook/'), ('SEX', 'M'), ('DATE', '29 DEC 1995'), ('FAMC', 'F1')], 
            'I2': [('NAME', 'Elena /Brook/'), ('SEX', 'F'), ('DATE', '1 JAN 1976'), ('DEAT', '1 JAN 2012'), ('FAMS', 'F1'), ('FAMC', 'F2')], 
            'I3': [('NAME', 'Stevens /Brook/'), ('SEX', 'M'), ('DATE', '1 DEC 1969'), ('FAMS', 'F1'), ('FAMC', 'F3')], 
            'I4': [('NAME', 'Kamala /Brook/'), ('SEX', 'F'), ('DATE', '3 DEC 2005'), ('FAMC', 'F1')],
            'I5': [('NAME', 'John /Brook/'), ('SEX', 'M'), ('DATE', '15 AUG 2010'), ('FAMC', 'F1')]
        }

        families =  {
            'F1': [('HUSB', 'I3'), ('WIFE', 'I2'), ('CHIL', 'I1'), ('CHIL', 'I4'), ('CHIL', 'I5'), ('MARR', '12 JAN 1995')]
        }
        self.assertEqual(parse.birth_dates_of_siblings_should_be_more_than_eight_months_apart(individuals,families), True)
        print('US13 Test Case 4 Passed: Birth Dates are more than 8 months apart')

    def test_US13_5(self):
        individuals =  {
            'I1': [('NAME', 'Richard /Potts/'), ('SEX', 'M'), ('DATE', '29 DEC 1995'), ('FAMC', 'F1')], 
            'I2': [('NAME', 'Elena /Potts/'), ('SEX', 'F'), ('DATE', '1 JAN 1976'), ('DEAT', '1 JAN 2012'), ('FAMS', 'F1'), ('FAMC', 'F2')], 
            'I3': [('NAME', 'Stevens /Potts/'), ('SEX', 'M'), ('DATE', '1 DEC 1969'), ('FAMS', 'F1'), ('FAMC', 'F3')], 
            'I4': [('NAME', 'Kamala /Potts/'), ('SEX', 'F'), ('DATE', '3 DEC 2005'), ('FAMC', 'F1')],
            'I5': [('NAME', 'Harry /Potts/'), ('SEX', 'M'), ('DATE', '15 MAR 2006'), ('FAMC', 'F1')]
        }

        families =  {
            'F1': [('HUSB', 'I3'), ('WIFE', 'I2'), ('CHIL', 'I1'), ('CHIL', 'I4'), ('CHIL', 'I5'), ('MARR', '12 JAN 1995')]
        }
        self.assertEqual(parse.birth_dates_of_siblings_should_be_more_than_eight_months_apart(individuals,families), False)
        print('US13 Test Case 5 Passed: Birth Dates are not more than 8 months apart')
    
    #Refactoring Updated Test Cases   Refactoring Assignment
    # def test_US13_6(self):
    #     individuals = {
    #         'I1': [('NAME', 'John /Doe/'), ('SEX', 'M'), ('DATE', '01 Jan 1990')],
    #         'I2': [('NAME', 'Jane /Smith/'), ('SEX', 'F'), ('DATE', '15 Jun 1985')],
    #         'I3': [('NAME', 'Mike /Johnson/'), ('SEX', 'M'), ('DATE', '05 Sep 1978')],
    #         'I4': [('NAME', 'Anna /Davis/'), ('SEX', 'F'), ('DATE', '30 Nov 1995')],
    #     }

    #     families = {
    #         'F1': [('HUSB', 'I1'), ('WIFE', 'I2'), ('CHIL', 'I3'), ('CHIL', 'I4')]
    #     }

    #     result = parse.birth_dates_of_siblings_should_be_more_than_eight_months_apart(individuals, families)
    #     self.assertTrue(result)
    #     print('US13 Test Case 6 Passed: Birth Dates are more than 8 months apart')

    # def test_US13_7(self):
    #     individuals = {
    #         'I1': [('NAME', 'John /Doe/'), ('SEX', 'M'), ('DATE', '01 Jan 1990')],
    #         'I2': [('NAME', 'Jane /Smith/'), ('SEX', 'F'), ('DATE', '15 Jun 1991')],
    #         'I3': [('NAME', 'Mike /Johnson/'), ('SEX', 'M'), ('DATE', '05 Sep 1992')],
    #         'I4': [('NAME', 'Anna /Davis/'), ('SEX', 'F'), ('DATE', '30 Nov 1993')],
    #     }

    #     families = {
    #         'F1': [('HUSB', 'I1'), ('WIFE', 'I2'), ('CHIL', 'I3'), ('CHIL', 'I4')]
    #     }

    #     result = parse.birth_dates_of_siblings_should_be_more_than_eight_months_apart(individuals, families)
    #     self.assertTrue(result)
    #     print('US13 Test Case 7 Passed: Birth Dates are more than 8 months apart')

if __name__ == '__main__':
    unittest.main()