class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
def delete(head, key):
    temp = head
    while temp:
        next_node = temp.next 
        if temp.data == key:
            if temp == head:
                head = temp.next
                if head:
                    head.prev = None
            else:
                if temp.prev:
                    temp.prev.next = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
        temp = next_node
    return head
def printll(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    print("None")
n = int(input())
head = None
temp = None
for _ in range(n):
    val = int(input())
    new_node = Node(val)
    if head is None:
        head = new_node
        temp = head
    else:
        temp.next = new_node
        new_node.prev = temp  
        temp = new_node
k = int(input())
head = delete(head, k)
printll(head)