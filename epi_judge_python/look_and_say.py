from test_framework import generic_test


def look_and_say(n):
    answer = ""
    print(n)
    for i in range(0, n):
        answer += "1    "
    return answer


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("look_and_say.py", "look_and_say.tsv",
                                       look_and_say))
