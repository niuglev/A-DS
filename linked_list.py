"""Модуль "заглушка" для тестов"""


class LinkedListItem:
    """Узел связного списка"""
    def __init__(self, data=None):
        self.data = data
        self._next = None
        self._prev = None

    @property
    def next_item(self):
        """Следующий элемент"""
        return self._next

    @next_item.setter
    def next_item(self, value):
        if isinstance(value, LinkedListItem) or value is None:
            self._next = value
        else:
            raise ValueError()

    @property
    def previous_item(self):
        """Предыдущий элемент"""
        return self._prev

    @previous_item.setter
    def previous_item(self, value):
        if isinstance(value, LinkedListItem) or value is None:
            self._prev = value
        else:
            raise ValueError()

    def __repr__(self):
        return str(self.data)


class LinkedList:
    """Связный список"""
    def __init__(self, first_item=None):
        self.head = None

    @property
    def last(self):
        """Последний элемент"""
        raise NotImplementedError()

    def append_left(self, item):
        """Добавление слева"""
        new_item = LinkedListItem(item)
        if self.head is None:
            self.head = new_item
            self.head.next_item = new_item
            self.head.prev_item = new_item
        else:
            last_item = self.head.prev_item
            new_item.next_item = self.head
            new_item.prev_item = last_item
            last_item.next_item = new_item
            self.head = new_item

    def append_right(self, item):
        """Добавление справа"""
        raise NotImplementedError()

    def append(self, item):
        """Добавление справа"""
        raise NotImplementedError()

    def remove(self, item):
        """Удаление"""
        raise NotImplementedError()

    def insert(self, previous, item):
        """Вставка справа"""
        raise NotImplementedError()

    def __len__(self):
        raise NotImplementedError()

    def __iter__(self):
        raise NotImplementedError()

    def __getitem__(self, index):
        raise NotImplementedError()

    def __contains__(self, item):
        raise NotImplementedError()

    def __reversed__(self):
        raise NotImplementedError()

    def __repr__(self):
        if self.head is None:
            return "LinkedList()"
        else:
            nodes = []
            current = self.head
            while current:
                nodes.append(repr(current.data))  # Используем repr для элементов списка
                current = current.next_item
            return "LinkedList(" + " -> ".join(nodes) + ")"
