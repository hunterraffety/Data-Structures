import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

"""
Queue operates on a First In, First Out basis. Meaning, one end is used for insertion, and the other is used for the deletion

Typically this will use at least two pointers. Queue always uses "enqueue" and "dequeue". Queue is the more complex version for shifting things around. Enqueuing adds something to the read and dequeuing pushes that item from the front. (Insert / Delete).

The pointers need to have access to both the rear and front of the data list.

Think of it like this for queue:

A person is in line for movie tickets. The person in the front, will get a ticket first before the person in the back, who will receive theirs last.

Time complexity: O(1) - constant.

### access / finding in lists is more difficult. removing things from the middle.
"""

class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # time complexity > * (it's constant)
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_head(value)

    def dequeue(self):
        if self.len() > 0:
            self.size -= 1
            value = self.storage.tail.value
            self.storage.remove_from_tail()
            return value

    def len(self):
        return self.storage.__len__()

