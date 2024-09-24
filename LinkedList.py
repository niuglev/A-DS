"""linked list"""

import LinkedListItem


class LinkedList:
    def __init__(self):
        self.head = None

    def append_left(self, item):
        new_item = LinkedListItem(item)
        if new_item is None:
            self.head = new_item
            self.head.next_item = new_item
            self.head.prev_item = new_item
        else:
            last_item = self.head.prev_item
            new_item.next_item = self.head
            new_item.prev_item = last_item
            last_item.next_item = new_item
            self.head = new_item
