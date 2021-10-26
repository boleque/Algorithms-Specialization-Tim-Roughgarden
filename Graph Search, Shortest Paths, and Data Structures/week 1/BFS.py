# explores nodes in "layers"
# compute shortes part
# connected components of unidirected graphs
# Run time: O(n+m)


def bfs(graph, start):
    queue = [start]
    visited = {start}
    while queue:
        node = queue.pop(0)
        for child in graph[node]:
            if child not in visited:
                visited.add(child)
                queue.append(child)
    return visited