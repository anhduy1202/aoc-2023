import sys
import os
from typing import *
script_dir = os.path.dirname(__file__)
mymodule_dir = os.path.join(script_dir, '..')
sys.path.append(mymodule_dir)
from helpers import file_util

numbers_map = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five' : 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

def solution():
    res = 0
    data = file_util.textTo1DList('data.txt')
    for lines in data:
        lineStr = ''
        for idx, char in enumerate(lines):
            first_three = lines[idx:idx+3]
            first_four = lines[idx:idx+4]
            first_five = lines[idx:idx+5]
            if char.isdigit():
                lineStr = ''.join([str(lineStr), char])
            else:
                if first_three in numbers_map:
                    lineStr = ''.join([str(lineStr), str(numbers_map[first_three])])
                elif first_four in numbers_map:
                    lineStr = ''.join([str(lineStr), str(numbers_map[first_four])])
                elif first_five in numbers_map:
                    lineStr = ''.join([str(lineStr), str(numbers_map[first_five])])
        res += int(lineStr[0] + lineStr[-1])
    print(res)

solution()