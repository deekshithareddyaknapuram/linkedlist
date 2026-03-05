class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None
head=None
temp=None
n1=Node(10)
n2=Node(20)
n1.prev=None
n1.next=n2
n2.prev=n1
n2.next=None
head=n1
temp=head
# print('NOne')
while temp:
    # print('None')
    print(temp.data,end="<-->")
    temp=temp.next
print('None')
