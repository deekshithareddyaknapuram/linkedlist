class Node:
    def __init__(self, url):
        self.url = url
        self.prev = None
        self.next = None
class BrowserHistory:
    def __init__(self, homepage: str):
        self.current = Node(homepage)
    def visit(self, url: str):
        new_node = Node(url)
        self.current.next = None
        new_node.prev = self.current
        self.current.next = new_node
        self.current = new_node
    def back(self, steps: int):
        while steps > 0 and self.current.prev:
            self.current = self.current.prev
            steps -= 1
        return self.current.url
    def forward(self, steps: int):
        while steps > 0 and self.current.next:
            self.current = self.current.next
            steps -= 1
        return self.current.url

bh = BrowserHistory("google.com")
bh.visit("youtube.com")
bh.visit("linkedin.com")
print(bh.back(1))     
print(bh.back(1))   
print(bh.forward(1))   
bh.visit("github.com") 
print(bh.forward(2))   
print(bh.back(2))     