def dfs(graph, vertex, visited=None):
    if visited is None:
        visited = [vertex]
    else:
        visited.append(vertex)

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited