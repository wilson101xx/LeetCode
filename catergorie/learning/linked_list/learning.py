class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegin(self, data):
        print(f"Inserting {data} at the beginning of the list.")
        
        # Step 1: Create a new node with the given data
        new_node = Node(data)
        print(f"Created a new node with data={new_node.data} and next={new_node.next}")
        
        # Step 2: Link the new node to the current head
        new_node.next = self.head
        print(f"Set new_node.next to point to current head: {self.head}")
        
        # Step 3: Update the head to the new node
        self.head = new_node
        print(f"Updated the head of the list to the new node: {self.head.data}\n")



    def insertAtIndex(self, data, index):
        if (index == 0):
            self.insertAtBegin(data)
            return
        
        position = 0
        current_node = self.head
        while (current_node != None and position+1 != index):
            position = position+1
            current_node = current_node.next

        if current_node != None:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node

        else:
            print("Index Not presented")

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        current_node = self.head
        while (current_node.next):
            current_node = current_node.next
        current_node.next = new_node
    
    def updateNode(self, val, index):
        current_node = self.head
        position = 0
        if position == index:
            current_node.data == val
        else:
            while (current_node != None and position != index):
                position = position+1
                current_node = current_node.next

            if current_node != None:
                current_node.data = val
            else:
                print("index is not present")
    
    def remove_first_node(self):
        if(self.head == None):
            return
        
        self.head = self.head.next

    def remove_last_node(self):
        if self.head is None:  # If the list is empty, nothing to remove
            return

        if self.head.next is None:  # If there's only one node
            self.head = None  # Remove it by setting head to None
            return

        # Traverse the list to find the second-to-last node
        curr_node = self.head
        while curr_node.next.next is not None:  # Stop at the second-to-last node
            curr_node = curr_node.next

        # Remove the last node
        curr_node.next = None

# Method to remove at given index
    def remove_at_index(self, index):
        if self.head is None:
            return

        current_node = self.head
        position = 0
        
        if index == 0:
            self.remove_first_node()
        else:
            while current_node is not None and position < index - 1:
                position += 1
                current_node = current_node.next
            
            if current_node is None or current_node.next is None:
                print("Index not present")
            else:
                current_node.next = current_node.next.next

    def sizeOfLL(self):
        size = 0
        if(self.head):
            current_node = self.head
            while(current_node):
                size = size+1
                current_node = current_node.next
            return size
        else:
            return 0



    def display(self):
        current = self.head
        print("Displaying the linked list:")
        while current:
            print(current.data, end=" => ")
            current = current.next
        print("None")



llist = LinkedList()

# Insert elements into the linked list
llist.insertAtBegin(50)
llist.remove_last_node()
# llist.updateNode(3,1)
# llist.insertAtIndex("5", 2)
# llist.insertAtEnd(5)

# Display the linked list
llist.display()
