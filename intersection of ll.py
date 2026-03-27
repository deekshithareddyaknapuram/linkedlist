class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def intersection(head1,head2):
    if not head1 or not head2:
        return None
    t1=head1
    t2=head2
    while t1!=t2:
       t1=t1.next if t1 else head2
       t2=t2.next if t2 else head1
    return t1
def printll(head):
    temp=head
    while temp:
        print(temp.data,end="->")
        temp=temp.next
    print(None)
n1 = int(input("Enter size of first list: "))
head1 = None
temp = None

for _ in range(n1):
    val = int(input())
    new_node = Node(val)
    if head1 is None:
        head1 = new_node
        temp = head1
    else:
        temp.next = new_node
        temp = temp.next

nodes = []
temp = head1
while temp:
    nodes.append(temp)
    temp = temp.next
n2 = int(input("Enter size of second list: "))
head2 = None
temp = None
for _ in range(n2):
    val = int(input())
    new_node = Node(val)
    if head2 is None:
        head2 = new_node
        temp = head2
    else:
        temp.next = new_node
        temp = temp.next

pos = int(input("Enter position to intersect in first list (0 for no intersection): "))

if pos > 0 and pos <= len(nodes):
    temp.next = nodes[pos - 1]  
print("List 1:")
printll(head1)

print("List 2:")
printll(head2)

res = intersection(head1, head2)

if res:
    print("Intersection at node with value:", res.data)
else:
    print("No intersection")