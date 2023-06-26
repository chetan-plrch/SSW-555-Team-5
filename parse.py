import datetime
from dateutil.relativedelta import relativedelta
from prettytable import PrettyTable

def get_all_individual_data_by_key(individuals, id, key):
    meta_data = []
    for meta in individuals[id]:
        if meta[0] == key: meta_data.append(meta[1])
    return meta_data

def get_all_data_of_a_person(families, person_id, key):
    family_ids, child_ids = [], []

    for id in families:
        for meta in families[id]:
            if ((meta[0] == 'WIFE') or (meta[0] == 'HUSB')) and (meta[1] == person_id): family_ids.append(id)

    for id in family_ids:
        for meta in families[id]:
            if meta[0] == key: child_ids.append(meta[1])

    return child_ids

def get_from_all_records_all_family_data(families, key):
    meta_data = []
    for id in families:
        for meta in families[id]:
            if meta[0] == key: meta_data.append(meta[1])
    return meta_data

def get_all_husband_and_wives(families):
    husband_and_wives = []
    for family_id, family_values in families.items():
        hub = get_family_data_by_key(families, family_id, 'HUSB')
        wife = get_family_data_by_key(families, family_id, 'WIFE')

        if hub and wife:
            husband_and_wives.append((hub, wife))
        else:
            print('ERROR: Husband or Wife ID not present for a pair')
    return husband_and_wives

def get_individual_data_by_key(individuals, id, key):
    meta_data = None
    for meta in individuals[id]:
        if meta[0] == key: meta_data = meta[1]
    return meta_data

def get_family_data_by_key(families, id, key):
    meta_data = None
    for meta in families[id]:
        if meta[0] == key: meta_data = meta[1]
    return meta_data

def get_marriage_date_by_key(families, id, key):
    meta_data = []

    for meta in families[id]:
        if meta[0] == "MARR":
            meta_data.append(meta[1]) 
    return meta_data

def get_div_date_by_key(families, id, key):
    meta_data = []
    
    for meta in families[id]:
        if meta[0] == "DIV":
            meta_data.append(meta[1]) 
    return meta_data

def is_not_supported_tags(level, tag):
    return (level == 1 and tag == 'DATE') or (level == 2 and tag == 'NAME')

def clean_gedcom_tags(file_path, supported_tags):
    clean_tags = []

    with open(file_path) as file:
        raw_gedcom = file.read().splitlines()

    for tag in raw_gedcom:
        tag_parts = tag.strip().split(" ", 2)

        if len(tag_parts) < 2:
            continue

        if len(tag_parts) > 2 and tag_parts[1] in ['INDI', 'FAM']:
            continue

        if len(tag_parts) > 2 and tag_parts[2] in ['INDI', 'FAM']:
            tag_parts[1], tag_parts[2] = tag_parts[2], tag_parts[1]

        if len(tag_parts) > 2:
            if tag_parts[1] in supported_tags and supported_tags[tag_parts[1]] == tag_parts[0]:
                clean_tags.append((tag_parts[0], tag_parts[1], tag_parts[2]))
            elif tag_parts[0:2] == ["In", ""]:
                clean_tags.append(tag_parts)

        elif len(tag_parts) == 2:
            if tag_parts[1] in supported_tags and supported_tags[tag_parts[1]] == tag_parts[0]:
                clean_tags.append((tag_parts[0], tag_parts[1]))

    clean_tags = clean_tags[1:-1]
    clean_tags = list(filter(('1', 'BIRT').__ne__, clean_tags))

    return clean_tags

