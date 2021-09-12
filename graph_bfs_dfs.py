from collections import defaultdict
import math

class Graph_BFS_DFS:
 
    def __init__(self):
        self.graph = defaultdict(list)
 
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    # Modified BFS to find only the shortest path from x to y    
    def BFS(self, x, y):
        pi = self.BFS_procedure(x, y)
        path = []
        path.append(y)
        end = pi[y]
        while end != -1:
            path.append(end)
            end = pi[end]
        path.reverse()
        return path


    def BFS_procedure(self, x, y):

        return_path = []

        visited = [False] * (max(self.graph) + 1)

        queue = []

        pi = [-1] * (max(self.graph) + 1)
 
        queue.append(x)
        visited[x] = True
 
        while queue:

            x = queue.pop(0)
            print (x, " ")
            return_path.append(x)

            for i in self.graph[x]:
                print("Olha o i:", i)
                if visited[i] == False:
                    queue.append(i)
                    pi[i] = x
                    visited[i] = True
                    if i == y:
                        queue.clear()
                        break

        return pi

    def DFSUtil(self, v, visited):
        visited.add(v)
        print(v, " ")
  
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)
  
    def DFS(self, v):
        visited = set()
  
        self.DFSUtil(v, visited)