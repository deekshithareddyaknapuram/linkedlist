class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
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
def odd_even_ll(head):
    if head is None or head.next is None:
        return head
    odd = head
    even = head.next
    even_head = even
    while even is not None and even.next is not None:
        odd.next = odd.next.next
        odd = odd.next
        even.next = even.next.next
        even = even.next
    odd.next = even_head
    return head
n = int(input("Enter number of nodes: "))
head = create_ll(n)
print("Original Linked List")
display(head)
head = odd_even_ll(head)
print("After Odd-Even Rearrangement")
display(head)