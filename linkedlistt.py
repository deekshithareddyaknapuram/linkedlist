'''class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
n1=Node(10)
n2=Node(20)
n3=Node(30)
n1.next=n2
n2.next=n3
head=n1
curr=head
while curr:
    print(curr.data,end=" ")
    curr=curr.next
print("None") '''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
n=int(input('enter number of values'))
head=None
curr=None
for i in range(n):
    vals=int(input('enter the values'))
    new_node=Node(vals)
    if head is None:
        head=new_node
        curr=head
    else:
        curr.next=new_node
        curr=curr.next
curr=head

while curr:
    print(curr.data)
    
    curr=curr.next
print('Null')
