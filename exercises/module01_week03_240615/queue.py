from typing import List


class Queue:
    def __init__(self, capacity: int) -> None:
        self._capacity = capacity
        self._data: List[int] = []
        pass

    def is_empty(self):
        return not bool(len(self._data))

    def is_full(self):
        return len(self._data) == self._capacity

    def dequeue(self) -> int | None:
        if not self.is_empty():
            return self._data.pop(0)
        return None

    def enqueue(self, v: int):
        self._data.append(v)

    def front(self):
        if not self.is_empty():
            return self._data[0]
        return None


if __name__ == "__main__":
    queue1 = Queue(capacity=5)
    queue1.enqueue(1)
    queue1.enqueue(2)
    print(queue1.is_full())
    print(queue1.front())
    print(queue1.dequeue())
    print(queue1.front())
    print(queue1.dequeue())
    print(queue1.is_empty())
