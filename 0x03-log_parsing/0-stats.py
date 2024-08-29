#!/usr/bin/python3
"""
This script reads from stdin line by line and computes metrics from the input.

The input format is expected to be:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

If the input format is not as expected, the line is skipped.

After every 10 lines and/or a keyboard interruption (CTRL + C),
the script prints the following statistics from the beginning:

1. Total file size: File size: <total size>
   where <total size> is the sum of all previous <file size>

2. Number of lines by status code:
   Possible status codes: 200, 301, 400, 401, 403, 404, 405 and 500
   If a status code doesn’t appear or is not an integer,
    nothing is printed for this status code
   The format is: <status code>: <number>
   Status codes are printed in ascending order

Note:
The script assumes that the input is provided via stdin,
 such as by redirection from a file.
"""
import sys


size = 0
stats = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}
count = 0
try:
    for line in sys.stdin:

        data = line.strip().split()
        if len(data) == 9:
            size += int(data[-1])
            if data[-2] in stats:
                stats[data[-2]] += 1
            count += 1
        if count == 10:
            print('File size: {}'.format(size))
            for key, value in sorted(stats.items()):
                if value:
                    print('{}: {}'.format(key, value))
            count = 0
except (KeyboardInterrupt, EOFError):
    print('File size: {}'.format(size))
    for key, value in sorted(stats.items()):
        if value:
            print('{}: {}'.format(key, value))
