#!/usr/bin/python3
"""
Sccript to check if the unicodes of a given set of integers is
encodable to utf-8 format
"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """
    check if integers in the data list are utf-8 encodable
    """
    # take track of the bytes required to encode the current code point
    num_bytes = 1

    for num in data:
        # get the least 8 significant bits of each number
        num = num & 0xFF
        # check if the current num represent the start of a new character
        # in utf-8 encoded format
        if num_bytes == 1:
            if num >> 7 == 0:
                # then its a single byte character
                num_bytes = 1

            elif num >> 5 == 0b110:
                # then its a 2 byte character
                num_bytes = 2

            elif num >> 4 == 0b1110:
                # its a 3 byte character
                num_bytes = 3

            elif num >> 3 == 0b11110:
                # its a 4 byte character/code point
                num_bytes = 4

            else:
                return False

        # check if the continuation byte havr 10 as its initial
        else:
            if num >> 6 != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 1
