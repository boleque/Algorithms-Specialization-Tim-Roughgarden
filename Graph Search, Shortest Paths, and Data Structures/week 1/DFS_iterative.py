def dfs(graph, start):
    visited = []
    stack = [start]
    while stack:       
        node = stack.pop()
        if node not in visited:
            
            visited.append(node)
            for neighbor in graph[node]:
                stack.append(neighbor)
    print('visited: ', visited)
    return visited
    
if __name__ == '__main__':
    graph = {
        's': ['b', 'a'], 
        'a': ['b', 'c', ],
        'b': ['s', 'd', 'd'], 
        'c': ['a', 'd', 'e'], 
        'd': ['b', 'c', 'e'],
        'e': ['c', 'd'], 
    }

    visited = dfs(graph, 's')
    print('>> visited ', visited)