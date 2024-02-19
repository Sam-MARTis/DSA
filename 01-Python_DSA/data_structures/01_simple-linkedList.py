class Node:
    def __init__(self, data = None, next_node=None) -> None:
        '''
        Basic "Node" data structure. 
        
        Contains just some number at this point but can hold anything.
        
        :param data: information to be contained in the node.
        :param next_node: the next node that this node points to.
        :type next_node: Node
        '''
        self.data = data
        self.next_node = next_node
    def updatePointer(self, next_node) -> None:
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
    
    def insertAt(self, index: int, data):
        '''
        Used to insert  nodes to a specific index.
        
        O(N) time complex.
        For index n, inserts the node between indexes n-1 and n. 
        Note: Starts counting from 0, like an array.
        Another way to understand it is that the inserted node will be at position [index] after insertion.
        
        '''
        self.current = self.head
        if index==0:
            self.addNode(data)
            print(Warning("Note: Use addNode instead of insertAt\n"))
            return Warning("Warning: Use addNode instead of insertAt\n") 
        # current = 0
        for i in range(1, index):
            if self.current.next_node == None:
                raise IndexError("Index out of range")
            self.current = self.current.next_node
        else:
            self.current.next_node = Node(data, self.current.next_node)
            return "Inserted"
        raise NotImplementedError("Error inserting node at value")
                
            
    
    
    
    
    def spanList(self):
        self.current = self.head
        count = 1
        while self.current.next_node is not None:
            print(f"{count}{'(Head)'*(count==1)}:[data: {self.current.data}]", end="  ->  ")
            self.current = self.current.next_node
            count+=1
        print(f"{count}(Tail):[data: {self.current.data}]")
        
# Testing purposes. Uncomment lines for demo.
ll = LinkedList()
ll.addNode(3)
ll.addNode(4)
ll.addNode(5)
ll.insertAt(2, 6)
ll.insertAt(4, 7)
ll.insertAt(4, 7)
ll.insertAt(5, "Hello")
ll.spanList()
 
        