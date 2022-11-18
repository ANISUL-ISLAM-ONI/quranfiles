import os
import json
import xmltodict
files = [".".join(f.split(".")[:-1]) for f in os.listdir() if os.path.isfile(f) and f.split(".")[-1] == "xml"]
for file in files:
    with open(file+'.xml', 'r', encoding='utf-8') as xml_file:
        try:
            data = xml_file.read()
            data_dict = xmltodict.parse(data, attr_prefix='', cdata_key='')
            json_data = json.dumps(data_dict, ensure_ascii=False, indent=2).encode('utf8')
            with open(file+'.json', 'w', encoding='utf-8') as json_file:
                json_file.write(json_data.decode())
        except:
            print(file)


