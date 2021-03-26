# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        ptr = head
        if not ptr: #0 nodes
            return (head)
        if not ptr.next: #1 node
            return (head)
        firsttime = True
        newhead = 0
        while (head.next):
            while (ptr.next.next):
                ptr = ptr.next
            if firsttime:
                newhead = ptr.next
                firsttime = False
            ptr.next.next = ptr
            ptr.next = None
            ptr = head
        return (newhead)
