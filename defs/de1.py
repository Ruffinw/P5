import random

def push(queue, value):
    queue.append(value)

def pop(queue):
    try:
        return queue.pop()
    except IndexError:
        print("queue is empty")

def lastItem(queue):
    print(queue[len(queue) - 1])

def lenStack(queue):
    return len(queue)
#####################
queue = []
print(queue)

for i in range(10):
    push(queue, i)
print(queue)
queue.reverse()
print(pop(queue))
print(queue) 