def collect_individual_metadata(individuals, clean_tags):
    x = PrettyTable()
    x.field_names = ['ID', 'Name', 'Gender', 'Birthday', 'Age', 'Alive', 'Death', 'Child', 'Spouse']

    for i, tag in enumerate(clean_tags):
        if tag[1] == 'INDI' and tag[0] == '0':
            indi_key = tag[2][1:-1]
            values = []
            j = i + 1
            skip_tag = 0

            while clean_tags[j][1] != 'INDI':
                if clean_tags[j][1] == 'FAM' and clean_tags[j][0] == '0':
                    skip_tag = 1
                    break
                elif clean_tags[j][1] == 'DEAT' and clean_tags[j][2] == 'Y':
                    values.append(('DEAT', clean_tags[j + 1][2]))
                    j += 1
                elif clean_tags[j][1] in ('FAMS', 'FAMC'):
                    values.append((clean_tags[j][1], clean_tags[j][2][1:-1]))
                else:
                    values.append((clean_tags[j][1], clean_tags[j][2]))
                j += 1

            individuals[indi_key] = values

            if skip_tag == 1:
                break

    for key, value in individuals.items():
        name, gender, birth_date, death_date = "", "", "", "-"
        husband_id, wife_id = "", ""
        alive = True
        for i in range(len(value)):
            family_child, family_spouse = "-", "-"
            tag = value[i][0]
            if tag == 'NAME':
                name = value[i][1]
            if tag == 'SEX':
                gender = value[i][1]
            if tag == 'DATE':
                birth_date = value[i][1]
                birth_date = datetime.datetime.strptime(birth_date, '%d %b %Y').date()
            if tag == 'DEAT':
                death_date = value[i][1]
                death_date = datetime.datetime.strptime(death_date, '%d %b %Y').date()
            if tag == 'FAMC':
                family_child = value[i][1]
            if tag == 'FAMS':
                family_spouse = value[i][1]

        if any('DEAT' in i for i in value):
            alive = False
            age = relativedelta(death_date, birth_date).years
        else:
            age = relativedelta(datetime.datetime.now(), birth_date).years
        
        check_if_birth_before_death(birth_date, death_date)

        x.add_row([key, name, gender, birth_date, age, alive, death_date, family_child, family_spouse])

    print("Individuals")
    print(x)
    x.clear_rows()


def collect_family_metadata(individuals, families, clean_tags):
    y = PrettyTable()

    for i in range(len(clean_tags)):
        values = []
        j = i + 1
        if clean_tags[i][1] == 'FAM' and clean_tags[i][0] == '0':
            family_key = clean_tags[i][2][1:-1]

            while j < len(clean_tags):
                tag = clean_tags[j][1]
                data = clean_tags[j][2][1:-1] if len(clean_tags[j]) > 2 else ""

                if tag not in ['MARR', 'DIV', 'DATE', 'FAM']:
                    values.append((tag, data))
                elif tag == 'MARR' and len(clean_tags[j + 1]) > 2:
                    values.append(('MARR', clean_tags[j + 1][2]))
                elif tag == 'DIV' and len(clean_tags[j + 1]) > 2:
                    values.append(('DIV', clean_tags[j + 1][2]))
                elif tag == 'FAM' and clean_tags[j][0] == '0':
                    break

                j += 1

            families[family_key] = values

    y.field_names = ['ID', 'Married', 'Divorced', 'Husband ID', 'Husband Name', 'Wife ID', 'Wife Name', 'Children']

    for key, value in families.items():
        children = []
        married_date, divorce_date = "", "-"
        husband_id, wife_id = "", ""
        husband_name, wife_name = "", ""

        for tag, data in value:
            if tag == 'HUSB':
                husband_id = data
                husband_name = individuals[husband_id][0][1]
            elif tag == 'WIFE':
                wife_id = data
                wife_name = individuals[wife_id][0][1]
            elif tag == 'CHIL':
                children.append(data)
            elif tag == 'MARR':
                married_date = datetime.datetime.strptime(data, '%d %b %Y').date()
            elif tag == 'DIV':
                divorce_date = datetime.datetime.strptime(data, '%d %b %Y').date()

        check_if_married_before_divorce(married_date, divorce_date)
        check_if_married_before_death(married_date, get_individual_data_by_key(individuals, husband_id, 'DEAT'))
        check_if_married_before_death(married_date, get_individual_data_by_key(individuals, wife_id, 'DEAT'))

        check_if_birth_before_marriage(get_individual_data_by_key(individuals, husband_id, 'DATE'), married_date)
        check_if_birth_before_marriage(get_individual_data_by_key(individuals, wife_id, 'DATE'), married_date)

        check_divorce_before_death(families,individuals) #US06
        # check_birth_after_parent_marriage(families,individuals) #US08
        noBigamy(families, individuals)

        y.add_row([key, married_date, divorce_date, husband_id, husband_name, wife_id, wife_name, children])

    print("Families")
    print(y)
    y.clear_rows()

