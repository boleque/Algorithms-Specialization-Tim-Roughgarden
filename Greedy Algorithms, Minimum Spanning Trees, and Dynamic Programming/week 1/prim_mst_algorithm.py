#This file describes an undirected graph with integer edge costs.  It has the format
#
#[number_of_nodes] [number_of_edges]
#
#[one_node_of_edge_1] [other_node_of_edge_1] [edge_1_cost]
#
#[one_node_of_edge_2] [other_node_of_edge_2] [edge_2_cost]
#
#...
#
#For example, the third line of the file is "2 3 -8874", indicating that there is an edge connecting vertex #2 and vertex #3 that has cost -8874. 
#
#You should NOT assume that edge costs are positive, nor should you assume that they are distinct.
#Your task is to run Prim's minimum spanning tree algorithm on this graph.  You should report the overall cost of a minimum spanning tree --- an integer, which may or may not be negative --- in the box below. 
#IMPLEMENTATION NOTES: This graph is small enough that the straightforward O(mn) time implementation of Prim's algorithm should work fine. OPTIONAL: For those of you seeking an additional challenge, try implementing a heap-based version. The simpler approach, which should already give you a healthy speed-up, is to maintain relevant edges in a heap (with keys = edge costs).  The superior approach stores the unprocessed vertices in the heap, as described in lecture.  Note this requires a heap that supports deletions, and you'll probably need to maintain some kind of mapping between vertices and their positions in the heap.

from collections import namedtuple, defaultdict

Vertex = namedtuple('Vertex', ['cost', 'id', 'parent_id'])


def get_data():
    with open("edges.txt") as f:
        lines = iter(f.readlines())
        number_of_nodes, number_of_edges = [int(value) for value in next(lines).split()]
        graph = defaultdict(list)
        for line in lines:
            vertex, neighbor, cost = [int(v) for v in line.split()]
            graph[vertex].append((neighbor, cost))
            graph[neighbor].append((vertex, cost))
        return number_of_nodes, number_of_edges, graph

def get_next_vertex(min_dist_table):
    min_vertex = Vertex(float('inf'), None, None)
    for vertext_obj in min_dist_table:
        if min_vertex.cost > vertext_obj.cost:
            min_vertex = vertext_obj

    min_dist_table[min_vertex.id - 1] = Vertex(float('inf'), min_vertex.id, min_vertex.parent_id)
    return min_vertex

def prim_mst_classic_impl(graph, number_of_nodes, start_vertex):
    mst = []
    visited = set()
    min_dist_table = [
        Vertex(float('inf'), vertex, None) for vertex in range(1, number_of_nodes + 1)
    ]

    min_dist_table[start_vertex - 1] = Vertex(0, start_vertex, None)
    while len(visited) != number_of_nodes:
        next_vertex = get_next_vertex(min_dist_table)
        mst.append(next_vertex)
        for neighbor, cost in graph[next_vertex.id]:
            if neighbor not in visited:
                if min_dist_table[neighbor - 1].cost > cost:
                    min_dist_table[neighbor - 1] = Vertex(cost, neighbor, next_vertex.id)
        visited.add(next_vertex.id)
    return mst

def mst_total_cost(number_of_nodes, graph):
    start_vertex = 1
    mst = prim_mst_classic_impl(graph, number_of_nodes, start_vertex)
    return sum(node.cost for node in mst)

# -3612829