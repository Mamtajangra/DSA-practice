class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
    def __repr__(self):
        return f"<< {self.data} >>"
    def __str__(self):
        return f"<< {self.data} >>"

class doubly_list:
    def __init__(self,head=None):
        self.head = head


    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

        print()



# main code --- H-> [10,n2,n1] -> [20, n3, n1] -> [30, None, n2]

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
head = n1

# Manually connecting the nodes
n1.next = n2
n1.prev = head

n2.next = n3
n2.prev = n1

n3.prev = n2


dll1_obj = doubly_list(head)

dll1_obj.traverse()