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
def postfix_eval(s): 
    s=s.split()
    n=len(s)
    stack =[] 
    for i in range(n):
        if s[i].isdigit():
            stack.append(int(s[i])) 
        elif s[i]=="+": 
            a=stack.pop()
            b=stack.pop()
            stack.append(int(a)+int(b))
        elif s[i]=="*": 
            a=stack.pop()
            b=stack.pop()
            stack.append(int(a)*int(b)) 
        elif s[i]=="/": 
            a=stack.pop()
            b=stack.pop()
            stack.append(int(b)/int(a))
        elif s[i]=="-": 
            a=stack.pop()
            b=stack.pop()
            stack.append(int(b)-int(a)) 
    return stack.pop()

def doMath(op,op1,op2): 
    if op == "^": 
        return op1 ^ op2 
    elif op == "*": 
        return op1 * op2 
    elif op == "/": 
        return op1 / op2 
    elif op == "//": 
        return op1 // op2 
    elif op == "+": 
        return op1 + op2 
    else: 
        return op1 - op2 
s=input("enter string:") 
val=postfix_eval(s) 
print("The value of postfix expression",s,"is",val)
