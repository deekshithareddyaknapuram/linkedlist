import heapq

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
def build_list(arr):
    head = None
    temp = None
    for val in arr:
        new_node = ListNode(val)
        if head is None:
            head = new_node
            temp = head
        else:
            temp.next = new_node
            temp = temp.next
    return head
def mergek(lists):
    heap = []
    for i, l in enumerate(lists):
        if l:
            heapq.heappush(heap, (l.data, i, l))
    dummy = ListNode(0)
    curr = dummy

    while heap:
        data, i, node = heapq.heappop(heap)

        curr.next = node
        curr = curr.next

        if node.next:
            heapq.heappush(heap, (node.next.data, i, node.next))
    return dummy.next
def printll(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    print("None")
k = int(input())
lists = []
for _ in range(k):
    n = int(input())
    arr = list(map(int, input().split()))   
    head = build_list(arr)
    lists.append(head)
result = mergek(lists)
printll(result)