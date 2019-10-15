from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')

class TextBuffer:
    def __init__(self, init=None):
        self.storage = DoublyLinkedList()

        if init:
            for char in init:
                self.storage.add_to_tail(char)

    def __str__(self):
        #print contents of buffer
        s = ""
        current = self.storage.head
        while current:
            s += current.value
            current = current.next
        return s

    def append(self, string_to_add):
        for char in string_to_add:
            self.storage.add_to_tail(char)

    def prepend(self, string_to_add):
        for char in string_to_add[::-1]:
            self.storage.add_to_head(char)

    def delete_front(self, chars_to_remove):
        for _ in range(chars_to_remove):
            self.storage.remove_from_head()

    def delete_back(self, chars_to_remove):
        for _ in range(chars_to_remove):
            self.storage.remove_from_tail()

    def join(self, other_buffer):
        self.storage.tail.next = other_buffer.storage.head
        other_buffer.storage.head.prev = self.storage.tail
        other_buffer.storage.head = self.storage.head
        self.storage.tail = other_buffer.storage.tail

    def split(self, place_to_split):
        pass

    def join_string(self, string_to_join):
        new_buffer = TextBuffer(string_to_join)
        self.join(new_buffer)

        #self.append(string_to_join)

if __name__ == "__main__":
    text = TextBuffer("Super")

    print(text)

    text.join_string("bubaubauba")

    print(text)

    text.append(" asldaskld")