# Story Id - US02:
def check_if_birth_before_marriage(birth_date, marriage_date):
    #Birth before Marriage
    if (birth_date == '-') and (marriage_date == '-'): 
        return None
    if (birth_date != '-') and (marriage_date == '-'): 
        return None
    
    if (birth_date == '-') and (marriage_date != '-'):
        err = "Birth Date needs to be present if marriage date is present"
        print(err)
        return err

    if birth_date and marriage_date:
        birth_date_formatted = datetime.datetime.strptime(birth_date, '%d %b %Y').date()
        if birth_date_formatted > marriage_date:
            err = "Birth date cannot be after marriage date"
            print(err)
            return err
        
        if birth_date_formatted == marriage_date:
            err = "Birth date cannot be same as marriage date"
            print(err)
            return err

# # Story Id - US03:
def check_if_birth_before_death(birth_date, death_date):
    #Birth before Death
    if (birth_date == '-') and (death_date == '-'): return None
    if (birth_date != '-') and (death_date == '-'): return None

    if (birth_date == '-') and (death_date != '-'):
        err = "Birth Date needs to be present if death date is present"
        print(err)
        return err

    if birth_date and death_date:
        if birth_date > death_date:
            err = "Birth date cannot be after death date"
            print(err)
            return err
        
        if birth_date == death_date:
            err = "Birth date cannot be same as death date"
            print(err)
            return err

# Story Id - US04:
def check_if_married_before_divorce(marriage_date, divorce_date):
    # Marriage before Divorce
    if (marriage_date == '-') and (divorce_date == '-'): return None
    if (marriage_date != '-') and (divorce_date == '-'): return None

    if (marriage_date == '-') and (divorce_date != '-'):
        err = "ERROR: US04: Marriage date needs to be present if divorce date is present"
        print(err)
        return err

    if marriage_date and divorce_date:
        if marriage_date > divorce_date:
            err = "ERROR: US04: Marriage date cannot be after divorce date"
            print(err)
            return err

        if marriage_date == divorce_date:
            err = "ERROR: US04: Marriage date cannot be equal to divorce date"
            print(err)
            return err

# Story Id - US05:
def check_if_married_before_death(marriage_date, death_date):
    # Marriage before Death
    if (marriage_date == '-') or (death_date == '-'): return None
    if (marriage_date != '-') and (death_date == '-'): return None

    if marriage_date and death_date:
        death_date_formatted = datetime.datetime.strptime(death_date, '%d %b %Y').date()
        if marriage_date > death_date_formatted:
            err = "ERROR: US05: Marriage date cannot be after death date"
            print(err)
            return err

        if marriage_date == death_date_formatted:
            err = "ERROR: US05: Marriage date cannot be equal to death date"
            print(err)
            return err


def get_individual_name(indi_id, individuals):
    return individuals[indi_id]["NAME"]

