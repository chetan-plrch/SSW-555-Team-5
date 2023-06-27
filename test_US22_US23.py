import unittest
import parse
import datetime

class MyTestCase(unittest.TestCase):
    # US22: Unique ID
    def test_US22_1(case):
        individuals = {
            "@I1@": {
            "NAME": "Arthur /Li/",
            "SEX": "M",
            "BIRT": "",
            "DATE": "10 OCT 1974",
            "FAMS": "@F1@",
            "FAMC": "@F3@",
        },
            "@I2@": {
            "NAME": "Amanda /Yu/",
            "SEX": "F",
            "BIRT": "",
            "DATE": "29 OCT 1976",
            "DEAT": "Y",
            "DEATH_DATE": "26 NOV 2000",
            "FAMS": "@F1@",
            "FAMC": "@F4@",
        }}
        case.assertIsNone(parse.unique_id(individuals, '-'))
        print('US22 Test Case #1 - Missing families')

    def test_US22_2(case):
        families = {
            "@F1@": {"HUSB": "@I1@", "WIFE": "@I2@","DIV": "30 APR 2000"},
            "@F2@": {"HUSB": "@I6@", "WIFE": "@I7@"},
            "@F3@": {"HUSB": "@I8@", "WIFE": "@I10@","DIV": "13 JUN 2013"}}
        case.assertIsNone(parse.unique_id('-', families))
        print('US22 Test Case #2 - Missing individuals')

    def test_US22_3(case):
        individuals = {
            "@I1@": {
            "NAME": "Arthur /Li/",
            "SEX": "M",
            "BIRT": "",
            "DATE": "10 OCT 1974",
            "FAMS": "@F1@",
            "FAMC": "@F3@",
        },
            "@I2@": {
            "NAME": "Amanda /Yu/",
            "SEX": "F",
            "BIRT": "",
            "DATE": "29 OCT 1976",
            "DEAT": "Y",
            "DEATH_DATE": "26 NOV 2000",
            "FAMS": "@F1@",
            "FAMC": "@F4@",
        }}
        families = {
            "@F1@": {"HUSB": "@I1@", "WIFE": "@I2@","DIV": "30 APR 2000"},
            "@F2@": {"HUSB": "@I6@", "WIFE": "@I7@"},
            "@F3@": {"HUSB": "@I8@", "WIFE": "@I10@","DIV": "13 JUN 2013"}}

        case.assertEqual(parse.unique_id(individuals, families), True)
        print('US22 Test Case #3 - Passed: All have unique IDs')

    def test_US22_4(case):
        individuals = {
            "@I1@": {
            "NAME": "Arthur /Li/",
            "SEX": "M",
            "BIRT": "",
            "DATE": "10 OCT 1974",
            "FAMS": "@F1@",
            "FAMC": "@F3@",
        },
            "@I2@": {
            "NAME": "Amanda /Yu/",
            "SEX": "F",
            "BIRT": "",
            "DATE": "29 OCT 1976",
            "DEAT": "Y",
            "DEATH_DATE": "26 NOV 2000",
            "FAMS": "@F1@",
            "FAMC": "@F4@",
        }}
        families = {
            "@F1@": {"HUSB": "@I1@", "WIFE": "@I2@","DIV": "30 APR 2000"},
            "@F1@": {"HUSB": "@I6@", "WIFE": "@I7@"},
            "@F3@": {"HUSB": "@I8@", "WIFE": "@I10@","DIV": "13 JUN 2013"}}
        case.assertEqual(parse.unique_id(individuals, families), True)
        print('US22 Test Case #4 - Family has matching IDs: however dictionary removes duplicates')
        
    def test_US22_5(case):
        individuals = {
            "@I1@": {
            "NAME": "Arthur /Li/",
            "SEX": "M",
            "BIRT": "",
            "DATE": "10 OCT 1974",
            "FAMS": "@F1@",
            "FAMC": "@F3@",
        },
            "@I1@": {
            "NAME": "Amanda /Yu/",
            "SEX": "F",
            "BIRT": "",
            "DATE": "29 OCT 1976",
            "DEAT": "Y",
            "DEATH_DATE": "26 NOV 2000",
            "FAMS": "@F1@",
            "FAMC": "@F4@",
        }}
        families = {
            "@F1@": {"HUSB": "@I1@", "WIFE": "@I2@","DIV": "30 APR 2000"},
            "@F2@": {"HUSB": "@I6@", "WIFE": "@I7@"},
            "@F3@": {"HUSB": "@I8@", "WIFE": "@I10@","DIV": "13 JUN 2013"}}
        case.assertEqual(parse.unique_id(individuals, families), True)
        print('US22 Test Case #5 - Individual has matching IDs: however dictionary removes duplicates')
        
    # US23: Unique name and birthday
    def test_US23_1(case):
        case.assertIsNone(parse.unique_name_and_birth('-') )
        print('US23 Test Case #1 - Passed: Marriage date and birth date are not present')

    def test_US23_2(case):
        individuals = {
            "@I1@": {
            "NAME": "Arthur /Li/",
            "SEX": "M",
            "BIRT": "",
            "DATE": "10 OCT 1974",
            "FAMS": "@F1@",
            "FAMC": "@F3@",
        },
            "@I2@": {
            "NAME": "Amanda /Yu/",
            "SEX": "F",
            "BIRT": "",
            "DATE": "29 OCT 1976",
            "DEAT": "Y",
            "DEATH_DATE": "26 NOV 2000",
            "FAMS": "@F1@",
            "FAMC": "@F4@",
        }}
        case.assertEqual(parse.unique_name_and_birth(individuals), True)
        print('US23 Test Case #2 - Passed: All individuals have a unqie name and birthday')

    def test_US23_3(case):
        individuals = {
            "@I1@": {
            "NAME": "Amanda /Yu/",
            "SEX": "M",
            "BIRT": "",
            "DATE": "10 OCT 1974",
            "FAMS": "@F1@",
            "FAMC": "@F3@",
        },
            "@I2@": {
            "NAME": "Amanda /Yu/",
            "SEX": "F",
            "BIRT": "",
            "DATE": "29 OCT 1976",
            "DEAT": "Y",
            "DEATH_DATE": "26 NOV 2000",
            "FAMS": "@F1@",
            "FAMC": "@F4@",
        }}
        case.assertEqual(parse.unique_name_and_birth(individuals), True)
        print('US23 Test Case #3 - Passed: Same name but not same birth')

    def test_US23_4(case):
        individuals = {
            "@I1@": {
            "NAME": "Arthur /Lee/",
            "SEX": "M",
            "BIRT": "",
            "DATE": "10 OCT 1976",
            "FAMS": "@F1@",
            "FAMC": "@F3@",
        },
            "@I2@": {
            "NAME": "Amanda /Yu/",
            "SEX": "F",
            "BIRT": "",
            "DATE": "29 OCT 1976",
            "DEAT": "Y",
            "DEATH_DATE": "26 NOV 2000",
            "FAMS": "@F1@",
            "FAMC": "@F4@",
        }}
        case.assertEqual(parse.unique_name_and_birth(individuals), True)
        print('US23 Test Case #4 - Passed: Same birthday but different names')

    def test_US23_5(case):
        individuals = {
            "@I1@": {
            "NAME": "Arthur /Lee/",
            "SEX": "M",
            "BIRT": "",
            "DATE": "10 OCT 1976",
            "FAMS": "@F1@",
            "FAMC": "@F3@",
        },
            "@I2@": {
            "NAME": "Arthur /Yu/",
            "SEX": "F",
            "BIRT": "",
            "DATE": "29 OCT 1976",
            "DEAT": "Y",
            "DEATH_DATE": "26 NOV 2000",
            "FAMS": "@F1@",
            "FAMC": "@F4@",
        }}
        case.assertEqual(parse.unique_name_and_birth(individuals), True)
        print('US23 Test Case #5 - Same name and birth')

if __name__ == '__main__':
    unittest.main()