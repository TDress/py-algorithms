from lib.assertion import equals

from heapq import heappop, heappush, heapify

class Graph:
    def __init__(self):
        self.nodes = []

# Adjacency list implementation.  Useful if you want the representation to 
# maintain information about node ordering, where lookup of adjacent node by
# posistion in the list could be important.  Otherwise adjacency map is superior.
class NodeAdjacencyList:
    __slots__ = 'value', 'children'

    def __init__(self, value, graph):
        self.value = value
        graph.nodes.append(self)
        # Children elements are destination nodes adjacent to this node.
        self.children = []

    def __hash__(self):
        return hash(id(self))

# Adjacency Map implementation.  Constant time lookup in set, where nodes are keys.
class NodeAdjacencyMap:
    __slots__ = 'value', 'children'

    def __init__(self, value, graph):
        self.value = value
        graph.nodes.append(self)
        self.children = set()

    def __repr__(self):
        return self.value

    def __hash__(self):
        return hash(id(self))

    # simple comparison using node values
    def __lt__(a, b):
        return a.value < b.value
    def __gt__(a, b):
        return a.value > b.value


def explore(node, visited):
    visited.add(node)
    for n in node.children:
        if not n in visited:
            explore(n, visited)


def dfs(G, visited):
    if not isinstance(G, Graph):
        raise TypeError('argument is not a valid graph')

    for node in G.nodes:
        if not node in visited:
            explore(node, visited)

#These functions for getting connected components of a graph only work
# for undirected graphs.  Directed is more complicated
def explore_connected_component(node, visited, ccs, ccs_count):
    """Modified version of explore function, for counting connected components"""
    visited.add(node)
    ccs[node] = ccs_count
    for c in node.children:
        if not c in visited:
            explore_connected_component(c, visited, ccs, ccs_count)

def get_connected_components(G, visited, ccs):
    """Get the connected components of the graph.  Modified dfs implementation.

    :dict ccs: mapping of nodes to connected component numbers.
    """
    ccs_count = 0
    for node in G.nodes:
        if not node in visited:
            ccs_count += 1
            explore_connected_component(node, visited, ccs, ccs_count)

    return ccs_count

def is_cyclic_explore(node, visited, path):
    # previsit
    path.add(node)
    visited.add(node)

    for c in node.children:
        if (c in path 
            or (not c in visited and is_cyclic_explore(c, visited, path))):
            # The node has already been seen or a recursive call fails
            return True

    path.remove(node)
    return False

def is_cyclic(G, visited):
    path = set()
    for node in G.nodes:
        if not node in visited:
            if is_cyclic_explore(node, visited, path):
                return True

    return False

# NOTE: THIS IS AN INEFFICIENT IMPLEMENTATION OF DIJKSTRAS SHORTEST PATH
# BECAUSE THE HEAPQ MODULE DOESN'T HAVE A REDUCEKEY METHOD THAT DOES
# LOGN BUBBLING OF A SINGLE ITEM.  WE HAVE TO RE-HEAPIFY EVERY TIME THE
# PRIORITY OF AN ITEM CHANGES AND SO THE ALGO RUN TIME IS O(V**2) INSTEAD
# OF WHAT IT SHOULD BE: O(VLOGV)
def dijkstra(G, start, dist, prev):
    """shortest path algorithm

    :param Graph G: graph to traverse
    :param NodeAdjacencyList start: node to start at
    :param dict dist: a mapping of nodes to distances from the starting node
    :param dict prev: a mapping of nodes to the previous node along the 
        shortest path to that node from the starting node.
    """
    int_max = (1 << 32) - 1
    dist, prev = dict.fromkeys(G.nodes, int_max), dict.fromkeys(G.nodes)
    dist[start] = 0
    pq, visited = [(0, start)], set()

    while len(pq) > 0:
        distance, node = heappop(pq)
        for weight, child in node.children:
            if distance + weight < dist[child]:
                prev[child] = node
                dist[child] = distance + weight
                if child not in visited:
                    heappush(pq, (dist[child], child))
                    visited.add(child)


def main():
    graph = Graph()

    nodeA = NodeAdjacencyMap('A', graph)
    nodeB = NodeAdjacencyMap('B', graph)
    nodeC = NodeAdjacencyMap('C', graph)
    nodeD = NodeAdjacencyMap('D', graph)
    nodeE = NodeAdjacencyMap('E', graph)
    nodeF = NodeAdjacencyMap('F', graph)
    nodeG = NodeAdjacencyMap('G', graph)
    nodeH = NodeAdjacencyMap('H', graph)

    nodeA.children.add(nodeB)
    nodeB.children.add(nodeC)
    nodeC.children.add(nodeD)
    nodeC.children.add(nodeE)
    nodeC.children.add(nodeH)
    nodeF.children.add(nodeE)
    nodeG.children.add(nodeH)
    nodeH.children.add(nodeF)
    nodeH.children.add(nodeA)

    # C has three outgoing edges
    equals(3, len(nodeC.children))
    # G doesn't have any incoming edges 
    all_children = (nodeA.children | nodeB.children | nodeC.children 
                    | nodeD.children | nodeE.children | nodeF.children 
                    | nodeG.children | nodeH.children)
    equals(False, nodeG in all_children)
    
    visited = set()
    explore(nodeA, visited)
    equals(False, nodeG in visited)
    equals(all_children, visited)
    
    visited.clear()
    explore(nodeG, visited)
    equals(set([nodeG]) | all_children, visited)

    visited.clear()
    explore(nodeF, visited)
    equals(set([nodeE, nodeF]), visited)

    # Find connected components in an undirected graph.  
    u_graph = Graph()
    nodeI = NodeAdjacencyMap('I', u_graph)
    nodeJ = NodeAdjacencyMap('J', u_graph)
    nodeK = NodeAdjacencyMap('K', u_graph)
    nodeL = NodeAdjacencyMap('L', u_graph)
    
    nodeI.children.add(nodeJ)
    nodeJ.children.add(nodeI)
    ccs = {}
    visited = set()

    ccs_count = get_connected_components(u_graph, visited, ccs)
    #There should be 3 connected components and one of them should have both I and J
    equals(3, ccs_count)
    equals(True, ccs[nodeI] == ccs[nodeJ])

    # Test for cycle in directed graph
    equals(True, is_cyclic(graph, set()))
    nodeB.children.clear()
    equals(False, is_cyclic(graph, set()))
    
    # test Dijkstra's shortest path
    graph_weighted = Graph()
    nodeA = NodeAdjacencyMap('A', graph_weighted)
    nodeB = NodeAdjacencyMap('B', graph_weighted)
    nodeC = NodeAdjacencyMap('C', graph_weighted)
    nodeD = NodeAdjacencyMap('D', graph_weighted)
    nodeE = NodeAdjacencyMap('E', graph_weighted)
    nodeF = NodeAdjacencyMap('F', graph_weighted)
    nodeG = NodeAdjacencyMap('G', graph_weighted)
    nodeH = NodeAdjacencyMap('H', graph_weighted)

    nodeA.children.add((2, nodeB))
    nodeB.children.add((2, nodeC))
    nodeC.children.add((5, nodeD))
    nodeC.children.add((2, nodeE))
    nodeC.children.add((3, nodeH))
    nodeF.children.add((4, nodeE))
    nodeG.children.add((2, nodeH))
    nodeH.children.add((6, nodeF))
    nodeH.children.add((2, nodeA))

    dist, prev = {}, {}
    # what's the shortest path from G to E
    dijkstra(graph_weighted, nodeG, dist, prev)
                 
if __name__ == "__main__":
    main()
