import re
import sys
import time
from disjoint_set import DisjointSet
from collections import defaultdict
from itertools import combinations

#The question is: what is the largest value of k such that there is a k-clustering 
#with spacing at least 3?  That is, how many clusters are needed to ensure that no pair 
#of nodes with all but 2 bits in common get split into different clusters?

def hamming_1(bits_length, distance):
    for i in range(bits_length):
        mask = 1 << i
        yield distance ^ mask

def hamming_2(bits_length, distance):
    for i in range(bits_length):
        for j in range(i + 1, bits_length):
            mask = (1 << i) ^ (1 << j)
            yield distance ^ mask

def clustering(nodes_by_distance, bits_number):
    disjoint_set = DisjointSet()
    # initially put every node into separate cluster
    for nodes in nodes_by_distance.keys():
        disjoint_set.make_set(nodes)

    for distance in nodes_by_distance.keys():

        for neighbor in hamming_1(bits_number, distance):           
            if neighbor in nodes_by_distance:
                node1_cluster = disjoint_set.get_node_by_id(distance)
                node2_cluster = disjoint_set.get_node_by_id(neighbor)
                disjoint_set.union(node1_cluster, node2_cluster)

        for neighbor in hamming_2(bits_number, distance):    
            if neighbor in nodes_by_distance:
                node1_cluster = disjoint_set.get_node_by_id(distance)
                node2_cluster = disjoint_set.get_node_by_id(neighbor)
                disjoint_set.union(node1_cluster, node2_cluster)
    
    return disjoint_set

def get_data():
    with open("clustering_big.txt") as f:
        nodes_by_distance = defaultdict(list)
        lines = iter(f.readlines())
        bits_and_nodes_info_str = next(lines)
        nodes_number, bits_number = [int(v) for v in bits_and_nodes_info_str.split()]      
        for node, bit_distance in enumerate(lines, 1):
            # remove tab and spaces
            bit_distance = int(re.sub('\s+', '', bit_distance), 2)
            nodes_by_distance[bit_distance].append(node)
        return nodes_number, bits_number, nodes_by_distance

if __name__ == '__main__':
    nodes_number, bits_number, nodes_by_distance = get_data()
    disjoint_set = clustering(nodes_by_distance, bits_number)
    print(disjoint_set.sets_counter)
     # 6118