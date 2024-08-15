#!/usr/bin/python3
"""
a script that reads stdin line by line and computes metrics:
"""
import sys


def print_stats(total_size, status_codes):
    """
    Function that prints the computed statistics

    Args:
    total_size (int): the total file size
    status_codes (dict) with status code counts.
    """
    print(f"File size: {total_size}")
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def parse_line(line):
    """
    parses a line to extract status code and file size"
    """
    try:
        parts = line.split()

        if len(parts) < 7:
            return None
        status_code = int(parts[-2])
        file_size = int(parts[-1])
        return status_code, file_size
    except (IndexError, ValueError):
        return None


def main():
    """
    the main function for executing the functions
    """
    total_size = 0
    line_count = 0
    status_codes = {
        200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    try:
        for line in sys.stdin:
            parsed = parse_line(line)
            if parsed:
                status_code, file_size = parsed
                total_size += file_size
                if status_code in status_codes:
                    status_codes[status_code] += 1
                if line_count == 9:
                    print_stats(total_size, status_codes)
            line_count += 1

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

    print_stats(total_size, status_code)


if __name__ == '__main__':
    main()
