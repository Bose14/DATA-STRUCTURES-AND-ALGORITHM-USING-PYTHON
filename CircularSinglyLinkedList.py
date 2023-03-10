class Node:
    def __init__(self,data):
        self.next=None
        self.data=data
        print("Node Created",data)
class CLList:
    def __init__(self):
        self.head=None
        self.ctr=0
    def insert_beg(self,data):
        node=Node(data)
        if self.head==None:
            self.head=node
            node.next=self.head
        else:
            temp=self.head
            while temp.next is not self.head:
                temp=temp.next
            temp.next=node
            node.next=self.head
            self.head=node
        print("Node inserted",data)
        self.ctr+=1
        return
    def insert_end(self,data):
        node=Node(data)
        if self.head==None:
            self.head=node
            node.next=self.head
        else:
            temp=self.head
            while temp.next is not self.head:
                temp=temp.next
            temp.next=node
            node.next=self.head
        self.ctr+=1
        print("Node inserted",data)
        return
    def insert_inter(self,pos,data):
        node=Node(data)
        if pos>self.ctr:
            print("Invalid position")
        else:
            temp=self.head
            i=1
            while i<pos:
                temp=temp.next
                i+=1
            node.next=temp.next
            temp.next=node
            self.ctr+=1
            print("Node Inserted",data)
        return
    def delete_beg(self):
        if self.head==None:
            print("No Nodes exist")
        elif self.ctr==1:
            print("Node deleted",self.head.data)
            self.head=None
            self.ctr-=1
        else:
            print("Node deleted",self.head.data)
            temp=self.head
            while temp.next is not self.head:
                temp=temp.next
            self.head=self.head.next
            temp.next=self.head
            self.ctr-=1
        return
    def delete_end(self):
        if self.head==None:
            print("No nodes exist")
        elif self.ctr==1:
            print("Node deleted",self.head.data)
            self.head=None
            self.ctr-=1
        else:
            temp=self.head
            prev=temp
            while temp.next is not self.head:
                prev=temp
                temp=temp.next
            print("Node deleted",temp.data)
            prev.next=temp.next
            self.ctr-=1
        return
    def delete_inter(self,pos):
        if self.head==None:
            print("No nodes exist")
        elif pos>self.ctr:
            print("Invalid position")
        elif self.ctr==1:
            print("Node deleted",self.head.data)
            self.head=None
            self.ctr-=1
        else:
            temp=self.head
            prev=temp
            i=0
            while i<pos:
                prev=temp
                temp=temp.next
                i+=1
            prev.next=temp.next
            print("Node deleted",temp.data)
            self.ctr-=1
        return
    def traverse(self):
        temp=self.head
        i=0
        while i<self.ctr:
            print(temp.data)
            temp=temp.next
            i+=1
        return
def Menu():
    print("1.Insert beginning:")
    print("2.Insert at middle:")
    print("3.Insert at end:")
    print("4.Delete at beginning:")
    print("5.Delete at middle:")
    print("6.Delete at end:")
    print("7.Traverse Forward:")
    print("8.Numbers of nodes:")
    print("9.Exit")
    ch=int(input("Enter choice:"))
    return ch
c=CLList()
print("****Circular Linked List****")
while True:
    ch=Menu()
    if ch==1:
        data=input("Enter data:")
        c.insert_beg(data)
    elif ch==2:
        data=input("Enter data:")
        pos=int(input("Enter position:"))
        c.insert_inter(pos,data)
    elif ch==3:
        data=input("Enter data:")
        c.insert_end(data)
    elif ch==4:
        c.delete_beg()
    elif ch==5:
        pos=int(input("Enter position:"))
        c.delete_inter(pos)
    elif ch==6:
        c.delete_end()
    elif ch==7:
        c.traverse()
    elif ch==8:
        print("Number of Nodes:",c.ctr)
    else:
        print("Exit")
        break
