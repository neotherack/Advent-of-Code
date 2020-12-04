import json
import re

INPUT_FILE = "2020/Day4/inputdata"
RULES_FILE = "2020/Day4/rules_partII.json"
#KEY_PLAN = {"byr": "mandatory", "iyr":"mandatory", "eyr":"mandatory", "hgt":"mandatory", "hcl":"mandatory", "ecl":"mandatory", "pid":"mandatory", "cid":"optional"}


def load_data(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except:
        print("exception on file read")
        return ""

def preprocess_data(str_data):
    entities = str_data.split("\n\n")
    return list(map(data_build, entities))

def data_build(str_item):
    #print(f"Data build func input: {str_item}")
    aux = str_item.replace("\n", " ").replace(" ", '","').replace(":", '":"')
    str_json = f"{{\"{aux}\"}}"
    #print(f"Data to build a JSON: {str_json}")
    try:
        return json.loads(str_json)
    except:
        return {}

def validate_key(key, passport, rules):
    if not key in rules:
        return False, f"E01 - Invalid key {key} in passport"
    
    if rules[key]["mandatory"]=="true" and not key in passport:
        return False, f"E02 - Missing mandatory key {key} in passport {passport}"

    if rules[key]["mandatory"]=="false":
        return True, f""

    if rules[key]["rule"]=="min_max":
        
        passport_value = passport[key]
        rule_min = rules[key]["min"]
        rule_max = rules[key]["max"]
        #print(f"DEBUG {key} _ min_max {passport_value} {rule_min} {rule_max}")
        try:
            amount = int(passport_value)

            if rule_min > amount:
                return False, f"E03A - Min {key} exceeded. Value {amount}, min limit {rule_min}"
            
            if rule_max < amount:
                return False, f"E03B - Max {key} exceeded. Value {amount}, max limit {rule_max}"
        except Exception as e:
            return False, f"E03x - Exception raised while converting to int at min_max function, msg: {e}"

    if rules[key]["rule"]=="min_max2":
        
        try:
            passport_value = passport[key]
            amount = int(passport_value[:-2])
            units = passport_value[-2:]
            #print(f"DEBUG {key} _ min_max2, units {units} amount {amount}")
        except Exception as e:
            #print(f"*** Exception {e}")
            return False, f"E04x - Exception while getting {key} data: {e}"

        if (units!="cm" and units!="in"):
            return False, f"E04 - Wrong unit on {key}"

        rule_min = rules[key][units]["min"]
        rule_max = rules[key][units]["max"]

        if rule_min > amount:
            return False, f"E04A - Min {key} exceeded. Value {amount}, min limit {rule_min}"
        
        if rule_max < amount:
            return False, f"E04B - Max {key} exceeded. Value {amount}, max limit {rule_max}"
    
    if rules[key]["rule"]=="hex":
        #print(f"DEBUG {key} _ hex")
        hex_count = rules[key]["size"]
        regex = f"^#([A-Fa-f0-9]{{{hex_count}}})$";
        if re.search(regex, passport[key]) is None:
            return False, f"E05 - Key {key} -> {passport[key]} hex match on {regex} error"

    if rules[key]["rule"]=="list":
        #print(f"DEBUG {key} _ list")
        value_list = rules[key]["list"]
        if not passport[key] in value_list:
            return False, f"E06 - Key {key} is {passport[key]} not in list {value_list}"

    if rules[key]["rule"]=="numbers":
        #print(f"DEBUG {key} _ numbers")
        num_count = rules[key]["size"]
        regex = f"^([0-9]{{{num_count}}})$";
        if re.search(regex, passport[key]) is None:
            return False, f"E07 - Key {key} is not number or has no lenght of {num_count}"

    return True, ""
        

def validate_passport(passport, rules):
    try:
        for key in rules:
            try:
                valid, msg = validate_key(key, passport, rules)
                if not valid:
                    print(f"- NOT valid!: {msg}, check here: {passport}")
                    return 0
                else:
                    pass
            except Exception as e:
                print(f"Exception occurred while validating passport {passport}, msg: {e}")
                return 0
        print(f"+ VALID: {passport}")
        return 1
    except Exception as e:
        print(f"*** Exception {e}")
        return 0

def loop_method(passports, rules):
    cont =  0
    for passport in passports:
        cont = cont + validate_passport(passport, rules)
    return cont


def main():
    passports = preprocess_data(load_data(INPUT_FILE))
    rules = json.loads(load_data(RULES_FILE))
    #print(f"{passports}")
    #print(f"{rules}")
    valid_count = loop_method(passports, rules)
    print(f"Found {valid_count} valid passports out of total of {len(passports)}")

if __name__ == "__main__":
    main()

print("NeoTheRack - completed!")