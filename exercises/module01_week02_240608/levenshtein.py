import numpy as np


def levenshtein_by_matrix(src_str: str, trg_str: str):
    if not src_str:
        print(len(trg_str))
        exit()

    if not trg_str:
        print(len(src_str))
        exit()

    src_list = ["#"] + list(src_str)
    trg_list = ["#"] + list(trg_str)
    src_len = len(src_list)
    trg_len = len(trg_list)

    leven_matrix = [[0] * trg_len for _ in range(src_len)]

    for i in range(1, src_len):
        leven_matrix[i][0] = i

    for i in range(1, trg_len):
        leven_matrix[0][i] = i

    for i in range(1, src_len):
        for j in range(1, trg_len):
            insert_cost = leven_matrix[i][j - 1] + 1
            delete_cost = leven_matrix[i - 1][j] + 1

            subs_cost = leven_matrix[i - 1][j - 1] + (
                0 if src_list[i] == trg_list[j] else 1
            )
            leven_matrix[i][j] = min(insert_cost, delete_cost, subs_cost)

    return leven_matrix[-1][-1]


def levenshtein_recursive(src_str: str, trg_str: str):
    len_str1 = len(src_str)
    len_str2 = len(trg_str)
    if len_str1 == 0:
        return len_str2
    if len_str2 == 0:
        return len_str1
    if src_str[len_str1 - 1] == trg_str[len_str2 - 1]:
        return levenshtein_recursive(src_str[:-1], trg_str[:-1])
    return 1 + min(
        # Insert
        levenshtein_recursive(src_str, trg_str[:-1]),
        min(
            # Remove
            levenshtein_recursive(src_str[:-1], trg_str),
            # Replace
            levenshtein_recursive(src_str[:-1], trg_str[:-1]),
        ),
    )


if __name__ == "__main__":
    src_str = input("Input source string: ")
    trg_str = input("Input target string: ")

    print("levenshtein_by_matrix: ", levenshtein_by_matrix(src_str, trg_str))
    print("levenshtein_recursive: ", levenshtein_recursive(src_str, trg_str))
