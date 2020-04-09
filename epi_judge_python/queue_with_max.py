from test_framework import generic_test
from test_framework.test_failure import TestFailure
from heapq import *


class QueueWithMax:
    max_vals = []
    values = []
    def enqueue(self, x):
        self.values.append(x)
        heappush(self.max_vals, ~x)
        return

    def dequeue(self):
        val = self.values.pop(0)
        self.max_vals.remove(~val)
        heapify(self.max_vals)
        return val

    def max(self):
        return ~self.max_vals[0]


def queue_tester(ops):

    try:
        q = QueueWithMax()

        for (op, arg) in ops:
            if op == 'QueueWithMax':
                q = QueueWithMax()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure("Dequeue: expected " + str(arg) +
                                      ", got " + str(result))
            elif op == 'max':
                result = q.max()
                if result != arg:
                    raise TestFailure(
                        "Max: expected " + str(arg) + ", got " + str(result))
            else:
                raise RuntimeError("Unsupported queue operation: " + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("queue_with_max.py",
                                       'queue_with_max.tsv', queue_tester))
