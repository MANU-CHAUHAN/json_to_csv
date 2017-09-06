import os
import sys
import csv
import json
from collections import defaultdict


# value_types = [str, float, int]


def read_file(file_to_read):
    data = []
    counter = 0
    with open(file_to_read, encoding='UTF-16') as file:
        for line in file:
            if counter == 0 and not line.startswith("["):
                line = "[" + line
                counter += 1
            data.append(line)

    data.append("]") if data[-1] != ']' else None

    return data


if len(sys.argv) == 1:
    sys.exit('\n \n No input file name given as parameter \n')

elif len(sys.argv) > 2:
    sys.exit('\n More parameters given than required \n')

elif len(sys.argv) == 2:
    input_file = sys.argv[1]

    if not os.path.isfile(input_file):
        sys.exit('\n File does not exists \n')

    data = read_file(input_file)

    str_data = ""
    for i in data:
        if not i == "\n":
            str_data += i

    ''' Uncomment this if json data does not have json objects separated by comma .
        Or add your use case of missing commas for replace here'''
        
    # if "}\n{" in str_data:
    #     str_data = str_data.replace("}\n{", "},\n{")
    # if "} {" in str_data:
	#     str_data = str_data.replace("} {", "},\n{")

    json_data = json.loads(str_data)

    dict_objects_list = []

    # currently only for one level down the top level eg: {"name": "john", "phone" :{"mobile": XXXX, "home": ZZZZ } }
    for item in json_data:
        if isinstance(item, dict):
            per_object_dict = defaultdict(str)
            for key, value in item.items():
                # if any((isinstance(value, types) for types in value_types)) or value is None:
                if not isinstance(value, dict):
                    per_object_dict[key] = str(value)
                elif isinstance(value, dict):
                    for inner_key, inner_value in value.items():
                        # if any((isinstance(inner_value, types) for types in value_types)) or value is None:
                        per_object_dict[key] = str(inner_value)

            dict_objects_list.append(per_object_dict)

    keys = set(key for key in dict_objects_list[0].keys())

    print('\n \n  keys : \n', sorted(keys))

    data = [[obj_dict[key] for key in sorted(keys)] for obj_dict in dict_objects_list]

    with open('output.csv', 'w', encoding='utf-8', newline='') as output:
        writer = csv.writer(output, delimiter=',')
        header = [key for key in sorted(keys)]
        writer.writerow(header)
        for item in data:
            writer.writerow(item)
