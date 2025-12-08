
def read_matrix():
    with open('data/day17input', 'r') as myfile:
        lines = myfile.readlines()

    res = [[[]]]
    for line in lines:
        res[0][0].append(list(line.strip()))
    return res


def get_element_from_matrix(m, x, y, z, w):
    if 0 <= x < len(m[0][0][0]) and 0 <= y < len(m[0][0]) and 0 <= z < len(m[0]) and 0 <= w < len(m):
        return m[w][z][y][x]
    else:
        return None


def print_matrix(m):
    print("Printing Matrix")
    for w in range(len(m)):
        for z in range(len(m[0])):
            print("z = " + str(z) + ", w = " + str(w))
            for line in m[w][z]:
                print("".join(line))
            print("")
    print("")


def extend_matrix(m):
    current_max_w = len(m)
    current_max_z = len(m[0])
    current_max_y = len(m[0][0])
    current_max_x = len(m[0][0][0])

    res = []
    for w in range(current_max_w+2):
        if w == 0 or w == current_max_w+1:
            res.append(get_empty_w(current_max_z + 2, current_max_y + 2, current_max_x + 2))
        else:
            res.append([])
            for z in range(current_max_z+2):
                if z == 0 or z == current_max_y+1:
                    res[w].append(get_empty_z(current_max_y + 2, current_max_x + 2))
                else:
                    res[w].append([])
                    for y in range(current_max_y+2):
                        res[w][z].append([])
                        for x in range(current_max_x+2):
                            if y == 0 or x == 0 or y == current_max_y+1 or x == current_max_x+1:
                                res[w][z][y].append('.')
                            else:
                                res[w][z][y].append(get_element_from_matrix(m, x-1, y-1, z-1, w-1))
    return res


def get_empty_z(row, col):
    res = []
    for r in range(row):
        add_row = []
        for c in range(col):
            add_row.append('.')
        res.append(add_row)
    return res


def get_empty_w(height, row, col):
    res = []
    for z in range(height):
        res.append([])
        for y in range(row):
            res[z].append([])
            for x in range(col):
                res[z][y].append('.')
    return res


def process_matrix(m):
    current_max_w = len(m)
    current_max_z = len(m[0])
    current_max_y = len(m[0][0])
    current_max_x = len(m[0][0][0])

    res = []
    for w in range(current_max_w):
        res.append([])
        for z in range(current_max_z):
            res[w].append([])
            for y in range(current_max_y):
                res[w][z].append([])
                for x in range(current_max_x):
                    current_element = get_element_from_matrix(m, x, y, z, w)
                    current_neighbors = get_neighbors(m, x, y, z, w)
                    if current_element == '#':
                        if current_neighbors.count('#') == 2 or current_neighbors.count('#') == 3:
                            res[w][z][y].append('#')
                        else:
                            res[w][z][y].append('.')
                    else:
                        if current_neighbors.count('#') == 3:
                            res[w][z][y].append('#')
                        else:
                            res[w][z][y].append('.')
    return res


def get_neighbors(m, x, y, z, w):
    res = []
    for x_deficit in range(-1, 2):
        for y_deficit in range(-1, 2):
            for z_deficit in range(-1, 2):
                for w_deficit in range(-1, 2):
                    if not (x_deficit == y_deficit == z_deficit == w_deficit == 0):
                        neighbor = get_element_from_matrix(m, x + x_deficit, y + y_deficit, z + z_deficit, w + w_deficit)
                        if neighbor is not None:
                            res.append(neighbor)
    return res


def count_active_elements(m):
    res = 0
    for w in range(len(m)):
        for z in range(len(m)):
            for y in range(len(m[0][0])):
                for x in range(len(m[0][0][0])):
                    if get_element_from_matrix(m, x, y, z, w) == '#':
                        res += 1
    return res


matrix = read_matrix()
# print_matrix(matrix)
for i in range(6):
    matrix = extend_matrix(matrix)
    matrix = process_matrix(matrix)
    # print_matrix(matrix)

print("Amount of active elements: " + str(count_active_elements(matrix)))