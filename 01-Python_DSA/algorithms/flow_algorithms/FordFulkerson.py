import sys
from typing import List

sys.path.append("/home/samanth/Code/DSA/01-Python_DSA/")
from data_structures.Graph import Graph, Node, DirectedEdge

flow = 0


def augmentPath(edgeList: List[DirectedEdge]):
    minCapacity = float("inf")
    if edgeList == []:
        raise ValueError("Edge list is empty")
    for edge in edgeList:
        edgeCapacity = edge.capacity
        if edgeCapacity < minCapacity:
            minCapacity = edgeCapacity
    for edge in edgeList:
        edge.capacitySetTo(edge.capacity - minCapacity)
    return minCapacity


def fordFulkerson(graph: Graph, sourceNodeID: int, sinkNodeID: int) -> int:
    global flow
    flow = 0
    # Nodes = graph.getNodes()
    sourceNode: Node = graph.getNodeByID(sourceNodeID)
    sinkNode: Node = graph.getNodeByID(sinkNodeID)
    sourceNode.state["visited"] = True

    iterations = 0
    while True:
        iterations += 1
        # print(f"Iteration {iterations}")
        toExploreQueue = []
        exploringEdges = []
        graph.initializeNodes()
        sourceNode.state["visited"] = True
        toExploreQueue.append([sourceNode, sourceNode.getEdges().copy()])

        while toExploreQueue:
            currentTask = toExploreQueue[-1]
            currentNode: Node = currentTask[0]
            edgesToExplore = currentTask[1]

            edgesToExploreCopy = edgesToExplore[:]
            for currentEdge in edgesToExploreCopy:
                if currentEdge.capacity <= 0:
                    edgesToExplore.remove(currentEdge)
                    continue
                else:

                    newNode = currentNode.traverse(currentEdge)[0]
                    if newNode.state["visited"] == True:
                        edgesToExplore.remove(currentEdge)

                        continue
                    newNode.state["visited"] = True
                    toExploreQueue.append([newNode, newNode.getEdges().copy()])

                    exploringEdges.append(currentEdge)
                    break
            else:
                toExploreQueue[-1] = currentTask
                if edgesToExplore == []:
                    try:
                        exploringEdges.pop()
                    except:
                        pass
                    toExploreQueue.pop()
                    if not toExploreQueue:
                        # print("\n\n\n\n\nThis should be printed if empty")
                        # print(f"Returning value of {flow}")
                        return flow

            if newNode == sinkNode:
                # print(f"Flow before is {flow}")
                # print(f"Path taken(Before augmentation): {exploringEdges}")
                augmentValue = augmentPath(exploringEdges)
                # print("\nAugmenting Path. Recieved Value of ", augmentValue, "\n")
                # print(f"Path taken(After Augmentation): {exploringEdges}\n\n")

                flow = flow + augmentValue
                # print("Flow is now: ", flow, "\n\n")
                exploringEdges = []  # Reset the exploringEdges list
                break

        else:
            print(
                f"""
            No longer able to find a path from source to sink.
            Process complete
            The flow is {flow}
            The number of iterations is {iterations}
            """
            )

            # break
            return flow


# if __name__ == "__main__":
#     graph = Graph()
#     graph.addNodes([Node(i) for i in range(6)])
#     graph.augmentedPathPairByID(0, 1, 16)
#     graph.augmentedPathPairByID(0, 2, 13)
#     graph.augmentedPathPairByID(1, 2, 10)
#     graph.augmentedPathPairByID(1, 3, 12)
#     # graph.augmentedPathPairByID(2, 1, 4)
#     graph.augmentedPathPairByID(2, 4, 14)
#     graph.augmentedPathPairByID(3, 2, 9)
#     graph.augmentedPathPairByID(3, 5, 20)
#     graph.augmentedPathPairByID(4, 3, 7)
#     graph.augmentedPathPairByID(4, 5, 4)
#     max_flow = fordFulkerson(graph, 0, 5)
#     print(f"Flow value is: {max_flow}")
import unittest
from fordFulkerson3 import Graph, Node


class TestFordFulkerson(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()
        self.graph.addNodes([Node(i) for i in range(8)])

    def test_flow(self):
        self.graph.augmentedPathPairByID(0, 1, 10)
        self.graph.augmentedPathPairByID(0, 2, 5)
        self.graph.augmentedPathPairByID(0, 3, 15)
        self.graph.augmentedPathPairByID(1, 4, 9)
        self.graph.augmentedPathPairByID(1, 5, 4)
        self.graph.augmentedPathPairByID(2, 1, 4)
        self.graph.augmentedPathPairByID(2, 5, 8)
        self.graph.augmentedPathPairByID(3, 6, 16)
        self.graph.augmentedPathPairByID(4, 7, 10)
        self.graph.augmentedPathPairByID(5, 7, 10)
        self.graph.augmentedPathPairByID(6, 2, 6)
        self.graph.augmentedPathPairByID(6, 7, 10)
        max_flow = fordFulkerson(self.graph, 0, 7)
        self.assertEqual(max_flow, 29)


if __name__ == "__main__":
    unittest.main()
