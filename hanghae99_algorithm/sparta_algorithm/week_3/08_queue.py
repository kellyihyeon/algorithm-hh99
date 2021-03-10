class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_node = Node(value)      #[3]만들기

        if self.is_empty():
            self.head = new_node
            self.tail = new_node

        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if self.is_empty():
            return "Queue is Empty"

        # [4]->[2]->[3]
        delete_head = self.head     # [4] 노드가 저장
        self.head = self.head.next

        return delete_head.data     # 노드에 들어있는 값 4만 반환

    def peek(self):
        if self.is_empty():
            return "Queue is Empty"
        return self.head.data

    def is_empty(self):
        return self.head is None

queue = Queue()
queue.enqueue(3)
print(queue.peek())
queue.enqueue(4)
print(queue.peek())
queue.enqueue(5)
print(queue.dequeue())
print(queue.peek())
print(queue.is_empty())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.is_empty())

