class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node 
            return 
        #the next element after the new node is self.head
        new_node.next = self.head
        #the head pointer is at the new node 
        self.head = new_node 

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node 
        self.tail.next = new_node 
        self.tail = new_node 
    def delete_node(self, key):
        #if the linked list is empty
        if self.head is None:
            return 
        #if the head is the key 
        if self.head.data == key:
            #delete the head node 
            self.head = self.head.next
            return 
        current = self.head
        prev = None
        #continue checking until you find the key  
        while current and current.data != key:
            prev = current 
            current = current.next 
        
        #if key is not found in the linked list
        if current is None:
            return
        
        #if key is found, delete the key 
        prev.next = current.next
        return 

        
    def display_list(self):
        current = self.head 
        while current: 
            print(current.data, end="->")
            current = current.next 
        print("None")     
     

ll = LinkedList()
#ll.insert_at_beginning(10)
#ll.insert_at_beginning(20)
#ll.insert_at_beginning(30)
#ll.insert_at_beginning(40)
#ll.insert_at_beginning(50)

ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.insert_at_end(40)
ll.insert_at_end(50)


ll.display_list()
