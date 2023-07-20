import sys
import re

def print_statistics(file_size, Status_Code):
    """
    prints the calculated statistics e.g file size
    to the console
    """
    print("File size: {}".format(file_size))
    for code in sorted(Status_Code.keys()):
        print("{}: {}".format(code, Status_Code[code]))

def log_parser():
    """
    accesses stdin inputs and sieves out information
    based on a specified protocol
    """
    file_size = 0
    total_size = 0
    Status_Code = {}
    line_pattern = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[.*\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)$'

    try:
        for count, line in enumerate(sys.stdin, 1):
            line = line.strip()
            match = re.match(line_pattern, line)
            if not match:
                continue
            try:
                ip_address = match.group(1)
                status_code, file_size = map(int, match.group(2, 3))
                total_size += file_size
                Status_Code[status_code] = Status_Code.get(status_code, 0) + 1
            except (ValueError, TypeError):
                pass
            if count % 10 == 0:
                print_statistics(total_size, Status_Code)
    except KeyboardInterrupt:
        print_statistics(total_size, Status_Code)

if __name__ == "__main__":
    log_parser()

