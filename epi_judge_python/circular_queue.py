from test_framework import generic_test
from test_framework.test_failure import TestFailure
from collections import deque


class Queue:
    # arr = deque()
    arr = []
    def __init__(self, capacity):
        # TODO - you fill in here.
        return

    def enqueue(self, x):
        # self.arr.append(x)
        self.arr.append(x)
        return

    def dequeue(self):
        return self.arr.pop(0)

    def size(self):
        return len(self.arr)


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure(
                    "Dequeue: expected " + str(arg) + ", got " + str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure(
                    "Size: expected " + str(arg) + ", got " + str(result))
        else:
            raise RuntimeError("Unsupported queue operation: " + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("circular_queue.py",
                                       'circular_queue.tsv', queue_tester))
