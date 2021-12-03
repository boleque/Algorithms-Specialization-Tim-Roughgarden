#This file describes a distance function (equivalently, a complete graph with edge costs).  
#It has the following format:
#
#[number_of_nodes]
#
#[edge 1 node 1] [edge 1 node 2] [edge 1 cost]
#
#[edge 2 node 1] [edge 2 node 2] [edge 2 cost]
#
#There is one edge (i,j)(i,j)(i,j) for each choice of 1≤i<j≤n1 \leq i \lt j \leq n1≤i<j≤n, where nnn is the number of nodes.
#For example, the third line of the file is "1 3 5250", indicating that the distance between nodes 1 and 3 (equivalently, the cost of the edge (1,3)) is 5250.  You can assume that distances are positive, but you should NOT assume that they are distinct.
#Your task in this problem is to run the clustering algorithm from lecture on this data set, where the target number kkk of clusters is set to 4.  What is the maximum spacing of a 4-clustering?
#ADVICE: If you're not getting the correct answer, try debugging your algorithm using some small test cases.  And then post them to the discussion forum!



def get_data():
    with open("clustering1.txt") as f:
        edges = []
        lines = iter(f.readlines())
        number_of_nodes = int(next(lines))       
        for line in lines:
            vertex, neighbor, cost = [int(v) for v in line.split()]
            edges.append((vertex, neighbor, cost))
        return number_of_verticies, edges