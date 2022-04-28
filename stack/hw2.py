class ListStack:
    def __init__(self):
        self.__stack = []
    
    def push(self, x):
        self.__stack.insert(0, x)
        #self.__stack.append(x)
    
    def pop(self):
        return self.__stack.pop(0)
        #return self.__stack.pop()
    
    def top(self):
        if self.isEmpty():
            print("No element in stack")
            return None
        else:
            return self.__stack[0]
            #return self.__stack[-1]

    def isEmpty(self) -> bool:
        return not bool(self.__stack)
    
    def popAll(self):
        self.__stack.clear()

    def printStack(self):
        print("Stack: ")
        for i in range(len(self.__stack)):
            print('stack[', i, ']:', self.__stack[i])

##Debugging
lst = ListStack()
lst.push(1)
lst.push(2)
lst.push(3)
lst.printStack()
lst.pop()
lst.printStack()
