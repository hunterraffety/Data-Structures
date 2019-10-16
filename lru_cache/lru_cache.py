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
        self.limit = limit  #limit is implied as param #max
        self.dll = DoublyLinkedList() #provides access to my helper methods
        self.size = 0 #needs to be able to know it's own size to compare against the limit being set
        self.storage = {} #dirs say to create a dict. so here. #stores nodes
        pass

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.storage:
            node = self.storage[key] #this key exists, so we will "reinvigorate it" and make it the most recently thing, by moving it to the front
    #this will utilize something like if this key is in the storage dict, so if this key is in self.storage, do something.
    #this will also need to be able to use move_to_front() from my dll?
            self.dll.move_to_end(node) #shifts our guy around. shakes a can of soda to make it active.
            return node.value[1]
        else:
            return None

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
        # in the case where the key exists, overwrite old value with the old key with the newly specific value
        if key in self.storage: #
            node = self.storage[key] #references key param to create node
            node.value = (key, value) #sets value prop on node
            self.dll.move_to_end(node)
            return
        
        #needs another if, because the cache may be at max capacity
        if self.size == self.limit:
            del self.storage[self.dll.head.value[0]]
            self.dll.remove_from_head()
            self.size -= 1


        #add the key-value pair to the cache
        #add the ll to the tail
        self.dll.add_to_tail((key, value))
        #add to dictionary
        self.storage[key] = self.dll.tail
        self.size += 1
        #needs a case where its not existent? I think
