#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length
    count = 0

    for i in tickets:
        hash_table_insert(hashtable, i.source, i.destination)

    def rec_func(key = 'NONE'):
        nonlocal count
        if  hash_table_retrieve(hashtable, key) == 'NONE':
            print('exit')
            print(route[:-1])
            return route[:-1]
        else:
            route[count] = hash_table_retrieve(hashtable, key)
            count += 1
            print(route[count])
            rec_func(hash_table_retrieve(hashtable, key))
    return rec_func()


                
