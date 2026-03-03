class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

n=int(input())
head=None
temp=None

for i in range(n):
    val=int(input())
    new_node=Node(val)
    if head is None:
        head=new_node
        temp=head
    else:
        temp.next=new_node
        temp=temp.next

def delete_k(head,k):
    if head is None:
        return None

    if k==1:
        return head.next

    temp=head
    for i in range(k-2):
        if temp is None or temp.next is None:
            return head
        temp=temp.next

    if temp.next is not None:
        temp.next=temp.next.next

    return head

k=int(input())

head=delete_k(head,k)   

temp=head
while temp:
    print(temp.data,end=" -> ")
    temp=temp.next
print("None")