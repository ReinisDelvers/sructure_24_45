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
        self.count = 0
    
    def add(self, new, index = -1):
        if index < 0 or index >= self.count:
            if self.first == None:
                self.first = Node(new)
            else:
                last = self.first
                while last.next:
                    last = last.next
                last.next = Node(new, before = last)
        else:
            if index == 0:
                element = Node(new, after = self.first)
                element.next.prev = element
                self.first = element
            else:
                tail = self.first
                for i in range(index):
                    tail = tail.next
                head = tail.prev
                element = Node(new, head, tail)
                head.next = element
                tail.prev = element
        self.count += 1
    
    def pop(self):
        if self.count == 0:
            print("Nothing to delete!")
            return
        if self.count == 1:
            self.first = None
            self.count = 0
            return
        before_last = self.first
        while before_last.next.next:
            before_last = before_last.next
        before_last.next = None
        self.count -= 1
        return

    def read(self):
        if self.first == None:
            print("List is empty!")

        current = self.first
        while current:
            current.read()
            current = current.next

list = List()

list.add("Suns")
list.add("Kāja")
list.add("Māja")
list.add(2,1)
list.pop()
list.add("Kaija")
list.add("Mala")

list.read()
print("=============")

list.first.next.next.next.prev.prev.read()