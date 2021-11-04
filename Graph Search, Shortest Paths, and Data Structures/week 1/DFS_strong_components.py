import sys

t = 0 # number of nodes processed so far, for finishing times in 1st pass
s = None # most recent vertex from wich dfs was initiated, for leaders in 2nd pass
leaders = {} # len of graph
finishing_time = {} # len of graph

def dfs(graph, vertex, visited, reverse=False):
    global leaders, finishing_time
    global t, s

    visited.add(vertex)
    leaders[vertex] = s
    if reverse:
        pass # todo substitute node with it neighbor to reverse direction        
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    t += 1
    finishing_time[vertex] = t

def dfs_loop(graph, nodes):
    global s

    visited = set()
    # start interation from max node
    nodes.sort(reverse=True)
    for node in nodes:
        if node not in visited:
            s = node
            dfs(graph, node, visited)

def strong_components(graph):
    nodes = graph.keys()
    dfs_loop(graph, nodes, reverse=True)

if __name__ == '__main__':
    # for testing
    graph = {
        1: [7],
        2: [5],
        3: [9],
        4: [1],
        5: [8],
        6: [3, 8],
        7: [4, 9],
        8: [2],
        9: [6],
    
    }

    #with open('SCC.txt', 'r') as source:
    #    for line in source:
    #        values = line.split()
    #        if len(values) >= 1:
    #            vertex = int(values[0])
    #            neighbors = graph.setdefault(vertex, [])
    #            neighbors.append(int(values[1]))

    SCCs = strong_components(graph)
    if SCCs:
        SCCs.sort()
        print('5 first maximum strong components: ', SCCs[:5])