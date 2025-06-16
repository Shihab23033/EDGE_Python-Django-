from collections import deque

class Graph:
    def __init__(self, n):
        self.adj = {}

    def add_edge(self, u, v):
        if u not in self.adj:
            self.adj[u] = []
        if v not in self.adj:
            self.adj[v] = []
        self.adj[u].append(v)
        self.adj[v].append(u)  

    def __getitem__(self, node):
        return self.adj.get(node, [])

def shortest_path(graph, start, end):
    q = deque([start])
    visited = {start: None} #stores the parent of each node
    while q:
        current = q.popleft()
        if current == end:
            path = []
            while current is not None:
                path.append(current)
                current = visited[current]
            return path[::-1] #reverse the path by slicing
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited[neighbor] = current
                q.append(neighbor)
    return None

if __name__ == "__main__":
    n = int(input("Enter the number of edges: "))
    g = Graph(n)
    for i in range(n):
        print(f"Edge {i+1}:", end=" ")
        s = input()
        u, v = map(str, s.split())
        g.add_edge(u, v)

    start = input("Enter the start vertex: ")
    end = input("Enter the end vertex: ")
    path = shortest_path(g, start, end)

    if path:
        print(f"Shortest path from {start} to {end}: {' -> '.join(path)}")
    else:
        print(f"No path found from {start} to {end}.")
