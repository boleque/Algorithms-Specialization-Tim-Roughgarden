
import random

def choose_random_edge(graph):
    u = random.choice(list(graph.keys()))
    v = random.choice(graph[u])
    return u, v

def min_cut(graph):
	v = 0
	while len(graph) > 2:
		v, u = choose_random_edge(graph)
		contract(graph, v, u)
	return len(graph[v])

def contract(graph, v, u):
	for node in graph[u]:
		if node != v:
			graph[v].append(node) # merge all u's children to v
		graph[node].remove(u) 	  # remove merged vertex from all children
		if node != v:
			graph[node].append(v) # add vertex over removed vertex u
	del graph[u]	

if __name__ == "__main__":
    graph = {}
    with open('kargerMinCut.txt') as f:
        for ln in f:
            line = ln.split()
            if line:
                verticies = [int(x) for x in line]
                graph[verticies[0]] = verticies[1:]
