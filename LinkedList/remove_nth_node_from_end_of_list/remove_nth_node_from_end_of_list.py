# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode()
        dummy.val = head.val
        dummy.next = head.next
        head.next = dummy
        ptr1 = head
        ptr2 = head
        for i in range(n + 1):
            ptr2 = ptr2.next
        while (ptr2):
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        temp = ptr1.next.next
        ptr1.next.next = None
        ptr1.next = temp
        return (head.next)
