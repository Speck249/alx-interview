#!/usr/bin/python3

import sys


def print_msg(status_codes, total_file_size):
    """
    Prints the status codes and total file size.
    
    Args:
        status_codes (dict): Dictionary of status codes.
        total_file_size (int): Total file size.
    """
    print("File size: {}".format(total_file_size))
    for code, count in sorted(status_codes.items()):
        if count != 0:
            print("{}: {}".format(code, count))


total_file_size = 0
status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

counter = 0

try:
    for line in sys.stdin:
        parsed_line = line.split()  # Trim and split the line
        parsed_line = parsed_line[::-1]  # Reverse the line

        if len(parsed_line) > 2:
            counter += 1

            if counter <= 10:
                total_file_size += int(parsed_line[0])  # Get file size
                code = parsed_line[1]  # Get status code

                if code in status_codes:
                    status_codes[code] += 1

            if counter == 10:
                print_msg(status_codes, total_file_size)
                counter = 0

finally:
    print_msg(status_codes, total_file_size)
