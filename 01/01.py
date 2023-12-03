#!/usr/bin/env python3

import re
sum = 0
with open('input') as input:
  for line in input:
    x = re.findall('[0-9]',line.strip())
    number = str(x[0]) + str(x[-1])
    sum = sum + int(number)
print('part 1', sum)

sum = 0
with open('input') as input:
  for line in input:
    temp = line
    line = line.replace('oneight', '18')
    line = line.replace('twone', '21')
    line = line.replace('threeight', '38')
    line = line.replace('fiveight', '58')
    line = line.replace('sevenine', '79')
    line = line.replace('eightwo', '82')
    line = line.replace('nineight', '21')
    line = line.replace('one', '1')
    line = line.replace('two', '2')
    line = line.replace('three', '3')
    line = line.replace('four', '4')
    line = line.replace('five', '5')
    line = line.replace('six', '6')
    line = line.replace('seven', '7')
    line = line.replace('eight', '8')
    line = line.replace('nine', '9')
    x = re.findall('[0-9]',line.strip())
    number = x[0] + x[-1]
    sum = sum + int(number)
print('part 2', sum)
