from linkedStack import LinkedStack

class parenBalanceChecker:
    def __init__(self):
        self.__stack = LinkedStack()
    
    def parenBalance(self, s) -> bool:
        left = 0
        right = 0

        for i in range(len(s)):
            if s[i] == '(':
                left += 1
            if s[i] == ')':
                right += 1
        print(left, right)
            
        return left == right

if __name__ == "__main__":
    s1 = "(asdf)asd(fds)((fh))ghk()tk))(()((()"
    s2 = "()"
    checker = parenBalanceChecker()
    #stck = checker.parenBalance(s1)
    stck = checker.parenBalance(s2)
    if stck == True:
        print("True")
    else:
        print("False")
