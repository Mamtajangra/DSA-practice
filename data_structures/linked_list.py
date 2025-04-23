# define a node class 
class Node:
    # constructor shows the feature 
    def __init__(self,data):
        # these are feature of node or having data 
        self.data = data
        self.next = None


# define a linked list class 
class Linked_list:
    # define constructer 
    def __init__(self):
        # we dont know about head 
        self.head = None



# determine some functions of linked list like insert,append,delete,traversing 
    def traverse(self):
        # it starts from the head of the list 
        temp = self.head 
        # start a loop until it return none 
        while temp:
            # print the data of each node 
            print(temp.data,end="--->")
            temp = temp.next
        # otherwise return none value 
        return None
    

    # now define a function for insert
    def insert(self,value):
        # we take new node data from NODE class 
        new_node = Node(value)
        # in case of insert function node is added at  beginning so new_node's next is head of node 
        new_node.next = self.head
        # again that head node became new node 
        self.head = new_node 


# define append function where we add node at last instead of beginning 
    def append(self,value):
        new_node = Node(value)
    # two cases arise either list is empty or full .. so firstly we will handle the case of empty list 
        if self.head is None:
        # new node become the first node in this case 
            self.head = new_node
            return
    # if there are several node and we want to append new node 
    # here temp pointer points the head node 
        temp = self.head
    # we are using a loop here until we reach out last node
        while temp.next:
            temp = temp.next
        # on last node we add new node there 
        temp.next = new_node    



    # define a function for deletion 
    def delete(self,value):
        temp = self.head
        # if temp shows the head node then there is no node in previous of head node 
        prev = None 

# case 1 check list is empty 
        if temp is None:
            print("the list is empty")     ## node is empty here 
            return 
    
# case 2  the value we want to delete is in head we  handle this case 
        if temp.data == value:
            # this node is directing to next 
            self.head = temp.next                         
            # one time temp is none 
            temp = None 
            return   


# case 3 searching the node in entire list  
        while temp and temp.data != value :   ## here the value we want to delete is not equal to temp.data and we assign previous value to temp and again temp is moving to the next value
            prev = temp                      ## [10] -> [20] -> [30] -> [40] -> None
                                        #   temp = 10, value != 30 → prev = 10, temp = 20   
                                        #   temp = 20, value != 30 → prev = 20, temp = 30
                                        #   temp = 30, value == 30 → Loop break hota hai
            temp = temp.next
        
# case 4 if the node we want to delete is not in linked list 
        if temp is None:
            print(f"there is no value in the list")       ## here value is none inside the node
            return 
        
# case 5 we found the node and we deleted it 
        prev.next = temp.next                     ## the next of 20 is 40 now because 30 is deleted now 
        temp = None                               ## it is just for clarity now because there is no item in temp 




# these are the data of each node 
n1 = Node("banana")
n2 = Node("cherry")
n3 = Node("apple")
n4 = Node("peach")
n5 = Node("mango")
n6 = Node("mullberry")
n7 = Node("pomegranate")
n8 = Node("sapota")



# initialize head to n1
head = n1
# linkage another node is present at the next of one
 
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n8


LL1 = Linked_list()
LL1.head = n1

# traversing before insert any node
LL1.traverse()
LL1.insert(10)
LL1.insert(20)
LL1.insert(40)
LL1.insert(60)
LL1.insert(80)
LL1.insert(100)
LL1.insert("capsicum") 
LL1.append("500")  

LL1.delete("pomegranate")
LL1.delete("mango")
print("delete mango and pomegranate" )
LL1.traverse()
print("after insert and append node")

# traversing after insert and append 
LL1.traverse()

