from typing import List, Tuple


class Node:
    def __init__(self, id, state: dict = None) -> None:
        self.id = id
        self.edges = []
        self.state = state

    def addEdge(self, edgeToUse):
        self.edges.append(edgeToUse)

    def getEdges(self) -> list:
        return self.edges

    def getInfo(self):
        return (self.id, self.edges, self.state)
    
    def traverse(self, edge):
        return edge.traverse(self)
        


class UndirectedEdge:
    def __init__(
        self, node1: Node, node2: Node, weight: int = 1, state: dict = None
    ) -> None:
        self.nodes: List[Node] = [node1, node2]
        self.weight = weight
        self.state = state

    def traverse(self, currentNode: Node) -> Tuple[Node, int]:
        assert (
            currentNode in self.nodes
        ), "This undirected edge doesn't connect the current node"
        if self.nodes[0] == currentNode:
            return (self.nodes[1], self.weight)
        elif self.nodes[1] == currentNode:
            return (self.nodes[0], self.weight)

    def getInfo(self) -> tuple:
        return (self.nodes, self.weight, self.state)


class DirectedEdge:
    def __init__(
        self, fromNode: Node, toNode: Node, weight: int = 1, state: dict = None
    ) -> None:
        self.fromNode: Node = fromNode
        self.toNode: Node = toNode
        self.weight = weight
        self.state = state

    def traverse(self, currentNode: Node) -> tuple:
        assert (
            currentNode == self.fromNode
        ), "This directed edge doesn't start from the current node"
        return (self.toNode, self.weight)

    def getInfo(self) -> tuple:
        return ((self.fromNode, self.toNode), self.weight, self.state)


class Graph:
    def __init__(self):
        self.nodes= {}
        # self.directedEdges: List[DirectedEdge] = []
        # self.undirectedEdges: List[UndirectedEdge] = []
        self.source = None
        self.sink = None

    def addNodes(self, nodesList: List[Node] = None):
        if nodesList is None:
            nodesList = []
            
        for node in nodesList:
            self.nodes[node.id] = node
    def getNodes(self):
        return self.nodes

    def makeDirectedEdge(self, fromNode: Node, toNode: Node, weight: int = 1) -> None:
        assert fromNode in self.nodes.values(), "FromNode is not in graph nodes!"
        assert toNode in self.nodes.values(), "ToNode is not in graph nodes!"

        edge = DirectedEdge(fromNode, toNode, weight)
        fromNode.addEdge(edge)
        # toNode.addEdge(edge)

    def makeUndirectedEdge(self, node1: Node, node2: Node, weight: int = 1) -> None:
        assert node1 in self.nodes.values(), "Node1 is not in graph nodes!"
        assert node2 in self.nodes.values(), "Node2 is not in graph nodes!"

        edge = UndirectedEdge(node1, node2, weight)
        node1.addEdge(edge)
        node2.addEdge(edge)

    def makeDirectedEdgeByID(self, fromNodeID, toNodeID, weight: int = 1) -> None:
        assert fromNodeID in self.nodes.keys(), "FromNodeID is not in graph nodes!"
        assert toNodeID in self.nodes.keys(), "ToNodeID is not in graph nodes!"
        fromNode: Node = self.nodes[fromNodeID]
        toNode: Node = self.nodes[toNodeID]

        edge = DirectedEdge(fromNode, toNode, weight)
        fromNode.addEdge(edge)
        # toNode.addEdge(edge)

    def makeUndirectedEdgeByID(self, Node1ID, Node2ID, weight: int = 1) -> None:
        assert Node1ID in self.nodes.keys(), "FromNodeID is not in graph nodes!"
        assert Node2ID in self.nodes.keys(), "ToNodeID is not in graph nodes!"
        node1: Node = self.nodes[Node1ID]
        node2: Node = self.nodes[Node2ID]

        edge = UndirectedEdge(node1, node2, weight)
        node1.addEdge(edge)
        node2.addEdge(edge)
    def getID(self, nodeToFindIDOf: Node):
        if nodeToFindIDOf.id in self.nodes.keys():
            return nodeToFindIDOf.id
        else:
            return Warning("Node not in graph")
