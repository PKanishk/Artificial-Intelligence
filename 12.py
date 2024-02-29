class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def is_safe(self, v, color, c):
        for i in range(self.V):
            if i in self.graph[v] and color[i] == c:
                return False
        return True

    def graph_coloring_util(self, m, color, v):
        if v == self.V:
            return True

        for c in range(1, m + 1):
            if self.is_safe(v, color, c):
                color[v] = c
                if self.graph_coloring_util(m, color, v + 1):
                    return True
                color[v] = 0

    def graph_coloring(self, m):
        color = [0] * self.V
        if not self.graph_coloring_util(m, color, 0):
            return False

        print("The assigned colors are:")
        for c in color:
            print(c, end=" ")
        return True


if __name__ == "__main__":
    g = Graph(5)
    g.graph = [
        [0, 1, 1, 1, 0],
        [1, 0, 1, 0, 1],
        [1, 1, 0, 1, 0],
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0]
    ]
    m = 3  # Number of colors
    if not g.graph_coloring(m):
        print("Solution does not exist")
