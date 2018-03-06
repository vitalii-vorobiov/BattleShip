import random


def read_data(filename):
    """
    (str) -> (data)

    Reads a file from the "filename" field and writes it in a convenient format
    date The game's field in the file is represented by 10 ribbons containing
    the * - Part of the ship that has not yet sank, X is the part of the ship
    that has already drowned and the space character is part of a field that
    does not contain a ship.
    """
    data = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f.readlines():
            data.append(line.strip().split(","))
    return data


def has_ship(data, coordinates):
    """
    (data, tuple) -> (bool)

    A function based on read data and cell coordinates (for example ("J", 1) or
    ("A", 10)) determines whether a ship is in this cell.
    """
    let_num = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7,
               "I": 8, "J": 9}
    try:
        assert (0 <= int(coordinates[1]) - 1 <= 9)
        assert (coordinates[0] in let_num)
    except AssertionError:
        return False

    if data[int(coordinates[1]) - 1][let_num[coordinates[0]]] == "*":
        return True
    else:
        return False


def ship_size(data, coordinates):
    """
    (data, tuple) -> (tuple)

    A function based on read data and cell coordinates (for example ("J", 1) or
    ("A", 10)) defines the size of the ship, part of which is in this cell.
    """
    size = 1
    let_num = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7,
               "I": 8, "J": 9}

    try:
        assert (0 <= int(coordinates[1]) - 1 <= 9)
        assert (coordinates[0] in let_num)
    except AssertionError:
        return 0, 0

    # Checks ship vertically

    if (0 <= int(coordinates[1]) <= 9) and data[int(coordinates[1])][let_num[coordinates[0]]] == "*":
        size += 1  # Size = 2
        if (0 <= int(coordinates[1]+1) <= 9) and data[int(coordinates[1]+1)][let_num[coordinates[0]]] == "*":
            size += 1  # Size = 3
            if (0 <= int(coordinates[1]+2) <= 9) and data[int(coordinates[1]+2)][let_num[coordinates[0]]] == "*":
                size += 1  # Size = 4
    if (0 <= int(coordinates[1]-2) <= 9) and data[int(coordinates[1]-2)][let_num[coordinates[0]]] == "*":
        size += 1  # Size = 2
        if (0 <= int(coordinates[1]-3) <= 9) and data[int(coordinates[1]-3)][let_num[coordinates[0]]] == "*":
            size += 1  # Size = 3
            if (0 <= int(coordinates[1]-4) <= 9) and data[int(coordinates[1]-4)][let_num[coordinates[0]]] == "*":
                size += 1  # Size = 4

    if size > 1:
        return 1, size

    # Checks ship horizontally

    if (0 <= let_num[coordinates[0]]+1 <= 9) and data[int(coordinates[1]-1)][let_num[coordinates[0]]+1] == "*":
        size += 1  # Size = 2
        if (0 <= let_num[coordinates[0]]+2 <= 9) and data[int(coordinates[1]-1)][let_num[coordinates[0]]+2] == "*":
            size += 1  # Size = 3
            if (0 <= let_num[coordinates[0]]+3 <= 9) and data[int(coordinates[1]-1)][let_num[coordinates[0]]+3] == "*":
                size += 1  # Size = 4
    if (0 <= let_num[coordinates[0]]-1 <= 9) and data[int(coordinates[1]-1)][let_num[coordinates[0]]-1] == "*":
        size += 1  # Size = 2
        if (0 <= let_num[coordinates[0]]-2 <= 9) and data[int(coordinates[1]-1)][let_num[coordinates[0]]-2] == "*":
            size += 1  # Size = 3
            if (0 <= let_num[coordinates[0]]-3 <= 9) and data[int(coordinates[1]-1)][let_num[coordinates[0]]-3] == "*":
                size += 1  # Size = 4

    if size > 1:
        return size, 1

    return 1, 1


