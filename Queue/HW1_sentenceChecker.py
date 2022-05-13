from LinkedQueue import *

class sentenceChecker:
    def __init__(self):
        self.__queue = LinkedQueue()
    
    def is_included(self, s):
        idx = s.find('$')

        for i in range(idx):
            self.__queue.enqueue(s[i])

        for i in range(idx+1, len(s)):
            prev = self.__queue.dequeue()
            curr = s[i]
            print(prev, curr)

            if prev != curr:
                return False
        
        return self.__queue.isEmpty()
