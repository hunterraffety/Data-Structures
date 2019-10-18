from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')

"""
Stack utilizes a Last In, First Out method. The same end is used to insert and delete elements. This makes the MOST sense to me because it is super similar to how JavaScript operates with the push and pop methods for arrays.

This is the simpler implementation of getting things around in a list.

Stack pushes the item to the top and pop pops the element off of the top of the stack. (Insert / Delete)

Stack uses one pointer to reference the same place, because that's the place that push and pop are going to impact.

Time complexity: O(1) - constant.

"""

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # time complexity is constant.
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.size += 1
        self.storage.add_to_head(value)

    def pop(self):
        if self.len() > 0:
            self.size -= 1
            value = self.storage.head.value
            self.storage.remove_from_head()
            return value

    def len(self):
        return self.storage.__len__()
