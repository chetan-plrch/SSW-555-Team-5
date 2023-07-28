import unittest
import parse

individuals = {
    "I1": [
        ("NAME", "Hamilton P /Kirk/"),
        ("SEX", "M"),
        ("DATE", "29 DEC 1995"),
        ("FAMC", "F1"),
    ],
    "I2": [
        ("NAME", "Elena /Golecha/"),
        ("SEX", "F"),
        ("DATE", "1 JAN 1926"),
        ("DEAT", "1 JAN 2012"),
        ("FAMS", "F1"),
        ("FAMC", "F2"),
    ],
    "I3": [
        ("NAME", "Stevens /Krik/"),
        ("SEX", "M"),
        ("DATE", "1 DEC 1969"),
        ("FAMS", "F1"),
        ("FAMC", "F3"),
    ],
    "I4": [
        ("NAME", "Kamala /Kirk/"),
        ("SEX", "M"),
        ("DATE", "29 DEC 1995"),
        ("FAMC", "F1"),
    ],
    "I5": [
        ("NAME", "Keerthi /Kirk/"),
        ("SEX", "M"),
        ("DATE", "29 DEC 1995"),
        ("FAMC", "F1"),
    ],
    "I6": [
        ("NAME", "Rex /Stevens/"),
        ("SEX", "M"),
        ("DATE", "29 DEC 1995"),
        ("FAMC", "F1"),
    ],
    "I7": [
        ("NAME", "Tom /Golecha/"),
        ("SEX", "M"),
        ("DATE", "29 DEC 1995"),
        ("FAMC", "F1"),
    ],
    "I8": [
        ("NAME", "Jared /Golecha/"),
        ("SEX", "M"),
        ("DATE", "29 DEC 1995"),
        ("FAMC", "F1"),
    ],
    "I9": [
        ("NAME", "Putli /Bafna/"),
        ("SEX", "F"),
        ("DATE", "13 FEB 1952"),
        ("DEAT", "13 FEB 1985"),
        ("FAMS", "F3"),
    ],
    "I10": [
        ("NAME", "Jasraj /Kirk/"),
        ("SEX", "M"),
        ("DATE", "13 FEB 1950"),
        ("DEAT", "13 FEB 1975"),
        ("FAMS", "F3"),
        ("FAMC", "F8"),
    ],
    "I11": [
        ("NAME", "Felix /Stevens/"),
        ("SEX", "M"),
        ("DATE", "29 DEC 1995"),
        ("FAMC", "F1"),
    ],
    "I12": [
        ("NAME", "Manoj /Kirk/"),
        ("SEX", "M"),
        ("DATE", "12 FEB 1930"),
        ("DEAT", "12 FEB 1980"),
        ("FAMS", "F5"),
    ],
    "I13": [
        ("NAME", "Teena /Alma/"),
        ("SEX", "F"),
        ("DATE", "1 MAR 1930"),
        ("DEAT", "12 FEB 1985"),
        ("FAMS", "F5"),
    ],
    "I14": [
        ("NAME", "Anjali /Ambani/"),
        ("SEX", "F"),
        ("DATE", "12 JUL 1925"),
        ("DEAT", "2 AUG 1999"),
        ("FAMS", "F8"),
    ],
    "I15": [
        ("NAME", "James /Kirk/"),
        ("SEX", "M"),
        ("DATE", "12 SEP 1930"),
        ("DEAT", "12 SEP 2000"),
        ("FAMS", "F8"),
    ],
    "I16": [
        ("NAME", "Jen /Folger/"),
        ("SEX", "F"),
        ("DATE", "12 MAR 1979"),
        ("FAMS", "F7"),
    ],
    "I17": [
        ("NAME", "Kim /Smith/"),
        ("SEX", "F"),
        ("DATE", "18 OCT 1985"),
        ("FAMS", "F6"),
    ],
}

