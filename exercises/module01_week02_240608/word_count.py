import os
from collections import Counter
from typing import Dict


def preprocess_text(text: str) -> str:
    s = text.lower().strip()
    return s


def read_file(path: str) -> str:
    f = open(path)
    text = f.read()
    f.close()
    return text


def get_word_count(text: str) -> Dict[str, int]:
    words = text.split()
    word_count = dict(Counter(words))
    return word_count


if __name__ == "__main__":
    input_file_path = input("Input file path: ")
    if not os.path.isfile(input_file_path):
        print(f"{input_file_path} not existed...")

    text = read_file(input_file_path)
    text = preprocess_text(text)
    word_count = get_word_count(text)
    print(word_count)
