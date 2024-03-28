import sys
from typing import List

sys.path.append("/home/samanth/Code/DSA/01-Python_DSA/")
from data_structures.Graph import Graph, Node, DirectedEdge
flow = 0

def augmentPath(edgeList: List[DirectedEdge]):
    minCapacity = float('inf')
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
    sourceNode.state['visited'] = True

    iterations = 0
    while True:
        iterations+=1
        print(f"Iteration {iterations}")
        toExploreQueue = []
        exploringEdges = []
        graph.initializeNodes()
        sourceNode.state["visited"] = True
        toExploreQueue.append([sourceNode, sourceNode.getEdges().copy()])

        while toExploreQueue:
            # print([node.state['visited'] for node in graph.getNodes().values()])
            # print(f"Exploring edges: {exploringEdges}, toExploreQueue: {toExploreQueue}, flow: {flow}")
            currentTask = toExploreQueue[-1]
            # print(f"Current Task: {currentTask}")
            currentNode: Node = currentTask[0]
            edgesToExplore = currentTask[1]
            # print(f"Edges to explore {edgesToExplore}")

            edgesToExploreCopy = edgesToExplore[:]
            # print(f"Edges to explore copy {edgesToExploreCopy}")
            for currentEdge in edgesToExploreCopy:
                # print(f"Current Edge capacity: {currentEdge.capacity}")
                # print(f"\nAnalysing edge: {currentEdge}")
                if currentEdge.capacity <= 0:
                    # print(f"edgesToExplore before: {edgesToExplore}")
                    edgesToExplore.remove(currentEdge)
                    # print(f"{currentEdge} is full. Removing")
                    # print(f"edgesToExplore after: {edgesToExplore}")
                    continue
                else:

                    newNode = currentNode.traverse(currentEdge)[0]
                    if newNode.state['visited']==True:
                        edgesToExplore.remove(currentEdge)
                        # print(f"{currentEdge} already used to visit node{newNode.id}. Removing")

                        continue
                    newNode.state['visited'] = True
                    toExploreQueue.append([newNode, newNode.getEdges().copy()])
                    # print("Adding new entry to toExploreQueue")
                    # print(f"Added edge: {currentEdge}")

                    exploringEdges.append(currentEdge)
                    # print("breaking after appending Queue")
                    break
            else:
                # print(f"\nPopping entry, edgesToExplore is {edgesToExplore}\n")

                # print(f"Current Task: {currentTask}")
                # print(f"edgesToExplore: {edgesToExplore}")
                toExploreQueue[-1] = currentTask
                if edgesToExplore == []:
                    # print("Popping\n")
                    # print(f"ToExploreQueue before: {toExploreQueue}")
                    toExploreQueue.pop()
                    # print(f"ToExploreQueue after: {toExploreQueue}")
                    if not toExploreQueue:
                        print("\n\n\n\n\nThis should be printed if empty")
                        print(f"Returning value of {flow}")
                        return flow

            if newNode == sinkNode:
                print(f"Flow before is {flow}")
                print(f"Path taken(Before augmentation): {exploringEdges}")
                augmentValue = augmentPath(exploringEdges)
                print("\nAugmenting Path. Recieved Value of ", augmentValue, "\n")
                print(f"Path taken(After Augmentation): {exploringEdges}\n\n")

                flow = flow + augmentValue
                print("Flow is now: ", flow, "\n\n")
                exploringEdges = []  # Reset the exploringEdges list
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



#Mine
# if __name__ == "__main__":
#     # Create a graph
#     graph = Graph()

#     # Create nodes
#     # for i in range(6):
#     # graph.addNodes([Node(i) for i in range(7)])

#     # Create edges with capacities
#     graph.addNodes([Node(i) for i in range(6)])
#     graph.augmentedPathPairByID(0, 1, 10)
#     graph.augmentedPathPairByID(0, 2, 20)
#     graph.augmentedPathPairByID(1, 2, 5)
#     graph.augmentedPathPairByID(1, 3, 15)
#     graph.augmentedPathPairByID(2, 4, 35)
#     graph.augmentedPathPairByID(4, 3, 5)
#     graph.augmentedPathPairByID(3, 5, 20)
#     graph.augmentedPathPairByID(4, 5, 15)
#     # graph.augmentedPathPairByID(2, 1, 4)

#     # # graph.augmentedPathPairByID(2, 1, 4)
#     # graph.augmentedPathPairByID(2, 4, 14)
#     # # graph.augmentedPathPairByID(3, 2, 9)
#     # graph.augmentedPathPairByID(3, 5, 20)
#     # graph.augmentedPathPairByID(4, 3, 7)
#     # graph.augmentedPathPairByID(4, 5, 4)
#     # max_flow = fordFulkerson(graph, 0, 5)
#     # assert max_flow == 23
#     # print(f"Flow value is: {max_flow}")


#     # Run Ford-Fulkerson algorithm
#     print(f"Flow value is: {fordFulkerson(graph, 0, 5)}")
#     print(graph.getNodeByID(1).getEdges())
#     print(graph.getNodeByID(2).getEdges())








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



if __name__ == "__main__":
    graph = Graph()
    graph.addNodes([Node(i) for i in range(6)])
    graph.augmentedPathPairByID(0, 1, 16)
    graph.augmentedPathPairByID(0, 2, 13)
    graph.augmentedPathPairByID(1, 2, 10)
    graph.augmentedPathPairByID(1, 3, 12)
    # graph.augmentedPathPairByID(2, 1, 4)
    graph.augmentedPathPairByID(2, 4, 14)
    graph.augmentedPathPairByID(3, 2, 9)
    graph.augmentedPathPairByID(3, 5, 20)
    graph.augmentedPathPairByID(4, 3, 7)
    graph.augmentedPathPairByID(4, 5, 4)
    max_flow = fordFulkerson(graph, 0, 5)
    print(f"Flow value is: {max_flow}")