class AdjancedMatrix: 

    def __init__(self, matrix):
        self.matrix = matrix
        self.n = len(matrix)

    def get_successors(self, vertex):
        return [i for i in range(self.n) if self.matrix[vertex][i] == 1]
    
    def get_predecessors(self, vertex):
        return [i for i in range(self.n) if self.matrix[i][vertex] == 1]
    
    def has_edges(self, u, v):
        return self.matrix[u][v] == 1 
    
    def get_vertices(self):
        return list(range(self.n))
    
    def get_in_degree(self, vertex):
        return sum(self.matrix[vertex] for i in range(self.n))

    def __str__(self):
        return "Macierz sąsiedztwa:\n" + "\n".join([str(row) for row in self.matrix])
    

class AdjacencyList:

    def __init__(self, matrix):
        self.n = len(matrix)
        self.adj_list = [[] for _ in range(self.n)]
        self.in_edges = [[] for _ in range(self.n)]
        
        for i in range(self.n):
            for j in range(self.n):
                if matrix[i][j] == 1:
                    self.adj_list[i].append(j)
                    self.in_edges[j].append(i)
    
    def get_successors(self, vertex):
        return self.adj_list[vertex]
    
    def get_predecessors(self, vertex):
        return self.in_edges[vertex]
    
    def has_edge(self, u, v):
        return v in self.adj_list[u]
    
    def get_vertices(self):
        return list(range(self.n))
    
    def get_in_degree(self, vertex):
        return len(self.in_edges[vertex])
    
    def __str__(self):
        result = "Lista sąsiedztwa:\n"
        for i in range(self.n):
            result += f"{i}: {self.adj_list[i]}\n"
        return result


class EdgeList:  
    def __init__(self, matrix):
        self.n = len(matrix)
        self.edges = []
        for i in range(self.n):
            for j in range(self.n):
                if matrix[i][j] == 1:
                    self.edges.append((i, j))
        
        self.successors = [[] for _ in range(self.n)]
        self.predecessors = [[] for _ in range(self.n)]
        
        for u, v in self.edges:
            self.successors[u].append(v)
            self.predecessors[v].append(u)
    
    def get_successors(self, vertex):
        return self.successors[vertex]
    
    def get_predecessors(self, vertex):
        return self.predecessors[vertex]
    
    def has_edge(self, u, v):
        return (u, v) in self.edges
    
    def get_vertices(self):
        return list(range(self.n))
    
    def get_in_degree(self, vertex):
        return len(self.predecessors[vertex])
    
    def __str__(self):
        return "Lista krawędzi:\n" + "\n".join([f"{u} -> {v}" for u, v in self.edges])
       