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


def fordFulkerson(graph: Graph, sourceNodeID: int, sinkNodeID: int):
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
            currentTask = toExploreQueue[-1]
            currentNode: Node = currentTask[0]
            edgesToExplore = currentTask[1]

            if edgesToExplore==[]:
                print("No more edges to explore")
                try:
                    exploringEdges.pop()
                except IndexError:
                    raise IndexError("ExploringEdges list was empty. Can't pop. Ensure that graph doesn't contain only one node")
                toExploreQueue.pop()
                continue
            edgesToExploreCopy = edgesToExplore[:]
            for currentEdge in edgesToExploreCopy:
                if currentEdge.capacity <= 0:
                    edgesToExplore.remove(currentEdge)
                    continue
                print(currentNode)
                # print(currentEdge)
                print(currentNode.traverse(currentEdge))
                newNode = currentNode.traverse(currentEdge)[0]
                if newNode.state['visited']==True:
                    edgesToExplore.remove(currentEdge)
                    continue
                newNode.state['visited'] = True
                toExploreQueue.append([newNode, newNode.getEdges()])
                exploringEdges.append(currentEdge)
                break
            if newNode == sinkNode:
                flow+=augmentPath(exploringEdges)
                # print()
                break
            print(f"ToExploreQueue: {toExploreQueue}")
        else:
            print(f'''
            No longer able to find a path from source to sink.
            Process complete
            The flow is {flow}
            The number of iterations is {iterations}
            ''')
            break
        


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
    graph.addNodes([Node(i) for i in range(6)])

    # Create edges with capacities
    graph.augmentedPathPairByID(0, 1, 16)
    graph.augmentedPathPairByID(0, 2, 13)
    graph.augmentedPathPairByID(1, 2, 10)
    graph.augmentedPathPairByID(1, 3, 12)
    graph.augmentedPathPairByID(2, 1, 4)
    graph.augmentedPathPairByID(2, 4, 14)
    graph.augmentedPathPairByID(3, 2, 9)
    graph.augmentedPathPairByID(3, 5, 20)
    graph.augmentedPathPairByID(4, 3, 7)
    graph.augmentedPathPairByID(4, 5, 4)

    # Run Ford-Fulkerson algorithm
    fordFulkerson(graph, 0, 5)

    # The maximum flow of this graph is known to be 23
    # assert graph.getNodeByID(5).incomingFlow() == 23, "The maximum flow is incorrect"

    # print("All tests passed!")
