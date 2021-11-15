import heapq
from collections import defaultdict


def load_graph():
	with open("dijkstraData.txt") as f:
		content = f.readlines()
		content = [x.strip('\n') for x in content]
		graph = defaultdict(list)
		for line in content:
			line_entries = line.split()
			parent_vtx = int(line_entries[0])
			for target, dist in (l.split(',') for l in line_entries[1:]):
				graph[parent_vtx].append((int(target), int(dist)))
		return graph

def dijkstra_shortest_path(graph, start_vtx, target_vtx):
    paths = {} # computed shortest path distances from start vertex
    queue = [(0, start_vtx)]
    visited = set()
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
    graph = load_graph()
    start_vertex = 1
    target_verticies = (7, 37, 59, 82, 99, 115, 133, 165, 188, 197)
    for target_vertex in target_verticies:
        print('shortest path={} from={} to={}'.format(dijkstra_shortest_path(graph, start_vertex, target_vertex), start_vertex, target_vertex))

    # shortest path=2599 from=1 to=7
    # shortest path=2610 from=1 to=37
    # shortest path=2947 from=1 to=59
    # shortest path=2052 from=1 to=82
    # shortest path=2367 from=1 to=99
    # shortest path=2399 from=1 to=115
    # shortest path=2029 from=1 to=133
    # shortest path=2442 from=1 to=165
    # shortest path=2505 from=1 to=188
    # shortest path=3068 from=1 to=197