families = {
    'F1': [('HUSB', 'I3'), ('WIFE', 'I2'), ('CHIL', 'I1'), ('CHIL', 'I4'), ('CHIL', 'I5'), ('CHIL', 'I6'), ('CHIL', 'I7'), ('CHIL', 'I8'), ('CHIL', 'I11'),('MARR', '12 JAN 1995')],
    'F2': [('HUSB', 'I9'), ('WIFE', 'I10'), ('MARR', '12 SEP 1968')]
}


individuals2 = {
    "I1": [
        ("NAME", "Hamilton P /Kirk/"),
        ("SEX", "M"),
        ("DATE", "29 DEC 1995"),
        ("FAMC", "F1"),
    ],
    "I2": [
        ("NAME", "Elena /Golecha/"),
        ("SEX", "F"),
        ("DATE", "1 JAN 1926"),
        ("DEAT", "1 JAN 2012"),
        ("FAMS", "F1"),
        ("FAMC", "F2"),
    ],
    "I3": [
        ("NAME", "Stevens /Krik/"),
        ("SEX", "M"),
        ("DATE", "1 DEC 1969"),
        ("FAMS", "F1"),
        ("FAMC", "F3"),
    ],
    "I4": [
        ("NAME", "Kamala /Kirk/"),
        ("SEX", "M"),
        ("DATE", "29 DEC 1995"),
        ("FAMC", "F1"),
    ],
    "I5": [
        ("NAME", "Keerthi /Kirk/"),
        ("SEX", "M"),
        ("DATE", "29 DEC 1995"),
        ("FAMC", "F1"),
    ],
    "I6": [
        ("NAME", "Rex /Stevens/"),
        ("SEX", "M"),
        ("DATE", "29 DEC 1995"),
        ("FAMC", "F1"),
    ],
    "I7": [
        ("NAME", "Tom /Golecha/"),
        ("SEX", "M"),
        ("DATE", "29 DEC 1995"),
        ("FAMC", "F1"),
    ],
    "I8": [
        ("NAME", "Jared /Golecha/"),
        ("SEX", "M"),
        ("DATE", "29 DEC 1995"),
        ("FAMC", "F1"),
    ],
    "I9": [
        ("NAME", "Putli /Bafna/"),
        ("SEX", "F"),
        ("DATE", "13 FEB 1952"),
        ("DEAT", "13 FEB 1985"),
        ("FAMS", "F3"),
    ],
    "I10": [
        ("NAME", "Jasraj /Kirk/"),
        ("SEX", "M"),
        ("DATE", "13 FEB 1950"),
        ("DEAT", "13 FEB 1975"),
        ("FAMS", "F3"),
        ("FAMC", "F8"),
    ],
    "I11": [
        ("NAME", "Felix /Stevens/"),
        ("SEX", "M"),
        ("DATE", "29 DEC 1995"),
        ("FAMC", "F1"),
    ],
    "I12": [
        ("NAME", "Manoj /Kirk/"),
        ("SEX", "M"),
        ("DATE", "12 FEB 1930"),
        ("DEAT", "12 FEB 1980"),
        ("FAMS", "F5"),
    ],
    "I13": [
        ("NAME", "Teena /Alma/"),
        ("SEX", "F"),
        ("DATE", "1 MAR 1930"),
        ("DEAT", "12 FEB 1985"),
        ("FAMS", "F5"),
    ],
    "I14": [
        ("NAME", "Anjali /Ambani/"),
        ("SEX", "F"),
        ("DATE", "12 JUL 1925"),
        ("DEAT", "2 AUG 1999"),
        ("FAMS", "F8"),
    ],
    "I15": [
        ("NAME", "James /Kirk/"),
        ("SEX", "M"),
        ("DATE", "12 SEP 1930"),
        ("DEAT", "12 SEP 2000"),
        ("FAMS", "F8"),
    ],
    "I16": [
        ("NAME", "Jen /Folger/"),
        ("SEX", "F"),
        ("DATE", "12 MAR 1979"),
        ("FAMS", "F7"),
    ],
    "I17": [
        ("NAME", "Kim /Smith/"),
        ("SEX", "F"),
        ("DATE", "18 OCT 1985"),
        ("FAMS", "F6"),
    ],
}

