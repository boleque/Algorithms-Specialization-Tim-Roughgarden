def bfs_shortest_path(graph, start):
    queue = [start]
    dist = {start: 0}
    while queue:
        node = queue.pop(0)
        for child in graph[node]:
            if child not in dist:
                dist[child] = dist[node] + 1
                queue.append(child)
    return dist