import json
import xmltodict
import os

directory = os.path.dirname(os.path.realpath(__file__))

for filename in os.listdir(directory):
    if filename.endswith('.xml'): 
        orig_filepath = os.path.join(directory, filename)
        filename_base = os.path.splitext(os.path.basename(orig_filepath))[0]

        target_filepath = os.path.join(directory, "json", f"{filename_base}.json")
        print(orig_filepath)

        # Read the XML file
        with open(orig_filepath) as xml_file:
            xml_input = xml_file.read()
            print(xml_input)
            print(f"now on file: {filename}")
            data_dict = xmltodict.parse(xml_input)

        # Convert the dictionary to a JSON object
        json_data = json.dumps(data_dict, ensure_ascii=False).encode('utf8').decode()

        # Write the JSON data to an output file
        with open(target_filepath, "w") as json_file:
            json_file.write(json_data)
        print(f"finished file: {filename}")
