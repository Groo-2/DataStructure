from LinkedQueue import*

class TwoQueueStack:
    def __init__(self):
        self.__q = LinkedQueue()
        self.__tq = LinkedQueue()
        self.numItems = 0

    def push(self, x):
        self.__q.enqueue(x)
        self.numItems += 1

    def pop(self):
        if self.__q.isEmpty():
            return None

        size = self.numItems

        while size != 1:
            self.__tq.enqueue(self.__q.dequeue())
            size -= 1

        self.numItems -= 1

        last = self.__q.dequeue()
        
        self.__q, self.__tq = self.__tq, self.__q
        return last


st = TwoQueueStack()
st.push(1)
st.push(2)
st.push(3)
print(st.pop())
print(st.pop())
print(st.pop())
