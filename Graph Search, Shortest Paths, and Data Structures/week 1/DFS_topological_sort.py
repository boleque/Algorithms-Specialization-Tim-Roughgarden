

def dfs(graph, vertex, visited=None):
    if visited is None:
        visited = [vertex]
    else:
        visited.append(vertex)

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited

def dfs_loop(graph, vertex):
    n = len(graph.keys())
    visited = []
    current_label = n - 1
    ordering = [0] * n

    if vertex not in visited:
        dfs(graph, vertex, visited)
        for node in visited:
            ordering[current_label] = node
            current_label -= 1
    return ordering