families2 = {
    'F1': [('HUSB', 'I3'), ('WIFE', 'I2'), ('CHIL', 'I1'), ('CHIL', 'I4'), ('CHIL', 'I5'), ('CHIL', 'I6'), ('CHIL', 'I7'), ('CHIL', 'I8'), ('CHIL', 'I11'),('MARR', '12 JAN 1995')],
    'F2': [('HUSB', 'I9'), ('WIFE', 'I10'), ('MARR', '12 SEP 1968')]
}

individuals3 = {
    "I1": [
        ("NAME", "Hamilton P /Kirk/"),
        ("SEX", "M"),
        ("DATE", "29 DEC 1995"),
        ("FAMC", "F1"),
    ],
    "I2": [
        ("NAME", "Elena /Golecha/"),
        ("SEX", "F"),
        ("DATE", "1 JAN 1976"),
        ("DEAT", "1 JAN 2012"),
        ("FAMS", "F1"),
        ("FAMC", "F2"),
    ],
    "I3": [
        ("NAME", "Stevens /Krik/"),
        ("SEX", "M"),
        ("DATE", "1 DEC 1969"),
        ("FAMS", "F1"),
        ("FAMC", "F3"),
    ],
    "I4": [
        ("NAME", "Kamala /Kirk/"),
        ("SEX", "M"),
        ("DATE", "29 DEC 1995"),
        ("FAMC", "F1"),
    ],
    "I5": [
        ("NAME", "Keerthi /Kirk/"),
        ("SEX", "M"),
        ("DATE", "29 DEC 1995"),
        ("FAMC", "F1"),
    ],
    "I6": [
        ("NAME", "Rex /Stevens/"),
        ("SEX", "M"),
        ("DATE", "29 DEC 1995"),
        ("FAMC", "F1"),
    ],
    "I7": [
        ("NAME", "Tom /Golecha/"),
        ("SEX", "M"),
        ("DATE", "29 DEC 1995"),
        ("FAMC", "F1"),
    ],
    "I8": [
        ("NAME", "Jared /Golecha/"),
        ("SEX", "M"),
        ("DATE", "29 DEC 1993"),
        ("FAMC", "F1"),
    ],
    "I9": [
        ("NAME", "Putli /Bafna/"),
        ("SEX", "F"),
        ("DATE", "13 FEB 1952"),
        ("DEAT", "13 FEB 1985"),
        ("FAMS", "F3"),
    ],
    "I10": [
        ("NAME", "Jasraj /Kirk/"),
        ("SEX", "M"),
        ("DATE", "13 FEB 1950"),
        ("DEAT", "13 FEB 1975"),
        ("FAMS", "F3"),
        ("FAMC", "F8"),
    ],
    "I11": [
        ("NAME", "Felix /Stevens/"),
        ("SEX", "M"),
        ("DATE", "29 DEC 1996"),
        ("FAMC", "F1"),
    ],
    "I12": [
        ("NAME", "Manoj /Kirk/"),
        ("SEX", "M"),
        ("DATE", "12 FEB 1930"),
        ("DEAT", "12 FEB 1980"),
        ("FAMS", "F5"),
    ],
    "I13": [
        ("NAME", "Teena /Alma/"),
        ("SEX", "F"),
        ("DATE", "1 MAR 1930"),
        ("DEAT", "12 FEB 1985"),
        ("FAMS", "F5"),
    ],
    "I14": [
        ("NAME", "Anjali /Ambani/"),
        ("SEX", "F"),
        ("DATE", "12 JUL 1925"),
        ("DEAT", "2 AUG 1999"),
        ("FAMS", "F8"),
    ],
    "I15": [
        ("NAME", "James /Kirk/"),
        ("SEX", "M"),
        ("DATE", "12 SEP 1930"),
        ("DEAT", "12 SEP 2000"),
        ("FAMS", "F8"),
    ],
    "I16": [
        ("NAME", "Jen /Folger/"),
        ("SEX", "F"),
        ("DATE", "12 MAR 1979"),
        ("FAMS", "F7"),
    ],
    "I17": [
        ("NAME", "Kim /Smith/"),
        ("SEX", "F"),
        ("DATE", "18 OCT 1985"),
        ("FAMS", "F6"),
    ],
}

