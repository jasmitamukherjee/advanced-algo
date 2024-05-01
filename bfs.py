from collections import deque

def bfs(adjList, startNode, visited):
    q = deque()
    visited[startNode] = True
    q.append(startNode)

    while q:
        currentNode = q.popleft()
        print(currentNode, end=" ")

        for neighbor in adjList[currentNode]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append(neighbor)

def addEdge(adjList, u, v):
    adjList[u].append(v)

def main():
    vertices = int(input("Enter the number of vertices in the graph: "))
    adjList = [[] for _ in range(vertices)]

    print("Enter edges in the format 'u v' (separated by space), enter 'done' when finished:")
    while True:
        edge = input().strip().split()
        if edge[0] == 'done':
            break
        u, v = map(int, edge)
        addEdge(adjList, u, v)

    startNode = int(input("Enter the starting vertex for BFS traversal: "))

    visited = [False] * vertices

    print("Breadth First Traversal starting from vertex", startNode, ":", end=" ")
    bfs(adjList, startNode, visited)

if __name__ == "__main__":
    main()
