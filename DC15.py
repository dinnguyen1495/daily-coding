# Daily Coding 15
# Given a stream of elements too large to store in memory, pick a random element from the stream with 
# uniform probability. (Problem is: we don't always know the length of the stream, it could be very big)

# Algorith: Reservoir sampling

import random

def stream_of_elements(N):
    for i in range(N):
        yield i

def pick_up_one(stream):
    memory = None

    for key, item in enumerate(stream):
        if key == 0:
            memory = item
        elif random.randint(0, key) == 0:
            memory = item
    return memory
            
def pick_up_many(capacity, stream):
    memory = list()

    for key, item in enumerate(stream):
        if key < capacity:
            memory.append(item)
        else:
            replaced_position = random.randint(0, key)
            if replaced_position < capacity:
                memory[replaced_position] = item
    return memory
    
print(pick_up_one(stream_of_elements(10000)))
print(pick_up_many(10, stream_of_elements(10000)))