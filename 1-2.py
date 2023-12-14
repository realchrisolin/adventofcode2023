""""Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?"""

import re

text_to_number = {
    'one': 1,
    '1': 1,
    'two': 2,
    '2': 2,
    'three': 3,
    '3': 3,
    'four': 4,
    '4': 4,
    'five': 5,
    '5': 5,
    'six': 6,
    '6': 6,
    'seven': 7,
    '7': 7,
    'eight': 8,
    '8': 8,
    'nine': 9,
    '9': 9
}

def cal_val(data: str) -> str:
    if len(data) == 0:
        return 0
    elif len(data) == 1:
        a = data[0]
        b = data[0]
        x = int(f'{a}{b}')
        return x
    else:
        a = data[0]
        b = data[-1]
        x = int(f'{a}{b}')
        print(x)
        return x

total = 0
try:
    with open('1.input', 'r', newline='\n') as input_file:
        for line in input_file:
            raw_value = line
            matching_keys = []
            for key,val in text_to_number.items():
                start = 0
                while start < len(line):
                    index = line.find(key, start)
                    if index == -1:
                        break
                    matching_keys.append((val, index))
                    start = index + 1
            matching_keys.sort(key=lambda x: x[1])
            matching_keys = [key for key, _ in matching_keys]
            print(f'raw value: {raw_value.strip()}')
            print(f'total before adding cal val: {total}')
            print(f'matching keys: {matching_keys}')
            total += cal_val(matching_keys)
            print(f'total after adding cal val: {total}')
            print(f'*'*5)
except Exception as e:
    print({e})
print(total)

