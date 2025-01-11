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
                head = self.first
                for i in range(index):
                    head = head.next
                tail = head.prev
                element = Node(new, tail, head)
                tail.next = element
                head.prev = element
        self.count += 1
    
    def pop(self, index = -1):
        if self.count == 0:
            print("Nothing to delete!")
            return
        if self.count == 1:
            self.first = None
            self.count = 0
            return
        if index < 0:
            before_last = self.first
            while before_last.next.next:
                before_last = before_last.next
            before_last.next = None
            self.count -= 1
            return
        elif index == 0:
            head = self.first
            head = head.next
            head.prev = None
            self.first = head
            self.count -= 1
            return
        else:
            head = self.first
            for i in range(index+1):
                head = head.next
            tail = head.prev.prev
            tail.next = head
            head.prev = tail
            self.count -= 1
            return

    def read(self, index = -1):
        if index < 0 or index >= self.count:
            if self.first == None:
                print("Nothing to read!")
            else:
                current = self.first
                while current:
                    current.read()
                    current = current.next
        else:
            if index == 0:
                self.first.read()
            else:
                current = self.first
                for i in range(index):
                    current = current.next
                current.read()
    
    def switch(self, index1 = -1, index2 = -1):
        if self.count < 2:
            print("Not enough elements!")
        if (index1 < 0 or index2 < 0) or (index1 == index2):
            print("Invalid indexes!")
        
        element1 = self.first
        element2 = self.first
        for i in range(index1):
            element1 = element1.next
        for i in range(index2):
            element2 = element2.next

        if index1 == 0 and index2 == self.count-1:
            head1 = element1.next
            tail1 = None
            head2 = None
            tail2 = element2.prev

            head1.prev = element2
            tail2.next = element1

            element1.next = head2
            element1.prev = tail2
            element2.next = head1
            element2.prev = tail1

            self.first = element2

        elif index1 == self.count-1 and index2 == 0:
            head1 = None
            tail1 = element1.prev
            head2 = element2.next
            tail2 = None

            tail1.next = element2
            head2.prev = element1

            element1.next = head2
            element1.prev = tail2
            element2.next = head1
            element2.prev = tail1

            self.first = element1

        elif element1.next == element2:
            head1 = element1
            tail1 = element1.prev
            head2 = element2.next
            tail2 = element2

            tail1.next = element2
            head1.prev = element2
            tail2.next = element1
            head2.prev = element1

            element1.next = head2
            element1.prev = tail2
            element2.next = head1
            element2.prev = tail1

        elif element2.next == element1:
            head1 = element1.next
            tail1 = element1
            head2 = element2
            tail2 = element2.prev

            tail1.next = element2
            head1.prev = element2
            tail2.next = element1
            head2.prev = element1

            element1.next = head2
            element1.prev = tail2
            element2.next = head1
            element2.prev = tail1
        
        elif index1 == 0:
            head1 = element1.next
            tail1 = None
            head2 = element2.next
            tail2 = element2.prev

            head1.prev = element2
            tail2.next = element1
            head2.prev = element1

            element1.next = head2
            element1.prev = tail2
            element2.next = head1
            element2.prev = tail1

            self.first = element2

        elif index2 == 0:
            head1 = element1.next
            tail1 = element1.prev
            head2 = element2.next
            tail2 = None

            tail1.next = element2
            head1.prev = element2
            head2.prev = element1

            element1.next = head2
            element1.prev = tail2
            element2.next = head1
            element2.prev = tail1

            self.first = element1

        elif index1 == self.count-1:
            head1 = None
            tail1 = element1.prev
            head2 = element2.next
            tail2 = element2.prev

            tail1.next = element2
            tail2.next = element1
            head2.prev = element1

            element1.next = head2
            element1.prev = tail2
            element2.next = head1
            element2.prev = tail1
        
        elif index2 == self.count-1:
            head1 = element1.next
            tail1 = element1.prev
            head2 = None
            tail2 = element2.prev

            tail1.next = element2
            head1.prev = element2
            tail2.next = element1

            element1.next = head2
            element1.prev = tail2
            element2.next = head1
            element2.prev = tail1

        else:
            head1 = element1.next
            tail1 = element1.prev
            head2 = element2.next
            tail2 = element2.prev

            tail1.next = element2
            head1.prev = element2
            tail2.next = element1
            head2.prev = element1

            element1.next = head2
            element1.prev = tail2
            element2.next = head1
            element2.prev = tail1


            


list = List()

list.add(1)
list.add(2)
list.add(3)
list.add(4)
list.add(5)
list.add(6)
list.add(7)

list.read()
print("=============")
list.switch(3,6)
list.read()
print("=============")
# list.first.next.next.next.prev.prev.read()

