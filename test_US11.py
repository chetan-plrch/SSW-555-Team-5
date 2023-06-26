import unittest
import parse
import datetime

class MyTestCase(unittest.TestCase):
    def test_US10_1(self):
        families = {
            'F1': [('HUSB', 'I1'), ('WIFE', 'I2'), ('MARR', '1 JAN 2000'), ('DIV', '10 JAN 2010')],
            'F2': [('HUSB', 'I3'), ('WIFE', 'I4'), ('MARR', '1 JAN 2010')],
            'F3': [('HUSB', 'I5'), ('WIFE', 'I6'), ('MARR', '1 JAN 2020')]
        }
        individuals = {
            'I1': [],
            'I2': [],
            'I3': [],
            'I4': [],
            'I5': [],
            'I6': []
        }
        
        result = parse.noBigamy(families, individuals)
        self.assertEqual(result, "No Bigamy")
    
    def test_US10_2(self):
        families = {
            'F1': [('HUSB', 'I1'), ('WIFE', 'I2'), ('MARR', '15 OCT 2004'), ('DIV', '10 DEC 2010')],
            'F2': [('HUSB', 'I3'), ('WIFE', 'I4'), ('MARR', '1 JAN 2010')],
            'F3': [('HUSB', 'I5'), ('WIFE', 'I6'), ('MARR', '1 JAN 2020')]
        }
        individuals = {
            'I1': [],
            'I2': [],
            'I3': [],
            'I4': [],
            'I5': [],
            'I6': []
        }
        
        result = parse.noBigamy(families, individuals)
        self.assertEqual(result, "No Bigamy")
    
    def test_US10_3(self):
        families = {
            'F1': [('HUSB', 'I1'), ('WIFE', 'I2'), ('MARR', '15 NOV 2009'), ('DIV', '12 DEC 2008')],
            'F2': [('HUSB', 'I3'), ('WIFE', 'I4'), ('MARR', '1 JAN 2010')],
            'F3': [('HUSB', 'I5'), ('WIFE', 'I6'), ('MARR', '1 JAN 2020')]
        }
        individuals = {
            'I1': [],
            'I2': [],
            'I3': [],
            'I4': [],
            'I5': [],
            'I6': []
        }
        
        result = parse.noBigamy(families, individuals)
        self.assertEqual(result, "No Bigamy")
    
    def test_US10_4(self):
        families = {
            'F1': [],
            'F2': [],
            'F3': []
        }
        individuals = {
            'I1': [],
            'I2': [],
            'I3': [],
            'I4': [],
            'I5': [],
            'I6': []
        }
        
        result = parse.noBigamy(families, individuals)
        self.assertEqual(result, None)
    
    def test_US10_5(self):
        families = {
            'F1': [('HUSB', 'I1'), ('WIFE', 'I2'), ('MARR', '15 NOV 2000'), ('DIV', '12 DEC 2008')],
            'F2': [('HUSB', 'I3'), ('WIFE', 'I4'), ('MARR', '1 JAN 2010')],
            'F3': [('HUSB', 'I5'), ('WIFE', 'I6'), ('MARR', '1 JAN 2020')]
        }
        individuals = {
            'I1': [],
            'I2': [],
            'I3': [],
            'I4': [],
            'I5': [],
            'I6': []
        }
        
        result = parse.noBigamy(families, individuals)
        self.assertEqual(result, "No Bigamy")
    
    def test_US10_6(self):
        families = {
            'F1': [('HUSB', 'I1'), ('WIFE', 'I2'), ('MARR', '15 NOV 2000'), ('MARR', '15 DEC 2006'), ('DIV', '12 DEC 2008')],
            'F2': [('HUSB', 'I3'), ('WIFE', 'I4'), ('MARR', '1 JAN 2010')],
            'F3': [('HUSB', 'I5'), ('WIFE', 'I6'), ('MARR', '1 JAN 2020')]
        }
        individuals = {
            'I1': [],
            'I2': [],
            'I3': [],
            'I4': [],
            'I5': [],
            'I6': []
        }
        
        result = parse.noBigamy(families, individuals)
        self.assertEqual(result, "Bigamy caught")
    
    def test_US10_7(self):
        families = {
            'F1': [('HUSB', 'I1'), ('WIFE', 'I2'), ('MARR', '15 NOV 2000'), ('MARR', '15 DEC 2006'), ('MARR', '25 APR 2012'), ('DIV', '12 DEC 2008'), ('DIV', '25 DEC 2014')],
            'F2': [('HUSB', 'I3'), ('WIFE', 'I4'), ('MARR', '1 JAN 2010'), ('MARR', '5 JAN 2013'), ('DIV', '25 DEC 2014')],
            'F3': [('HUSB', 'I5'), ('WIFE', 'I6'), ('MARR', '1 JAN 2020')]
        }
        individuals = {
            'I1': [],
            'I2': [],
            'I3': [],
            'I4': [],
            'I5': [],
            'I6': []
        }
        
        result = parse.noBigamy(families, individuals)
        self.assertEqual(result, "Bigamy caught")
    
    def test_US10_8(self):
        families = {
            'F1': [('HUSB', 'I1'), ('WIFE', 'I2'), ('MARR', '15 NOV 2000')],
            'F2': [('HUSB', 'I3'), ('WIFE', 'I4'), ('MARR', '1 JAN 2010'), ('MARR', '5 JAN 2013'), ('DIV', '25 DEC 2014')],
            'F3': [('HUSB', 'I5'), ('WIFE', 'I6'), ('MARR', '1 JAN 2020')]
        }
        individuals = {
            'I1': [],
            'I2': [],
            'I3': [],
            'I4': [],
            'I5': [],
            'I6': []
        }
        
        result = parse.noBigamy(families, individuals)
        self.assertEqual(result, "Bigamy caught")
        
if __name__ == '__main__':
    unittest.main()


