class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None

    def add_at_beginning(self,value):
        node=Node(value,self.head)
        self.head=node

    def add_at_end(self,value):
        if self.head is None:
            self.add_at_beginning(value)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(value,None)


    def print(self):
        itr=self.head
        ans=''
        while itr:
            ans+=str(itr.data)+'-->'
            itr=itr.next
        print(ans)
        return

if __name__=='__main__':
    ll=LinkedList()
    ll.add_at_beginning(5)
    ll.add_at_end(5)
    ll.add_at_end(15)
    ll.add_at_beginning(20)
    ll.print()