#!/usr/bin/python3
"""
Determine if given data set
represents valid UTF-8 encoding
"""


def validUTF8(data):
    """
    Validate UTF encoding
    """
    num_bytes = 0

    for num in data:
        if num_bytes == 0:
            mask = 1 << 7
            while mask & num:
                num_bytes += 1
                mask >>= 1

            if num_bytes == 1 or num_bytes > 4:
                return False

            if num_bytes == 0:
                continue

        else:
            if not (num >> 6 == 0b10):
                return False

        num_bytes -= 1

    return num_bytes == 0
