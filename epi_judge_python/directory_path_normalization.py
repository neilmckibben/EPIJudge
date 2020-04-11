from test_framework import generic_test


def shortest_equivalent_path(path: str) -> str:
    path = path.split("/")
    list_path = []
    for movement in path:
        if movement == "..":
            if len(list_path) == 0 or list_path[-1] == "..":
                list_path.append("..")
            else:
                list_path.pop()
        elif movement != ".":
            list_path.append(movement)

    if list_path[-1] == "":
        list_path = list_path[:-1]
    answer_path = functools.reduce(lambda a, b: a + "/" + str(b), list_path)

    return answer_path


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('directory_path_normalization.py',
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
