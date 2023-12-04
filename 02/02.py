#!/usr/bin/env python3

check = {
  'red': 12,
  'green': 13,
  'blue': 14
}
possible = { }
sum = 0
with open('input') as input:
  for line in input:
    line = line.replace('Game ', '').strip()
    line = line.split(':')
    print('game', line[0])
    possible[line[0]] = 0
    game = line[1].split(';')
    print('draws', len(game))
    for draw in game:
      cubes = draw.split(',')
      for color in cubes:
        for x in check:
          if x in color:
            count = color.replace(x, '').replace(' ', '')
            if int(count) > check[x]:
              print(line[0],'impossible')
              possible[line[0]] = 1
            else:
              print('possible')
for x in possible:
  if possible[x] == 0:
    print(x, 'possible')
    sum = sum + int(x)
  else:
    print(x, 'impossible')

print('part 1', sum)

sum = 0
with open('input') as input:
  for line in input:
    mincolors = {
      'red': 0,
      'green': 0,
      'blue': 0
    }
    line = line.replace('Game ', '').strip()
    line = line.split(':')
    print('game', line[0])
    possible[line[0]] = 0
    game = line[1].split(';')
    print('draws', len(game))
    for draw in game:
      cubes = draw.split(',')
      for color in cubes:
        for x in check:
          if x in color:
            count = int(color.replace(x, '').replace(' ', ''))
            if count > mincolors[x]:
              mincolors[x] = count
    print(mincolors)
    sum = sum + (mincolors['red']*mincolors['green']*mincolors['blue'])
  print('part 2', sum) 
            

