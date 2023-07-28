#!/usr/bin/python3

""" Determines if a given data set represents a valid UTF-8 encoding """


def reverse_bits(num):
    """ reverses bits and returns list of bits """

    bits = []

    while num:
        bit = num & 1
        bits.append(bit)
        num >>= 1

    bits.reverse()
    return bits


def isASCII(num):
    """ checks if number is ASCII encoded """

    if num < 128:
        return True

    return False


def validUTF8(data):
    """ determines if a given data set represents a valid UTF-8 encoding """

    for x in data:
        if not isASCII(x):
            return False

    return True
