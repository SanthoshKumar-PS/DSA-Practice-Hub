class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None

    def get_length(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count

    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return
        itr=self.head
        string=''
        while itr:
            string+=str(itr.data)+'-->' if itr.next else str(itr.data)
            itr=itr.next
        print(string)


    def add_at_begginning(self,data):
        node=Node(data,self.head)
        self.head=node

    def add_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)

    def add_at(self,index,data):
        if index<0 or index>self.get_length():
            print("------Error-----")
            return
        if index==0:
            self.add_at_begginning(data)
            return
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                node=Node(data,itr.next)
                itr.next=node
                break
            count+=1
            itr=itr.next

    def remove_at(self,index):
        if index<0 or index>self.get_length():
            print("Index out of bounds")
            return
        if index==0:
            self.head=self.head.next
            return
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                itr.next=itr.next.next

            count+=1
            itr=itr.next




if __name__=='__main__':
    ll=LinkedList()
    ll.add_at_begginning(10)
    ll.add_at_begginning(15)
    ll.add_at_end(20)
    ll.get_length()
    ll.add_at(2,5)
    ll.print()
    ll.remove_at(0)
    ll.print()
    ll.remove_at(1)
    ll.print()

