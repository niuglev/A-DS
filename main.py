# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from linked_list import LinkedList, LinkedListItem


if __name__ == '__main__':
    new_list = LinkedList()
    new_list.append_left(LinkedListItem(10))
    new_list.append_left(LinkedListItem(20))
    print(new_list)


