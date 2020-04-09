from test_framework import generic_test

symbols = ["+", "-", "/", "*"]


def evaluate(expression):
    arguments = expression.split(",")
    arguments.reverse()
    answer = process(arguments)
    return answer


def process(expression):
    values = []
    while len(expression) != 0:
        argument = expression.pop()
        if argument in symbols:
            if argument == "+":
                values.append(values.pop() + values.pop())
            elif argument == "-":
                front = values.pop()
                values.append(values.pop() - front)
            elif argument == "/":
                denom = values.pop()
                values.append(values.pop() // denom)
            else:
                values.append(values.pop() * values.pop())
        else:
            values.append(int(argument))
    return values.pop()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("evaluate_rpn.py", 'evaluate_rpn.tsv',
                                       evaluate))
