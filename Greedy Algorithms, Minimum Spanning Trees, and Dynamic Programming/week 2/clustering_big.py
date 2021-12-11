from disjoint_set import DisjointSet

#[# of nodes] [# of bits for each node's label]
#[first bit of node 1] ... [last bit of node 1]
#[first bit of node 2] ... [last bit of node 2]

#The question is: what is the largest value of k such that there is a k-clustering 
#with spacing at least 3?  That is, how many clusters are needed to ensure that no pair 
#of nodes with all but 2 bits in common get split into different clusters?

def filter_nodes_by_distance_1(nodes_map, bits_number):
    for node in nodes_map:
        for i in range(0, bits_number):
            neighbor = node ^ 1 << i
            if neighbor in nodes_map:
                yield (node, neighbor)

def filter_nodes_by_distance_2(nodes_map, bits_number):
    for node in nodes_map:
        for i in range(0, bits_number):
            neighbor = node ^ 1 << i
            for j in range(1, bits_number):
                neighbor ^= 1 << j
                if neighbor in nodes_map:
                    yield (node, neighbor)

def clustering(nodes_map, bits_number):
    disjoint_set = DisjointSet()
    # initially put every node into separate cluster
    for node in nodes_map.itervalues():
        disjoint_set.make_set(node)
    
    for node, neighbor in filter_nodes_by_distance_1(nodes_map, bits_number):
        pass

    for node, neighbor in filter_nodes_by_distance_2(nodes_map, bits_number):
        pass


def get_data():
    with open("clustering_big.txt") as f:
        nodes_map = {}
        lines = iter(f.readlines())
        bits_and_nodes_info_str = next(lines)
        nodes_number, bits_number = [int(v) for v in bits_and_nodes_info_str.split()]      
        for node, bit_distance in enumerate(lines, 1):
            nodes_map[bit_distance] = node
        return nodes_number, bits_number, nodes_map
        
if __name__ == '__main__':
    get_data()