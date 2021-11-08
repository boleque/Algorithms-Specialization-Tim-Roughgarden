
import sys
import resource
from collections import defaultdict, Counter


resource.setrlimit(resource.RLIMIT_STACK, (2**30, -1))
sys.setrecursionlimit(10**6)


def dfs_topological_order(graph, vertex, visited):
    global node_time, finishing_times

    visited.add(vertex)
    for neighbor in graph.get(vertex, []):
        if neighbor not in visited:
            dfs_topological_order(graph, neighbor, visited)
    finishing_times[node_time] = vertex
    node_time -= 1

def dfs_scc(graph, vertex, visited):
    global leaders, current_leader

    leaders[current_leader].append(vertex)
    visited.add(vertex)
    for neighbor in graph.get(vertex, []):
        if neighbor not in visited:
            dfs_scc(graph, neighbor, visited)

def dfs_loop(graph, verticies, loop_fun):
    global current_leader, leaders

    current_leader = None
    visited = set()
    leaders = defaultdict(list)
    for vertex in verticies:
        if vertex not in visited:
            current_leader = vertex
            loop_fun(graph, vertex, visited)

def strong_components(graph, graph_reversed, nodes_num):
    global node_time, finishing_times

    node_time = nodes_num - 1
    finishing_times = [0] * nodes_num

    dfs_loop(graph_reversed, range(1, nodes_num), dfs_topological_order)
    dfs_loop(graph, finishing_times, dfs_scc)

def most_common(leader, x):
    results = [len(v) for k, v in leader.items()]

    return sorted(results, reverse=True)[: x]

def load_graph(filename):
    graph = {}
    graph_reversed = {}
    unique_nodes = set()
    with open(filename, 'r') as source:
        for line in source:
            values = line.split()
            if values:
                vertex = int(values[0])
                neighbor = int(values[1])

                neighbors = graph.setdefault(vertex, [])                
                neighbors.append(neighbor)

                neighbors_reversed = graph_reversed.setdefault(neighbor, [])
                neighbors_reversed.append(vertex)

                unique_nodes.add(vertex)
                unique_nodes.add(neighbor)
    return graph, graph_reversed, len(unique_nodes)

def five_largest_SCCs():
    global leaders

    graph, graph_reversed, nodes = load_graph("SCC.txt")
    SCCs = strong_components(graph, graph_reversed, nodes)
    return sorted([len(v) for k, v in leaders.items()], reverse=True)[:5]

if __name__ == '__main__':
    print('result: ', five_largest_SCCs())
    # 434821, 968, 459, 313, 211