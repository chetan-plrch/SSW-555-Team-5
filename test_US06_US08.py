import pytest

from parse import *

# US06: Divorce before death

def test_US06_1():
    families = {"@F1@": {"HUSB": "@I1@", "WIFE": "@I2@","DIV": "30 APR 2000"}}
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
    assert check_divorce_before_death(families, individuals) == True
    print('Divorce is before Wife death date')

def test_US06_2():
    families = {"@F1@": {"HUSB": "@I1@", "WIFE": "@I2@","DIV": "30 APR 2018"}}
    individuals = {
        "@I1@": {
        "NAME": "Arthur /Li/",
        "SEX": "M",
        "BIRT": "",
        "DATE": "10 OCT 1974",
        "DEAT": "Y",
        "DEATH_DATE": "26 NOV 2020",
        "FAMS": "@F1@",
        "FAMC": "@F3@",
    },
        "@I2@": {
        "NAME": "Amanda /Yu/",
        "SEX": "F",
        "BIRT": "",
        "DATE": "29 OCT 1976",
        "FAMS": "@F1@",
        "FAMC": "@F4@",
    }}
    assert check_divorce_before_death(families, individuals) == True
    print('Divorce is before Husband death date')


def test_US06_3():
    families = {"@F1@": {"HUSB": "@I1@", "WIFE": "@I2@","DIV": "30 APR 2018"}}
    individuals = {
        "@I1@": {
        "NAME": "Arthur /Li/",
        "SEX": "M",
        "BIRT": "",
        "DATE": "10 OCT 1974",
        "DEAT": "Y",
        "DEATH_DATE": "26 NOV 2000",
        "FAMS": "@F1@",
        "FAMC": "@F3@",
    },
        "@I2@": {
        "NAME": "Amanda /Yu/",
        "SEX": "F",
        "BIRT": "",
        "DATE": "29 OCT 1976",
        "FAMS": "@F1@",
        "FAMC": "@F4@",
    }}
    assert check_divorce_before_death(families, individuals) == False
    print('Divorce is after Husband death date')

def test_US06_4():
    families = {"@F1@": {"HUSB": "@I1@", "WIFE": "@I2@"}}
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
    assert check_divorce_before_death(families, individuals) == True
    print('No divorce date found')

def test_US06_5():
    families = {"@F1@": {"HUSB": "@I1@", "WIFE": "@I2@","DIV": "30 APR 2018"}}
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
    assert check_divorce_before_death(families, individuals) == False
    print('Divorce is after Wife death date')

# US08: Birth After Parents Marriage

def test_US08_1():
    families = {"@F1@": 
        [("HUSB", "@I1@"), 
         ("WIFE", "@I2@"),
         ("CHIL", "@I3@"),
         ("MARR", "30 APR 1997")
        ]}
    
    individuals = {
        "@I3@": [
        ("NAME", "Lawrence /Li/"),
        ("SEX","M"),
        ("BIRT", ""),
        ("DATE", "5 JAN 1998"),
        ("FAMC", "@F1@")
    ]}
    assert check_birth_after_parent_marriage(families, individuals) == True
    print('Birth is after Parent Marriage')

def test_US08_2():
    families = {"@F1@": 
        [("HUSB", "@I1@"), 
         ("WIFE", "@I2@"),
         ("CHIL", "@I3@"),
         ("MARR", "30 APR 2000")
        ]}
    
    individuals = {
        "@I3@": [
        ("NAME", "Lawrence /Li/"),
        ("SEX","M"),
        ("BIRT", ""),
        ("DATE", "5 JAN 1998"),
        ("FAMC", "@F1@")
    ]}
    assert check_birth_after_parent_marriage(families, individuals) == False
    print('Birth is before Parent Marriage')

def test_US08_3():
    families = {"@F1@": 
        [("HUSB", "@I1@"), 
         ("WIFE", "@I2@"),
         ("CHIL", "@I3@"),
         ("MARR", "6 JAN 2000")
        ]}
    
    individuals = {
        "@I3@": [
        ("NAME", "Lawrence /Li/"),
        ("SEX","M"),
        ("BIRT", ""),
        ("DATE", "5 JAN 1998"),
        ("FAMC", "@F1@")
    ]}
    assert check_birth_after_parent_marriage(families, individuals) == False
    print('No Marriage Date')

def test_US08_4():
    families = {"@F1@": 
        [("HUSB", "@I1@"), 
         ("WIFE", "@I2@"),
         ("CHIL", "@I3@"),
         ("MARR", "6 JAN 2000")
        ]}
    
    individuals = {
        "@I3@": [
        ("NAME", "Lawrence /Li/"),
        ("SEX","M"),
        ("BIRT", ""),
        ("DATE", "5 JAN 2000"),
        ("FAMC", "@F1@")
    ]}
    assert check_birth_after_parent_marriage(families, individuals) == False
    print('Marriage After Birthday')

def test_US08_5():
    families = {"@F1@": 
        [("HUSB", "@I1@"), 
         ("WIFE", "@I2@"),
         ("CHIL", "@I3@"),
         ("MARR", "4 JAN 2000")
        ]}

    #a = {"fid": [("MARR", "2023-06-16"), ("HUSB", "A"), ("WIFE", "B")]}
    
    individuals = {
        "@I3@": [
        ("NAME", "Lawrence /Li/"),
        ("SEX","M"),
        ("BIRT", ""),
        ("DATE", "5 JAN 2000"),
        ("FAMC", "@F1@")
    ]}
    assert check_birth_after_parent_marriage(families, individuals) == True
    print('Marriage After Birthday')
