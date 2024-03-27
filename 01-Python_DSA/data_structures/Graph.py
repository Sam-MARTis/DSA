from typing import List, Tuple
from collections import deque
from abc import ABC


class Edge:
    def __init__(self, capacity: int = 1, state: dict = dict()) -> None:
        self.capacity = capacity
        self.state = state

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.capacity})"


class Node:
    def __init__(self, id, state: dict = {}) -> None:
        self.id = id
        self.edges = []
        self.state = {"visited": False}

    def addEdge(self, edgeToUse):
        self.edges.append(edgeToUse)

    def traverse(self, edge):
        return edge.traverse(self)

    def getEdgeTo(self, node: "Node"):
        for edge in self.edges:
            if self.traverse(edge)[0] == node:
                return edge
        return None

    # @getattr
    def getEdges(self):
        return self.edges


class UndirectedEdge(Edge):
    def __init__(
        self, node1: Node, node2: Node, capacity: int = 1, state: dict = None
    ) -> None:
        super().__init__(capacity, state)
        self.nodes: List[Node] = [node1, node2]
        # self.capacity = capacity
        # self.state = state

    def traverse(self, currentNode: Node) -> Tuple[Node, int]:
        assert (
            currentNode in self.nodes
        ), "This undirected edge doesn't connect the current node"
        return (
            self.nodes[1] if self.nodes[0] == currentNode else self.nodes[0],
            self.capacity,
        )


class DirectedEdge(Edge):
    def __init__(
        self,
        fromNode: Node,
        toNode: Node,
        capacity: int = 1,
        isAugmentedEdge: bool = False,
        state: dict = None,
    ) -> None:
        super().__init__(capacity, state)
        self.fromNode: Node = fromNode
        self.toNode: Node = toNode
        self.isAugmentedEdge = isAugmentedEdge
        # self.capacity = capacity
        # self.state = state

    def __repr__(self) -> str:
        return f"{self.fromNode.id} -{self.__class__.__name__}({self.capacity})-> {self.toNode.id}"

    def traverse(self, currentNode: Node) -> tuple:
        assert (
            currentNode == self.fromNode
        ), "This directed edge doesn't start from the current node"
        return (self.toNode, self.capacity)


class Graph:
    def __init__(self):
        self.nodes = {}
        self.source = None
        self.sink = None

    # @property
    def getNodes(self):
        return self.nodes

    def addNodes(self, nodesList: List[Node] = None):
        if nodesList is None:
            nodesList = []

        for node in nodesList:
            self.nodes[node.id] = node

    def makeDirectedEdge(self, fromNode: Node, toNode: Node, capacity: int = 1) -> None:
        edge = DirectedEdge(fromNode, toNode, capacity)
        fromNode.addEdge(edge)

    def makeUndirectedEdge(self, node1: Node, node2: Node, capacity: int = 1) -> None:
        edge = UndirectedEdge(node1, node2, capacity)
        node1.addEdge(edge)
        node2.addEdge(edge)

    def makeDirectedEdgeByID(
        self, fromNodeID, toNodeID, capacity: int = 1, isAugmentedEdge: bool = False
    ) -> None:
        fromNode: Node = self.nodes[fromNodeID]
        toNode: Node = self.nodes[toNodeID]

        edge = DirectedEdge(fromNode, toNode, capacity, isAugmentedEdge=isAugmentedEdge)
        fromNode.addEdge(edge)

    def makeUndirectedEdgeByID(
        self, Node1ID, Node2ID, capacity: int = 1, isAugmentedEdge: bool = False
    ) -> None:
        node1: Node = self.nodes[Node1ID]
        node2: Node = self.nodes[Node2ID]

        edge = UndirectedEdge(node1, node2, capacity, isAugmentedEdge=isAugmentedEdge)
        node1.addEdge(edge)
        node2.addEdge(edge)

    def augmentedPathPairByID(self, fromNodeID, toNodeID, capacity: int) -> None:
        fromNode: Node = self.nodes[fromNodeID]
        toNode: Node = self.nodes[toNodeID]
        edgeNormal = DirectedEdge(fromNode, toNode, capacity, isAugmentedEdge=False)
        edgeAugmented = DirectedEdge(toNode, fromNode, 0, isAugmentedEdge=True)
        max_capacity = capacity
        fromNode.addEdge([edgeNormal, edgeAugmented, max_capacity])
        toNode.addEdge([edgeAugmented, edgeNormal, max_capacity])

