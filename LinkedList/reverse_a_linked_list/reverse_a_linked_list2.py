# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return (head)
        if not head.next:
            return (head)
        listOfNodes = [] #n SC
        ptr = head #1 SC
        while (ptr):
            listOfNodes.append(ptr) #n TC
            ptr = ptr.next
        for i in range(len(listOfNodes) - 1, 0, -1): #don't want to set the last node to anything
            listOfNodes[i].next = listOfNodes[i - 1] #n - 1 TC
        listOfNodes[0].next = None
        return(listOfNodes[-1])
#TOTAL TC: O(n), SC: O(n)
