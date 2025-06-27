class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None
    def insert_at_last(self,data):
        if self.head is None:
            node=Node(data,None)
            self.head=node
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)

    def print(self):
        if self.head is None:
            print("Print 0 ele")
            return
        itr=self.head
        ans=''
        while itr:
            ans+=str(itr.data)+"-->" if  itr.next else str(itr.data)
            itr=itr.next
        print(ans)
        return
    def add_list(self,data_list):
        self.head=None
        for data in data_list:
            self.insert_at_last(data)

    def remove_dupicates(self):
        itr=self.head
        while itr is not None and itr.next is not None:
            if itr.data == itr.next.data:
                itr.next=itr.next.next
            else:
                itr=itr.next



if __name__=='__main__':
    l=LinkedList()
    l.add_list([1,1,1,2,2,4,4,5,5])
    l.remove_dupicates()
    l.print()

