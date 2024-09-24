"""linked list"""


class LinkedListItem:
    def __init__(self, data):
        self.data = data
        self._next = None
        self._prev = None


    @property
    def next_item(self):
        return self._next

    @next_item.setter
    def next_item(self, linkedlistitem):
        if isinstance(linkedlistitem, LinkedListItem) or linkedlistitem is None:
            self._next = linkedlistitem
        else:
            raise ValueError()

    @property
    def prev_item(self):
        return self._prev

    @prev_item.setter
    def prev_item(self, linkedlistitem):
        if isinstance(linkedlistitem, LinkedListItem) or linkedlistitem is None:
            self._prev = linkedlistitem
        else:
            raise NotImplementedError()