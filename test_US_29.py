import unittest
import parse
import datetime

class MyTestCase(unittest.TestCase):
    def test_US29_1(self):
        individuals =  {
            'I1': [('NAME', 'John /Doe/'), ('SEX', 'M'), ('DATE', '01 Jan 1990'), ('DEAT', '10 Mar 2022')], 
            'I2': [('NAME', 'Jane /Smith/'), ('SEX', 'F'), ('DATE', '15 Jun 1985'), ('FAMS', 'F1'), ('FAMC', 'F2')], 
            'I3': [('NAME', 'Mike /Johnson/'), ('SEX', 'M'), ('DATE', '05 Sep 1978'), ('DEAT', '20 Jul 2021'), ('FAMS', 'F1'), ('FAMC', 'F3')], 
            'I4': [('NAME', 'Anna /Davis/'), ('SEX', 'F'), ('DATE', '30 Nov 1995'), ('FAMC', 'F1')]
        }

        expected_deceased = ['10 Mar 2022', '20 Jul 2021']
        result = parse.list_deceased(individuals)
        self.assertEqual(result, expected_deceased)
        print('US29 Test Case 1 Passed: Deceased dates are displayed')

    def test_US29_2(self):
        individuals = {
            'I1': [('NAME', 'John /Doe/'), ('SEX', 'M'), ('DATE', '01 Jan 1990')],
            'I2': [('NAME', 'Jane /Smith/'), ('SEX', 'F'), ('DATE', '15 Jun 1985')],
            'I3': [('NAME', 'Mike /Johnson/'), ('SEX', 'M'), ('DATE', '05 Sep 1978')],
            'I4': [('NAME', 'Anna /Davis/'), ('SEX', 'F'), ('DATE', '30 Nov 1995')],
        }

        expected_deceased = []
        result = parse.list_deceased(individuals)
        self.assertEqual(result, expected_deceased)
        print('US29 Test Case 2 Passed: No deceased dates')

    def test_US29_3(self):
        individuals = {
            'I1': [('NAME', 'John /Doe/'), ('SEX', 'M'), ('DATE', '01 Jan 1990'), ('DEAT', '10 Mar 2022')],
            'I2': [('NAME', 'Jane /Smith/'), ('SEX', 'F'), ('DATE', '15 Jun 1985'), ('FAMS', 'F1'), ('FAMC', 'F2')],
            'I3': [('NAME', 'Mike /Johnson/'), ('SEX', 'M'), ('DATE', '05 Sep 1978')],
            'I4': [('NAME', 'Anna /Davis/'), ('SEX', 'F'), ('DATE', '30 Nov 1995')],
        }

        expected_deceased = ['10 Mar 2022']
        result = parse.list_deceased(individuals)
        self.assertEqual(result, expected_deceased)
        print('US29 Test Case 3 Passed: One deceased date')

    def test_US29_4(self):
        individuals = {
            'I1': [('NAME', 'John /Doe/'), ('SEX', 'M'), ('DATE', '01 Jan 1990'), ('DEAT', '10 Mar 2022')],
            'I2': [('NAME', 'Jane /Smith/'), ('SEX', 'F'), ('DATE', '15 Jun 1985'), ('FAMS', 'F1'), ('FAMC', 'F2')],
            'I3': [('NAME', 'Mike /Johnson/'), ('SEX', 'M'), ('DATE', '05 Sep 1978'), ('DEAT', '20 Jul 2021'), ('FAMS', 'F1'), ('FAMC', 'F3')],
            'I4': [('NAME', 'Anna /Davis/'), ('SEX', 'F'), ('DATE', '30 Nov 1995')],
        }

        expected_deceased = ['10 Mar 2022', '20 Jul 2021']
        result = parse.list_deceased(individuals)
        self.assertEqual(result, expected_deceased)
        print('US29 Test Case 4 Passed: Multiple deceased dates')

    def test_US29_5(self):
        individuals = {
            'I1': [('NAME', 'John /Doe/'), ('SEX', 'M'), ('DATE', '01 Jan 1990'), ('DEAT', '10 Mar 2022')],
            'I2': [('NAME', 'Jane /Smith/'), ('SEX', 'F'), ('DATE', '15 Jun 1985'), ('DEAT', '10 Mar 2022'), ('FAMS', 'F1'), ('FAMC', 'F2')],
            'I3': [('NAME', 'Mike /Johnson/'), ('SEX', 'M'), ('DATE', '05 Sep 1978'), ('DEAT', '10 Mar 2022'), ('FAMS', 'F1'), ('FAMC', 'F3')],
            'I4': [('NAME', 'Anna /Davis/'), ('SEX', 'F'), ('DATE', '30 Nov 1995')],
        }

        expected_deceased = ['10 Mar 2022', '10 Mar 2022', '10 Mar 2022']
        result = parse.list_deceased(individuals)
        self.assertEqual(result, expected_deceased)
        print('US29 Test Case 5 Passed: Multiple individuals with the same deceased date')
    
    #Refactoring Updated Test Cases   Refactoring Assignment
    # def test_US29_6(self):
    #     individuals = {
    #         'I1': [('NAME', 'John /Doe/'), ('SEX', 'M'), ('DATE', '01 Jan 1990'), ('DEAT', '10 Mar 2022')],
    #         'I2': [('NAME', 'Jane /Smith/'), ('SEX', 'F'), ('DATE', '15 Jun 1985')],
    #         'I3': [('NAME', 'Mike /Johnson/'), ('SEX', 'M'), ('DATE', '05 Sep 1978'), ('DEAT', '20 Jul 2021')],
    #         'I4': [('NAME', 'Anna /Davis/'), ('SEX', 'F'), ('DATE', '30 Nov 1995')],
    #     }

    #     expected_deceased = ['10 Mar 2022', '20 Jul 2021']
    #     result = parse.list_deceased(individuals)
    #     self.assertEqual(result, expected_deceased)
    #     print('US29 Test Case 6 Passed: Multiple deceased dates')


    # def test_US29_7(self):
    #     individuals = {
    #         'I1': [('NAME', 'John /Doe/'), ('SEX', 'M'), ('DATE', '01 Jan 1990')],
    #         'I2': [('NAME', 'Jane /Smith/'), ('SEX', 'F'), ('DATE', '15 Jun 1985')],
    #         'I3': [('NAME', 'Mike /Johnson/'), ('SEX', 'M'), ('DATE', '05 Sep 1978')],
    #         'I4': [('NAME', 'Anna /Davis/'), ('SEX', 'F'), ('DATE', '30 Nov 1995')],
    #     }

    #     expected_deceased = []
    #     result = parse.list_deceased(individuals)
    #     self.assertEqual(result, expected_deceased)
    #     print('US29 Test Case 7 Passed: No deceased dates')

if __name__ == '__main__':
    unittest.main()