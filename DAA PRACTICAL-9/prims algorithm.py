def prim(graph, n):
    visited = [False] * n
    visited[0] = True
    cost = 0
    print("Minimum Spanning Tree:")
    for i in range(n - 1):
        min_cost = 999
        x = 0
        y = 0
        for j in range(n):
            if visited[j]:
                for k in range(n):
                    if not visited[k] and graph[j][k] < min_cost:
                        min_cost = graph[j][k]
                        x = j
                        y = k
        print(x, "-", y, ":", min_cost)
        cost += min_cost
        visited[y] = True
    print("Total Cost:", cost)
n = int(input("Enter number of vertices: "))
graph = []
print("Enter adjacency matrix (use 999 for no edge):")
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
prim(graph, n)