def check_divorce_before_death(families, individuals):
    count = 0
    for id in families:
        if "DIV" in families[id]:
            div_date = datetime.datetime.strptime(families[id]["DIV"], "%d %b %Y")
            print(div_date)
            husb_ID = families[id]["HUSB"]
            wife_ID = families[id]["WIFE"]
            if "DEAT" in individuals[husb_ID] and "DEAT" in individuals[wife_ID]:
                husbDeath = datetime.datetime.strptime(
                    individuals[husb_ID]["DEATH_DATE"], "%d %b %Y"
                )
                wifeDeath = datetime.datetime.strptime(
                    individuals[wife_ID]["DEATH_DATE"], "%d %b %Y"
                )
                if div_date > husbDeath and div_date > wifeDeath:
                    count += 1
                    print(
                        "ERROR: FAMILY: US06: Divorce between "
                        + "'"
                        + get_individual_name(husb_ID, individuals).replace("/", "")
                        + "' and '"
                        + get_individual_name(wife_ID, individuals).replace("/", "")
                        + "' cannot occur after both partners' deaths."
                    )
            elif "DEAT" in individuals[husb_ID]:
                husbDeath = datetime.datetime.strptime(
                    individuals[husb_ID]["DEATH_DATE"], "%d %b %Y"
                )
                if div_date > husbDeath:
                    count += 1
                    print(
                        "ERROR: FAMILY: US06: Divorce between "
                        + "'"
                        + get_individual_name(husb_ID, individuals).replace("/", "")
                        + "' and '"
                        + get_individual_name(wife_ID, individuals).replace("/", "")
                        + "' cannot occur after "
                        + get_individual_name(husb_ID, individuals).replace("/", "")
                        + "'s death."
                    )
            elif "DEAT" in individuals[wife_ID]:
                wifeDeath = datetime.datetime.strptime(
                    individuals[wife_ID]["DEATH_DATE"], "%d %b %Y")
                if div_date > wifeDeath:
                    count += 1
                    print(
                        "ERROR: FAMILY: US06: Divorce between "
                    + "'"
                    + get_individual_name(husb_ID, individuals).replace("/", "")
                    + "' and '"
                    + get_individual_name(wife_ID, individuals).replace("/", "")
                    + "' cannot occur after "
                    + get_individual_name(wife_ID, individuals).replace("/", "")
                    + "'s death."
                )
    if count == 0:
        return True
    else:
        return False

def check_birth_after_parent_marriage(families, individuals):
    is_valid = True
    for id in families:
        #if "MARR" in families[id]:
        if get_family_data_by_key(families,id,"MARR"):
            marriageDate = datetime.datetime.strptime(get_family_data_by_key(families,id,"MARR"), "%d %b %Y").date()
            for childID in get_family_data_by_key(families,id,"CHIL"):
                childBirthDate = datetime.datetime.strptime(get_family_data_by_key(families,id,"MARR"), "%d %b %Y").date()
                if childBirthDate < marriageDate:
                    print("ANOMALY: FAMILY: US08: Child ("
                            + get_individual_name(childID, individuals).replace("/", "")
                            + ") born before marriage of parents in family: "
                            + id
                            + ".")
                    is_valid = False
        else:
            print(families[id])
            print("ERROR: FILE: US08: Marriage date not set or properly formatted of family: "
                + id
                + ".")
            is_valid = False
    return is_valid
    
#Story US09:
def birth_after_parent_death(parentA, parentB, child):
    #Birth after parents death 
    if(parentA == '-' or parentB == '-' or child == '-'):
        return None
    childBirth= datetime.datetime(2, 2, 2).date()
    parentADeath= datetime.datetime(9999, 1, 1).date()
    parentBDeath= datetime.datetime(9999, 1, 1).date()
    is_dead = False
    childBirth = datetime.datetime.strptime(child['DATE'], "%d %b %Y").date()
    for id in parentA:  
        if id == "DEAT":
            is_dead = True
            parentADeath = temp
        if id == "DATE":
            temp = datetime.datetime.strptime(parentA[id], "%d %b %Y").date()
    for id in parentB:  
        if id == "DEAT":
            is_dead = True
            parentBDeath = temp
        if id == "DATE":
            temp = datetime.datetime.strptime(parentB[id], "%d %b %Y").date()
    if (childBirth > parentADeath or childBirth > parentBDeath):
        print("ERROR: US09: Child born after death of parent")
        return True
    else:
        return False

#Story US10:
def married_before_fourteen(marriage_year, birth_year):
    # Marriage before age of 14
    if (marriage_year == '-' or birth_year == '-'):
        return None
    ageAtMarriage = marriage_year-birth_year
    if marriage_year:
        if ageAtMarriage <= 14:
            err = "ERROR: US10: Marriage date is before 14"
            print(err)
            return True
    return False

