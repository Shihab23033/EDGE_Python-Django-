class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)  # For undirected graph

    def display(self):
        for vertex in self.graph:
            print(f"{vertex} -> {', '.join(map(str, self.graph[vertex]))}")


if __name__ == "__main__":
    n=int(input("Enter the number of edges: "))
    g = Graph(n)
    for i in range(n):
        print(f"Edge {i+1}:",end=" ")
        s=input()
        u, v = map(str, s.split())
        g.add_edge(u,v)
    
    print("Graph representation:")
    g.display()


