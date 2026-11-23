from itertools import permutations
def TSP(graph, n):
    cities = list(range(1, n))
    min_cost = float('inf')
    best_path = []
    for path in permutations(cities):
        cost = 0
        current = 0
        for city in path:
            cost += graph[current][city]
            current = city
        cost += graph[current][0]
        if cost < min_cost:
            min_cost = cost
            best_path = [0] + list(path) + [0]
    return min_cost, best_path
n = int(input("Enter number of cities: "))
graph = []
print("Enter the cost matrix:")
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
cost, path = TSP(graph, n)
print("Minimum Cost:", cost)
print("Best Path:", path)
