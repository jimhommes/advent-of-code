import string
import copy


class Node:
    def __init__(self, id, value):
        self.id = id
        self.value = value
        self.distance = 999

    def __repr__(self):
        return '(N' + str(self.id) + ', v' + str(self.value) + ', d' + str(self.distance) + ')'

    def update_distance(self, dist):
        self.distance = min(self.distance, dist)


class Edge:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.cost = 1

    def __repr__(self):
        return '(E ' + str(self.start.id) + '-' + str(self.end.id) + ')'


class Graph:
    def __init__(self):
        self.start = None
        self.nodes = {}
        self.edges = {}
        self.unvisited_nodes = None

    def __repr__(self):
        return 'Nodes: ' + str(self.nodes) + '\n' + 'Edges: ' + str(self.edges)

    def print_graph(self, max_x, max_y, distance=False):
        for j in range(max_y):
            rowprint = ''
            # Print sideways
            for i in range(max_x):
                # Print first row
                index = j*max_x+i
                if distance:
                    rowprint += str(self.nodes[index].distance).ljust(3)
                else:
                    rowprint += str(self.nodes[index].value).ljust(3)
                if str(index+1) in [str(edge.end.id) for edge in self.edges[index]]:
                    rowprint += '-  '
                else:
                    rowprint += '   '
            print(rowprint)
            rowprint = ''
            # Print vertical
            for i in range(max_x):
                index = j * max_x + i
                if str(index+max_x) in [str(edge.end.id) for edge in self.edges[index]]:
                    rowprint += '|     '
                else:
                    rowprint += '      '
            print(rowprint)

    def read_grid(self, grid, height_condition=True):
        self.read_grid_nodes(grid)
        self.read_grid_edges(grid, height_condition)

    def read_grid_nodes(self, grid):
        max_x = len(grid[0])
        for i in range(len(grid)):
            for j in range(max_x):
                node_id = i * max_x + j
                if node_id not in self.nodes.keys():
                    self.nodes[node_id] = Node(node_id, grid[i][j])

    def read_grid_edges(self, grid, height_condition):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                node_id = i * len(grid[0]) + j
                if height_condition:
                    self.edges[node_id] = [Edge(self.nodes[node_id], self.nodes[k]) for k in
                                           get_accessible_nodes_from_node(grid, j, i)]
                else:
                    self.edges[node_id] = [Edge(self.nodes[node_id], self.nodes[k]) for k in
                                           get_all_nodes_from_node(grid, j, i)]

    def dijkstra(self, src_node_id, debug=False, max_x=0, max_y=0):
        print('Executing complete Dijkstra for source ' + str(self.nodes[src_node_id]))
        src_node = self.nodes[src_node_id]
        src_node.distance = 0
        nodes_to_visit = [src_node]
        self.unvisited_nodes = copy.deepcopy(self.nodes)
        while len(nodes_to_visit) > 0:
            curr_node = nodes_to_visit[0]
            del nodes_to_visit[0]

            if curr_node.id in self.unvisited_nodes.keys():
                if debug:
                    print('Current node: ' + str(curr_node))
                    self.print_graph(max_x, max_y, distance=True)
                del self.unvisited_nodes[curr_node.id]
                nodes_to_visit += [i.end for i in self.edges[curr_node.id]]

                for edge in self.edges[curr_node.id]:
                    edge.end.update_distance(curr_node.distance + edge.cost)


def get_accessible_nodes_from_node(grid, x, y):
    value = grid[y][x]
    max_x = len(grid[0])
    max_y = len(grid)
    res = []
    # Left
    if x > 0 and grid[y][x-1] - value <= 1:
        res.append(y * max_x + x - 1)
    # Right
    if x < (max_x - 1) and grid[y][x+1] - value <= 1:
        res.append(y * max_x + x + 1)
    # Up
    if y > 0 and grid[y-1][x] - value <= 1:
        res.append((y - 1) * max_x + x)
    # Down
    if y < (max_y - 1) and grid[y+1][x] - value <= 1:
        res.append((y + 1) * max_x + x)

    return res


def get_all_nodes_from_node(grid, x, y):
    max_x = len(grid[0])
    max_y = len(grid)
    res = []
    # Left
    if x > 0:
        res.append(y * max_x + x - 1)
    # Right
    if x < (max_x - 1):
        res.append(y * max_x + x + 1)
    # Up
    if y > 0:
        res.append((y - 1) * max_x + x)
    # Down
    if y < (max_y - 1):
        res.append((y + 1) * max_x + x)

    return res


all_solutions = []


def find_all_path_lengths(m, from_node, end, prev_nodes):
    if from_node[0] == end.x and from_node[1] == end.y:
        # We made it! current node == end
        all_solutions.append(len(prev_nodes) + 1)
    else:
        # We are still searching
        prev_nodes.append(from_node)

        # Iterate over all possible go to neighbors
        accessible_neighbors = m.get_all_to_nodes(from_node)
        for node in accessible_neighbors:
            # Check if we didn't cross this node yet
            if node not in prev_nodes:
                find_all_path_lengths(m, node, end, prev_nodes)

        prev_nodes.remove(from_node)


class Coordinates:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def __repr__(self):
        return self.name + ': (' + str(self.x) + ',' + str(self.y) + ')'

    def get_id(self, max_x):
        return self.y * max_x + self.x


with open('input/12.txt') as f:
    lines = f.readlines()


# Find S and E and replace
S = Coordinates('S', -1, -1)
E = Coordinates('E', -1, -1)
print('Finding S and E')
for find_y in range(len(lines)):
    line = lines[find_y]
    for coordinate in [S, E]:
        try:
            find_x = line.index(coordinate.name)
            coordinate.y = find_y
            coordinate.x = find_x
            line = line.replace(coordinate.name, 'a' if coordinate.name == 'S' else 'z')
            lines[find_y] = line.strip()
        except ValueError:
            lines[find_y] = line.strip()
print('Done')
print(str(S))
print(str(E))

graph = Graph()
grid = [[string.ascii_lowercase.index(j.strip()) for j in i] for i in lines]
graph.read_grid(grid)
graph.print_graph(len(grid[0]), len(grid))
graph.dijkstra(S.get_id(len(grid[0])), debug=False, max_x=len(grid[0]), max_y=len(grid))
graph.print_graph(len(grid[0]), len(grid), distance=True)
highest_point = max([node.value for node in graph.nodes.values() if node.distance < 999])
print('Highest point: ' + str(highest_point))
smallest_distance_to_highest_point = min([node.distance for node in graph.nodes.values() if node.value == highest_point])
print('Smallest distance to that highest point: ' + str(smallest_distance_to_highest_point))
print('Distance to E: ' + str(graph.nodes[E.get_id(len(grid[0]))].distance))

for node in graph.nodes.values():
    node.distance = 999

graph.print_graph(len(grid[0]), len(grid))
graph.dijkstra(E.get_id(len(grid[0])), debug=False, max_x=len(grid[0]), max_y=len(grid))
graph.print_graph(len(grid[0]), len(grid), distance=True)
sorted_a = [node for node in graph.nodes.values() if node.value == 0]

distance_to_e = 999
for sorted_node in sorted_a:
    for node in graph.nodes.values():
        node.distance = 999
    graph.dijkstra(sorted_node.id)
    distance_to_e_new = graph.nodes[E.get_id(len(grid[0]))].distance
    if distance_to_e_new < distance_to_e:
        distance_to_e = distance_to_e_new

print(distance_to_e)
