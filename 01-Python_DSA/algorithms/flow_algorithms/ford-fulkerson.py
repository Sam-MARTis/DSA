import sys
from typing import List

sys.path.append("/home/samanth/Code/DSA/01-Python_DSA/")
from data_structures.graph import Graph, Node

graph = Graph()
graph.addNodes(
    [
        Node(1, {'visited': False}),
        Node(2, {'visited': False}),
        Node(3, {'visited': False}),
        Node(4, {'visited': False}),
        Node(5, {'visited': False}),
        Node(6, {'visited': False}),
        Node(7, {'visited': False}),
        Node(8, {'visited': False}),
        Node(9, {'visited': False}),
        Node(10, {'visited': False}),
    ]
)

GraphNodes = graph.getNodes()
graph.makeDirectedEdge(fromNode=GraphNodes[1], toNode=GraphNodes[2], weight=10)
graph.makeDirectedEdge(fromNode=GraphNodes[2], toNode=GraphNodes[3], weight=20)
graph.makeDirectedEdge(fromNode=GraphNodes[3], toNode=GraphNodes[1], weight=20)
node1 = GraphNodes[1]
node1Edge1 = node1.edges[0]
node2 = node1.traverse(node1Edge1)[0]
node2Edge1 = node2.edges[0]
node3 = node2.traverse(node2Edge1)[0]
node3Edge1 = node3.edges[0]
node4 = node3.traverse(node3Edge1)[0]
print(node2.id)
print(node3.id)
print(node4.id)

# print(GraphNodes[1].traverse(GraphNodes[1].edges[0]))

# def Floyd_Fulkerson(Graph):
#     source = Graph.source

def DFS_connected_check(graph, startID, endID) -> bool:
    Nodes: List[Node] = graph.getNodes()
    StartNode: Node = Nodes[startID]
    EndNode: Node = Nodes[endID]
    queueToExplore = [[startID, StartNode.getEdges() ]] #Node ID, unexplored edges
    while len(queueToExplore)>0:
        currentItem = queueToExplore[-1]
        # print(currentItem)
        currentNode: Node = Nodes[currentItem[0]]
        currentNodeEdges = currentItem[1]

        if currentNode.id == endID:
            # print("Found ittt")
            return True
        
        if currentNodeEdges==[] or currentNodeEdges == [[]]:
            # print(queueToExplore)
            queueToExplore.pop()
            continue
        for edge in currentNodeEdges:
            # print(f"CurrentNodeID = {currentNode.id}")
            newNode: Node = currentNode.traverse(edge)[0]
            # print(f"NewNodeID = {newNode.id}")
            # print(f"{newNode.id}.state['visited'] = {newNode.state['visited']}")
            if newNode.state['visited']==False:
                # print(f"Setting {newNode.id}.state['visited'] = True")
                newNode.state['visited'] = True
                queueToExplore.append([newNode.id, newNode.getEdges()])
                print(queueToExplore)
                break
            else:
                currentNodeEdges.remove(edge)







        # # print(currentNodeEdges)
        # chosenEdge = currentNodeEdges.pop()
        # # print(chosenEdge)
        # # print(currentNode.id)
        # # print(f"Traversing: {currentNode.traverse(chosenEdge)}")
        # newNode: Node = currentNode.traverse(chosenEdge)[0]
        # if newNode.state['visited']==False:
        #     newNode.state['visited'] = True
        #     queueToExplore.append([newNode.id, newNode.getEdges()])
            
    print('Not found')
    return False
DFS_connected_check(graph, 1, 3)