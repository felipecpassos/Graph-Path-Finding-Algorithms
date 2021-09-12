from collections import defaultdict
import math

from priority_queue import PriorityQueue

class Graph_A_Star:
 
    def __init__(self):
        self.graph = defaultdict(list)
        self.H = []
 
    def add_weighted_edge(self,u,v,w):
        self.graph[u].append({"node": v, "weight": w})
        self.graph[v].append({"node": u, "weight": w})

    def append_H_value(self, H_value):
        self.H.append(H_value)

    def A_star(self, x, y):
        pi = self.A_star_procedure(x, y)
        # print("Olha o Pi: ", pi)
        path = []
        path.append(y)
        end = pi[y]
        while end != -1:
            path.append(end)
            end = pi[end]
        path.reverse()
        return path


    def A_star_procedure(self, x, y):

        # visited = [False] * (max(self.graph) + 1)
        
        F = []
        for i in self.graph:
            F.append(math.inf)
        F[0] = 0
        G = []
        for i in self.graph:
            G.append(math.inf)
        G[0] = 0

        last = [-1] * (max(self.graph) + 1)

        queue = PriorityQueue()

        queue.insert((0, x))
 

        # visited[x] = True
 
        while not queue.isEmpty():

            x = queue.delete()
            
            queue_f = x[0]
            queue_node = x[1]
            # print (x, " ")

            # looking at the neighboors
            for i in self.graph[queue_node]:
                visit_node = i.get("node")
                visit_weight = i.get("weight")
                # print("Olha o visited node e weight:", i)
                current_distance = visit_weight + G[queue_node]
                # print("current distance: ", current_distance)
                if current_distance < G[visit_node]:
                    G[visit_node] = current_distance
                    F[visit_node] = G[visit_node] + self.H[visit_node]
                    last[visit_node] = queue_node
                    queue.insert((F[visit_node], visit_node))

        # print("F:", F)
        # print("G:", G)
        # print("last: ", last)
        return last



### A Star Algorithm ###
g = Graph_A_Star()

N = input()
for i in range(0,int(N)):
    H_value_aux = int(input())
    g.append_H_value(int(H_value_aux))

E = input()
for i in range(0,int(E)):
    abw = input()
    a = int(abw.split(" ")[0]) - 1
    b = int(abw.split(" ")[1]) - 1
    w = int(abw.split(" ")[2])
    g.add_weighted_edge(a, b, w)

xy = input()
x = int(xy.split(" ")[0]) - 1
y = int(xy.split(" ")[1]) - 1
path = g.A_star(x, y)
# print("Path: ")
for i in path:
    if i != y:
        print(str(i+1) + "-", end="")
    else:
        print(str(i+1), end="")