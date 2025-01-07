class Node:
    def __init__(self, content, before=None, after=None):
        self.info = content
        self.next = after
        self.prev = before

    def read(self):
        print(self.info)


class List:
    def __init__(self):
        self.first = None
    
    def add(self, new):
        if self.first == None:
            self.first = Node(new)
        else:
            last = self.first
            while last.next:
                last = last.next
            last.next = Node(new, before = last)

    def read(self):
        if self.first == None:
            print("List is empty!")

        current= self.first
        while current:
            current.read()
            current = current.next

list = List()

list.add("Suns")
list.add("Kāja")
list.add("Māja")
list.add(2)

list.read()
print("=============")

list.first.next.next.next.prev.prev.prev.read()