import time
import matplotlib.pyplot as plt
import numpy as np
from implementations import AdjacencyMatrix, AdjacencyList, EdgeList
from algorithms import (
    dfs_adjacency_matrix, bfs_adjacency_matrix,
    dfs_adjacency_list, bfs_adjacency_list,
    dfs_edge_list, bfs_edge_list,
    tarjan_adjacency_matrix, tarjan_adjacency_list, tarjan_edge_list,
    kahn_adjacency_matrix, kahn_adjacency_list, kahn_edge_list
)

def generate_dag(n, saturation_ratio=0.5):
    max_edges = n * (n - 1) // 2
    target_edges = int(max_edges * saturation_ratio)

    adj_matrix = [[0 for _ in range(n)] for _ in range(n)]
    edges_added = 0
    while edges_added < target_edges:
        i = np.random.randint(0, n-1)
        j = np.random.randint(i+1, n)  
        
        if adj_matrix[i][j] == 0:  
            adj_matrix[i][j] = 1
            edges_added += 1
    
    return adj_matrix

def input_dag_manually(n):
    print(f"Wprowadź macierz sąsiedztwa ({n}x{n}) wiersz po wierszu:")
    adj_matrix = []
    for i in range(n):
        while True:
            try:
                row_input = input(f"Wiersz {i+1}: ").split()
                row = list(map(int, row_input))
                
                if len(row) != n:
                    print(f"Błąd: Każdy wiersz musi mieć {n} elementów. Spróbuj ponownie.")
                    continue
                
                if not all(val in [0, 1] for val in row):
                    print("Błąd: Macierz sąsiedztwa może zawierać tylko wartości 0 i 1. Spróbuj ponownie.")
                    continue
                
                adj_matrix.append(row)
                break
                
            except ValueError:
                print("Błąd: Wprowadzaj liczby całkowite (0 lub 1) oddzielone spacjami.") 
    cycles_found = False
    for i in range(n):
        for j in range(i+1):
            if adj_matrix[i][j] != 0 and i != j:
                cycles_found = True
                adj_matrix[i][j] = 0 
    if cycles_found:
        print("Macierz zawierała cykle. Została przekształcona w acykliczną.")
    return adj_matrix

def visualize_graph(adj_matrix):
    n = len(adj_matrix)
    
    print("\nWizualizacja grafu:")
    print("* Macierz sąsiedztwa:")
    for row in adj_matrix:
        print(" ".join(map(str, row)))
    
    print("\n* Lista sąsiedztwa:")
    for i in range(n):
        successors = [j for j in range(n) if adj_matrix[i][j] == 1]
        print(f"{i}: {successors}")
    
    print("\n* Lista krawędzi:")
    edges = [(i, j) for i in range(n) for j in range(n) if adj_matrix[i][j] == 1]
    for edge in edges:
        print(f"{edge[0]} -> {edge[1]}")

