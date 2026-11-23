def floyd_warshall(graph, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j],
                                  graph[i][k] + graph[k][j])
    print("Shortest Distance Matrix:")
    for i in range(n):
        for j in range(n):
            print(graph[i][j], end=" ")
        print()
n = int(input("Enter number of vertices: "))
graph = []
print("Enter adjacency matrix (use 999 for infinity):")
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
floyd_warshall(graph, n)
