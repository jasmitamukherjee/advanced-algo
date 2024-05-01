class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        return None

    def is_empty(self):
        return len(self.queue) == 0


def bfs(adjList, startNode, visited):
    q = Queue()
    visited[startNode] = True
    q.enqueue(startNode)

    while not q.is_empty():
        currentNode = q.dequeue()
        print(currentNode, end=" ")

        for neighbor in adjList[currentNode]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.enqueue(neighbor)


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



# 0 1
# 0 2
# 1 3
# 1 4
# 2 4
# done
