#!/usr/bin/python3

"""
A script for parsing HTTP request logs.
"""

import sys


def print_statistics(status_code_counts, total_size):
    """Prints the computed information."""
    print("Total file size: {:d}".format(total_size))
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] != 0:
            print("{}: {:d}".format(code, status_code_counts[code]))


status_code_counts = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
                      "404": 0, "405": 0, "500": 0}

line_count = 0
total_size = 0

try:
    for line in sys.stdin:
        if line_count != 0 and line_count % 10 == 0:
            print_statistics(status_code_counts, total_size)

        parts = line.split()
        line_count += 1

        try:
            size = int(parts[-1])
            total_size += size
        except ValueError:
            pass

        try:
            status_code = parts[-2]
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1
        except IndexError:
            pass

    print_statistics(status_code_counts, total_size)

except KeyboardInterrupt:
    print_statistics(status_code_counts, total_size)
    raise
