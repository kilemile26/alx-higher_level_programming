#!/usr/bin/python3
"""module that reads stdin line by line and computes metrics"""


import sys


# List of possible status codes
status_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]

# Dictionary to store the count of each status code
status_count = {code: 0 for code in status_codes}

# Variable to keep track of the total file size
total_size = 0

# Variable to count the lines processed
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        tokens = line.split()
        if len(tokens) >= 7:
            status_code = tokens[-2]
            file_size = int(tokens[-1])
            if status_code in status_codes:
                status_count[status_code] += 1
            total_size += file_size

        if line_count % 10 == 0:
            print("File size: {:d}".format(total_size))
            for code in sorted(status_count.keys()):
                if status_count[code] > 0:
                    print("{}: {:d}".format(code, status_count[code]))


except KeyboardInterrupt:
    pass
finally:
    print("File size: {:d}".format(total_size))
    for code in sorted(status_count.keys()):
        if status_count[code] > 0:
            print("{}: {:d}".format(code, status_count[code]))
