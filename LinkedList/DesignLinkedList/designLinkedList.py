class Node:
    def __init__(self, value=None):
        self.val = value
        self.next = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val = None
        self.next = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        indCounter = 0
        node = self
        while (indCounter < index):
            if (node.next):
                node = node.next
                indCounter += 1
            else:
                return (-1)
        if (indCounter == index and node.next):
            return (node.next.val)
        else:
            return (-1)

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        ptr = self
        newNode = Node(val)
        newNode.next = ptr.next
        ptr.next = newNode

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        ptr = self
        newNode = Node(val)
        while (ptr.next != None):
            ptr = ptr.next
        ptr.next = newNode
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        counter = 0
        ptr = self
        while (counter < index):
            if ptr.next:
                ptr = ptr.next
            else:
                return 
            counter += 1
        if counter == index: #don't check if ptr.next here - if it is not the end of the list, you would have had a problem in the above while loop!
            node = Node(val)
            node.next = ptr.next
            ptr.next = node


    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        ptr = self
        counter = 0
        while (counter < index):
            if (ptr.next):
                ptr = ptr.next
                counter += 1
            else:
                return
        if (counter == index):
            if (ptr.next):
                temp = ptr.next.next
                ptr.next.next = None
                ptr.next = temp
                
    def printList(self) -> None:
        print("HI")
        ptr = self
        while (ptr != None):
            print(ptr.val, end = " ")
            ptr = ptr.next
        print()

head = MyLinkedList()
head.addAtHead(7)
head.addAtHead(2)
head.addAtHead(1)
head.addAtIndex(3,0)
head.deleteAtIndex(2)
head.addAtHead(6)
head.addAtTail(4)
head.printList()
head.deleteAtIndex(1)
head.printList()
print(head.get(1))
#head.printList()

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
