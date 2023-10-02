#!/usr/bin/python3
"""
This script adds all command line arguments to a Python list and saves them to a JSON file.
"""

import sys
import json

def save_to_json_file(my_obj, filename):
    """
    Save an object to a JSON file.
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)

def load_from_json_file(filename):
    """
    Load an object from a JSON file.
    """
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def main():
    # Define the JSON filename
    filename = "add_item.json"

    # Load the existing list from the JSON file, or create an empty list
    items = load_from_json_file(6-load_from_json_file.py)

    # Add command line arguments to the list
    items.extend(sys.argv[1:])

    # Save the updated list to the JSON file
    save_to_json_file(items, 5-save_to_json_file.py)


if __name__ == "__main__":
    main()
