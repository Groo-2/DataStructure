class TwoStackQueue:
    def __init__(self):
        self.__s = []
        self.__ts = []

    def __move_element__(self, s, ts):
        while not s == []:
            ts.append(s.pop())

    def enqueue(self, x):
        self.__s.append(x)

    def dequeue(self):
        if self.__ts == []:
            self.__move_element__(self.__s, self.__ts)
        
        return self.__ts.pop()


sq = TwoStackQueue()
sq.enqueue(1)
sq.enqueue(2)
sq.enqueue(3)

print(sq.dequeue())
print(sq.dequeue())
print(sq.dequeue())
