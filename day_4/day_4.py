import re

needed = {
    'byr': r'^[1][9][2-9][0-9]$|^[2][0][0][0-2]$',
    'iyr': r'^[2][0][1][0-9]$|^2020$',
    'eyr': r'^[2][0][2][0-9]$|^2030$',
    'hgt': r'^[1][5-8][0-9]cm$|^[1][9][0-3]cm$|^59in$|^[6][0-9]in$|^[7][0-6]in$',
    'hcl': r'^#[a-f0-9]{6}$',
    'ecl': r'^amb$|^blu$|^brn$|^gry$|^grn$|^hzl$|^oth$',
    'pid': r'^[0-9]{9}$'
}

with open('input.txt', 'r') as f:
    data = [
        i.replace('\n', ' ').split()
        for i in f.read().split('\n\n')
    ]
    print(data)
    part1, part2 = 0, 0
    for passport in data:
        passport = {i.split(':')[0]: i.split(':')[1] for i in passport}
        part1 += all(passport.get(i) for i in needed.keys())
        part2 += all(re.match(regx, passport.get(key, ''))
                     is not None for key, regx in needed.items())

    print(part1)
    print(part2)
