from collections import deque 

# BFS 

def bfs_adjancency_matrix(graph):
    n = graph.n
    visited = [False] * n
    transversal = []

    queue = deque([0])
    visited[0] = True

    while queue:
        vertex = queue.popleft()
        transversal.append(vertex)

        