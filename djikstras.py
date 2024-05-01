class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def printSolution(self, dist):
        print("Vertex \t Distance from Source")
        for node in range(self.V):
            print(node, "\t\t", dist[node])

    def minDistance(self, dist, sptSet):
        min_dist = float('inf')
        min_index = -1
        for v in range(self.V):
            if dist[v] < min_dist and not sptSet[v]:
                min_dist = dist[v]
                min_index = v
        return min_index

    def dijkstra(self, src):
        dist = [float('inf')] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for _ in range(self.V):
            u = self.minDistance(dist, sptSet)
            sptSet[u] = True
            for v in range(self.V):
                if (not sptSet[v] and self.graph[u][v] > 0
                        and dist[u] + self.graph[u][v] < dist[v]):
                    dist[v] = dist[u] + self.graph[u][v]

        self.printSolution(dist)

if __name__ == '__main__':
    num_vertices = int(input("Enter the number of vertices in the graph: "))
    g = Graph(num_vertices)

    print("Enter the adjacency matrix of the graph (each row separated by space):")
    for i in range(num_vertices):
        g.graph[i] = list(map(int, input().split()))

    source_vertex = int(input("Enter the source vertex: "))
    g.dijkstra(source_vertex)



# 5
# 0 4 0 0 0
# 4 0 8 0 0
# 0 8 0 7 0
# 0 0 7 0 9
# 0 0 0 9 0