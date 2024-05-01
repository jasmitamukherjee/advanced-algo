class Graph: 
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 

    def addEdge(self, u, v, w): 
        self.graph.append([u, v, w]) 

    def find(self, parent, i): 
        if parent[i] != i: 
            parent[i] = self.find(parent, parent[i]) 
        return parent[i] 

    def union(self, parent, rank, x, y): 
        if rank[x] < rank[y]: 
            parent[x] = y 
        elif rank[x] > rank[y]: 
            parent[y] = x 
        else: 
            parent[y] = x 
            rank[x] += 1

    def KruskalMST(self): 
        result = [] 
        i = 0
        e = 0
        self.graph = sorted(self.graph, key=lambda item: item[2]) 
        parent = [] 
        rank = [] 
        for node in range(self.V): 
            parent.append(node) 
            rank.append(0) 
        while e < self.V - 1: 
            u, v, w = self.graph[i] 
            i = i + 1
            x = self.find(parent, u) 
            y = self.find(parent, v) 
            if x != y: 
                e = e + 1
                result.append([u, v, w]) 
                self.union(parent, rank, x, y) 

        minimumCost = 0
        print("Edges in the constructed MST") 
        for u, v, weight in result: 
            minimumCost += weight 
            print("%d -- %d == %d" % (u, v, weight)) 
        print("Minimum Spanning Tree Cost", minimumCost) 

if __name__ == '__main__': 
    num_vertices = int(input("Enter the number of vertices in the graph: "))
    g = Graph(num_vertices) 
    
    print("Enter edges in the format 'u v w' (separated by space), enter 'done' when finished:")
    while True:
        edge = input().strip().split()
        if edge[0] == 'done':
            break
        u, v, w = map(int, edge)
        g.addEdge(u, v, w)
    
    g.KruskalMST() 



# 0 1 5
# 0 2 10
# 1 3 8
# 1 4 6
# 2 3 7
# 2 5 9
# 3 4 11
# 4 5 12
# done