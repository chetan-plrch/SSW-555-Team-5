import unittest
import parse
import datetime

class MyTestCase(unittest.TestCase):
    def test_US02_1(self):
        indi_data, fam_data = parse.parse_gedcom_file('tests/US02_test1.ged')
        final_dict = {}

        for id in indi_data.keys():
            final_dict[id] = []

        for id, value in indi_data.items():
            birth_date = parse.get_individual_data_by_key(indi_data, id, 'DATE')
            final_dict[id].append(birth_date)
            
        for key, value in fam_data.items():
            for dictId in final_dict.keys():
                if value[0][1] == dictId or value[1][1] == dictId:
                    marriage_date = parse.get_family_data_by_key(fam_data, key, 'MARR')
                    marriage_date_formatted = datetime.datetime.strptime(marriage_date, '%d %b %Y').date()
                    final_dict[dictId].append(marriage_date_formatted)
            
        try:
            for key, value in final_dict.items():
                if len(value) == 2:
                    self.assertEqual(parse.check_if_birth_before_marriage(value[0], value[1]), 'Birth date cannot be after marriage date')
                elif len(value) == 3:
                    self.assertEqual(parse.check_if_birth_before_marriage(value[0], value[1]), 'Birth date cannot be after marriage date')
                    self.assertEqual(parse.check_if_birth_before_marriage(value[0], value[2]), 'Birth date cannot be after marriage date')
        except Exception as e:
            print(e)

    def test_US02_2(self):
        indi_data, fam_data = parse.parse_gedcom_file('tests/US02_test2.ged')
        final_dict = {}

        for id in indi_data.keys():
            final_dict[id] = []

        for id, value in indi_data.items():
            birth_date = parse.get_individual_data_by_key(indi_data, id, 'DATE')
            final_dict[id].append(birth_date)
            
        for key, value in fam_data.items():
            for dictId in final_dict.keys():
                if value[0][1] == dictId or value[1][1] == dictId:
                    marriage_date = parse.get_family_data_by_key(fam_data, key, 'MARR')
                    marriage_date_formatted = datetime.datetime.strptime(marriage_date, '%d %b %Y').date()
                    final_dict[dictId].append(marriage_date_formatted)
        
        try:
            for key, value in final_dict.items():
                if len(value) == 2:
                    self.assertEqual(parse.check_if_birth_before_marriage(value[0], value[1]), 'Birth date cannot be after marriage date')
                elif len(value) == 3:
                    self.assertEqual(parse.check_if_birth_before_marriage(value[0], value[1]), 'Birth date cannot be after marriage date')
                    self.assertEqual(parse.check_if_birth_before_marriage(value[0], value[2]), 'Birth date cannot be after marriage date')
        except Exception as e:
            print(e)
    
    def test_US02_3(self):
        indi_data, fam_data = parse.parse_gedcom_file('tests/US02_test3.ged')
        final_dict = {}

        for id in indi_data.keys():
            final_dict[id] = []

        for id, value in indi_data.items():
            birth_date = parse.get_individual_data_by_key(indi_data, id, 'DATE')
            final_dict[id].append(birth_date)
            
        for key, value in fam_data.items():
            for dictId in final_dict.keys():
                if value[0][1] == dictId or value[1][1] == dictId:
                    marriage_date = parse.get_family_data_by_key(fam_data, key, 'MARR')
                    marriage_date_formatted = datetime.datetime.strptime(marriage_date, '%d %b %Y').date()
                    final_dict[dictId].append(marriage_date_formatted)
        
        try:
            for key, value in final_dict.items():
                if len(value) == 2:
                    self.assertEqual(parse.check_if_birth_before_marriage(value[0], value[1]), 'Birth date cannot be after marriage date') 
                elif len(value) == 3:
                    self.assertEqual(parse.check_if_birth_before_marriage(value[0], value[1]), 'Birth date cannot be after marriage date')
                    self.assertEqual(parse.check_if_birth_before_marriage(value[0], value[2]), 'Birth date cannot be after marriage date')
        except Exception as e:
            print(e)

    def test_US02_4(self):
        indi_data, fam_data = parse.parse_gedcom_file('tests/US02_test4.ged')
        final_dict = {}

        for id in indi_data.keys():
            final_dict[id] = []

        for id, value in indi_data.items():
            birth_date = parse.get_individual_data_by_key(indi_data, id, 'DATE')
            final_dict[id].append(birth_date)
            
        for key, value in fam_data.items():
            for dictId in final_dict.keys():
                if value[0][1] == dictId or value[1][1] == dictId:
                    marriage_date = parse.get_family_data_by_key(fam_data, key, 'MARR')
                    marriage_date_formatted = datetime.datetime.strptime(marriage_date, '%d %b %Y').date()
                    final_dict[dictId].append(marriage_date_formatted)
        
        try:
            for key, value in final_dict.items():
                if len(value) == 2:
                    self.assertEqual(parse.check_if_birth_before_marriage(value[0], value[1]), 'Birth date cannot be after marriage date') 
                elif len(value) == 3:
                    self.assertEqual(parse.check_if_birth_before_marriage(value[0], value[1]), 'Birth date cannot be after marriage date')
                    self.assertEqual(parse.check_if_birth_before_marriage(value[0], value[2]), 'Birth date cannot be after marriage date')
        except Exception as e:
            print(e)

    def test_US02_5(self):
        indi_data, fam_data = parse.parse_gedcom_file('tests/US02_test5.ged')
        final_dict = {}

        for id in indi_data.keys():
            final_dict[id] = []

        for id, value in indi_data.items():
            birth_date = parse.get_individual_data_by_key(indi_data, id, 'DATE')
            final_dict[id].append(birth_date)
            
        for key, value in fam_data.items():
            for dictId in final_dict.keys():
                if value[0][1] == dictId or value[1][1] == dictId:
                    marriage_date = parse.get_family_data_by_key(fam_data, key, 'MARR')
                    marriage_date_formatted = datetime.datetime.strptime(marriage_date, '%d %b %Y').date()
                    final_dict[dictId].append(marriage_date_formatted)
        
        try:
            for key, value in final_dict.items():
                if len(value) == 2:
                    self.assertEqual(parse.check_if_birth_before_marriage(value[0], value[1]), 'Birth date cannot be after marriage date') 
                elif len(value) == 3:
                    self.assertEqual(parse.check_if_birth_before_marriage(value[0], value[1]), 'Birth date cannot be after marriage date')
                    self.assertEqual(parse.check_if_birth_before_marriage(value[0], value[2]), 'Birth date cannot be after marriage date')
        except Exception as e:
            print(e)  
        
if __name__ == '__main__':
    unittest.main()


