class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None

    def getlength(self):
        if self.head is None:
            return 0
        itr=self.head
        count=0
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
            string+=str(itr.data)+ "-->" if itr.next else str(itr.data)
            itr=itr.next
        print(string)
        return string

    def insert_at_end(self,data):
        if self.head is None:
            node=Node(data,None)
            self.head=node
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)

    def insert_values(self,data_list):
        self.head=None
        for data in data_list:
            self.insert_at_end(data)

    def insert_after_value(self,before,value):
        itr=self.head
        while itr:
            if itr.data==before:
                itr.next=Node(value,itr.next)
                return
            itr=itr.next

    def remove_at(self,index):
        if index<0 or index>self.getlength():
            print("Length is small")
            return
        if index==1:
            self.head=self.head.next
            return
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                itr.next=itr.next.next
            count+=1
            itr=itr.next

    def remove_by_value(self,value):
        if self.head is None:
            print("There is no value in list")
            return

        if self.head.data==value:
            self.head=self.head.next
            return
        itr=self.head
        while itr.next:
            if itr.next.data==value:
                itr.next=itr.next.next
                return
            itr=itr.next





if __name__=='__main__':
    ll=LinkedList()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.print()
    ll.insert_after_value("mango", "apple")  # insert apple after mango
    ll.print()
    ll.remove_by_value("grapes")  # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    print("----")
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()

# ll = LinkedList()
# ll.print()
# ll.insert_after_value("mango", "apple")  # insert apple after mango
# ll.print()
# ll.remove_by_value("orange")  # remove orange from linked list
# ll.print()
# ll.remove_by_value("figs")
# ll.print()
# ll.remove_by_value("banana")
# ll.remove_by_value("mango")
# ll.remove_by_value("apple")
# ll.remove_by_value("grapes")
# ll.print()