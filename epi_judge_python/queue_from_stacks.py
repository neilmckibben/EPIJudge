from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
    stack = []
    def enqueue(self, x: int) -> None:
        self.stack.append(x)
        return

    def dequeue(self) -> int:
        temp = []
        while len(self.stack) != 1:
            temp.append(self.stack.pop())
        val = self.stack.pop()
        while temp:
            self.stack.append(temp.pop())
        return val


def queue_tester(ops):
    try:
        q = Queue()

        for (op, arg) in ops:
            if op == 'Queue':
                q = Queue()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure('Dequeue: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported queue operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('queue_from_stacks.py',
                                       'queue_from_stacks.tsv', queue_tester))
