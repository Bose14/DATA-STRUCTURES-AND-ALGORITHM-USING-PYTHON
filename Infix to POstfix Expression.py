class Stack:
        def __init__(self):
                self.items = []
        def isEmpty(self):
                return self.items == []
        def push(self, item):
            self.items.append(item)
        def pop(self):
            return self.items.pop()
        def peek(self):
            return self.items[len(self.items)-1]
def size(self):
        return len(self.items)
def infix_postfix(infixexp):
                prec={}
                prec["^"]=4
                prec["*"]=3
                prec["/"]=3
                prec["+"]=2
                prec["-"]=2
                prec["("]=1
                opStack=Stack()
                postfixList=[]
                tokenList=infixexp.split()
                for token in tokenList:
                        if (token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or  token in
                            "abcdefghijklmnopqrstuvwxyz" or  token in "0123456789"):
                            postfixList.append(token)
                        elif token == '(':
                            opStack.push(token)
                        elif token == ')':
                            topToken = opStack.pop()
                            while topToken != '(':
                                postfixList.append(topToken)
                                topToken=opStack.pop()
                        else:
                            while (not opStack.isEmpty()) and \
                                    (prec[opStack.peek()]>=prec[token]):
                                            postfixList.append(opStack.pop())
                            opStack.push(token)
                while not opStack.isEmpty():
                        postfixList.append(opStack.pop())
                return " ".join(postfixList)
a=infix_postfix('A + B * C - D / E * H')
print("The postfix expression of infix expression A + B * C - D / E * H is \n",a)

