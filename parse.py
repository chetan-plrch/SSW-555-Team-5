import sys

def is_tag_valid(tag):
    return tag in ['INDI', 'NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS', 'FAM', 'MARR', 'HUSB', 'WIFE', 'CHIL', 'DIV', 'DATE', 'HEAD', 'TRLR', 'NOTE']

def is_exception_tag(level, arguments):
    return level == 0 and (arguments in ['INDI', 'FAM'])

def is_not_supported_tags(level, tag):
    return (level == 1 and tag == 'DATE') or (level == 2 and tag == 'NAME')

def understand_line(line):
    line = line.rstrip('\n')
    output = []

    parts = line.split(' ')
    level = int(parts[0])
    tag = parts[1]
    arguments = ' '.join(parts[2:])

    output.append('--> ' + line)

    valid = 'N'
    if is_exception_tag(level, arguments):
        if is_tag_valid(arguments): valid = 'Y'
    else:
        if is_tag_valid(tag): valid = 'Y'

    if is_not_supported_tags(level, tag):
        pass
    elif is_exception_tag(level, arguments):
        output.append('<-- {}|{}|{}|{}'.format(level, arguments, valid, tag))
    else:
        output.append('<-- {}|{}|{}|{}'.format(level, tag, valid, arguments))

    write_to_output(output)

def write_to_output(lines):
    f = open("output.txt", "a")
    for line in lines:
        f.write(f"{line}\n")
    f.close()

def read_file():
    with open(sys.argv[1], 'r') as file:
        for line in file:
            understand_line(line)

# Instructions on how to run the file:
# 1. Please navigate the project folder
# 2. Clean the output.txt file
# 3. Please use the command "python3 parse.py sample.ged" to process the file "sample.ged" and generate output in "output.txt" file
read_file()