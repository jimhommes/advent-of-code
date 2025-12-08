with open('input/14.txt') as f:
    lines = f.readlines()


class RockLine:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __repr__(self):
        return '(S:' + str(self.x1) + ',' + str(self.y1) + ' E:' + str(self.x2) + ',' + str(self.y2) + ')'

    def get_all_coordinates(self):
        if self.x1 != self.x2:
            # Horizontal
            return [(i, self.y1) for i in range(min(self.x1, self.x2), max(self.x1, self.x2) + 1)]
        else:
            # Vertical
            return [(self.x1, i) for i in range(min(self.y1, self.y2), max(self.y1, self.y2) + 1)]


class SandGrain:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def can_move_and_update(self, blockgrid):
        try:
            # Check downward
            if blockgrid.get_blocked(self.x, self.y + 1) is False:
                self.y = self.y + 1
                return True
            # Check diagonal left
            elif blockgrid.get_blocked(self.x - 1, self.y + 1) is False:
                self.x = self.x - 1
                self.y = self.y + 1
                return True
            # Check diagonal right
            elif blockgrid.get_blocked(self.x + 1, self.y + 1) is False:
                self.x = self.x + 1
                self.y = self.y + 1
                return True
            return False
        except IndexError:
            return False

    def __repr__(self):
        return 'S(' + str(self.x) + ',' + str(self.y) + ')'


class BlockedGrid:
    def __init__(self, start_x, end_x, start_y, end_y):
        self.start_x = start_x
        self.end_x = end_x
        self.start_y = start_y
        self.end_y = end_y
        self.blockedgrid = [[False for i in range(end_x - start_x + 1)] for j in range(end_y - start_y + 1)]
        self.source_x = 500
        self.source_y = 0

    def print_grid(self):
        elwidth = 4
        print(" ".join([str(i).ljust(elwidth) for i in ['-'] + list(range(self.start_x, self.end_x + 1))])) # Header
        row_indices = range(self.start_y, self.end_y + 1)
        for row_index_grid in range(len(self.blockedgrid)):
            row = self.blockedgrid[row_index_grid]
            row_index = str(row_indices[row_index_grid]).ljust(elwidth)
            line = row_index + ' '
            for el in row:
                if el:
                    line += "#".ljust(elwidth) + ' '
                else:
                    line += ".".ljust(elwidth) + ' '
            print(line)

    def get_grid_coordinates(self, x, y):
        return x - self.start_x, y - self.start_y

    def draw_rockline(self, rockline):
        for coordinates in rockline.get_all_coordinates():
            grid_coordinates = self.get_grid_coordinates(coordinates[0], coordinates[1])
            self.blockedgrid[grid_coordinates[1]][grid_coordinates[0]] = True

    def trickle(self):
        sandgrain_coordinates = self.get_grid_coordinates(self.source_x, self.source_y)
        sandgrain = SandGrain(sandgrain_coordinates[0], sandgrain_coordinates[1])
        while sandgrain.can_move_and_update(self):
            pass
        if not (sandgrain.x == 0 or sandgrain.x == len(self.blockedgrid[0]) or sandgrain.y == len(self.blockedgrid)-1):
            self.blockedgrid[sandgrain.y][sandgrain.x] = True
            return True
        else:
            return False

    def get_blocked(self, x, y):
        return self.blockedgrid[y][x]



#
# Read all data
#
rocklines = []
all_x = []
all_y = []
for line in lines:
    spl = line.strip().split(' -> ')
    begin = spl[0]
    for end in spl[1:]:
        beginspl = begin.split(',')
        endspl = end.split(',')
        rocklines.append(RockLine(int(beginspl[0]), int(beginspl[1]), int(endspl[0]), int(endspl[1])))
        all_x += [int(beginspl[0]), int(endspl[0])]
        all_y += [int(beginspl[1]), int(endspl[1])]
        begin = end

min_x = min(all_x)
max_x = max(all_x)
min_y = min(all_y)
max_y = max(all_y)

#
# Create BlockedGrid
#
blockedgrid = BlockedGrid(min_x, max_x, 0, max_y)

#
# Draw all lines on blockedgrid
#
for rockline in rocklines:
    blockedgrid.draw_rockline(rockline)
print('Initial grid')
blockedgrid.print_grid()

#
# Simulate sande trickles
#
count = 0
print('Attempting grain 1..')
while blockedgrid.trickle():
    count += 1
    # blockedgrid.print_grid()
    print('Attempting grain ' + str(count + 1) + '..')
print(str(count) + ' successfull grains trickled')
