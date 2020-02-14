#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    max = limit
    idx = 0
    for i in weights:
        hash_table_insert(ht, i, idx)
        idx += 1

    one = None
    count = 0
    for i in weights:
        one = hash_table_retrieve(ht, limit - i)
        if one is not None:
            zero = count
            if zero > one:
                return(zero, one)
            else:
                return(one, zero)
        count +=1


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