def is_valid(data):
    """
    (data) -> (bool)

    The function checks whether a field read from a file can be a play field on
    which all ships are loaded.
    """
    num_let = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H",
               8: "I", 9: "J"}
    count = 0

    small_ship = 0
    double_ship = 0
    triple_ship = 0
    big_ship = 0
    all_ships = 0
    free_space = 0
    for row in range(len(data)):
            count += len(data[row])
            for item in range(len(data[row])):
                if data[row][item] == "-":
                    free_space += 1
                if has_ship(data, (num_let[item], row+1)):
                    all_ships += 1
                    size = ship_size(data, (num_let[item], row+1))
                    if size == (1, 1):
                        small_ship += 1
                    elif size == (1, 2) or size == (2, 1):
                        double_ship += 1
                    elif size == (1, 3) or size == (3, 1):
                        triple_ship += 1
                    elif size == (1, 4) or size == (4, 1):
                        big_ship += 1
    print(free_space)
    if count == 100 and\
       small_ship == 4 and\
       double_ship == 6 and\
       triple_ship == 6 and\
       big_ship == 4:
        return True
    else:
        return False


def field_to_str(data):
    """
    (data) -> (str)

    The function allows the selected data format to be converted into a string
    that can be write into the file or display on screen.

    X ship is hitted
    - free space
    0 missed shot
    """
    lst = []
    for i in data:
        for j in i:
            # if j == "*":
            #     lst.append("~")
            # else:
            lst.append(j)

    return "   A B C D E F G H I J\n"\
           " 1 %s %s %s %s %s %s %s %s %s %s\n"\
           " 2 %s %s %s %s %s %s %s %s %s %s\n"\
           " 3 %s %s %s %s %s %s %s %s %s %s\n"\
           " 4 %s %s %s %s %s %s %s %s %s %s\n"\
           " 5 %s %s %s %s %s %s %s %s %s %s\n"\
           " 6 %s %s %s %s %s %s %s %s %s %s\n"\
           " 7 %s %s %s %s %s %s %s %s %s %s\n"\
           " 8 %s %s %s %s %s %s %s %s %s %s\n"\
           " 9 %s %s %s %s %s %s %s %s %s %s\n"\
           "10 %s %s %s %s %s %s %s %s %s %s\n" % tuple(lst)


def generate_field():
    """
    () -> (data)

    The function allows you to generate a random field in the selected format
    on which classic ships are placed.
    """

    field = [["-" for i in range(10)] for j in range(10)]
    coordinates = [i for i in range(100)]
    ships = [1,1,1,1,2,2,2,3,3,4]

    while len(ships) != 0:
        orientation = random.randint(0, 1)
        if orientation == 1:
            ship = ships.pop()
            coor = random.choice(coordinates)
            while coor%10 > 10 - ship:
                coor = random.choice(coordinates)
            for i in range(ship):
                field[coor//10][(coor%10)+i] = "*"
            for i in range(ship+3):
                if coor-1+i in coordinates:
                    coordinates.remove(coor-1+i)
                if coor-11+i in coordinates:
                    coordinates.remove(coor-11+i)
                if coor+9+i in coordinates:
                    coordinates.remove(coor+9+i)
                print(field_to_str(field))
        else:
            ship = ships.pop()
            coor = random.choice(coordinates)
            while coor // 10 > 10 - ship:
                coor = random.choice(coordinates)
            for i in range(ship):
                field[(coor // 10)+i][(coor % 10)] = "*"
            for i in range(ship+3):
                if coor-10+i*10 in coordinates:
                    coordinates.remove(coor-10+i*10)
                if coor-11+i*10 in coordinates:
                    coordinates.remove(coor-11+i*10)
                if coor-9+i*10 in coordinates:
                    coordinates.remove(coor-9+i*10)
                print(field_to_str(field))
    return field


field = generate_field()
# print(is_valid(field))
print(field_to_str(field))