def run_algorithm_tests(n_values):
    results = {
        "n": n_values,
        "bfs_matrix": [], "bfs_list": [], "bfs_edges": [],
        "dfs_matrix": [], "dfs_list": [], "dfs_edges": [],
        "tarjan_matrix": [], "tarjan_list": [], "tarjan_edges": [],
        "kahn_matrix": [], "kahn_list": [], "kahn_edges": []
    }
    
    for n in n_values:
        print(f"\nTestowanie z rozmiarem grafu n={n}")
        adj_matrix = generate_dag(n)
        matrix_repr = AdjacencyMatrix(adj_matrix)
        list_repr = AdjacencyList(adj_matrix)  
        edge_repr = EdgeList(adj_matrix)
        
        start = time.time()
        bfs_adjacency_matrix(matrix_repr)
        results["bfs_matrix"].append(time.time() - start)
        
        start = time.time()
        bfs_adjacency_list(list_repr)
        results["bfs_list"].append(time.time() - start)
        
        start = time.time()
        bfs_edge_list(edge_repr)
        results["bfs_edges"].append(time.time() - start)
        
        start = time.time()
        dfs_adjacency_matrix(matrix_repr)
        results["dfs_matrix"].append(time.time() - start)
        
        start = time.time()
        dfs_adjacency_list(list_repr)
        results["dfs_list"].append(time.time() - start)
        
        start = time.time()
        dfs_edge_list(edge_repr)
        results["dfs_edges"].append(time.time() - start)
        
        start = time.time()
        tarjan_adjacency_matrix(matrix_repr)
        results["tarjan_matrix"].append(time.time() - start)
        
        start = time.time()
        tarjan_adjacency_list(list_repr)
        results["tarjan_list"].append(time.time() - start)
        
        start = time.time()
        tarjan_edge_list(edge_repr)
        results["tarjan_edges"].append(time.time() - start)
        
        start = time.time()
        kahn_adjacency_matrix(matrix_repr)
        results["kahn_matrix"].append(time.time() - start)
        
        start = time.time()
        kahn_adjacency_list(list_repr)
        results["kahn_list"].append(time.time() - start)
        
        start = time.time()
        kahn_edge_list(edge_repr)
        results["kahn_edges"].append(time.time() - start)
    
    plt.figure(figsize=(15, 10))
    
    plt.subplot(2, 2, 1)
    plt.plot(n_values, results["bfs_matrix"], 'o-', label='Macierz sąsiedztwa')
    plt.plot(n_values, results["bfs_list"], 's-', label='Lista sąsiedztwa')
    plt.plot(n_values, results["bfs_edges"], '^-', label='Lista krawędzi')
    plt.title('Wydajność BFS')
    plt.xlabel('n')
    plt.ylabel('Czas (s)')
    plt.legend()
    plt.grid(True)
    
    plt.subplot(2, 2, 2)
    plt.plot(n_values, results["dfs_matrix"], 'o-', label='Macierz sąsiedztwa')
    plt.plot(n_values, results["dfs_list"], 's-', label='Lista sąsiedztwa')
    plt.plot(n_values, results["dfs_edges"], '^-', label='Lista krawędzi')
    plt.title('Wydajność DFS')
    plt.xlabel('n')
    plt.ylabel('Czas (s)')
    plt.legend()
    plt.grid(True)
    
    plt.subplot(2, 2, 3)
    plt.plot(n_values, results["tarjan_matrix"], 'o-', label='Macierz sąsiedztwa')
    plt.plot(n_values, results["tarjan_list"], 's-', label='Lista sąsiedztwa')
    plt.plot(n_values, results["tarjan_edges"], '^-', label='Lista krawędzi')
    plt.title('Wydajność sortowania topologicznego Tarjana')
    plt.xlabel('n')
    plt.ylabel('Czas (s)')
    plt.legend()
    plt.grid(True)
    
    plt.subplot(2, 2, 4)
    plt.plot(n_values, results["kahn_matrix"], 'o-', label='Macierz sąsiedztwa')
    plt.plot(n_values, results["kahn_list"], 's-', label='Lista sąsiedztwa')
    plt.plot(n_values, results["kahn_edges"], '^-', label='Lista krawędzi')
    plt.title('Wydajność sortowania topologicznego Kahna')
    plt.xlabel('n')
    plt.ylabel('Czas (s)')
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.savefig('algorithm_performance.png')
    plt.show()

