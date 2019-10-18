"""
How do you find and return the middle node of a singly linked list in one pass? You do not have access to the length of the list. If the list is even, you should return the first of the two “middle” nodes.
"""

slow_iter = self.head
        fast_iter = self.head
        while (fast_iter != None):
            fast_iter = fast_iter.next.next
            slow_iter = slow_iter
        return slow_iter
