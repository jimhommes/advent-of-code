
def read_matrix():
    with open('data/day17input', 'r') as myfile:
        lines = myfile.readlines()

    matrix = [[]]
    for line in lines:
        matrix[0].append(list(line.strip()))
    return matrix


def get_element_from_matrix(m, x, y, z):
    if 0 <= x < len(m[0][0]) and 0 <= y < len(m[0]) and 0 <= z < len(m):
        return m[z][y][x]
    else:
        return None


def print_matrix(m):
    print("Printing Matrix")
    for i in range(len(m)):
        print("z = " + str(i))
        for line in m[i]:
            print("".join(line))
        print("")
    print("")


def extend_matrix(m):
    current_height_length = len(m)
    current_row_length = len(m[0])
    current_col_length = len(m[0][0])

    res = []
    for z in range(current_height_length+2):
        if z == 0 or z == current_height_length+1:
            res.append(get_empty_layer(current_row_length + 2, current_col_length + 2))
        else:
            res.append([])
            for y in range(current_row_length+2):
                res[z].append([])
                for x in range(current_col_length+2):
                    if y == 0 or x == 0 or y == current_row_length+1 or x == current_col_length+1:
                        res[z][y].append('.')
                    else:
                        res[z][y].append(get_element_from_matrix(m, x-1, y-1, z-1))
    return res


def get_empty_layer(row, col):
    res = []
    #     First Layer
    for r in range(row):
        add_row = []
        for c in range(col):
            add_row.append('.')
        res.append(add_row)
    return res


def process_matrix(m):
    matrix_height = len(m)
    matrix_rows = len(m[0])
    matrix_cols = len(m[0][0])

    res = []
    for z in range(matrix_height):
        res.append([])
        for y in range(matrix_rows):
            res[z].append([])
            for x in range(matrix_cols):
                current_element = get_element_from_matrix(m, x, y, z)
                current_neighbors = get_neighbors(m, x, y, z)
                if current_element == '#':
                    if current_neighbors.count('#') == 2 or current_neighbors.count('#') == 3:
                        res[z][y].append('#')
                    else:
                        res[z][y].append('.')
                else:
                    if current_neighbors.count('#') == 3:
                        res[z][y].append('#')
                    else:
                        res[z][y].append('.')
    return res


def get_neighbors(m, x, y, z):
    res = []
    for x_deficit in range(-1, 2):
        for y_deficit in range(-1, 2):
            for z_deficit in range(-1, 2):
                if not (x_deficit == y_deficit == z_deficit == 0):
                    neighbor = get_element_from_matrix(m, x + x_deficit, y + y_deficit, z + z_deficit)
                    if not neighbor is None:
                        res.append(neighbor)
    return res


def count_active_elements(m):
    res = 0
    for z in range(len(m)):
        for y in range(len(m[0])):
            for x in range(len(m[0][0])):
                if get_element_from_matrix(m, x, y, z) == '#':
                    res += 1
    return res


matrix = read_matrix()
print_matrix(matrix)
for i in range(6):
    matrix = extend_matrix(matrix)
    matrix = process_matrix(matrix)
    print_matrix(matrix)

print("Amount of active elements: " + str(count_active_elements(matrix)))