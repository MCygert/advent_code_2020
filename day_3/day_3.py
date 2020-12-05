f = open("input.txt", "r")
whole_maze = f.readlines()


def count_trees_on_path(right, maze):
    counter_of_place = 0
    counter_of_tree = 0
    for path in maze:
        single_path = path.strip()
        if(counter_of_place >= 31):
            counter_of_place = counter_of_place % 31
        if(single_path[counter_of_place] == "#"):
            counter_of_tree += 1
        counter_of_place += right
    return counter_of_tree

first = count_trees_on_path(1, whole_maze)
second = count_trees_on_path(3, whole_maze)
third = count_trees_on_path(5, whole_maze)
fourth = count_trees_on_path(7, whole_maze)
# half_of_maze = whole_maze[::2]
fifth = count_trees_on_path(1, whole_maze[::2])

print(first*second*third*fourth*fifth)

