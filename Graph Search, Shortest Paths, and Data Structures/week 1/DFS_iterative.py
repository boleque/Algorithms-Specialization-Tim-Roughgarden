def dfs(graph, start):
    visited = []
    stack = [start]
    while stack:       
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            for neighbor in graph[node]:
                stack.append(neighbor)
    return visited