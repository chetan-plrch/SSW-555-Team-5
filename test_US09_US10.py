import unittest
import parse
import datetime

class MyTestCase(unittest.TestCase):
    # US09: Birth After Death of Parents
    def test_US09_1(case):
        parentB = {
            "@I3@": {
            "NAME": "Christopher /Li/",
            "SEX": "M",
            "BIRT": "",
            "DATE": "14 MAY 1975",
            "DEAT": "",
            "DATE": "16 JUL 2010",
            "FAMC": "@F1@"
        }}
        child = {
            "@I3@": {
            "NAME": "Jenn",
            "SEX": "F",
            "BIRT": "",
            "DATE": "5 JAN 1998",
            "FAMC": "@F1@"
        }}
        case.assertIsNone(parse.birth_after_parent_death('-', parentB, child))
        print('Missing parentA')

    def test_US09_2(case):
        parentA = {
            "@I3@": {
            "NAME": "Natalie /Li/",
            "SEX": "F",
            "BIRT": "",
            "DATE": "21 DEC 1981",
            "DEAT": "",
            "DATE": "30 MAR 2020",
            "FAMC": "@F1@"
        }}
        parentB = {
            "@I3@": {
            "NAME": "Christopher /Li/",
            "SEX": "M",
            "BIRT": "",
            "DATE": "14 MAY 1975",
            "DEAT": "",
            "DATE": "16 JUL 2010",
            "FAMC": "@F1@"
        }}
        case.assertIsNone(parse.birth_after_parent_death(parentA, parentB, '-'))
        print('Missing child')

    def test_US09_3(case):
        parentA = {
            "@I3@": {
            "NAME": "Natalie /Li/",
            "SEX": "F",
            "BIRT": "",
            "DATE": "21 DEC 1981",
            "DEAT": "",
            "DATE": "30 MAR 2020",
            "FAMC": "@F1@"
        }}
        parentB = {
            "@I3@": {
            "NAME": "Christopher /Li/",
            "SEX": "M",
            "BIRT": "",
            "DATE": "14 MAY 1975",
            "DEAT": "",
            "DATE": "16 JUL 2010",
            "FAMC": "@F1@"
        }}
        child = {
            "@I3@": {
            "NAME": "Jenn",
            "SEX": "F",
            "BIRT": "",
            "DATE": "5 JAN 1998",
            "FAMC": "@F1@"
        }}
        case.assertEqual(parse.birth_after_parent_death(parentA, parentB, child), False)
        print('Birth before death of a parent')

    def test_US09_4(case):
        parentA = {
            "@I3@": {
            "NAME": "Natalie /Li/",
            "SEX": "F",
            "BIRT": "",
            "DATE": "21 DEC 1981",
            "DEAT": "",
            "DATE": "30 MAR 1997",
            "FAMC": "@F1@"
        }}
        parentB = {
            "@I3@": {
            "NAME": "Christopher /Li/",
            "SEX": "M",
            "BIRT": "",
            "DATE": "14 MAY 1975",
            "DEAT": "",
            "DATE": "16 JUL 2010",
            "FAMC": "@F1@"
        }}
        child = {
            "@I3@": {
            "NAME": "Jenn",
            "SEX": "F",
            "BIRT": "",
            "DATE": "5 JAN 1998",
            "FAMC": "@F1@"
        }}
        case.assertEqual(parse.birth_after_parent_death(parentA, parentB, child), True)
        print('Birth after death of a parent')

    def test_US09_5(case):
        parentA = {
            "@I3@": {
            "NAME": "Natalie /Li/",
            "SEX": "F",
            "BIRT": "",
            "DATE": "21 DEC 1981",
            "DEAT": "",
            "DATE": "30 MAR 2020",
            "FAMC": "@F1@"
        }}
        parentB = {
            "@I3@": {
            "NAME": "Christopher /Li/",
            "SEX": "M",
            "BIRT": "",
            "DATE": "14 MAY 1975",
            "DEAT": "",
            "DATE": "16 JUL 1996",
            "FAMC": "@F1@"
        }}
        child = {
            "@I3@": {
            "NAME": "Jenn",
            "SEX": "F",
            "BIRT": "",
            "DATE": "5 JAN 1998",
            "FAMC": "@F1@"
        }}
        case.assertEqual(parse.birth_after_parent_death(parentA, parentB, child), True)
        print('Born after death of parent')
        
    # US10: Marriage before 14
    def test_US10_1(case):
        case.assertIsNone(parse.married_before_fourteen('-', '-') )
        print('US10 Test Case #1 - Passed: Marriage date and birth date are not present')

    def test_US10_2(case):
        case.assertIsNone(parse.married_before_fourteen('-', 1995))
        print('US10 Test Case #2 - Passed: Marriage date is not present and birth date is present')

    def test_US10_3(case):
        case.assertIsNone(parse.married_before_fourteen(1995, '-'))
        print('US10 Test Case #3 - Passed: Marriage date is present and birth date is not present')

    def test_US10_4(case):
        case.assertEqual(parse.married_before_fourteen(1995, 1984), True)
        print('US10 Test Case #4 - Marriage date is before 14')

    def test_US10_5(case):
        case.assertEqual(parse.married_before_fourteen(1995, 1975), False)
        print('US10 Test Case #5 - Marriage date is after 14')

if __name__ == '__main__':
    unittest.main()