def main():
    print("Program Skierowanego Grafu Acyklicznego (DAG)")
    print("==============================================")
    
    while True:
        try:
            n = int(input("Wprowadź liczbę wierzchołków (n): "))
            if n <= 0:
                print("Liczba wierzchołków musi być dodatnia.")
                continue
            break
        except ValueError:
            print("Proszę wprowadzić prawidłową liczbę całkowitą.")
    
    print("\nJak chcesz utworzyć graf?")
    print("1. Wygeneruj losowy DAG z 50% nasyceniem")
    print("2. Wprowadź macierz sąsiedztwa ręcznie")
    
    while True:
        user_input = input("Wprowadź swój wybór (1/2 lub 'losowy'/'ręczny'): ").strip().lower()
        
        creation_map = {
            '1': 1, 'losowy': 1, 'random': 1, 'generuj': 1,
            '2': 2, 'ręczny': 2, 'reczny': 2, 'manual': 2, 'ręcznie': 2, 'recznie': 2
        }
        
        choice = creation_map.get(user_input)
        if choice in [1, 2]:
            break
        else:
            print("Proszę wprowadzić 1, 2 lub nazwę opcji (losowy/ręczny).")
    
    if choice == 1:
        adj_matrix = generate_dag(n)
        print(f"Wygenerowano losowy DAG z {n} wierzchołkami.")
    else:
        adj_matrix = input_dag_manually(n)
    
    matrix_repr = AdjacencyMatrix(adj_matrix)
    list_repr = AdjacencyList(adj_matrix)
    edge_repr = EdgeList(adj_matrix)
    
    visualize_graph(adj_matrix)
    
    while True:
        print("\nOperacje na grafie:")
        print("1. BFS / Przechodzenie BFS")
        print("2. DFS / Przechodzenie DFS")
        print("3. Tarjan / Sortowanie topologiczne Tarjana")
        print("4. Kahn / Sortowanie topologiczne Kahna")
        print("5. Wizualizacja / Wizualizuj graf")
        print("6. Testy / Uruchom testy algorytmów")
        print("7. Wyjście / Exit")
        
        user_input = input("Wybierz operację (1-7 lub nazwę): ").strip().lower()
        
        operation_map = {
            '1': 1, 'bfs': 1, 'przechodzenie bfs': 1,
            '2': 2, 'dfs': 2, 'przechodzenie dfs': 2,
            '3': 3, 'tarjan': 3, 'sortowanie topologiczne tarjana': 3, 'sortowanie tarjana': 3,
            '4': 4, 'kahn': 4, 'sortowanie topologiczne kahna': 4, 'sortowanie kahna': 4,
            '5': 5, 'wizualizacja': 5, 'wizualizuj graf': 5, 'wizualizuj': 5,
            '6': 6, 'testy': 6, 'uruchom testy algorytmów': 6, 'testy algorytmów': 6,
            '7': 7, 'wyjście': 7, 'exit': 7, 'wyjscie': 7
        }
        
        op = operation_map.get(user_input)
        
        if op == 1:
            print("\nPrzechodzenie BFS (wszerz):")
            print("* Używając macierzy sąsiedztwa:", bfs_adjacency_matrix(matrix_repr))
            print("* Używając listy sąsiedztwa:", bfs_adjacency_list(list_repr))
            print("* Używając listy krawędzi:", bfs_edge_list(edge_repr))
            
        elif op == 2:
            print("\nPrzechodzenie DFS (w głąb):")
            print("* Używając macierzy sąsiedztwa:", dfs_adjacency_matrix(matrix_repr))
            print("* Używając listy sąsiedztwa:", dfs_adjacency_list(list_repr))
            print("* Używając listy krawędzi:", dfs_edge_list(edge_repr))
            
        elif op == 3:
            print("\nSortowanie topologiczne Tarjana:")
            print("* Używając macierzy sąsiedztwa:", tarjan_adjacency_matrix(matrix_repr))
            print("* Używając listy sąsiedztwa:", tarjan_adjacency_list(list_repr))
            print("* Używając listy krawędzi:", tarjan_edge_list(edge_repr))
            
        elif op == 4:
            print("\nSortowanie topologiczne Kahna:")
            print("* Używając macierzy sąsiedztwa:", kahn_adjacency_matrix(matrix_repr))
            print("* Używając listy sąsiedztwa:", kahn_adjacency_list(list_repr))
            print("* Używając listy krawędzi:", kahn_edge_list(edge_repr))
            
        elif op == 5:
            visualize_graph(adj_matrix)
            
        elif op == 6:
            n_values = [200, 400, 600, 800, 1000]
            run_algorithm_tests(n_values)
            
        elif op == 7:
            print("Zamykanie programu.")
            break
            
        else:
            print("Nieprawidłowa opcja. Proszę wprowadzić numer 1-7 lub nazwę operacji.")
            print("Dostępne nazwy: bfs, dfs, tarjan, kahn, wizualizacja, testy, wyjście")

if __name__ == "__main__":
    main()