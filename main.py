"""
Project: Path Finder using Graph (BFS / DFS)
Author: [Your Name]
Description:
    This program finds a path between two cities using Graph traversal algorithms (BFS and DFS).
    The user can input cities (as nodes) and their connections (as edges),
    and the algorithm finds whether a path exists between a source and a destination.
"""

from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, city1, city2):
        """Adds an undirected edge between two cities."""
        if city1 not in self.graph:
            self.graph[city1] = []
        if city2 not in self.graph:
            self.graph[city2] = []
        self.graph[city1].append(city2)
        self.graph[city2].append(city1)

    def bfs(self, start, goal):
        """Breadth-First Search to find the shortest path."""
        visited = set()
        queue = deque([[start]])

        if start == goal:
            return [start]

        while queue:
            path = queue.popleft()
            node = path[-1]

            if node not in visited:
                neighbours = self.graph.get(node, [])

                for neighbour in neighbours:
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)

                    if neighbour == goal:
                        return new_path
                visited.add(node)
        return None

    def dfs(self, start, goal, visited=None, path=None):
        """Depth-First Search using recursion to find a path."""
        if visited is None:
            visited = set()
        if path is None:
            path = []

        visited.add(start)
        path.append(start)

        if start == goal:
            return path

        for neighbour in self.graph.get(start, []):
            if neighbour not in visited:
                result = self.dfs(neighbour, goal, visited, path)
                if result:
                    return result

        path.pop()
        return None


# --------- MAIN PROGRAM ---------
if __name__ == "__main__":
    g = Graph()

    print("=== PATH FINDER USING GRAPH (BFS / DFS) ===")
    print("Enter city connections (e.g., A B). Type 'done' when finished.\n")

    while True:
        connection = input("Enter connection: ").strip()
        if connection.lower() == 'done':
            break
        try:
            city1, city2 = connection.split()
            g.add_edge(city1, city2)
        except ValueError:
            print("Invalid input! Enter two cities separated by space.")

    print("\nGraph connections:")
    for city, neighbours in g.graph.items():
        print(f"{city} -> {', '.join(neighbours)}")

    source = input("\nEnter source city: ").strip()
    destination = input("Enter destination city: ").strip()

    print("\nChoose search method:")
    print("1. Breadth-First Search (BFS)")
    print("2. Depth-First Search (DFS)")
    choice = input("Enter 1 or 2: ").strip()

    if choice == '1':
        path = g.bfs(source, destination)
        method = "BFS"
    elif choice == '2':
        path = g.dfs(source, destination)
        method = "DFS"
    else:
        print("Invalid choice!")
        exit()

    print(f"\n--- {method} Result ---")
    if path:
        print("Path found:", " -> ".join(path))
    else:
        print("No path found between", source, "and", destination)
