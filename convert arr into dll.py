class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None
arr=list(map(int,input().split()))
head=None
temp=None
for i in arr:
    # val=int(input())
    new_node=Node(i)
    if head is None:
        head=new_node
        temp=head
    else:
        temp.next=new_node
        new_node.prev=temp
        temp=new_node
temp=head
while temp:
    print(temp.data,end=" ->")
    temp=temp.next
print('none')
