import datetime
from dateutil.relativedelta import relativedelta
from prettytable import PrettyTable

def get_individual_data_by_key(individuals, id, key):
    # Example Individual data: key(NAME, SEX, DATE, DEAT, FAMS, FAMC)
    # {
    #     'I2': [
    #         ('NAME', 'Elena /Golecha/'), ('SEX', 'F'), ('DATE', '1 JAN 1976'),
    #         ('DEAT', '1 JAN 2012'), ('FAMS', 'F1'), ('FAMC', 'F2')
    #     ],
    # }
    meta_data = None
    for meta in individuals[id]:
        if meta[0] == key: meta_data = meta[1]
    return meta_data

def get_family_data_by_key(families, id, key):
    #print(families)
    #return families[id][key]
    #if key not in families[id][0]:
    #    return False
    #return families[id][0][key]
    #meta_data = None
    #for meta in families[id]:
    #    if meta[0] == key: meta_data = meta[1]
    #return meta_data
    family_data_list = families[id]
    for tuple in family_data_list:
        if tuple[0] == key:
            return tuple[1]
    #if execution reaches here key was not found
    return False

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
        check_birth_after_parent_marriage(families,individuals) #US08

        check_age_under_onefifty(individuals) #US07
        check_gender_role(families, individuals) #US21
        large_age_difference(families, individuals) #US34
        recent_births(individuals) #US35

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
            err = "ERROR: US04: Marriage date cannot be after death date"
            print(err)
            return err

        if marriage_date == death_date_formatted:
            err = "ERROR: US04: Marriage date cannot be equal to death date"
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
            childID = get_family_data_by_key(families,id,"CHIL")
            if childID:
                childBirthDate = datetime.datetime.strptime(get_individual_data_by_key(individuals,childID,"DATE"), "%d %b %Y").date()
                if childBirthDate < marriageDate:
                    print("ANOMALY: FAMILY: US08: Child ("
                            + childID
                            + ") born before marriage of parents in family: "
                            + id
                            + ".")
                    is_valid = False
        else:
            print("ERROR: FILE: US08: Marriage date not set or properly formatted of family: "
                + id
                + ".")
            is_valid = False
    return is_valid

#US07
def check_age(birth_date):
    today = datetime.datetime.today()
    birth = datetime.datetime.strptime(birth_date, "%d %b %Y")
    age_from_today = today - birth
    age = age_from_today.days
    return age

def check_age_under_onefifty(individuals):
    is_valid = True
    birth_date = 0
    for id in individuals:
        individual = individuals[id]
        birthday = get_individual_data_by_key(individuals,id,"DATE")
        day_age = check_age(birthday)
        age = day_age/365.25
        if age >= 150:
            is_valid = False
            print("Age is over 150")
    return is_valid    

#US21
def check_gender_role(families, individuals):
    is_valid = True
    for id in families:
        husbID = get_family_data_by_key(families,id,"HUSB")
        if husbID:
            gender = get_individual_data_by_key(individuals,husbID,"SEX")
            if gender != "M":
                print("Gender does not match Marriage Role")
                is_valid = False
        wifeID = get_family_data_by_key(families,id,"WIFE")
        if wifeID:
            gender = get_individual_data_by_key(individuals,wifeID,"SEX")
            if gender != "F":
                print("Gender does not match Marriage Role")
                is_valid = False
        return is_valid

#US34
def large_age_difference(families, individuals):
    is_valid = True
    for id in families:
        husbID = get_family_data_by_key(families,id,"HUSB")
        if husbID:
            husb_bday = get_individual_data_by_key(individuals,husbID,"DATE")
            husb_age1 = check_age(husb_bday)
            husb_age = husb_age1/365.25
            print(husb_age)
        wifeID = get_family_data_by_key(families,id,"WIFE")
        if wifeID:
            wife_bday = get_individual_data_by_key(individuals,wifeID,"DATE")
            wife_age1 = check_age(wife_bday)
            wife_age = wife_age1/365.25
            print(wife_age)
        if husb_age > 2*wife_age:
            print("Husband ", husbID, "is more than 2 times older than Wife ", wifeID)
        elif wife_age >2*husb_age:
            print("Wife ", wifeID, "is more than 2 times older than Husband ", husbID)
        else:
            print("Husband, ",husbID,"& Wife, ",wifeID,"do not have a large age gap")
            is_valid = False
        
        return is_valid

#US35
def recent_births(individuals):
    is_valid = True
    for id in individuals:
        individual = individuals[id]
        birthday = get_individual_data_by_key(individuals,id,"DATE")
        day_age = check_age(birthday)
        if day_age > 30:
            is_valid = False
            print("Born more than 30 days ago")
    return is_valid
    print("Born Recently")



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
    # clean_tags = clean_gedcom_tags('sample.ged', supported_tags)
    collect_individual_metadata(individuals, clean_tags)
    collect_family_metadata(individuals, families, clean_tags)
    return individuals, families

if __name__ == "__main__":
    parse_gedcom_file('sample.ged')
