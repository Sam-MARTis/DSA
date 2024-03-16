class Node:
    def __init__(self, ID) -> None:
        self.ID = ID
        self.value = float('inf')
        self.priority = float('inf')
        self.connectedTo= dict()
        self.explored = False
        
class Graph:
    def __init__(self, nodes: list):
        self.nodes = dict()
        for node in nodes:
            self.nodes[node.ID] = node  
    def makeConnection(self, fromNode:Node, toNode:Node, edgeWeight:float):
        fromID = fromNode.ID
        toID = toNode.ID
        fromNode.connectedTo[toID]= edgeWeight  
        toNode.connectedTo[fromID]= edgeWeight 
    
    def getValues(self):
        return self.nodes

    def dijkstra(self, startNode: Node):
        unexplored_nodes_ID = list(self.nodes.keys()).copy()
        explored_nodes = []
        startNode.value = 0
        current_node = startNode
        
        
        while True:
            for connectionNodeID in current_node.connectedTo.keys():
                connectingWeight = current_node.connectedTo[connectionNodeID]
                connectedNode = self.nodes[connectionNodeID]  
                if connectedNode.value > current_node.value + connectingWeight:
                    connectedNode.value = current_node.value + connectingWeight
            current_node.explored = True
            explored_nodes.append(current_node.ID)
            # print("Current Node: " , current_node.ID)
            # print("Unexplored nodes before: ", unexplored_nodes_ID)
            unexplored_nodes_ID.remove(current_node.ID)
            # print("Unexplored nodes after: ", unexplored_nodes_ID)
            if len(unexplored_nodes_ID) == 0:  
                break
            min_value = float('inf')
            for node_ID in unexplored_nodes_ID:
                node = self.nodes[node_ID]  # Get the node object
                if node.value <= min_value:
                    min_value = node.value
                    current_node = node
    def getNodeValues(self):
        node_dict_all = dict()
        for node in self.nodes.values():
            node_dict_all[node.ID] = node.connectedTo
        # print(node_dict_all)
        return node_dict_all
            

import heapq

def dijkstra(adj_list, start_node):
    distances = {node: float('inf') for node in adj_list}
    distances[start_node] = 0

    pq = [(0, start_node)]

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        if current_dist > distances[current_node]:
            continue

        for neighbor, weight in adj_list[current_node].items():
            distance = current_dist + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances





         
repeatitions = int(input())
for repeatition in range(repeatitions):
    number_nodes, nuber_edges, max_fuel = [int(i) for i in input().split()]
    max_fuel*=60
    nodeList = [Node(i+1) for i in range(number_nodes)]
    graph = Graph(nodeList)
    for edge in range(nuber_edges):
        fromNode, toNode, weight = [int(i)-1 for i in input().split()]
        weight+=1
        graph.makeConnection(nodeList[fromNode], nodeList[toNode], weight)
    distance_list = dijkstra(graph.getNodeValues(), 1)

    if(repeatition == repeatitions-1):
        for fuel in distance_list.values():
            if fuel>max_fuel:
                print("NO", end="")
                break
        else:
            print("YES", end="")
        
    else:
        for fuel in distance_list.values():
            if fuel>max_fuel:
                print("NO")
                break
        else:
            print("YES")
