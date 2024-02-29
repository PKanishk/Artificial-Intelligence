from queue import PriorityQueue
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(self.V)]

    def add_edge(self, src, dest, weight):
        self.graph[src].append((dest, weight))

    def best_first_search(self, source, target):
        visited = [False] * self.V
        pq = PriorityQueue()
        pq.put((0, source))
        while not pq.empty():
            u = pq.get()[1]
            print(u, end=" ")
            if u == target:
                print("\nTarget found!")
                break
            visited[u] = True
            for v, weight in self.graph[u]:
                if not visited[v]:
                    pq.put((weight, v))

graph = Graph(8)
graph.add_edge(0, 1, 4)
graph.add_edge(0, 2, 8)
graph.add_edge(1, 3, 3)
graph.add_edge(1, 4, 6)
graph.add_edge(2, 5, 7)
graph.add_edge(2, 6, 5)
graph.add_edge(3, 7, 9)
graph.add_edge(4, 7  , 8)
graph.add_edge(5, 7, 10)
graph.add_edge(6, 7, 5)
print("Best First Search starting from vertex 0:")
graph.best_first_search(0, 7)