families3 = {
    'F1': [('HUSB', 'I3'), ('WIFE', 'I2'), ('CHIL', 'I1'), ('CHIL', 'I4'), ('CHIL', 'I5'), ('CHIL', 'I6'), ('CHIL', 'I7'), ('CHIL', 'I8'), ('CHIL', 'I11'),('MARR', '12 JAN 1995')],
    'F2': [('HUSB', 'I9'), ('WIFE', 'I10'), ('MARR', '12 SEP 1968')]
}

individuals4 = {
    "I1": [
        ("NAME", "Hamilton P /Kirk/"),
        ("SEX", "M"),
        ("DATE", "29 DEC 1995"),
        ("FAMC", "F1"),
    ],
    "I2": [
        ("NAME", "Elena /Golecha/"),
        ("SEX", "F"),
        ("DATE", "1 JAN 1976"),
        ("DEAT", "1 JAN 2012"),
        ("FAMS", "F1"),
        ("FAMC", "F2"),
    ],
    "I3": [
        ("NAME", "Stevens /Krik/"),
        ("SEX", "M"),
        ("DATE", "1 DEC 1969"),
        ("FAMS", "F1"),
        ("FAMC", "F3"),
    ],
    "I4": [
        ("NAME", "Kamala /Kirk/"),
        ("SEX", "M"),
        ("DATE", "29 DEC 1995"),
        ("FAMC", "F1"),
    ],
    "I5": [
        ("NAME", "Keerthi /Kirk/"),
        ("SEX", "M"),
        ("DATE", "29 DEC 1995"),
        ("FAMC", "F1"),
    ],
    "I6": [
        ("NAME", "Rex /Stevens/"),
        ("SEX", "M"),
        ("DATE", "29 DEC 1995"),
        ("FAMC", "F1"),
    ],
    "I7": [
        ("NAME", "Tom /Golecha/"),
        ("SEX", "M"),
        ("DATE", "29 DEC 1995"),
        ("FAMC", "F1"),
    ],
    "I8": [
        ("NAME", "Jared /Golecha/"),
        ("SEX", "M"),
        ("DATE", "29 DEC 1993"),
        ("FAMC", "F1"),
    ],
    "I9": [
        ("NAME", "Putli /Bafna/"),
        ("SEX", "F"),
        ("DATE", "13 FEB 1952"),
        ("DEAT", "13 FEB 1985"),
        ("FAMS", "F3"),
    ],
    "I10": [
        ("NAME", "Jasraj /Kirk/"),
        ("SEX", "M"),
        ("DATE", "13 FEB 1950"),
        ("DEAT", "13 FEB 1975"),
        ("FAMS", "F3"),
        ("FAMC", "F8"),
    ],
    "I11": [
        ("NAME", "Felix /Stevens/"),
        ("SEX", "M"),
        ("DATE", "29 DEC 1996"),
        ("FAMC", "F1"),
    ],
    "I12": [
        ("NAME", "Manoj /Kirk/"),
        ("SEX", "M"),
        ("DATE", "12 FEB 1930"),
        ("DEAT", "12 FEB 1980"),
        ("FAMS", "F5"),
    ],
    "I13": [
        ("NAME", "Teena /Alma/"),
        ("SEX", "F"),
        ("DATE", "1 MAR 1930"),
        ("DEAT", "12 FEB 1985"),
        ("FAMS", "F5"),
    ],
    "I14": [
        ("NAME", "Anjali /Ambani/"),
        ("SEX", "F"),
        ("DATE", "12 JUL 1925"),
        ("DEAT", "2 AUG 1999"),
        ("FAMS", "F8"),
    ],
    "I15": [
        ("NAME", "James /Kirk/"),
        ("SEX", "M"),
        ("DATE", "12 SEP 1930"),
        ("DEAT", "12 SEP 2000"),
        ("FAMS", "F8"),
    ],
    "I16": [
        ("NAME", "Jen /Folger/"),
        ("SEX", "F"),
        ("DATE", "12 MAR 1979"),
        ("FAMS", "F7"),
    ],
    "I17": [
        ("NAME", "Kim /Smith/"),
        ("SEX", "F"),
        ("DATE", "18 OCT 1985"),
        ("FAMS", "F6"),
    ],
}

