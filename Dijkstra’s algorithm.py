# Dijkstra's Algorithm in Python
from collections import defaultdict

class Node_Dist:
    def __init__(self, name, dist) :
        self.name = name
        self.dist = dist

class DijkstraAlgorithm:

    def __init__(self, node_count) :
        self.adjacentlist = defaultdict(list)
        self.node_count = node_count

    def Adjacent_nodelist(self, src, node_dist) :
        self.adjacentlist[src].append(node_dist)

    def Dijkstras_Shortest_Path(self, source_node) :
        # Initialize the nodes with infinite value and source
        # node with 0
        dist = [999999999999] * self.node_count
        dist[source_node] = 0

        # we are creating a dict as said in the alogrithm with the
        # value pair <node, dist>
        dict_of_node_dist = {source_node: 0}

        while dict_of_node_dist :

            # Now, we are going to assing a pair <node, dist> to a
            # current_source_node but condition that dist value
            # should be the minimum value
            current_source_node = min(dict_of_node_dist,
                                      key = lambda k: dict_of_node_dist[k])

            # After assign that pair to the current_source_node,
            # delete that item from the dict
            del dict_of_node_dist[current_source_node]

            for node_dist in self.adjacentlist[current_source_node] :
                adjacentNode = node_dist.name
                source_to_adjacentNode_dist = node_dist.dist

                # We are doing here edge relaxation of the adjacent node
                if dist[adjacentNode] > dist[current_source_node] + \
                        source_to_adjacentNode_dist :
                    dist[adjacentNode] = dist[current_source_node] + \
                                         source_to_adjacentNode_dist
                    dict_of_node_dist[adjacentNode] = dist[adjacentNode]

        for i in range(self.node_count) :
            print("Distance From Source Node ("+str(source_node)+")  => to "
                        "Destination Node(" + str(i) + ")  => " + str(dist[i]))

def main() :
    graph = DijkstraAlgorithm(6)
    graph.Adjacent_nodelist(0, Node_Dist(1, 5))
    graph.Adjacent_nodelist(0, Node_Dist(2, 1))
    graph.Adjacent_nodelist(0, Node_Dist(3, 4))

    graph.Adjacent_nodelist(1, Node_Dist(0, 5))
    graph.Adjacent_nodelist(1, Node_Dist(2, 3))
    graph.Adjacent_nodelist(1, Node_Dist(4, 8))

    graph.Adjacent_nodelist(2, Node_Dist(0, 1))
    graph.Adjacent_nodelist(2, Node_Dist(1, 3))
    graph.Adjacent_nodelist(2, Node_Dist(3, 2))
    graph.Adjacent_nodelist(2, Node_Dist(4, 1))

    graph.Adjacent_nodelist(3, Node_Dist(0, 4))
    graph.Adjacent_nodelist(3, Node_Dist(2, 2))
    graph.Adjacent_nodelist(3, Node_Dist(4, 2))
    graph.Adjacent_nodelist(3, Node_Dist(5, 1))

    graph.Adjacent_nodelist(4, Node_Dist(1, 8))
    graph.Adjacent_nodelist(4, Node_Dist(2, 1))
    graph.Adjacent_nodelist(4, Node_Dist(3, 2))
    graph.Adjacent_nodelist(4, Node_Dist(5, 3))

    graph.Adjacent_nodelist(5, Node_Dist(3, 1))
    graph.Adjacent_nodelist(5, Node_Dist(4, 3))

    graph .Dijkstras_Shortest_Path(0)


if __name__ == "__main__" :
   main()
