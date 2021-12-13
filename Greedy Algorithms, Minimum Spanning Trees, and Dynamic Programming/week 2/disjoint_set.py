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
        self.sets_counter = 0

    def make_set(self, unique_id):
        if unique_id in self.nodes_map:
            return False
        new_node = DisjointSet.Node(unique_id)
        new_node.leader = new_node
        self.nodes_map[new_node.unique_id] = new_node
        self.sets_counter += 1
        return True

    def get_node_by_id(self, unique_id):
        return self.nodes_map.get(unique_id)

    def find(self, node):
        while node != node.leader:
            node = node.leader
        return node

    def union(self, x_set, y_set):
        x_leader = self.find(x_set)
        y_leader = self.find(y_set)

        if x_leader == y_leader:
            return False

        if x_leader.rank < y_leader.rank:
            x_leader.leader = y_leader
        elif x_leader.rank > y_leader.rank:
            y_leader.leader = x_leader
        else:
            x_leader.leader = y_leader
            y_leader.rank += 1

        self.sets_counter -= 1
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
    result = disjoint_set.union(a_node_obj, b_node_obj)
    
    assert result == True
    assert b_node_obj.rank == 1 and a_node_obj.rank == 0 
    assert a_node_obj.leader == b_node_obj.leader

def join_sets_with_same_leaders():
    a_node_id = 'a'
    disjoint_set = DisjointSet()
    disjoint_set.make_set(a_node_id)
    a_node_obj = disjoint_set.get_node_by_id(a_node_id)
    result = disjoint_set.union(a_node_obj, a_node_obj)

    assert result == False

if __name__ == '__main__':
    create_set()
    join_sets_with_distinct_leaders()
    join_sets_with_same_leaders()
    # 6118