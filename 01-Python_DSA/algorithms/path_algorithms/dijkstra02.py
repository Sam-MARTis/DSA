class Node:
    def __init__(self, ID) -> None:
        self.ID = ID
        self.value = float('inf')
        self.connectedTo= dict()

    def reset(self) -> None:
        self.value = float('inf')
        
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

    def resetValues(self):
        for node in self.nodes.values():
            node.reset()

    def getNodeValues(self):
        node_dict_all = dict()
        for node in self.nodes.values():
            node_dict_all[node.ID] = node.connectedTo
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
    number_nodes, number_edges, max_fuel = map(int, input().split())
    # max_fuel *= 60
    nodeList = [Node(i) for i in range(number_nodes)]
    graph = Graph(nodeList)
    for _ in range(number_edges):
        fromNode, toNode, weight = map(int, input().split())
        graph.makeConnection(nodeList[fromNode], nodeList[toNode], weight)
    min_people = float('inf')
    min_people_person = 0
    for i in range(number_nodes):
        people_get = 0
        distance_list = list(dijkstra(graph.getNodeValues(), i).values())
        for distance in distance_list:
            if distance <= max_fuel:
                people_get +=1
        if people_get <= min_people:
            min_people = people_get
            min_people_person = i
    print(min_people_person, end="" if repeatition == repeatitions-1 else "\n")
    graph.resetValues()