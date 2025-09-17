# Import the linked list and Node classes
from linked_list import Node, LinkedList
from blossom_lib import flower_definitions

# Define the HashMap class
class HashMap:
    def __init__(self, array_size):
        self.array_size = array_size
        # Initialize an array of LinkedLists for separate chaining
        self.array = [LinkedList() for _ in range(array_size)]

    # Hash function: sum of byte values of the key string
    def hash(self, key):
        key_bytes = key.encode()
        return sum(key_bytes)

    # Compression function: converts hash code to array index
    def compress(self, hash_code):
        return hash_code % self.array_size

    # Assign key-value pair using separate chaining
    def assign(self, key, value):
        array_index = self.compress(self.hash(key))
        list_at_array = self.array[array_index]

        # Check if key exists; if so, update value
        for node in list_at_array:
            if node[0] == key:
                node[1] = value
                return

        # Otherwise, insert new node
        payload = Node([key, value])
        list_at_array.insert(payload)

    # Retrieve value for a given key
    def retrieve(self, key):
        array_index = self.compress(self.hash(key))
        list_at_index = self.array[array_index]

        for node in list_at_index:
            if node[0] == key:
                return node[1]

        return None


# Create HashMap instance with size equal to number of flowers
blossom = HashMap(len(flower_definitions))

# Assign all flower meanings to the hash map
for flower in flower_definitions:
    blossom.assign(flower[0], flower[1])

# Example retrievals
print("Daisy meaning:", blossom.retrieve('daisy'))
print("Rose meaning:", blossom.retrieve('rose'))
print("Sunflower meaning:", blossom.retrieve('sunflower'))
