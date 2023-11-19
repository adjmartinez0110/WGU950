# creating the hash table class
# Reference: WGU C950 Webinar 1 - Let's Go Hashing
# Reference: WGU C950 Webinar 2 - Getting Greedy, who moved my data?
import csv

# This hash table uses chaining
class HashTable:

    # initialize method -> Big O of: O(N)
    def __init__(self, initial_capacity=22):
        # Initializing the hash table with empty bucket lists
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Insert method -> Big O of: O(N)
    def insert(self, key, item):  # does both insert and update
        # get the bucket list where this item will go.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # update key if it is already in the bucket
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                kv[1] = item
                return True

        # if not, insert the item to the end of the bucket list.
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Search method -> Big O of: O(N)
    def search(self, key):
        # get the bucket list where this key would be.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        # print(bucket_list)

        # search for the key in the bucket list
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                return kv[1]  # value
        return None

    # Remove method -> Big O of: O(N)
    def remove(self, key):
        # get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present.
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])

#Hash table object; used in package.py to insert packages into hash table
myHash = HashTable()


