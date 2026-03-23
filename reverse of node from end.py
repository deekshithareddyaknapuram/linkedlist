class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Create linked list with user input
    def create(self, n):
        temp = None
        for i in range(n):
            val = int(input(f"Enter value {i+1}: "))
            new_node = Node(val)

            if self.head is None:
                self.head = new_node
                temp = self.head
            else:
                temp.next = new_node
                temp = temp.next

    # Remove nth node from end
    def remove_nth_from_end(self, r):
        dummy = Node(0)
        dummy.next = self.head

        slow = dummy
        fast = dummy

        # Move fast r steps
        for _ in range(r):
            if fast.next is None:
                print("Invalid r (greater than length)")
                return
            fast = fast.next

        # Move both
        while fast.next:
            fast = fast.next
            slow = slow.next

        # Delete node
        slow.next = slow.next.next

        self.head = dummy.next

    # Print linked list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# -------- MAIN --------
ll = LinkedList()

n = int(input("Enter number of nodes: "))
ll.create(n)

r = int(input("Enter position from end to delete: "))
ll.remove_nth_from_end(r)

ll.display()