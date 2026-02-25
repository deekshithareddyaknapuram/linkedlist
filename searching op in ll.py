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
val=30
found=False
while curr:
    if curr.data==val:
        found=True
        break       
    curr=curr.next
if found:
    print(val,"found")
else:
    print('not found')

    

      