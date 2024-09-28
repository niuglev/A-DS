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
            value._prev = self
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
            value._next = self
        else:
            raise ValueError()

    def __repr__(self):
        return str(self.data)


class LinkedList:
    """Связный список"""
    def __init__(self, first_item=None):
        self.first_item = first_item
        self.head = first_item

    @property
    def last(self):
        """Последний элемент"""
        if self.head is None:
            return None
        return self.head.previous_item

    def append_left(self, item):
        """Добавление слева"""
        new_item = LinkedListItem(item)
        if self.head is None:
            self.head = self.first_item = new_item
            self.head.next_item = new_item
        else:
            last_item = self.head.previous_item
            new_item.next_item = self.head
            new_item.previous_item = last_item
            # last_item.next_item = new_item
            self.head.previous_item = new_item
            self.head = self.first_item = new_item

    def append_right(self, item):
        """Добавление справа"""
        new_item = LinkedListItem(item)
        if self.head is None:
            self.head = new_item
            self.head.next_item = new_item
            self.head.previous_item = new_item
        else:
            last_item = self.head.previous_item
            new_item.next_item = self.head
            self.head.previous_item = new_item
            new_item.previous_item = last_item
            last_item.next_item = new_item

    def append(self, item):
        """Добавление справа"""
        return self.append_right(item)

    def remove(self, item):
        """Удаление"""
        if self.head is None:
            raise ValueError("Список пуст, нечего удалять")

        current = self.head
        first_item = current

        # Обходим список для поиска элемента
        while True:
            if current.data == item:
                # Удаление текущего элемента
                prev_item = current.previous_item
                next_item = current.next_item

                # Если удаляем единственный элемент
                if current == current.next_item:
                    self.head = None  # Список становится пустым
                else:
                    prev_item.next_item = next_item
                    next_item.previous_item = prev_item

                    # Если удаляем голову, обновляем ссылку на новую голову
                    if current == self.head:
                        self.head = next_item

                return  # Элемент успешно удален

            current = current.next_item

            # Если вернулись к первому узлу, элемент не найден
            if current == first_item:
                raise ValueError(f"Элемент {item} не найден в списке")

    def insert(self, previous, item):
        """Вставка справа"""
        new_item = LinkedListItem(item)
        current = self.head

        if current is None:  # Если список пуст
            self.head = new_item
            new_item.next_item = new_item
            new_item.previous_item = new_item
            return

        for _ in range(previous):
            current = current.next_item
            if current == self.head:  # Индекс вне диапазона
                raise IndexError("Индекс вне диапазона")

        next_item = current.next_item
        new_item.previous_item = current
        new_item.next_item = next_item
        current.next_item = new_item
        next_item.previous_item = new_item

    def __len__(self):
        if self.head is None:
            return 0

        current = self.head
        counter = 1
        while True:
            current = current.next_item
            if current == self.head:
                return counter
            counter = counter + 1

    def __iter__(self):
        current = self.head
        first_item = current

        if current is None:
            return

        while True:
            yield current.data
            current = current.next_item

            if current == first_item:
                break

    def __getitem__(self, index):
        if self.head is None:
            raise IndexError("Список пуст")

        length = len(self)
        if index < 0:
            index = len(self) + index

        if index < 0 or index >= length:
            raise IndexError("Индекс вне списка")

        if index < length//2:
            current = self.head
            for _ in range(index):
                current = current.next_item
        else:
            current = self.head.previous_item
            for _ in range(length - index - 1):
                current = current.previous_item

        return current.data

    def __contains__(self, item):
        """Проверка наличия элемента в списке"""
        if self.head is None:
            return False  # Список пуст

        item = LinkedListItem(item)
        current = self.head
        first_item = current

        while True:
            if current.data == item.data:
                return True  # Элемент найден
            current = current.next_item
            if current == first_item:
                break  # Прошли по всему списку

        return False  # Элемент не найден

    def __reversed__(self):
        if self.head is None:
            return  # Если список пуст, итерация не нужна

        current = self.head.previous_item  # Начинаем с последнего элемента
        first_item = current  # Запоминаем последний элемент, чтобы знать, когда завершить обход

        while True:
            yield current.data  # Возвращаем значение текущего узла
            current = current.previous_item  # Двигаемся в обратном направлении
            if current == first_item:
                break  # Останавливаемся, когда снова достигли последнего элемента

    def __repr__(self):
        if self.head is None:
            return "LinkedList()"
        else:
            items = []
            current = self.head
            first_item = current
            while current:
                items.append(repr(current.data))  # Используем repr для элементов списка
                current = current.next_item
                if current == first_item:
                    break
            return "LinkedList(" + " -> ".join(items) + ")"
