import json
import string


def part1(input):
    passports = createPassportList(input)
    valid = 0
    invalid = 0
    for x in passports:
        count = len(x.keys())
        if count == 8:
            valid += 1
        elif count == 7:
            if x.get('cid', None) is None:
                valid += 1
            else:
                invalid += 1
        else:
            invalid += 1
    print(f"A total of {len(passports)} passports were checked.\n{valid} were valid.\n{invalid} were invalid.")


def part2(input):
    passports = createPassportList(input)
    valid = 0
    invalid = 0
    for x in passports:
        count = len(x.keys())
        if count == 8:
            byr = checkBYR(x)
            iyr = checkIYR(x)
            eyr = checkEYR(x)
            hgt = checkHGT(x)
            hcl = checkHCL(x)
            ecl = checkECL(x)
            pid = checkPID(x)
            if byr and iyr and eyr and hgt and hcl and ecl and pid:
                valid += 1
            else:
                invalid += 1

        elif count == 7:
            if x.get('cid', None) is None:
                byr = checkBYR(x)
                iyr = checkIYR(x)
                eyr = checkEYR(x)
                hgt = checkHGT(x)
                hcl = checkHCL(x)
                ecl = checkECL(x)
                pid = checkPID(x)
                if byr and iyr and eyr and hgt and hcl and ecl and pid:
                    valid += 1
                else:
                    invalid += 1
            else:
                invalid += 1
        else:
            invalid += 1
    print(f"A total of {len(passports)} passports were checked.\n{valid} were valid.\n{invalid} were invalid.")


def checkPID(x):
    pid = x.get('pid')
    if len(pid) == 9:
        pid = True
    else:
        pid = False
    return pid


def checkECL(x):
    ecl = x.get('ecl')
    if ecl == "amb" or ecl == "blu" or ecl == "brn" or ecl == "gry" or ecl == "grn" or ecl == "hzl" or ecl == "oth":
        ecl = True
    else:
        ecl = False
    return ecl


def checkHCL(x):
    hcl = x.get('hcl')
    if len(str(hcl)) == 7 and "#" in hcl:
        hcl = all(c in string.hexdigits for c in hcl.replace("#", ""))
    else:
        hcl = False
    return hcl


def checkHGT(x):
    hgt = x.get('hgt')
    if "cm" in hgt or "in" in hgt:
        if "cm" in hgt:
            hgt = int(hgt.replace("cm", ""))
            if 150 <= hgt <= 193:
                hgt = True
            else:
                hgt = False
        elif "in" in hgt:
            hgt = int(hgt.replace("in", ""))
            if 59 <= hgt <= 76:
                hgt = True
            else:
                hgt = False
    else:
        hgt = False
    return hgt


def checkEYR(x):
    eyr = x.get('eyr')
    if len(str(eyr)) == 4 and 2020 <= eyr <= 2030:
        eyr = True
    else:
        eyr = False
    return eyr


def checkIYR(x):
    iyr = x.get('iyr')
    if len(str(iyr)) == 4 and 2010 <= iyr <= 2020:
        iyr = True
    else:
        iyr = False
    return iyr


def checkBYR(x):
    byr = x.get('byr')
    if len(str(byr)) == 4 and 1920 <= byr <= 2002:
        byr = True
    else:
        byr = False
    return byr


def createPassportList(input):
    passports = [""] * len(input)
    current = 0
    for line in input:
        if line == "":
            current += 1
        else:
            if passports[current] == "":
                passports[current] += f"{line}"
            else:
                passports[current] += f" {line}"
    filtered = list(filter(None, passports))
    passports = []
    for x in filtered:
        string = "{"
        splitted = x.split(' ')
        for y in splitted:
            keyvalue = y.split(":")
            if keyvalue[0] == "byr":
                string += f'"{keyvalue[0]}":{keyvalue[1]},'
            if keyvalue[0] == "iyr":
                string += f'"{keyvalue[0]}":{keyvalue[1]},'
            if keyvalue[0] == "eyr":
                string += f'"{keyvalue[0]}":{keyvalue[1]},'
            if keyvalue[0] == "hgt":
                string += f'"{keyvalue[0]}":"{keyvalue[1]}",'
            if keyvalue[0] == "hcl":
                string += f'"{keyvalue[0]}":"{keyvalue[1]}",'
            if keyvalue[0] == "ecl":
                string += f'"{keyvalue[0]}":"{keyvalue[1]}",'
            if keyvalue[0] == "pid":
                string += f'"{keyvalue[0]}":"{keyvalue[1]}",'
            if keyvalue[0] == "cid":
                string += f'"{keyvalue[0]}":{keyvalue[1]},'
        string = string[:-1]
        string += "}"
        passports.append(json.loads(string))
    return passports


if __name__ == '__main__':
    input = []
    exampleInput = ["ecl:gry pid:860033327 eyr:2020 hcl:#fffffd",
                    "byr:1937 iyr:2017 cid:147 hgt:183cm",
                    "",
                    "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884",
                    "hcl:#cfa07d byr:1929",
                    "",
                    "hcl:#ae17e1 iyr:2013",
                    "eyr:2024",
                    "ecl:brn pid:760753108 byr:1931",
                    "hgt:179cm",
                    "",
                    "hcl:#cfa07d eyr:2025 pid:166559648",
                    "iyr:2011 ecl:brn hgt:59in"]

    exampleInput2 = ["eyr:1972 cid:100",
                     "hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926",
                     "",
                     "iyr:2019",
                     "hcl:#602927 eyr:1967 hgt:170cm",
                     "ecl:grn pid:012533040 byr:1946",
                     "",
                     "hcl:dab227 iyr:2012",
                     "ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277",
                     "",
                     "hgt:59cm ecl:zzz",
                     "eyr:2038 hcl:74454a iyr:2023",
                     "pid:3556412378 byr:2007",
                     "",
                     "pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980",
                     "hcl:#623a2f",
                     "",
                     "eyr:2029 ecl:blu cid:129 byr:1989",
                     "iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm",
                     "",
                     "hcl:#888785",
                     "hgt:164cm byr:2001 iyr:2015 cid:88",
                     "pid:545766238 ecl:hzl",
                     "eyr:2022",
                     "",
                     "iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"]

    f = open('../inputs/day4.txt', 'r')
    for x in f:
        input.append(x.rstrip())

    print("EXAMPLE PART 1")
    part1(exampleInput)
    print("------------------------------------------------------")
    print("PART 1")
    part1(input)
    print("------------------------------------------------------")
    print("EXAMPLE PART 2")
    part2(exampleInput2)
    print("------------------------------------------------------")
    print("PART 2")
    part2(input)
    print("------------------------------------------------------")
