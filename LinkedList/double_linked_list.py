class Node:
    def __init__(self,data=None,next=None,prev=None):
        self.data=data
        self.prev=prev
        self.next=next

class DoubleLinkedList:
    def __init__(self):
        self.head=None

    def insert_at_begin(self,data):
        if self.head is None:
            node = Node(prev=None, data=data, next=self.head)
            self.head = node
        else:
            node=Node(prev=None,data=data,next=self.head)
            self.head.prev=node
            self.head=node

    def instert_at_end(self,data):
        if self.head is None:
            node=Node(data,self.head,None)
            self.head=node
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None,itr)


    def print_selfforward(self):
        itr=self.head
        ans=''
        while itr:
            ans+=str(itr.data) +"-->" if itr.next else str(itr.data)
            itr=itr.next
        print(ans)

    def print_selfbackward(self):
        if self.head is None:
            print("0 elements found")
            return
        node=self.head
        while node.next:
            node=node.next
        ans=''
        while node:
            ans+=str(node.data)+'-->'  if node.prev else str(node.data)
            node=node.prev
        print(ans)
        return ans



if __name__=='__main__':
    ll=DoubleLinkedList()
    ll.insert_at_begin(5)
    ll.insert_at_begin(10)
    ll.insert_at_begin(15)
    ll.insert_at_begin(20)
    ll.print_selfforward()
    ll.print_selfbackward()


