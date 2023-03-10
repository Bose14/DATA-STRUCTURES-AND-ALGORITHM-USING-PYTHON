front=0 
rear=0 
mymax=eval(input("Enter maximum size of queue:")) 
def createQueue():
    queue=[]
    return queue 
def isEmpty(queue):
    return len(queue)==0 
def enqueue(queue,item):
    queue.append(item)
    print("Enqueued to queue",item) 
def dequeue(queue):
    if isEmpty(queue):
        return "Queue is empty"
    item=queue[0]
    del queue[0]
    return item 
queue=createQueue() 
while True:
    print("1.Enqueue")
    print("2.Dequeue")
    print("3.Display")
    print("4.Quit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        if rear<mymax:
            item=input("Enter any elements:")
            enqueue(queue,item)
            rear+=1
        else:
                print("Queue is full")
    elif ch==2:
        print(dequeue(queue))
    elif ch==3:
        print(queue)
    else:
        print("Exit")
        break
