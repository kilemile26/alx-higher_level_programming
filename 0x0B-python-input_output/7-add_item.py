#!/usr/bin/python3
"""
This script loads a list from a JSON file, adds command line arguments to the list,
and then saves the updated list back to the JSON file.
"""

import sys
import os.path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

# Filename for the JSON file
filename = "add_item.json"

# Check if the JSON file exists, and load its content if it does
if os.path.isfile(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

# Add the command line arguments to the list
for arg in sys.argv[1:]:
    my_list.append(arg)

# Save the updated list to the JSON file
save_to_json_file(my_list, filename)
