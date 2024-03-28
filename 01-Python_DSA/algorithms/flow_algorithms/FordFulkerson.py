import sys
from typing import List

sys.path.append("/home/samanth/Code/DSA/01-Python_DSA/")
from data_structures.Graph import Graph, Node, DirectedEdge


# def DFS(graph: Graph, startID, endID) -> bool:
#     Nodes = graph.getNodes().copy()
#     StartNode: Node = Nodes[startID]
#     weight = 0
#     edgesTaken = []

#     queueToExplore = [[startID, StartNode.getEdges()]]  # Node ID, unexplored edges
#     while len(queueToExplore) > 0:
#         currentItem = queueToExplore[-1]
#         currentNode: Node = Nodes[currentItem[0]]
#         currentNodeEdges = currentItem[1]

#         if currentNode.id == endID:
#             return [
#                 [items[0] for items in queueToExplore],
#                 [edge for edge in edgesTaken],
#                 weight,
#             ]

#         if currentNodeEdges == [] or currentNodeEdges == [[]]:
#             queueToExplore.pop()
#             continue
#         for edge in currentNodeEdges:
#             newNode: Node = currentNode.traverse(edge)[0]
#             if newNode.state["visited"] == False:
#                 newNode.state["visited"] = True
#                 queueToExplore.append([newNode.id, newNode.getEdges()])
#                 weight += edge.capacity
#                 edgesTaken.append(edge)
#                 break
#             else:
#                 currentNodend(edge)
#                 break
#             else:
#                 currentNodeEdges.remove(edge)
#                 edgesTaken.remove(edge)
#                 weight -= edge.capacity
#     else:
#         return None

def augmentPath(edgeList: List[DirectedEdge]):
    minCapacity = float('inf')
    for edge in edgeList:
        edgeCapacity = edge.capacity
        if edgeCapacity < minCapacity:
            minCapacity = edgeCapacity
    for edge in edgeList:
        edge.capacitySetTo(edge.capacity - minCapacity)
    return minCapacity


def fordFulkerson(graph: Graph, sourceNodeID: int, sinkNodeID: int) -> int:
    flow = 0
    # Nodes = graph.getNodes()
    sourceNode: Node = graph.getNodeByID(sourceNodeID)
    sinkNode: Node = graph.getNodeByID(sinkNodeID)
    sourceNode.state['visited'] = True

    iterations = 0
    while True:
        iterations+=1
        print(f"Iteration {iterations}")
        toExploreQueue = []
        exploringEdges = []
        graph.initializeNodes()
        toExploreQueue.append([sourceNode, sourceNode.getEdges().copy()])

        while toExploreQueue:
            print([node.state['visited'] for node in graph.getNodes().values()])
            # print(f"Exploring edges: {exploringEdges}, toExploreQueue: {toExploreQueue}, flow: {flow}")
            currentTask = toExploreQueue[-1]
            print(f"Current Task: {currentTask}")
            currentNode: Node = currentTask[0]
            edgesToExplore = currentTask[1]
            # print(f"Edges to explore {edgesToExplore}")

            edgesToExploreCopy = edgesToExplore[:]
            print(f"Edges to explore copy {edgesToExploreCopy}")
            for currentEdge in edgesToExploreCopy:
                # print(f"Current Edge capacity: {currentEdge.capacity}")
                print(f"Analysing edge: {currentEdge}")
                if currentEdge.capacity <= 0:
                    # print(f"edgesToExplore before: {edgesToExplore}")
                    edgesToExplore.remove(currentEdge)
                    print(f"{currentEdge} is full. Removing")
                    # print(f"edgesToExplore after: {edgesToExplore}")
                    continue
                newNode = currentNode.traverse(currentEdge)[0]
                if newNode.state['visited']==True:
                    edgesToExplore.remove(currentEdge)
                    print(f"{currentEdge} already used to visit node{newNode.id}. Removing")

                    continue
                newNode.state['visited'] = True
                toExploreQueue.append([newNode, newNode.getEdges()])
                print("Adding new entry to toExploreQueue")

                exploringEdges.append(currentEdge)
                print("breaking after appending Queue")
                break
            else:
                print(f"\nPopping entry, edgesToExplore is {edgesToExplore}\n")

            # print(f"Current Task: {currentTask}")
            # print(f"edgesToExplore: {edgesToExplore}")
                toExploreQueue[-1] = currentTask
                if edgesToExplore == []:
                    print("Popping\n")
                    print(f"ToExploreQueue before: {toExploreQueue}")
                    toExploreQueue.pop()
                    print(f"ToExploreQueue after: {toExploreQueue}")
                    if not toExploreQueue:
                        print("This should be printed if empty")
                        return flow

            if newNode == sinkNode:
                flow+=augmentPath(exploringEdges)
                print("Augmenting Path")
                break
      

        else:
            print(f'''
            No longer able to find a path from source to sink.
            Process complete
            The flow is {flow}
            The number of iterations is {iterations}
            ''')
            
            # break
            return flow 


# if __name__ == "__main__":
#     myGraph = Graph()
#     myGraph.addNodes([Node(i) for i in range(10)])
#     myGraph.augmentedPathPairByID(1, 2)
#     myGraph.augmentedPathPairByID(2, 3)

#     myGraph.augmentedPathPairByID(1, 4, 3)
#     myGraph.augmentedPathPairByID(4, 7, 2)
#     # print(DFS(myGraph, 1, 7))


if __name__ == "__main__":
    # Create a graph
    graph = Graph()

    # Create nodes
    # for i in range(6):
    graph.addNodes([Node(i) for i in range(7)])

    # Create edges with capacities
    graph.augmentedPathPairByID(0, 1, 16)

    graph.augmentedPathPairByID(0, 2, 5)
    graph.augmentedPathPairByID(2, 5, 10)
    graph.augmentedPathPairByID(1, 5, 12)
    graph.augmentedPathPairByID(1, 3, 10)
    graph.augmentedPathPairByID(3, 5, 20)


    # Run Ford-Fulkerson algorithm
    print(f"Flow value is: {fordFulkerson(graph, 1, 5)}")


# import unittest
# from data_structures.Graph import Graph, Node


# class TestFordFulkerson(unittest.TestCase):
#     def setUp(self):
#         self.graph = Graph()

#     def test_fordFulkerson_simple(self):
#         self.graph.addNodes([Node(i) for i in range(3)])
#         self.graph.augmentedPathPairByID(0, 1, 10)
#         self.graph.augmentedPathPairByID(1, 2, 5)
#         max_flow = fordFulkerson(self.graph, 0, 2)
#         self.assertEqual(max_flow, 5)

#     def test_fordFulkerson_complex(self):
#         self.graph.addNodes([Node(i) for i in range(6)])
#         self.graph.augmentedPathPairByID(0, 1, 16)
#         self.graph.augmentedPathPairByID(0, 2, 13)
#         self.graph.augmentedPathPairByID(1, 2, 10)
#         self.graph.augmentedPathPairByID(1, 3, 12)
#         self.graph.augmentedPathPairByID(2, 1, 4)
#         self.graph.augmentedPathPairByID(2, 4, 14)
#         self.graph.augmentedPathPairByID(3, 2, 9)
#         self.graph.augmentedPathPairByID(3, 5, 20)
#         self.graph.augmentedPathPairByID(4, 3, 7)
#         self.graph.augmentedPathPairByID(4, 5, 4)
#         max_flow = fordFulkerson(self.graph, 0, 5)
#         self.assertEqual(max_flow, 23)


# if __name__ == "__main__":
#     unittest.main()
