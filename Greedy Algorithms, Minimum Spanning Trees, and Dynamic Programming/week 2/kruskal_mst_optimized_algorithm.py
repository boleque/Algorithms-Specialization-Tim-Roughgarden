import time
from collections import defaultdict
from disjoint_set import DisjointSet


def kruskal_mst_optimized_impl(edges):
    mst = []
    edges_sorted = sorted(edges, key=lambda x: x[2])
    disjoint_set = DisjointSet()
    for (vtx_1, vtx_2, cost) in edges_sorted:
        if not find_cycle(disjoint_set, vtx_1, vtx_2):
            mst.append((vtx_1, vtx_2, cost))
    return mst

def find_cycle(disjoint_set, vtx_1, vtx_2):
    disjoint_set.make_set(vtx_1)
    disjoint_set.make_set(vtx_2)

    vtx_1_node = disjoint_set.get_node_by_id(vtx_1)
    vtx_2_node = disjoint_set.get_node_by_id(vtx_2)

    union_result = DisjointSet.union(vtx_1_node, vtx_2_node)
    find_cycle = not union_result

    return find_cycle

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
    mst = kruskal_mst_optimized_impl(edges)
    mst_cost = sum([cost for _, _, cost in mst])
    assert mst_cost == -3612829