from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Stack:
    array = []
    max_arr = []

    def empty(self) -> bool:
        if len(self.array) != 0:
            return False
        return True

    def max(self) -> int:
        if len(self.max_arr) != 0:
            self.max_arr.sort()
            return self.max_arr[-1]
        return 0

    def pop(self) -> int:
        value = self.array.pop()
        self.max_arr.remove(value)
        return value

    def push(self, x: int) -> None:
        self.array.append(x)
        self.max_arr.append(x)


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure('Pop: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure('Empty: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported stack operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('stack_with_max.py',
                                       'stack_with_max.tsv', stack_tester))
