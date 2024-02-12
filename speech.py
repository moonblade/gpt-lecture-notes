import sys
import json
import collections

def replace_single_quotes_with_double_quotes(json_string):
    # Replace single quotes with double quotes
    return json_string.replace("'", '"')

def print_text_from_json(filename):
    try:
        with open(filename, 'r') as file:
            # Read the content and replace single quotes with double quotes
            json_content = replace_single_quotes_with_double_quotes(file.read())
            print("Modified JSON content:", json_content)  # Print the modified JSON content for debugging
            # Parse JSON
            data = json.loads(json_content, object_pairs_hook=collections.OrderedDict)
            if 'text' in data:
                print(data['text'])
            else:
                print("The 'text' key is not present in the JSON.")
    except FileNotFoundError:
        print("File not found.")
    except json.decoder.JSONDecodeError as e:
        print("Error decoding JSON:", e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py filename")
    else:
        filename = sys.argv[1]
        print_text_from_json(filename)

