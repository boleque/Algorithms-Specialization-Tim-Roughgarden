from disjoint_set import DisjointSet


def maximum_spacing(edges_sorted, clusters):
    max_spacing = -1
    for node1, node2, cost in edges_sorted:
        node1_cluster = clusters.get_node_by_id(node1)
        node2_cluster = clusters.get_node_by_id(node2)
        if clusters.find(node1_cluster) != clusters.find(node2_cluster):
            max_spacing = cost
            break
    return max_spacing

def k_clustering(edges_sorted, k=4):
    disjoint_set = DisjointSet()
    # initially put every node into separate cluster
    for node1, node2, _cost in edges_sorted:
        disjoint_set.make_set(node1)
        disjoint_set.make_set(node2)

    edges_sorted_iter = iter(edges_sorted)
    while disjoint_set.sets_counter > k:
        node1, node2, _cost = next(edges_sorted_iter)
        node1_cluster = disjoint_set.get_node_by_id(node1)
        node2_cluster = disjoint_set.get_node_by_id(node2)
        disjoint_set.union(node1_cluster, node2_cluster)
    return disjoint_set

def get_data():
    with open("clustering1.txt") as f:
        edges = []
        lines = iter(f.readlines())
        number_of_nodes = int(next(lines))       
        for line in lines:
            vertex, neighbor, cost = [int(v) for v in line.split()]
            edges.append((vertex, neighbor, cost))
        edges_sorted = sorted(edges, key=lambda x: x[2])
        return number_of_nodes, edges_sorted


if __name__ == '__main__':
    number_of_nodes, edges_sorted = get_data()
    clusters = k_clustering(edges_sorted)
    max_spacing = maximum_spacing(edges_sorted, clusters)
    # 106