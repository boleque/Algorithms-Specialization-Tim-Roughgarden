# union by rank optimization is applied
# TBD: path compression optimization
class DisjointSet(object):

    class Node(object):
        def __init__(self, unique_id, leader=None, rank=0):   
            self.unique_id = unique_id
            self.leader = leader
            self.rank = rank

        def __repr__(self):
            return 'Node(id={} leader={} rank={})'.format(self.unique_id, self.leader.unique_id, self.rank)

    def __init__(self):
        self.nodes_map = {}

    def make_set(self, unique_id):
        new_node = DisjointSet.Node(unique_id)
        new_node.leader = new_node
        self.nodes_map[new_node.unique_id] = new_node
        return new_node

    def get_node_by_id(self, unique_id):
        return self.nodes_map.get(unique_id)

    @staticmethod
    def find(node):
        if node != node.leader:
            return DisjointSet.find(node.leader)
        return node

    @staticmethod
    def union(set1, set2):
        leader1 = DisjointSet.find(set1)
        leader2 = DisjointSet.find(set2)

        if leader1 == leader2:
            return False

        if leader1.rank == leader2.rank:
            leader1.leader = leader2
            leader2.rank += 1
        elif leader1.rank > leader2.rank:
            leader1.leader = leader2
        else:
            leader2.leader = leader1

        return True


def create_set():
    node_id = 'a'
    disjoint_set = DisjointSet()
    disjoint_set.make_set(node_id)
    node = disjoint_set.get_node_by_id(node_id)

    assert node.rank == 0 
    assert node.leader == node 
    assert node.unique_id == node_id

def join_sets_with_distinct_leaders():
    a_node_id = 'a'
    b_node_id = 'b'
    disjoint_set = DisjointSet()
    disjoint_set.make_set(a_node_id)
    disjoint_set.make_set(b_node_id)
    a_node_obj = disjoint_set.get_node_by_id(a_node_id)
    b_node_obj = disjoint_set.get_node_by_id(b_node_id)
    result = DisjointSet.union(a_node_obj, b_node_obj)
    
    assert result == True
    assert b_node_obj.rank == 1 and a_node_obj.rank == 0 
    assert a_node_obj.leader == b_node_obj.leader

def join_sets_with_same_leaders():
    a_node_id = 'a'
    disjoint_set = DisjointSet()
    disjoint_set.make_set(a_node_id)
    a_node_obj = disjoint_set.get_node_by_id(a_node_id)
    result = DisjointSet.union(a_node_obj, a_node_obj)

    assert result == False

if __name__ == '__main__':
    create_set()
    join_sets_with_distinct_leaders()
    join_sets_with_same_leaders()