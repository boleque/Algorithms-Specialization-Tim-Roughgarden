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
    
def connected_components(graph):
    visited = []
    connected_components = []
    for node in graph.iterkeys():
        if node not in visited:
            cc = bfs(graph, node)
            visited.extend(cc)
            connected_components.append(cc)
    return connected_components