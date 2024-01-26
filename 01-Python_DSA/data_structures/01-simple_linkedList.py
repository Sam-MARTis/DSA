class Node:
    def __init__(self, data, next_node) -> None:
        self.data = data
        self.next_node = next_node
    
class LinkedList:
    def __init__(self) -> None:
        self.tail = None
        self.current = None
    def addNode(self, data):
        self.tail = Node(data, None)
        pass # will fill out later
    
        
        