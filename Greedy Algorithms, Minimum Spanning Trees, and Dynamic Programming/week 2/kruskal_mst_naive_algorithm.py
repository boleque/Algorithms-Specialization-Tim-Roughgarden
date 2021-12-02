import time
from collections import defaultdict


def kruskal_mst_naive_impl(edges):
    mst = []
    # adj list to keep track of cycles
    graph = defaultdict(list) 
    edges_sorted = sorted(edges, key=lambda x: x[2])
    for (vtx_1, vtx_2, cost) in edges_sorted:
   
        graph[vtx_1].append(vtx_2)
        graph[vtx_2].append(vtx_1)

        if find_cycle(graph, vtx_1):
            # cicles are found, remove edge from graph
            graph[vtx_1].remove(vtx_2)
            graph[vtx_2].remove(vtx_1)
            if not graph[vtx_1]:
                del graph[vtx_1]
            if not graph[vtx_2]:
                del graph[vtx_2]
        else:
            mst.append(cost)

    return mst

def find_cycle(graph, start_vertex):
    queue = [start_vertex]
    visited = {start_vertex}
    verticies_states = {k: -1 for k in graph.iterkeys()}
    while queue:
        vertex = queue.pop(0)
        verticies_states[vertex] = 1
        for neighbor in graph[vertex]:
            if verticies_states[neighbor] == 0:
                return True
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                verticies_states[neighbor] = 0
    return False

def get_data():
    with open("edges.txt") as f:
        edges = []
        lines = iter(f.readlines())
        number_of_verticies = int(next(lines))       
        for line in lines:
            vertex, neighbor, cost = [int(v) for v in line.split()]
            edges.append((vertex, neighbor, cost))
        return number_of_verticies, edges


if __name__ == '__main__':
    _, edges = get_data()
    kruskal_mst_naive_impl(edges)
  
# mst costs -3612829
