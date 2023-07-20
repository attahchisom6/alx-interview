#!/usr/bin/python3
import sys
import re

def print_metrics(file_size, status_counts):
    print("File size:", file_size)
    for status_code in sorted(status_counts.keys()):
        print(f"{status_code}: {status_counts[status_code]}")

def main():
    total_size = 0
    status_counts = {}
    line_pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[.*\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)'

    try:
        for i, line in enumerate(sys.stdin, 1):
            line = line.strip()
            match = re.match(line_pattern, line)

            if not match:
                continue

            status_code, file_size = map(int, match.groups())
            total_size += file_size
            status_counts[status_code] = status_counts.get(status_code, 0) + 1

            if i % 10 == 0:
                print_metrics(total_size, status_counts)

    except KeyboardInterrupt:
        print_metrics(total_size, status_counts)

if __name__ == "__main__":
    main()