families4 = {
    'F1': [('HUSB', 'I3'), ('WIFE', 'I2'), ('CHIL', 'I1'), ('CHIL', 'I4'), ('CHIL', 'I5'), ('CHIL', 'I6'), ('CHIL', 'I7'), ('CHIL', 'I8'), ('CHIL', 'I11'),('MARR', '12 JAN 1995')],
    'F2': [('HUSB', 'I9'), ('WIFE', 'I10'), ('MARR', '12 SEP 1968')]
}


individuals5 = {
    "I1": [
        ("NAME", "Hamilton P /Kirk/"),
        ("SEX", "M"),
        ("DATE", "29 DEC 1995"),
        ("FAMC", "F1"),
    ],
    "I2": [
        ("NAME", "Elena /Golecha/"),
        ("SEX", "F"),
        ("DATE", "1 JAN 1976"),
        ("DEAT", "1 JAN 2012"),
        ("FAMS", "F1"),
        ("FAMC", "F2"),
    ],
    "I3": [
        ("NAME", "Stevens /Krik/"),
        ("SEX", "M"),
        ("DATE", "1 DEC 1969"),
        ("FAMS", "F1"),
        ("FAMC", "F3"),
    ],
    "I4": [
        ("NAME", "Kamala /Kirk/"),
        ("SEX", "M"),
        ("DATE", "29 DEC 1995"),
        ("FAMC", "F1"),
    ],
    "I5": [
        ("NAME", "Keerthi /Kirk/"),
        ("SEX", "M"),
        ("DATE", "29 DEC 1995"),
        ("FAMC", "F1"),
    ],
    "I6": [
        ("NAME", "Rex /Stevens/"),
        ("SEX", "M"),
        ("DATE", "29 DEC 1995"),
        ("FAMC", "F1"),
    ],
    "I7": [
        ("NAME", "Tom /Golecha/"),
        ("SEX", "M"),
        ("DATE", "29 DEC 1995"),
        ("FAMC", "F1"),
    ],
    "I8": [
        ("NAME", "Jared /Golecha/"),
        ("SEX", "M"),
        ("DATE", "29 DEC 1993"),
        ("FAMC", "F1"),
    ],
    "I9": [
        ("NAME", "Putli /Bafna/"),
        ("SEX", "F"),
        ("DATE", "13 FEB 1952"),
        ("DEAT", "13 FEB 1985"),
        ("FAMS", "F3"),
    ],
    "I10": [
        ("NAME", "Jasraj /Kirk/"),
        ("SEX", "M"),
        ("DATE", "13 FEB 1950"),
        ("DEAT", "13 FEB 1975"),
        ("FAMS", "F3"),
        ("FAMC", "F8"),
    ],
    "I11": [
        ("NAME", "Felix /Stevens/"),
        ("SEX", "M"),
        ("DATE", "29 DEC 1996"),
        ("FAMC", "F1"),
    ],
    "I12": [
        ("NAME", "Manoj /Kirk/"),
        ("SEX", "M"),
        ("DATE", "12 FEB 1930"),
        ("DEAT", "12 FEB 1980"),
        ("FAMS", "F5"),
    ],
    "I13": [
        ("NAME", "Teena /Alma/"),
        ("SEX", "F"),
        ("DATE", "1 MAR 1930"),
        ("DEAT", "12 FEB 1985"),
        ("FAMS", "F5"),
    ],
    "I14": [
        ("NAME", "Anjali /Ambani/"),
        ("SEX", "F"),
        ("DATE", "12 JUL 1925"),
        ("DEAT", "2 AUG 1999"),
        ("FAMS", "F8"),
    ],
    "I15": [
        ("NAME", "James /Kirk/"),
        ("SEX", "M"),
        ("DATE", "12 SEP 1930"),
        ("DEAT", "12 SEP 2000"),
        ("FAMS", "F8"),
    ],
    "I16": [
        ("NAME", "Jen /Folger/"),
        ("SEX", "F"),
        ("DATE", "12 MAR 1979"),
        ("FAMS", "F7"),
    ],
    "I17": [
        ("NAME", "Kim /Smith/"),
        ("SEX", "F"),
        ("DATE", "18 OCT 1985"),
        ("FAMS", "F6"),
    ],
}

