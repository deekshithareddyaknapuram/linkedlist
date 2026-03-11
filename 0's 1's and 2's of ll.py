class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def create_ll(n):
    head = None
    temp = None
    for i in range(n):
        val = int(input("Enter value: "))
        new_node = Node(val)
        if head is None:
            head = new_node
            temp = head
        else:
            temp.next = new_node
            temp = temp.next
    return head
def display(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")
def sort012(head):
    dummy0=Node(-1)
    dummy1=Node(-1)
    dummy2=Node(-1)
    tail0=dummy0
    tail1=dummy1
    tail2=dummy2
    temp=head
    while temp is not None:
        if temp.data==0:
            tail0.next=temp
            tail0=tail0.next
        elif temp.data==1:
            tail1.next=temp
            tail1=tail1.next
        else:
            tail2.next=temp
            tail2=tail2.next
        temp=temp.next
    tail0.next=dummy1.next if dummy1.next else dummy2.next
    tail1.next=dummy2.next
    tail2.next=None
    head=dummy0.next
    return head
n = int(input("Enter number of nodes "))
head = create_ll(n)
print("original Linked List")
display(head)
head = sort012(head)
print("After sort")
display(head)


   


