class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' ')
            current_node = current_node.next
        print()

    def reverse(self):
        prev_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node
    
    def delete_node(self, key):
        current_node = self.head
        prev_node = None

        if current_node and current_node.data == key:
            self.head = current_node.next
            return

        while current_node and current_node.data != key:
            prev_node = current_node
            current_node = current_node.next

        if not current_node:
            return

        prev_node.next = current_node.next
        current_node.next = None
        def delete_node_by_position(self, position):
            if position < 0:
                return
            current_node = self.head
            if position == 0:
                self.head = current_node.next
                return
            prev_node = None
            count = 0
            while current_node and count < position:
                prev_node = current_node
                current_node = current_node.next
                count += 1
            if not current_node:
                return
            prev_node.next = current_node.next
            current_node.next = None
            