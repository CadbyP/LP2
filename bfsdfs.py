from collections import deque

# Depth First Search (DFS - Recursive)
def dfs_recursive(graph, vertex, visited):
    visited.add(vertex)
    print(vertex, end=' ')
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

# Breadth First Search (BFS - Iterative)
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=' ')
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Main Program
def main():
    # Input graph
    graph = {}
    num_edges = int(input("Enter the number of edges: "))
    print("Enter edges (e.g., 'A B' or '0 1' for an edge between two vertices):")
    for _ in range(num_edges):
        u, v = input().split()
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)

    # Choose traversal method
    print("\nChoose Traversal Method:")
    print("1. Depth First Search (DFS)")
    print("2. Breadth First Search (BFS)")
    choice = int(input("Enter your choice (1 or 2): "))

    start_vertex = input("Enter the starting vertex: ")

    if start_vertex not in graph:
        print(f"Error: Vertex {start_vertex} does not exist in the graph.")
        return

    if choice == 1:
        print("DFS Traversal:")
        visited = set()
        dfs_recursive(graph, start_vertex, visited)
    elif choice == 2:
        print("BFS Traversal:")
        bfs(graph, start_vertex)
    else:
        print("Invalid choice! Please run the program again.")

# Run the program
if __name__ == "__main__":
    main()
