
import networkx as nx
import matplotlib.pyplot as plt

with open('data/day7input', 'r') as myfile:
    lines = myfile.readlines()

# Part 1

# nodeDict = {}
# G = nx.DiGraph()
#
# # Setting up the DiGraph
# for line in lines:
#     spl = line.split(" bags contain ")
#     parentStr = spl[0]
#     childrenStr = spl[1]
#
#     childrenEl = childrenStr.split(", ")
#     for child in childrenEl:
#         childSpl = child.split(" ")
#         childStr = childSpl[1] + " " + childSpl[2]
#         G.add_edge(childStr, parentStr)

# nx.draw(G, with_labels=True)
# plt.show()
# print(len(nx.descendants(G, 'shiny gold')))

# Part 2
def getAmountOfChildBags(name):
    print("Looking for... " + name)
    for line in lines:
        parentStr = line.split(" bags contain ")[0]
        if parentStr == name:
            amountOfChildBags = 0
            childrenEl = line.split(" bags contain ")[1].split(", ")
            print("Found, children are: " + str(childrenEl))
            for child in childrenEl:
                childSpl = child.split(" ")
                childName = childSpl[1] + " " + childSpl[2]
                if childSpl[0] != 'no':
                    rec = getAmountOfChildBags(childName)
                    if rec == 0:
                        amountOfChildBags += int(childSpl[0])
                    else:
                        amountOfChildBags += int(childSpl[0]) + int(childSpl[0]) * rec
                    print(name + " has " + childSpl[0] + " bags")
                    print("Function got back " + str(rec) + " from rec")
            print("Returning " + str(amountOfChildBags))
            return amountOfChildBags

print(getAmountOfChildBags("shiny gold"))