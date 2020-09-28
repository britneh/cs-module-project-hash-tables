class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """


    def __init__(self, capacity):
        #The capacity is the number of buckets in the hash table, and 
        # the initial capacity is simply the capacity at the time 
        # the hash table is created. -- Doesn't this mean more than min listed?
        self.capacity = capacity
        self.length = 0 #amount stored
        self.table = [None] * self.capacity


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity #or length of self.table


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # The load factor is a measure of how full the hash table is allowed
        # to get before its capacity is automatically increased
        #the number of items currently in the table divided by the size of the array
        return (self.length/self.capacity) 


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381
        byte_array = key.encode('utf-8')

        for byte in byte_array:
            hash = ((hash * 33) + byte)

        return hash & 0xffffffff


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        index = self.index_hash(key)
        # Create variable for the value at index
        current_node = self.table[index]

        # While the node has a value and we haven't reached the end of our list:
        while current_node is not None:
            # If the current node's key is key is the key we're looking for:
            if current_node.key == key:
                # Assign the value to the node
                current_node.value = value
                return
            else:
                # Or move on to the next node
                current_node = current_node.next

        # Create a new node with the HashTableEntry
        new_node = HashTableEntry(key, value)
        # Assign the index at the hash table we're on to be the .next node of the new_node
        new_node.next = self.table[index]
        # Assign the new_node to the index we're on
        self.table[index] = new_node

        # Add 1 to the total number of keys we're storing.
        self.length += 1


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        #find index
        index = self.index_hash(key)
        #set value of node of that index to none
        self.table[index] = None

        #decrement total of slots by one
        self.length -= 1



    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        #find index
        index = self.index_hash(key)
        #find node at index
        current_node = self.table[index]

        # If node is not empty:
        while current_node is not None:
            # And the current node's key is the key we're looking for:
            if current_node.key == key:
                # Return the value of the key
                return current_node.value 
            else:
                # Or move on to check the next node
                current_node = current_node.next


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
