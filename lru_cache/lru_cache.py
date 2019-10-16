from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')

#we need:
#fast lookup. fast removal. dict has a key / value relationship.
#how do you know where the lru is?
#dll instant access and remove in constant time, can touch both nodes and pop out. do not have to resize the list. no need to shift things around. no need for linearity. dll is an abstraction of pointers.

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit  #limit is implied as param
        self.dll = DoublyLinkedList() #provides access to my helper methods
        self.size = 0
        self.storage = {} #dirs say to create a dict. so here.
        pass

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        pass
    #this will utilize something like if this key is in the storage dict, so if this key is in self.storage, do something.
    #this will also need to be able to use move_to_front() from my dll?

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        #going to need to use #add_to_head()?
        #going to need to use #remove_from_tail()?
        #i don't know.
        pass
