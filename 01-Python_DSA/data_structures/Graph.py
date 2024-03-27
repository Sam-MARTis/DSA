from typing import List, Tuple
from collections import deque
from abc import ABC


class Edge:
    def __init__(self, weight: int = 1, state: dict = dict()) -> None:
        self.weight = weight
        self.state = state


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
        self, node1: Node, node2: Node, weight: int = 1, state: dict = None
    ) -> None:
        super().__init__(weight, state)
        self.nodes: List[Node] = [node1, node2]
        # self.weight = weight
        # self.state = state

    def traverse(self, currentNode: Node) -> Tuple[Node, int]:
        assert (
            currentNode in self.nodes
        ), "This undirected edge doesn't connect the current node"
        return (
            self.nodes[1] if self.nodes[0] == currentNode else self.nodes[0],
            self.weight,
        )


class DirectedEdge(Edge):
    def __init__(
        self,
        fromNode: Node,
        toNode: Node,
        weight: int = 1,
        isAugmentedEdge: bool = False,
        state: dict = None,
    ) -> None:
        super().__init__(weight, state)
        self.fromNode: Node = fromNode
        self.toNode: Node = toNode
        self.isAugmentedEdge = isAugmentedEdge
        # self.weight = weight
        # self.state = state

    def traverse(self, currentNode: Node) -> tuple:
        assert (
            currentNode == self.fromNode
        ), "This directed edge doesn't start from the current node"
        return (self.toNode, self.weight)


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

    def makeDirectedEdge(self, fromNode: Node, toNode: Node, weight: int = 1) -> None:
        edge = DirectedEdge(fromNode, toNode, weight)
        fromNode.addEdge(edge)

    def makeUndirectedEdge(self, node1: Node, node2: Node, weight: int = 1) -> None:
        edge = UndirectedEdge(node1, node2, weight)
        node1.addEdge(edge)
        node2.addEdge(edge)

    def makeDirectedEdgeByID(
        self, fromNodeID, toNodeID, weight: int = 1, isAugmentedEdge: bool = False
    ) -> None:
        fromNode: Node = self.nodes[fromNodeID]
        toNode: Node = self.nodes[toNodeID]

        edge = DirectedEdge(fromNode, toNode, weight, isAugmentedEdge=isAugmentedEdge)
        fromNode.addEdge(edge)

    def makeUndirectedEdgeByID(
        self, Node1ID, Node2ID, weight: int = 1, isAugmentedEdge: bool = False
    ) -> None:
        node1: Node = self.nodes[Node1ID]
        node2: Node = self.nodes[Node2ID]

        edge = UndirectedEdge(node1, node2, weight, isAugmentedEdge=isAugmentedEdge)
        node1.addEdge(edge)
        node2.addEdge(edge)


# class FordFulkerson:
#     def __init__(self, graph: Graph, source: Node, sink: Node):
#         self.graph = graph
#         self.source = source
#         self.sink = sink
#         self.max_flow = 0

#     def has_augmenting_path(self, parent_map):
#         visited = {node: False for node in self.graph.nodes.values()}
#         queue = deque([self.source])
#         visited[self.source] = True

#         while queue:
#             current_node = queue.popleft()

#             for edge in current_node.edges:
#                 residual_node, capacity = current_node.traverse(edge)

#                 if not visited[residual_node] and capacity > 0:
#                     parent_map[residual_node] = (current_node, edge)
#                     if residual_node == self.sink:
#                         return True

#                     queue.append(residual_node)
#                     visited[residual_node] = True

#         return False

#     def compute_max_flow(self):
#         parent_map = {}
#         paths = []  # List to store the nodes in each augmenting path

#         while self.has_augmenting_path(parent_map):
#             path_flow = float("Inf")
#             s = self.sink
#             path_nodes = []  # List to store the nodes in the current augmenting path

#             while s != self.source:
#                 node, edge = parent_map[s]
#                 _, capacity = node.traverse(edge)
#                 path_flow = min(path_flow, capacity)
#                 path_nodes.append(node)  # Add the node to the current path
#                 s = node

#             path_nodes.append(self.source)  # Add the source to the current path
#             paths.append(path_nodes)  # Add the current path to the paths list

#             self.max_flow += path_flow

#             v = self.sink
#             while v != self.source:
#                 node, edge = parent_map[v]
#                 _, capacity = node.traverse(edge)
#                 if isinstance(edge, DirectedEdge):
#                     edge.weight -= path_flow
#                 else:
#                     if edge.nodes[0] == node:
#                         edge.weight -= path_flow
#                     else:
#                         edge.weight += path_flow
#                 v = node

#         return self.max_flow, paths
