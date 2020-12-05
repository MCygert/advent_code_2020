import math

f = open('input.txt', 'r')

lines = f.readlines()
vertical = list(range(0, 127))
horizontal = list(range(0, 8))

seat_id_list = []
for line in lines:
    vertical_row = line[0:7:1]
    horizontal_row = line[7:10:1]
    temp_vertical = vertical
    temp_horizontal = horizontal
    for character in vertical_row:
        slicing_var = math.ceil(len(temp_vertical) / 2)
        if(character == "F"):
            temp_vertical = temp_vertical[:slicing_var]
        else:
            temp_vertical = temp_vertical[slicing_var:]
    for character in horizontal_row:
        slicing_var = math.ceil(len(temp_horizontal) / 2)
        if(character == "L"):
            temp_horizontal = temp_horizontal[:slicing_var]
        else:
            temp_horizontal = temp_horizontal[slicing_var:]
    seat_id = ((temp_vertical[0] * 8) + temp_horizontal[0])
    seat_id_list.append(seat_id)
seat_id_list.sort()
for i in range(len(seat_id_list)):
    higher_id = i+1
    if((seat_id_list[i] + 2) == seat_id_list[higher_id]):
        print(seat_id_list[i])
