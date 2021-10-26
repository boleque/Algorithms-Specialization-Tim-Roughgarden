import random
import copy
import sys

def merge(graph, u, v):
    for child in graph[v]:  
        graph[child] = [node if node != v else u for node in graph[child]]
        graph[u].append(child)
    graph[u] = [node for node in graph[u] if node != u]
    del graph[v]

def min_cut(graph):
    graph = copy.deepcopy(graph)
    verticies = graph.keys()
    while len(verticies) > 2:
        u = random.choice(verticies)
        v = random.choice(graph[u])
        verticies.remove(v) # todo remove with constant time
        merge(graph, u, v)
    else:
        return len(graph[u])

    
if __name__ == "__main__":
    graph = {}
    with open('kargerMinCut.txt') as f:
        for ln in f:
            line = ln.split()
            if line:
                verticies = [int(x) for x in line]
                graph[verticies[0]] = verticies[1:]
        
        N10 = 10
        min_cuts10 = []
        for _ in range(N10):
            min_cuts10.append(min_cut(graph))
        res10 = min(min_cuts10)
        print('>> For N={} min cut={}\n'.format(N10, res10))
        
        N100 = 100
        min_cuts100 = []
        for _ in range(N100):
            min_cuts100.append(min_cut(graph))
        res100 = min(min_cuts100)
        print('>> For N={} min cut={}\n'.format(N100, res100))
        
        N1000 = 1000
        min_cuts1000 = []
        for _ in range(N100):
            min_cuts1000.append(min_cut(graph))
        res1000 = min(min_cuts1000)
        print('>> For N={} min cut={}\n'.format(N1000, res1000))

        print('>> min cut ', min(res1, res10, res100, res1000)) # 17
        
