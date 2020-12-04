import json

INPUT_FILE = "2020/Day4/inputdata"
KEY_PLAN = {"byr": "mandatory", "iyr":"mandatory", "eyr":"mandatory", "hgt":"mandatory", "hcl":"mandatory", "ecl":"mandatory", "pid":"mandatory", "cid":"optional"}

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

def validate_passport(passport):
    for key in KEY_PLAN:
        if KEY_PLAN[key]=="mandatory" and not key in passport:
            print(f"- NOT valid!: {passport} <-- missing key {key}")
            return 0
        else:
            pass
    print(f"+ VALID: {passport}")
    return 1

def loop_method(passports):
    return len(list(filter(validate_passport, passports)))


def main():
    passports = preprocess_data(load_data(INPUT_FILE))
    #print(f"{passports}")
    valid_count = loop_method(passports)
    print(f"Found {valid_count} valid passports out of total of {len(passports)}")

if __name__ == "__main__":
    main()

print("NeoTheRack - completed!")