#Story US11
def noBigamy(families, individuals):
    err = None
    husb_ID = ""
    wife_ID = ""
    myDict = {}
    divDict = {}
    for id in families:
        for item in families[id]:
            if item[0] == "HUSB":
                husb_ID = item[1]
                myDict.setdefault(husb_ID)
                divDict.setdefault(husb_ID)
            elif item[0] == "WIFE":
                wife_ID = item[1]
                myDict.setdefault(wife_ID)
                divDict.setdefault(wife_ID)

    for key, values in myDict.items():
        for id in families:
            fam_husbId = get_family_data_by_key(families, id, 'HUSB')
            fam_wifeId = get_family_data_by_key(families, id, 'WIFE')
            
            if key == fam_husbId or key == fam_wifeId:
                marr_date = get_marriage_date_by_key(families, id, key)

                if key in myDict:
                    if isinstance(myDict[key], list):
                        myDict[key].append(marr_date)
                    else:
                        myDict[key] = [myDict[key], marr_date]
                else:
                    myDict[key] = [marr_date]
    
    for key, values in divDict.items():
        for id in families:
            fam_husbId = get_family_data_by_key(families, id, 'HUSB')
            fam_wifeId = get_family_data_by_key(families, id, 'WIFE')
            if key == fam_husbId or key == fam_wifeId:
                div_date = get_div_date_by_key(families, id, key)
                
                if key in divDict:
                    if isinstance(divDict[key], list):
                        divDict[key].append(div_date)
                    else:
                        divDict[key] = [divDict[key], div_date]
                else:
                    divDict[key] = [div_date]
                 
    updated_myDict = {key: [val for val in value if val is not None] for key, value in myDict.items()}
    updated_divDict = {key: [val for val in value if val is not None] for key, value in divDict.items()}

    for key in myDict:
        if key in divDict:
            my_dates = [date for sublist in myDict[key] if sublist for date in sublist] 
            div_dates = [date for sublist in divDict[key] if sublist for date in sublist]
            new_my_dates = [datetime.datetime.strptime(date, '%d %b %Y').date() for date in my_dates]
            new_div_dates = [datetime.datetime.strptime(date, '%d %b %Y').date() for date in div_dates]
            
            if len(new_my_dates) > 2 and len(new_div_dates) > 1:
                for i in range(len(new_my_dates) - 1):
                    if new_div_dates[i] > new_my_dates[i] and new_div_dates[i] < new_my_dates[i+1]:
                        err = "No Bigamy"

                    else:
                        err = "Bigamy caught"
                    return(err)
            
            elif (len(new_my_dates) == 2 and (len(new_div_dates) == 1 or len(new_div_dates) == 0)):
                if len(new_div_dates) == 0:
                    err = "Bigamy caught"
            
                else:
                    lesser_date = min(new_my_dates)
                    greater_date = max(new_my_dates)
                    div_date = new_div_dates[0]
            
                    if lesser_date < div_date < greater_date:
                        err = "No Bigamy"

                    else:
                        err = "Bigamy caught"
                return err
    
            else:
                err = "No Bigamy"
    return err


# Story Id: US18
def sibling_should_not_marry(families):
    invalid = False
    husb_wives = get_all_husband_and_wives(families)
    for family_id, family_data in families.items():
        sibling_ids = get_all_individual_data_by_key(families, family_id, 'CHIL')
        for hub_id, wife_id in husb_wives:
            if (hub_id in sibling_ids) and (wife_id in sibling_ids):
                invalid = True
                print(f"ERROR: US18: Siblings {hub_id} and {wife_id} should not marry.")
    return invalid

