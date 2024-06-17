import random
from typing import List


def get_random_num_list(length: int, min_value=-100, max_value=100) -> List[int]:
    num_list = [random.randint(min_value, max_value) for _ in range(length)]
    return num_list


def get_slide_max_of_list(num_list: List[int], slide_size=3) -> List[int]:
    list_len = len(num_list)
    return [max(num_list[i : i + slide_size]) for i in range(list_len - slide_size + 1)]


if __name__ == "__main__":
    list_len = int(input("Input length of list: n = "))
    k = int(input("Input 1D slide window size: k = "))
    num_list = get_random_num_list(list_len)
    print(f"Input list: {num_list}")
    slide_max = get_slide_max_of_list(num_list, k)
    print(f"Output list: {slide_max}")
