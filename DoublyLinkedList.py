class Node: 
    def __init__(self,data): 
        self.data=data 
        self.next=self.prev=None
class DLinkedList: 
    def __init__(self): 
        self.head=None 
        self.ctr=0 
    def insert_beg(self,data): 
        node=Node(data) 
        if self.head==None: 
            self.head=node 
        else: 
            node.next=self.head 
            self.head.prev=node 
            self.head=node 
        self.ctr +=1 
        print("Nodes inserted",data) 
        return
    def insert_end(self,data): 
        node=Node(data) 
        if self.head==None: 
            self.head=node 
        else: 
            temp=self.head 
            while(temp.next is not None): 
                temp=temp.next 
            temp.next=node 
            node.prev=temp 
        self.ctr +=1 
        print("Node inserted",data) 
        return
    def delete_beg(self): 
        if self.head==None: 
            print("No node exist") 
        else: 
            print("Node deleted",self.head.data) 
            self.head=self.head.next 
            self.head.prev=None 
            self.ctr -=1 
        return
    def delete_end(self): 
        if self.head==None: 
            print("No nodes exist") 
        elif self.ctr==1: 
            self.ctr=0 
            print ("Node deleted",self.head.data) 
            self.head=None 
        else: 
            temp=self.head 
            while temp.next is not None: 
                temp=temp.next 
            print("Node deleted",temp.data) 
            temp=temp.prev 
            temp.next=None 
            self.ctr -=1
        return 
    def insert_pos(self,pos,data): 
        if pos==0: 
            self.insert_beg(data) 
        elif pos==self.ctr: 
            self.insert_end(data) 
        else: 
            node=Node(data) 
            temp=self.head 
            i=1 
            while i<pos-1: 
                temp=temp.next 
                i +=1 
            node.next=temp.next 
            temp.next.prev=node 
            temp.next=node 
            node.prev=temp 
            self.ctr +=1 
            print("Node inserted",data) 
        return 
    def delete_pos(self,pos): 
        if self.head==None: 
            print("Node is empty") 
        else: 
            if pos==0: 
                self.delete_beg() 
            elif pos==self.ctr: 
                self.delete_end() 
            else: 
                temp=self.head 
                i=0 
                while i<pos: 
                    temp=temp.next 
                    i+=1 
                print("node deleted",temp.data) 
                temp.prev.next=temp.next 
                temp.next.prev=temp.prev 
                temp.next=None 
                temp.preve=None 
                self.ctr -=1 
            return 
    def traverse_f(self): 
        if self.head==None:
            print("No nodes exist") 
        temp=self.head 
        i=0 
        while i<self.ctr: 
            print(temp.data)
            temp=temp.next 
            i+=1 
        return 
    def traverse_r(self):
        if self.head==None: 
            print("No nodes exist") 
        temp=self.head 
        while temp.next is not None: 
            temp=temp.next 
        while temp is not None: 
            print(temp.data) 
            temp=temp.prev 
def menu():
    print("1.Insert at beginning") 
    print("2.Insert at position") 
    print("3.Insert at end") 
    print("4.Delete at beginning") 
    print("5.Delete at position") 
    print("6.Delete at end") 
    print("7.Count no of nodes") 
    print("8.Traverse forward")     
    print("9.Traverse reverse") 
    print("10.Quit") 
    ch=eval(input("Enter choice:")) 
    return ch
print("******************Double linked list**************") 
d=DLinkedList() 
while True : 
    ch=menu() 
    if ch==1: 
        data=eval(input("Enter data:")) 
        d.insert_beg(data) 
    elif ch==2: 
        data=eval(input("Enter data:")) 
        pos=int(input("Enter position:")) 
        d.insert_pos(pos,data) 
    elif ch==3: 
        data=eval(input("Enter data:")) 
        d.insert_end(data) 
    elif ch==4: 
        d.delete_beg() 
    elif ch==5: 
        pos=int(input("Enter position:")) 
        d.delete_pos(pos) 
    elif ch==6: 
        d.delete_end() 
    elif ch==7: 
        print("Number of nodes",d.ctr) 
    elif ch==8: 
        d.traverse_f() 
    elif ch==9: 
        d.traverse_r() 
    else: 
        print("Exit") 
        break
