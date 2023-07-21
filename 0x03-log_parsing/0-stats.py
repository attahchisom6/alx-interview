#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics.
"""
import sys


Status_Code = {
        200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0
        }
total_size = 0
count = 0


def print_statistics(file_size, Status_Code):
    """
    Prints the calculated statistics, e.g., file size,
    to the console.
    """
    print("File size: {}".format(file_size))
    for code, value in sorted(Status_Code.items()):
        if value != 0:
            print("{}: {}".format(code, value))


if __name__ == "__main__":
    """
    Accesses stdin inputs and sieves out information
    based on a specified protocol.
    """
    try:
        for line in sys.stdin:
            list_words = line.split()

            if len(list_words) > 4:
                status_code = int(list_words[-2])
                if status_code in Status_Code.keys():
                    Status_Code[status_code] += 1

                file_size = int(list_words[-1])
                total_size += file_size
                count += 1

            if count % 10 == 0:
                count = 0
                print_statistics(total_size, Status_Code)

    except Exception:
        pass
    finally:
        print_statistics(total_size, Status_Code)
