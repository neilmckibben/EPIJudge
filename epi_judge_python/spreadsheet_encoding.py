from test_framework import generic_test


def ss_decode_col_id(col: str) -> int:
    sum = 0
    for i in range(0, len(col)):
        sum += (ord(col[~i]) - 64) * (26 ** i)
    return sum


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spreadsheet_encoding.py',
                                       'spreadsheet_encoding.tsv',
                                       ss_decode_col_id))
