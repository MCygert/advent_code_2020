f = open("input.txt", "r")

lines = f.readlines()


count = 0
for line in lines:
    splittedLine = line.strip().split(' ')
    range_of_numbers = splittedLine[0].split('-')
    letter = splittedLine[1].split(':')[0]
    password = splittedLine[2]

    first_letter = password[int(range_of_numbers[0])-1]
    second_letter = password[int(range_of_numbers[1])-1]
    if(first_letter == second_letter):
        continue
    elif(first_letter == letter or second_letter == letter):
        count += 1

print(count)
