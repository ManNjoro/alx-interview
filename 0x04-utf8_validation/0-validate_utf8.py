#!/usr/bin/python3
'''
Script that determines if a given data set represents a valid UTF-8 encoding
'''


def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.

    Args:
    - data (list of int): List of integers representing 8-bit data bytes.

    Returns:
    - bool: True if data is a valid UTF-8 encoding, else return False.
    """

    def check_next_bytes(data, start, n):
        for i in range(start + 1, start + n + 1):
            if i >= len(data) or (data[i] >> 6) != 0b10:
                return False
        return True

    i = 0
    while i < len(data):
        byte = data[i]

        if byte >> 7 == 0:
            i += 1
            continue

        elif byte >> 5 == 0b110 and check_next_bytes(data, i, 1):
            i += 2
            continue

        elif byte >> 4 == 0b1110 and check_next_bytes(data, i, 2):
            i += 3
            continue

        elif byte >> 3 == 0b11110 and check_next_bytes(data, i, 3):
            i += 4
            continue

        else:
            return False

    return True
