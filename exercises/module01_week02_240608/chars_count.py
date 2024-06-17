from collections import Counter


def count_chars(s: str):
    counted_chars = Counter(list(s))
    return dict(counted_chars)


if __name__ == "__main__":

    input_str = input("Input string: s = ")
    counted_chars = count_chars(input_str)
    print(counted_chars)
