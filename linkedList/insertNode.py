from linkedlistdef import LinkedList
from linkedlistdef import Node

# Insert at the begining

def push(head, newData):
    
    newNode = Node(newData)
    newNode.next = head

    return newNode


# Insert after a given node



# Insert at the end of linkedList