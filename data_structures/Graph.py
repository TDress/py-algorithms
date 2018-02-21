from lib.assertion import equals

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


def dfs(node, visited):
    if not isinstance(node, NodeAdjacencyMap):
        raise TypeError('argument is not a valid node')
    visited.add(node)
    for n in node.children:
        if not n in visited:
            dfs(n, visited)



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
    dfs(nodeA, visited)
    equals(False, nodeG in visited)
    equals(all_children, visited)
    
    visited.clear()
    dfs(nodeG, visited)
    equals(set([nodeG]) | all_children, visited)

    visited.clear()
    dfs(nodeF, visited)
    equals(set([nodeE, nodeF]), visited)
                 
if __name__ == "__main__":
    main()
