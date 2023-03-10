top=0
item=1
mymax=eval(input("Enter Maximum size of stack:")) 
def createStack():
    stack=[] 
    return stack 
def isEmpty(stack): 
    return len(stack)==0 
def Push(stack,item): 
    stack.append(item) 
print("Pushed to stack",item) 
def Pop(stack):
     if isEmpty(stack): 
        return "stack underflow" 
     return stack.pop()
stack=createStack() 
while True: 
 print("1.Push") 
 print("2.Pop") 
 print("3.Display") 
 print("4.Quit")
 ch=int(input("Enter your choice:"))
 if ch==1:
     if top <mymax:
         item=input("Enter any elements:")
         Push(stack,item)
         top+=1
     else:
         print("Stack overflow")
 elif ch==2:
          print(Pop(stack))
 elif ch==3:
          print(stack) 
 else:
         print("Exit")
         break
