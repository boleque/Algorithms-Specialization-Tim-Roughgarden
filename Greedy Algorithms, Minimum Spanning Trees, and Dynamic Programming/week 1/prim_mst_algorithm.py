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
#
#Your task is to run Prim's minimum spanning tree algorithm on this graph.  You should report the overall cost of a minimum spanning tree --- an integer, which may or may not be negative --- in the box below. 
#
#IMPLEMENTATION NOTES: This graph is small enough that the straightforward O(mn) time implementation of Prim's algorithm should work fine. OPTIONAL: For those of you seeking an additional challenge, try implementing a heap-based version. The simpler approach, which should already give you a healthy speed-up, is to maintain relevant edges in a heap (with keys = edge costs).  The superior approach stores the unprocessed vertices in the heap, as described in lecture.  Note this requires a heap that supports deletions, and you'll probably need to maintain some kind of mapping between vertices and their positions in the heap.
import random


def get_data():
	with open("edges.txt") as f:
		content = f.readlines()
		content = [x.strip('\n') for x in content]
		graph = defaultdict(list)
		for line in content:
			line_entries = line.split()
			parent_vtx = int(line_entries[0])
			for target, dist in (l.split(',') for l in line_entries[1:]):
				graph[parent_vtx].append((int(target), int(dist)))
		return graph


def prim_mst_classic_impl(graph):
    paths = {} # computed shortest path distances from start vertex
    queue = [(0, start_vtx)]
    visited = set()
    
    all_verticies = graph.keys()
    start_vtx = random.choice(all_verticies)


def prim_mst_heap_impl(graph):
    all_verticies = graph.keys()
    start_vtx = random.choice(all_verticies)
    while queue:
        current_vtx_dist, current_vtx = heapq.heappop(queue)
        if current_vtx == target_vtx: 
            break
        visited.add(current_vtx)
        for neighbor, dist in graph[current_vtx]:
            if neighbor not in visited:
                new_dist = current_vtx_dist + dist
                if new_dist < paths.get(neighbor, float('inf')):
                    paths[neighbor] = new_dist
                    heapq.heappush(queue, (new_dist, neighbor))
    return paths.get(target_vtx, float('inf'))

if __name__ == '__main__':
    pass