from collections import defaultdict

from priority_queue import PriorityQueue

class Graph_Uniform_Cost:
 
    def __init__(self):
        self.graph = defaultdict(list)
 
    def add_weighted_edge(self,u,v,w):
        self.graph[u].append({"node": v, "weight": w})
        self.graph[v].append({"node": u, "weight": w})

        # Modified BFS to find only the shortest path from x to y    

    def uniform_cost_procedure(self, x, y):

        # print("Graph: ", self.graph)

        visited = [False] * (max(self.graph) + 1)

        queue = PriorityQueue()

        pi = [-1] * (max(self.graph) + 1)
        
        # (node, weight)
        queue.insert((x, 0))

        visited[x] = True
 
        while not queue.isEmpty():

            print("Queue: ", queue)

            x = queue.delete()
            print (x, " | ")

            if x[0] == y:
                queue.clear()
                break

            for i in self.graph[x[0]]:
                print("Olha o i: ", i)
                # node = i[0]
                node = i.get("node")
                # weight = i[1]
                weight = i.get("weight")
                if visited[node] == False:
                    queue.insert((node, weight))
                    pi[node] = x[0]
                    visited[node] = True
        return pi

    def uniform_cost(self, x, y):
        pi = self.uniform_cost_procedure(x, y)
        print("Olha o Pi: ", pi)
        path = []
        path.append(y)
        end = pi[y]
        while end != -1:
            path.append(end)
            end = pi[end]
        path.reverse()
        return path