import pytest

from parse import *

def test_US35_1():
    individuals = {
        "@I3@": [
        ("NAME", "Lawrence /Li/"),
        ("SEX","M"),
        ("BIRT", ""),
        ("DATE", "5 JUN 2023"),
        ("FAMC", "@F1@")
    ]}
    assert recent_births(individuals) == True
    print('Born within 30 days')

def test_US35_2():
    individuals = {
        "@I3@": [
        ("NAME", "Lawrence /Li/"),
        ("SEX","M"),
        ("BIRT", ""),
        ("DATE", "5 JUN 2000"),
        ("FAMC", "@F1@")
    ]}
    assert recent_births(individuals) == False
    print('Born within 30 days')

def test_US34_1():
    families = {"@F1@": 
        [("HUSB", "@I1@"), 
         ("WIFE", "@I2@"),
         ("CHIL", "@I3@"),
         ("MARR", "4 APR 1995")
        ]}
    
    individuals = {
        "@I1@": [
        ("NAME", "Arthur/Li/"),
        ("SEX","M"),
        ("BIRT", ""),
        ("DATE", "5 JAN 1900"),
        ("FAMC", "@F1@")],
        "@I2@": [
        ("NAME", "Amanda/Yu-Li/"),
        ("SEX","F"),
        ("BIRT", ""),
        ("DATE", "5 JUN 1970"),
        ("FAMC", "@F1@")]
    }
    assert large_age_difference(families, individuals) == True
    print('Large Age Difference')

def test_US34_2():
    families = {"@F1@": 
        [("HUSB", "@I1@"), 
         ("WIFE", "@I2@"),
         ("CHIL", "@I3@"),
         ("MARR", "4 APR 1995")
        ]}
    
    individuals = {
        "@I1@": [
        ("NAME", "Arthur/Li/"),
        ("SEX","M"),
        ("BIRT", ""),
        ("DATE", "5 JAN 1970"),
        ("FAMC", "@F1@")],
        "@I2@": [
        ("NAME", "Amanda/Yu-Li/"),
        ("SEX","F"),
        ("BIRT", ""),
        ("DATE", "5 JUN 1970"),
        ("FAMC", "@F1@")]
    }
    assert large_age_difference(families, individuals) == False
    print('Large Age Difference')