families5 = {
    'F1': [('HUSB', 'I3'), ('WIFE', 'I2'), ('CHIL', 'I1'), ('CHIL', 'I4'), ('CHIL', 'I5'), ('CHIL', 'I6'), ('CHIL', 'I7'), ('CHIL', 'I8'), ('CHIL', 'I11'),('MARR', '12 JAN 1995')],
    'F2': [('HUSB', 'I9'), ('WIFE', 'I10'), ('MARR', '12 SEP 1968')]
}

class MyTestCase(unittest.TestCase):
    # US14: Too many siblings at the same time
    def test_US14_1(self):
        self.assertEqual(parse.too_many_siblings_at_same_time(individuals, families), True)
        print('US14 Test Case #1 - Passed: Too many siblings with same date of birth')

    def test_US14_2(self):
        self.assertEqual(parse.too_many_siblings_at_same_time(individuals2, families2), True)
        print('US14 Test Case #2 - Passed: Too many siblings with same date of birth')

    def test_US14_3(self):
        self.assertEqual(parse.too_many_siblings_at_same_time(individuals3, families3), False)
        print('US14 Test Case #3 - Passed: Sibling with different date of birth')

    def test_US14_4(self):
        self.assertEqual(parse.too_many_siblings_at_same_time(individuals4, families4), False)
        print('US14 Test Case #4 - Passed: Sibling with different date of birth')

    def test_US14_5(self):
        self.assertEqual(parse.too_many_siblings_at_same_time(individuals5, families5), False)
        print('US14 Test Case #5 - Passed: Sibling with different date of birth')
    #
    # US12: Mother should not be older than 60 years for a child
    def test_US12_1(self):
        self.assertEqual(parse.mother_is_not_too_old_for_child(individuals, families), True)
        print('US12 Test Case #1 - Passed: Mother is older than 60 than her child')

    def test_US12_2(self):
        self.assertEqual(parse.mother_is_not_too_old_for_child(individuals2, families2), True)
        print('US12 Test Case #2 - Passed: Mother is older than 60 than her child')

    def test_US12_3(self):
        self.assertEqual(parse.mother_is_not_too_old_for_child(individuals3, families3), False)
        print('US12 Test Case #3 - Passed: Mother is older than 60 than her child')

    def test_US12_4(self):
        self.assertEqual(parse.mother_is_not_too_old_for_child(individuals3, families3), False)
        print('US12 Test Case #4 - Passed: Mother is older than 60 than her child')

    def test_US12_5(self):
        self.assertEqual(parse.mother_is_not_too_old_for_child(individuals3, families3), False)
        print('US12 Test Case #5 - Passed: Mother is older than 60 than her child')

if __name__ == '__main__':
    unittest.main()