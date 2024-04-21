class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None, itr)

    def insert(self, new_data):
        for data in new_data:
            self.insert_at_end(data)

    def print_forward(self):
        if self.head is None:
            print("Doubly Linked list is empty")
            return

        itr = self.head
        dll_str = ''

        while itr:
            dll_str += str(itr.data) + ' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(dll_str)

    def print_backward(self):
        while self.head.next:
            self.head = self.head.next

        itr = self.head
        dll_str = ''

        while itr:
            dll_str += str(itr.data) + ' --> ' if itr.prev else str(itr.data)
            itr = itr.prev
        print(dll_str)


if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.insert(["start", 1, 2, 3, 4, "end"])
    dll.print_forward()
    dll.print_backward()
