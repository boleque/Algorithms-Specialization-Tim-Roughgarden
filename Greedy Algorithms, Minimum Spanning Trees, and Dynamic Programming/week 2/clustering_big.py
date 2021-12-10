from disjoint_set import DisjointSet

#[# of nodes] [# of bits for each node's label]
#[first bit of node 1] ... [last bit of node 1]
#[first bit of node 2] ... [last bit of node 2]

def filter_node_within_distance(distance, bits_number, nodes):
    pass

def get_data():
    with open("clustering_big.txt") as f:
        nodes = {}
        lines = iter(f.readlines())
        bits_and_nodes_info_str = next(lines)
        nodes_number, bits_number = [int(v) for v in bits_and_nodes_info_str.split()]      
        for node, bit_distance in enumerate(lines, 1):
            nodes[bit_distance] = node
        return nodes_number, bits_number, nodes
        
if __name__ == '__main__':
    get_data()