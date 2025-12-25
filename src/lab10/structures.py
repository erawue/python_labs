# Реализация Stack и Queue
from collections import deque

class Stack:
    
    def __init__(self):
        self._data = []
    
    def push(self, item):
        self._data.append(item)
    
    def pop(self):
        if not self._data:
            raise IndexError("Стек пуст")
        return self._data.pop()
    
    def peek(self):
        return self._data[-1] if self._data else None
    
    def is_empty(self):
        return len(self._data) == 0
    
    def __len__(self):
        return len(self._data)
    
    def __str__(self):
        return f"Stack({self._data})"


class Queue:
    def __init__(self):
        self._data = deque()
    
    def enqueue(self, item):
        self._data.append(item)
    
    def dequeue(self):
        if not self._data:
            raise IndexError("Очередь пуста")
        return self._data.popleft()
    
    def peek(self):
        return self._data[0] if self._data else None
    
    def is_empty(self):
        return len(self._data) == 0
    
    def __len__(self):
        return len(self._data)
    
    def __str__(self):
        return f"Queue({list(self._data)})"
    
if __name__ == "__main__":
    print(" Демонстрация работы стека ")
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"Стек: {stack}")
    print(f"Вершина: {stack.peek()}")
    print(f"Извлечено: {stack.pop()}")
    
    print("\n Демонстрация работы очереди ")
    queue = Queue()
    queue.enqueue('A')
    queue.enqueue('B')
    queue.enqueue('C')
    print(f"Очередь: {queue}")
    print(f"Первый: {queue.peek()}")
    print(f"Обработано: {queue.dequeue()}")