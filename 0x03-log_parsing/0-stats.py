#!/usr/bin/python3
"""
a script that reads stdin line by line and computes metrics:
"""
import sys


if __name__ == '__main__':
    file_size = [0]
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0,
                    403: 0, 404: 0, 405: 0, 500: 0}

    def print_stats():
        """Method for printing the stats"""
        print('File size: {}'.format(file_size[0]))
        for key in sorted(status_codes.keys()):
            if status_codes[key]:
                print('{}: {}'.format(key, status_codes[key]))

    def parse_line(line):
        """Method for checking for the matches"""
        try:
            line = line[:-1]
            word = line.split(' ')
            # File size is last parameter on stdout
            file_size[0] += int(word[-1])
            # Status code comes before file size
            status_code = int(word[-2])
            # Move through dictionary of status codes
            if status_code in status_codes:
                status_codes[status_code] += 1
        except ValueError:
            pass

    line_num = 1
    try:
        for line in sys.stdin:
            parse_line(line)
            if line_num % 10 == 0:
                print_stats()
            line_num += 1
    except KeyboardInterrupt:
        print_stats()
        raise
    print_stats()
