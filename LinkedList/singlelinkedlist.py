#implement a singly linkedlist 
#inputs, outputs 

#insert data , display data

#Create a class for the Node
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None #Pointer to the next Node

class LinkedList:
    def __init__(self):
        self.head = None #Initially the head node will point to none

    #Method to insert a new node
        
    def insert(self, data):
        newnode = Node(data)
        if not self.head:
            self.head = newnode
            return 
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = newnode

        #Display linked List
    def display(self):
        curr = self.head
        while curr :
            print(curr.data, end=(" -> "))
            curr = curr.next
        print("None")
                
                

finalList = LinkedList()

#Append elements to the llinked list
finalList.insert(10)
finalList.insert(20)
finalList.insert(60)
finalList.insert(80)
finalList.insert(50)
finalList.insert(30)
finalList.insert(40)

#Display Linked List
finalList.display()



