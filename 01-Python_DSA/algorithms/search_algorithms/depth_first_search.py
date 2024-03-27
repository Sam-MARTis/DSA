import sys

sys.path.append("/home/samanth/Code/DSA/01-Python_DSA/")
from data_structures.Graph import Graph, Node


def DFS(graph: Graph, startID, endID) -> bool:
    Nodes = graph.getNodes().copy()
    StartNode: Node = Nodes[startID]
    weight = 0

    queueToExplore = [[startID, StartNode.getEdges()]]  # Node ID, unexplored edges
    while len(queueToExplore) > 0:
        currentItem = queueToExplore[-1]
        currentNode: Node = Nodes[currentItem[0]]
        currentNodeEdges = currentItem[1]

        if currentNode.id == endID:
            return [[items[0] for items in queueToExplore], weight]

        if currentNodeEdges == [] or currentNodeEdges == [[]]:
            queueToExplore.pop()
            continue
        for edge in currentNodeEdges:
            newNode: Node = currentNode.traverse(edge)[0]
            if newNode.state["visited"] == False:
                newNode.state["visited"] = True
                queueToExplore.append([newNode.id, newNode.getEdges()])
                weight += edge.weight
                break
            else:
                currentNodeEdges.remove(edge)
                weight -= edge.weight
    else:
        return None


if __name__ == "__main__":
    myGraph = Graph()
    myGraph.addNodes([Node(i) for i in range(5)])
    myGraph.makeDirectedEdgeByID(1, 2)
    myGraph.makeDirectedEdgeByID(2, 3)

    myGraph.makeDirectedEdgeByID(1, 4, 1)
    print(DFS(myGraph, 1, 4))
