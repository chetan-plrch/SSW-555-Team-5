import pytest

from parse import *

def test_US36_1():
    individuals = {
        "@I1@": [
        ("NAME", "Arthur/Li/"),
        ("SEX","M"),
        ("BIRT", ""),
        ("DATE", "5 JAN 1970"),
        ("DEAT", "6 AUG 2023"),
        ("FAMC", "@F1@")],
        "@I2@": [
        ("NAME", "Amanda/Yu-Li/"),
        ("SEX","F"),
        ("BIRT", ""),
        ("DATE", "5 JUN 1970"),
        ("DEAT", "6 AUG 2023"),
        ("FAMC", "@F1@")]
    }
    assert recent_deaths
    print('Died within last 30 days')


def test_US36_2():
    individuals = {
        "@I1@": [
        ("NAME", "Andrew/Li/"),
        ("SEX","M"),
        ("BIRT", ""),
        ("DATE", "5 JAN 1970"),
        ("DEAT", "6 AUG 2020"),
        ("FAMC", "@F1@")],
        "@I2@": [
        ("NAME", "Caleb/Yu/"),
        ("SEX","M"),
        ("BIRT", ""),
        ("DATE", "4 JUN 1972"),
        ("DEAT", "6 AUG 2020"),
        ("FAMC", "@F1@")]
    }
    assert recent_deaths
    print('Died within last 30 days')
    
def test_US36_3():
    individuals = {
        "@I1@": [
        ("NAME", "Andrew/Li/"),
        ("SEX","M"),
        ("BIRT", ""),
        ("DATE", "5 JAN 1970"),
        ("DEAT", "6 AUG 2020"),
        ("FAMC", "@F1@")],
        "@I2@": [
        ("NAME", "Caleb/Yu/"),
        ("SEX","M"),
        ("BIRT", ""),
        ("DATE", "4 JUN 1972"),
        ("DEAT", "6 AUG 2023"),
        ("FAMC", "@F1@")]
    }
    assert recent_deaths
def test_US37_1(): #Husb Recent Dead, Child 1 dead
    families = {"@F1@": 
        [("HUSB", "@I1@"), 
         ("WIFE", "@I2@"),
         ("CHIL", "@I3@","@I4@"),
         ("MARR", "4 FEB 1993")
        ]}
    individuals = {
        "@I1@": [
        ("NAME", "Arthur/Li/"),
        ("SEX","M"),
        ("BIRT", ""),
        ("DATE", "5 JAN 1970"),
        ("DEAT", "6 AUG 2023"),
        ("FAMC", "@F1@")],
        "@I2@": [
        ("NAME", "Amanda/Yu-Li/"),
        ("SEX","F"),
        ("BIRT", ""),
        ("DATE", "5 JUN 1970"),
        ("FAMC", "@F1@")],
        "@I3@": [
        ("NAME", "Andrew/Li/"),
        ("SEX","M"),
        ("BIRT", ""),
        ("DATE", "5 NOV 1995"),
        ("DEAT", "6 AUG 2023"),
        ("FAMC", "@F1@")],
        "@I4@": [
        ("NAME", "Caleb/Li/"),
        ("SEX","M"),
        ("BIRT", ""),
        ("DATE", "6 JUN 2000"),
        ("FAMC", "@F1@")]
    }
    assert recent_survivors
def test_US37_2(): #Wife Recent Dead
    families = {"@F1@": 
        [("HUSB", "@I1@"), 
         ("WIFE", "@I2@"),
         ("CHIL", "@I3@","@I4@"),
         ("MARR", "4 FEB 1993")
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
        ("DEAT", "6 AUG 2023"),
        ("FAMC", "@F1@")],
        "@I3@": [
        ("NAME", "Andrew/Li/"),
        ("SEX","M"),
        ("BIRT", ""),
        ("DATE", "5 NOV 1995"),
        ("DEAT", "6 AUG 2023"),
        ("FAMC", "@F1@")],
        "@I4@": [
        ("NAME", "Caleb/Li/"),
        ("SEX","M"),
        ("BIRT", ""),
        ("DATE", "6 JUN 2000"),
        ("FAMC", "@F1@")]
    }
    assert recent_survivors
def test_US37_3(): #No Family
    families = {"@F1@": 
        [("HUSB", ""), 
         ("WIFE", ""),
         ("CHIL", "@I1@"),
        ]}
    individuals = {
        "@I1@": [
        ("NAME", "Arthur/Li/"),
        ("SEX","M"),
        ("BIRT", ""),
        ("DATE", "5 JAN 1970"),
        ("FAMC", "@F1@")]
    }
    assert recent_survivors