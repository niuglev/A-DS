# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from linked_list import LinkedList, LinkedListItem


if __name__ == '__main__':
    new_list = LinkedList()
    new_list.append_left(10)
    new_list.append_left(20)
    new_list.append_right(50)
    new_item = 30
    new_list.append_left(new_item)
    new_list.append_right(40)
    new_list.append(10)
    new_list.remove(40)
    new_list.insert(50, 60)
    print(new_list)
    print(len(new_list))
    for item in new_list:
        print(item)
    print(f"Item -> {new_list.__getitem__(1)}")
