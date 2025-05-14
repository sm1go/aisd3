from collections import deque 

def bfs_adjacency_matrix(graph):
    n = graph.n
    visited = [False] * n
    transversal = []

    queue = deque([0])
    visited[0] = True

    while queue:
        vertex = queue.popleft()
        transversal.append(vertex)

        
        for neighbor in graph.get_successors(vertex):
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    for i in range(n):
        if not visited[i]:
            queue = deque([i])
            visited[i] = True

            while queue:
                vertex = queue.popleft()
                transversal.append(vertex)

                for neighbor in graph.get_successors(vertex):
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)

    return transversal

def bfs_adjacency_list(graph):
    n = graph.n
    visited = [False] * n
    transversal = []

    queue = deque([0])
    visited[0] = True

    while queue:
        vertex = queue.popleft()
        transversal.append(vertex)

        for neighbor in graph.get_successors(vertex):
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    for i in range(n):
        if not visited[i]:
            queue = deque([i])
            visited[i] = True

            while queue:
                vertex = queue.popleft()
                transversal.append(vertex)

                for neighbor in graph.get_successors(vertex):
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)

    return transversal
      
def bfs_edge_list(graph):
    n = graph.n
    visited = [False] * n
    transversal = []

    queue = deque([0])
    visited[0] = True

    while queue:
        vertex = queue.popleft()
        transversal.append(vertex)

        for neighbor in graph.get_successors(vertex):
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    for i in range(n):
        if not visited[i]:
            queue = deque([i])
            visited[i] = True

            while queue:
                vertex = queue.popleft()
                transversal.append(vertex)

                for neighbor in graph.get_successors(vertex):
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)

    return transversal

def dfs_adjacency_matrix(graph):
    n = graph.n
    visited = [False] * n
    transversal = []

    def dfs(vertex):
        visited[vertex] = True
        transversal.append(vertex)

        for neighbor in graph.get_successors(vertex):
            if not visited[neighbor]:
                dfs(neighbor)

    dfs(0)

    for i in range(n):
        if not visited[i]:
            dfs(i)

    return transversal

def dfs_adjacency_list(graph):
    n = graph.n
    visited = [False] * n
    transversal = []

    def dfs(v):
        visited[v] = True
        transversal.append(v)

        for neighbor in graph.get_successors(v):
            if not visited[neighbor]:
                dfs(neighbor)

    dfs(0)

    for i in range(n):
        if not visited[i]:
            dfs(i)

    return transversal

def dfs_edge_list(graph):
    n = graph.n
    visited = [False] * n
    transversal = []

    def dfs(v):
        visited[v] = True
        transversal.append(v)

        for neighbor in graph.get_successors(v):
            if not visited[neighbor]:
                dfs(neighbor)

    dfs(0)

    for i in range(n):
        if not visited[i]:
            dfs(i)

    return transversal

def tarjan_adjacency_matrix(graph):
    n = graph.n
    visited = [False] * n
    stack = []
    
    def dfs_util(v):
        visited[v] = True
        
        for neighbor in graph.get_successors(v):
            if not visited[neighbor]:
                dfs_util(neighbor)
        
        stack.append(v)

    for i in range(n):
        if not visited[i]:
            dfs_util(i)
    
    return stack[::-1]

def tarjan_edge_list(graph):
    n = graph.n
    visited = [False] * n
    stack = []
    
    def dfs_util(v):
        visited[v] = True
        
        for neighbor in graph.get_successors(v):
            if not visited[neighbor]:
                dfs_util(neighbor)
        
        stack.append(v)

    for i in range(n):
        if not visited[i]:
            dfs_util(i)
    
    return stack[::-1]

def kahn_adjacency_matrix(graph):
    n = graph.n
    result = []
    
    in_degree = [0] * n
    for i in range(n):
        in_degree[i] = graph.get_in_degree(i)
    
    queue = deque()
    for i in range(n):
        if in_degree[i] == 0:
            queue.append(i)
    
    while queue:
        u = queue.popleft()
        result.append(u)
        
        for v in graph.get_successors(u):
            in_degree[v] -= 1
            
            if in_degree[v] == 0:
                queue.append(v)
    
    return result

def kahn_edge_list(graph):
    n = graph.n
    result = []
    
    in_degree = [0] * n
    for i in range(n):
        in_degree[i] = graph.get_in_degree(i)
    
    queue = deque()
    for i in range(n):
        if in_degree[i] == 0:
            queue.append(i)
    
    while queue:
        u = queue.popleft()
        result.append(u)
        
        for v in graph.get_successors(u):
            in_degree[v] -= 1
            
            if in_degree[v] == 0:
                queue.append(v)
    
    return result

def kahn_edge_list(graph):
    n = graph.n
    result = []
    
    in_degree = [0] * n
    for i in range(n):
        in_degree[i] = graph.get_in_degree(i)
    
    queue = deque()
    for i in range(n):
        if in_degree[i] == 0:
            queue.append(i)
    
    while queue:
        u = queue.popleft()
        result.append(u)
        
        for v in graph.get_successors(u):
            in_degree[v] -= 1
            
            if in_degree[v] == 0:
                queue.append(v)
    
    return result