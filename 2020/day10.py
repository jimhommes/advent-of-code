import networkx as nx
from networkx.algorithms import approximation as approx

with open('data/day10input', 'r') as myfile:
    lines = myfile.readlines()

adapters = [int(x) for x in lines]
builtinAdapter = max(adapters) + 3
adapters.append(builtinAdapter)


def getNextAdapter(l, current):
    if len(l) > 0:
        possible = [i for i in l if i <= current + 3]
        return min(possible)
    else:
        return False


amountOf1Diff = 0
amountOf3Diff = 0
currentAdapter = 0

while (len(adapters) > 0):
    nextAdapter = getNextAdapter(adapters, currentAdapter)
    print("From adapter " + str(currentAdapter) + " to adapter " + str(nextAdapter))
    if nextAdapter - currentAdapter == 3:
        amountOf3Diff += 1
    elif nextAdapter - currentAdapter == 1:
        amountOf1Diff += 1
    currentAdapter = nextAdapter
    adapters.remove(currentAdapter)

print(amountOf1Diff * amountOf3Diff)


# def getPathsWithPossibility(paths, possibility):
#     res = []
#     for path in paths:
#         if possibility in path:
#             res.append(path)
#     return res
#
#
# def getNewPaths(currentPath, pathsWithPoss, poss):
#     res = []
#     for path in pathsWithPoss:
#         i = path.index(poss)
#         res.append(currentPath + path[i:])
#     return res
#
#
# def countAllPaths(l, current, end, currentPath, completedPaths):
#     currentPathcopy = tuple(currentPath)
#     currentPathcopy + (current,)
#     if current == end:
#         completedPaths.append(currentPathcopy)
#         return 1
#     else:
#         s = 0
#         for poss in getNextPossibleAdapters(l, current):
#             pathsWithPoss = getPathsWithPossibility(completedPaths, poss)
#             if len(pathsWithPoss) == 0:
#                 s += countAllPaths(l, poss, end, currentPathcopy, completedPaths)
#             else:
#                 s += len(pathsWithPoss)
#                 completedPaths.extend(getNewPaths(currentPath, pathsWithPoss, poss))
#         return s
#
#
# print(countAllPaths(adapters, 0, builtinAdapter, [], []))


def getNextPossibleAdapters(l, current):
    return [i for i in l if current + 3 >= i > current]


def getReachableByAdapters(l, current):
    return [i for i in l if current > i >= current-3]


adapters = [int(x) for x in lines]
builtinAdapter = max(adapters) + 3
adapters.append(builtinAdapter)
adapters.append(0)
adapters.sort(reverse=True)
#
# amountOfPaths = 1
# multiplier = 1
# for adapter in adapters:
#     amountNext = len(getNextPossibleAdapters(adapters, adapter))
#     amountOfPaths += multiplier * (amountNext - 1)
#     if amountNext > 0:
#         multiplier *= amountNext

# print(amountOfPaths)

def countAllPaths(l, current, visited):
    if current == 0:
        return 1
    else:
        if visited[current] > 0:
            return visited[current]
        else:
            s = 0
            for poss in getReachableByAdapters(l, current):
                s += countAllPaths(l, poss, visited)
            visited[current] = s
            return s


print(countAllPaths(adapters, builtinAdapter, [0] * (builtinAdapter+1)))