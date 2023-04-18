#!/usr/bin/python3

"""
    (sys): helps getting command line arguement
    (json): helps in working with json
    (save_to_json_file): save object in json file
    (load_from_json_file): load from json to python friendly
"""
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


def command_args_to_json():
    """
        Get command line line arguements and convert to json
        and decode to to python friendly data type
    """

    command_arg_len = len(sys.argv)
    filename = "add_item.json"
    my_list = []
    for i in range(1, command_arg_len):
        my_list.append(sys.argv[i])

    save_to_json_file(my_list, filename)
    data = load_from_json_file(filename)
    return data


if __name__ == "__main__":
    command_args_to_json()
