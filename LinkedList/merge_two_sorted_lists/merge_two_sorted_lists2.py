# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        #creating lists for ll
        list1 = []
        list2 = []

        if not l1 and not l2:
            return (None)
        #appending ll to these lists
        ptr = l1
        while ptr:
            list1.append(ptr) #SC size(l1) TC size(l1)
            ptr = ptr.next
        ptr = l2
        while ptr:
            list2.append(ptr) #SC size(l2) TC size(l2)
            ptr = ptr.next

        #appending 2 lists to new list
        newList = [] #return head.next
        list1r = list1[::-1] #SC size(l1)
        list2r = list2[::-1] #SC size(l1)
        while list1r or list2r:
            if list1r and list2r:
                newList.append(list1r.pop() if list1r[-1].val < list2r[-1].val else list2r.pop()) #TC size(l1) + size(l2) SC = size(l1) + size(l2)
            elif list1r:
                newList.append(list1r.pop())
            else:
                newList.append(list2r.pop())

        #tying together ll
        for i in range(len(newList) - 1):
            newList[i].next = newList[i + 1] #TC n

        #setting last elem to None
        newList[-1].next = None
        return (newList[0])

        #TC size(l1) + size(l2)
        #SC size(l1) + size(l2)
