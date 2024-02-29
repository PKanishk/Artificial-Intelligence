class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.colors = [0] * self.V
        self.graph = [[] for _ in range(self.V)]

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def is_safe(self, v, color):
        for i in self.graph[v]:
            if self.colors[i] == color:
                return False
        return True

    def graph_coloring_util(self, m, v):
        if v == self.V:
            return True

        for color in range(1, m + 1):
            if self.is_safe(v, color):
                self.colors[v] = color
                if self.graph_coloring_util(m, v + 1):
                    return True
                self.colors[v] = 0

    def graph_coloring(self, m):
        if not self.graph_coloring_util(m, 0):
            print("No solution exists.")
            return False
        print("The colors assigned to each region:")
        for i in range(self.V):
            print(f"Region {i}: Color {self.colors[i]}")
        return True

graph = Graph(5)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 3)
graph.add_edge(3, 4)
num_colors = 3  
graph.graph_coloring(num_colors)
