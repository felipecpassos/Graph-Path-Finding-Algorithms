from collections import defaultdict
import math

class Graph_Minimax:
 
    def __init__(self):
        self.graph = defaultdict(list)
        self.values = []
        self.leaves = []
 
    def add_edge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def set_leaf(self, l, value):
        self.values[l] = value

    # Modified BFS to find only the shortest path from x to y    
    def minimax(self, node):
        visited = set()

        self.values = [-1] * (max(self.graph) + 1)
        self.leaves = [False] * (max(self.graph) + 1)

        # get the leafs and their respective values from the input, and setting the values array accordingly
        Y = input()
        for i in range(0,int(Y)):
            ab = input()
            a = int(ab.split(" ")[0]) - 1
            b = int(ab.split(" ")[1])
            self.values[a] = b
            self.leaves[a] = True

        self.minimax_procedure(node, True)

    def minimax_procedure(self, node, maximizingPlayer):
        #if current node is leaf, return its heuristical value
        if self.leaves[node] != -1:
            


    # leaf = -1
    # #find the first leaf
    # for i in range(0, max(self.graph) + 1):
    #     if self.values[i] != -1:
    #         leaf = i        


    # def minimax_procedure(self, v, visited):
    #     visited.add(v)

    #     print(v+1, " ")

    #     for neighbour in self.graph[v]:
    #         if neighbour not in visited:
    #             self.minimax_procedure(neighbour, visited)



### A Star Algorithm ###
g = Graph_Minimax()

NE = input()
N = int(NE.split(" ")[0])
E = int(NE.split(" ")[1])
for i in range(0,int(E)):
    ab = input()
    a = int(ab.split(" ")[0]) - 1
    b = int(ab.split(" ")[1]) - 1
    g.add_edge(a, b)

final = g.minimax(0)
# print("Path: ")
print(final)