# Story Id: US14 (No more than five siblings should be born at the same time)
def too_many_siblings_at_same_time(individuals, families):
    invalid = False
    for ind_id in individuals:
        children_ids = get_all_data_of_a_person(families, ind_id, 'CHIL')
        same_date_count = {}
        for child_id in children_ids:
            birth_date = get_individual_data_by_key(individuals, child_id, 'DATE')
            if birth_date in same_date_count:
                same_date_count[birth_date] += 1
            else:
                same_date_count[birth_date] = 0

        for sibling_on_same_time_count in same_date_count.values():
            if sibling_on_same_time_count > 5:
                print(f"ERROR: US14: No more than five siblings should be born at the same time")
                invalid = True
    return invalid

# Story Id: US12 (Mother should be less than 60 years older than her children)
def mother_is_not_too_old_for_child(individuals, families):
    invalid = False
    for ind_id in individuals:
        gender = get_individual_data_by_key(individuals, ind_id, 'SEX')
        if gender == 'F':
            mother_birth_date = get_individual_data_by_key(individuals, ind_id, 'DATE')
            children_ids = get_all_data_of_a_person(families, ind_id, 'CHIL')
            for child_id in children_ids:
                child_birth_date = get_individual_data_by_key(individuals, child_id, 'DATE')
                delta_years = relativedelta(
                    datetime.datetime.strptime(child_birth_date, '%d %b %Y').date(),
                    datetime.datetime.strptime(mother_birth_date, '%d %b %Y').date()
                ).years
                if delta_years >= 60:
                    invalid = True
                    print(f"ERROR: US12: Mother should be less than 60 years older than her children")

    return invalid

# Story Id: US15
def fewer_than_15_siblings(families):
    invalid = False
    for family_id, family_data in families.items():
        siblings = get_all_individual_data_by_key(families, family_id, 'CHIL')
        if len(siblings) > 15:
            invalid = True
            print(f"ERROR: US15: Family has more than 15 siblings")
    return invalid

# Story Id: US17
def parents_should_not_marry_descendants(individuals, families):
    invalid = False
    for ind_id in individuals:
        children_ids = get_all_data_of_a_person(families, ind_id, 'CHIL')
        for child_id in children_ids:
            for family_id in families:
                husb_id = get_family_data_by_key(families, family_id, 'HUSB')
                wife_id = get_family_data_by_key(families, family_id, 'WIFE')

                if ((ind_id == husb_id) and (child_id == wife_id) or (ind_id == wife_id) and (child_id == husb_id)):
                    invalid = True
                    print(f"ERROR: US17: Parent is married to their descendant")
    return invalid

# Story Id: US25
def child_should_not_have_same_name_date(individuals, families):
    invalid = False
    for ind_id in individuals:
        children_ids = get_all_data_of_a_person(families, ind_id, 'CHIL')
        s = {}
        for child_id in children_ids:
            child_name = get_individual_data_by_key(individuals, child_id, 'NAME')
            child_birth_date = get_individual_data_by_key(individuals, child_id, 'DATE')
            if f'{child_name}_{child_birth_date}' in s:
                invalid = True
                print(f"ERROR: US25: Two child have same name and birth date")
            else:
                s[f'{child_name}_{child_birth_date}'] = True
    return invalid

def parse_gedcom_file(file_name):
    individuals = {}
    families = {}
    supported_tags = {
        'INDI': '0', 'NAME': '1', 'SEX': '1', 'BIRT': '1', 'DEAT': '1', 'FAMC': '1', 'FAMS': '1',
        'FAM': '0',
        'MARR': '1', 'HUSB': '1', 'WIFE': '1', 'CHIL': '1', 'DIV': '1', 'DATE': '2', 'HEAD': '0',
        'TRLR': '0', 'NOTE': '0'
    }
    clean_tags = clean_gedcom_tags(file_name, supported_tags)
    collect_individual_metadata(individuals, clean_tags)
    collect_family_metadata(individuals, families, clean_tags)
    sibling_should_not_marry(families)
    fewer_than_15_siblings(families)
    too_many_siblings_at_same_time(individuals, families)
    mother_is_not_too_old_for_child(individuals, families)
    parents_should_not_marry_descendants(individuals, families)
    child_should_not_have_same_name_date(individuals, families)
    return individuals, families

parse_gedcom_file('sample_new.ged')
