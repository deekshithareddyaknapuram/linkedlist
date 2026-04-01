class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def rotate(head, k):
    if not head or not head.next or k == 0:
        return head
    temp = head
    n = 1
    while temp.next:
        temp = temp.next
        n += 1
    temp.next = head
    k = k % n
    steps = n - k
    new_tail = head
    for _ in range(steps - 1):
        new_tail = new_tail.next
    new_head = new_tail.next
    new_tail.next = None
    return new_head
def printll(head):
    temp = head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")
n = int(input("Enter number of nodes: "))
head = None
temp = None
for _ in range(n):
    val = int(input("Enter value: "))
    new_node = Node(val)
    if not head:
        head = new_node
        temp = head
    else:
        temp.next = new_node
        temp = temp.next
k = int(input("Enter k: "))

head = rotate(head, k)
printll(head)
n = int(input("Enter number of nodes: "))
head = None
temp = None

for _ in range(n):
    val = int(input("Enter value: "))
    new_node = Node(val)

    if not head:
        head = new_node
        temp = head
    else:
        temp.next = new_node
        temp = temp.next
k = int(input("Enter k: "))
head = rotate(head, k)
printll(head)