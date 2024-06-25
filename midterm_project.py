import json
import sys

def read_json(file_name):
#Read the JSON file.
    with open(file_name, 'r') as file:
        return json.load(file)
    
# a comment




