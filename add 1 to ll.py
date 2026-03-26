class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def add_one_until(head):
    if head is None:
        return 1
    carry = add_one_until(head.next)
    total = head.data + carry
    head.data = total % 10
    return total // 10
def add_one(head):
    carry = add_one_until(head)
    if carry:
        new_node = Node(carry)
        new_node.next = head
        head = new_node
    return head
def printll(head):
    temp = head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")

n = int(input())
head = None
temp = None
for i in range(n):
    val = int(input())
    new_node = Node(val)

    if head is None:
        head = new_node
        temp = head
    else:
        temp.next = new_node
        temp = temp.next

head = add_one(head)
printll(head)