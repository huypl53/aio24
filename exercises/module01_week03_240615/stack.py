from typing import List


class Stack:
    def __init__(self, capacity: int) -> None:
        self._capcacity = capacity
        self._data: List[int] = []

    def is_empty(self) -> bool:
        return not bool(len(self._data))

    def is_full(self) -> bool:
        return len(self._data) == self._capcacity

    def pop(self) -> int:
        return self._data.pop()

    def push(self, v: int):
        if self.is_full():
            print("Stack is full")
        else:
            self._data.append(v)

    def top(self) -> int:
        return self._data[-1]


if __name__ == "__main__":
    stack1 = Stack(capacity=5)
    stack1.push(1)
    stack1.push(2)
    print(stack1.is_full())
    print(stack1.top())
    print(stack1.pop())
    print(stack1.top())
    print(stack1.pop())
    print(stack1.is_empty())
