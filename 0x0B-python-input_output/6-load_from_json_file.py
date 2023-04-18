#!/usr/bin/python3

"""
    No module was imported
"""
def load_from_json_file(filename):
    """
        Create a new file a new json file

        Args:
            filename: a new file
    """
    with open(filename, mode='w', encoding="utf-8") as file:
        file.close()
