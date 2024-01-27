class Node:
    def __init__(self, data, next_node) -> None:
        '''
        Basic "Node" data structure. 
        
        Contains just some number at this point but can hold anything.
        
        :param data: information to be contained in the node.
        :param next_node: the next node that this node points to.
        :type next_node: Node
        '''
        self.data = data
        self.next_node = next_node
        
    
class LinkedList:
    
    def __init__(self) -> None:
        '''
        Implementation of a simple linked list
        
        Insertion happens from the head, ie, start of the list.
        '''
        self.head = None
        self.current = None
    def addNode(self, data):
        self.head = Node(data, self.head)
        pass # will fill out later
    def spanList(self):
        self.current = self.head
        count = 1
        while self.current.next_node is not None:
            print(f"Node{count}: [data: {self.current.data}]", end=" -> ")
            self.current = self.current.next_node
            count+=1
        print(f"Final node({count}): [data: {self.current.data}]")
        
# # Testing purposes. Uncomment lines for demo.
# ll = LinkedList()
# ll.addNode(3)
# ll.addNode(4)
# ll.addNode(5)
# ll.spanList()
 
        