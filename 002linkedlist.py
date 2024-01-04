class Node:

    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next



class LinkedList:
    def __init__(self):
        self.head=None

    def insert_at_beginning(self,data):
        node=Node(data,self.head)
        self.head=node
    def insert_at_end(self,data):
        if self.head==None:
            self.head==Node(data)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)
        
    def print(self):
        if self.head==None:
            print("Linked list is none")
            return
        else:
            current=self.head
            value=''
            while current:
                value+=str(current.data)+'-->'
                current=current.next
            print(value)



if __name__=="__main__":
    linked_list=LinkedList()
    linked_list.insert_at_beginning(5)
    linked_list.insert_at_beginning(10)
    linked_list.insert_at_beginning(15)
    linked_list.insert_at_end(1)
    linked_list.print()