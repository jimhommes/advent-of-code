with open('input/8.txt') as f:
    lines = f.readlines()


def get_scenic(grid, x, y):
    tree_height = grid[y][x]
    horizontal_row_left, horizontal_row_right = get_horizontal_row_without(grid, y, x)
    horizontal_row_left.reverse()
    vertical_row_top, vertical_row_bottom = get_vertical_row_without(grid, x, y)
    vertical_row_top.reverse()

    count_left = count_visible_trees(horizontal_row_left, tree_height)
    count_right = count_visible_trees(horizontal_row_right, tree_height)
    count_top = count_visible_trees(vertical_row_top, tree_height)
    count_bottom = count_visible_trees(vertical_row_bottom, tree_height)

    return count_left * count_right * count_top * count_bottom


def count_visible_trees(trees, tree_height):
    trees = [min(i, tree_height) for i in trees]
    try:
        return trees.index(tree_height) + 1
    except ValueError:
        return len(trees)


def get_visible(grid, x, y):
    tree_height = grid[y][x]
    # Check horizontal axis
    horizontal_row_left, horizontal_row_right = get_horizontal_row_without(grid, y, x)
    max_horizontal_height_left = max(horizontal_row_left)
    max_horizontal_height_right = max(horizontal_row_right)
    vertical_row_top, vertical_row_bottom = get_vertical_row_without(grid, x, y)
    max_vertical_row_top = max(vertical_row_top)
    max_vertical_row_bottom = max(vertical_row_bottom)
    if tree_height > max_horizontal_height_left or \
            tree_height > max_horizontal_height_right or \
            tree_height > max_vertical_row_bottom or \
            tree_height > max_vertical_row_top:
        return 1
    else:
        return 0


def get_horizontal_row_without(grid, y, x):
    row = grid[y]
    return row[:x], row[(x+1):]


def get_vertical_row_without(grid, x, y):
    res = []
    for horizontal_row in grid:
        res.append(horizontal_row[x])
    return res[:y], res[(y+1):]


# Read Grid
grid = []
for line in lines:
    grid.append([int(i) for i in line.strip()])

# Determine visible grid
y_max = len(grid)
x_max = len(grid[0])
visible_grid = [[-1 for i in range(x_max)] for j in range(y_max)]
scenic_grid = [[-1 for i in range(x_max)] for j in range(y_max)]
for y in range(y_max):
    for x in range(x_max):
        # Ex 1
        if y == 0 or x == 0 or x == (x_max-1) or y == (y_max-1):
            visible_grid[y][x] = 1
        else:
            visible_grid[y][x] = get_visible(grid, x, y)
        # Ex 2
        scenic_grid[y][x] = get_scenic(grid, x, y)

print(sum([sum(i) for i in visible_grid]))
print(scenic_grid)
print(max([max(i) for i in scenic_grid]))
