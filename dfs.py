class Graph:
    def __init__(self):
        self.graph = {}

    def addEdge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]

    def DFSUtil(self, v, visited):
        visited.add(v)
        print(v, end=' ')
        for neighbour in self.graph.get(v, []):
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)

    def DFS(self, v):
        visited = set()
        self.DFSUtil(v, visited)

if __name__ == "__main__":
    g = Graph()

    print("Enter edges in the format 'u v' (separated by space), enter 'done' when finished:")
    while True:
        edge = input().strip().split()
        if edge[0] == 'done':
            break
        u, v = map(int, edge)
        g.addEdge(u, v)

    start_vertex = int(input("Enter the starting vertex for DFS traversal: "))

    print("Depth First Traversal (starting from vertex", start_vertex, "):")
    g.DFS(start_vertex)
