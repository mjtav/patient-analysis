"""This script counts the number of lines in standard input
Input: strings from the system's standard input
Output: a string with the total number of lines
"""


import sys

count = 0
for line in sys.stdin:
	count += 1

print(count, 'lines in standard input')

