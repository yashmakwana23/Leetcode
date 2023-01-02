# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head ==None or head.next ==None:
            return None

        slow = head #1
        fast= head.next.next #2

        while fast!=None and fast.next!=None:
            slow=slow.next #2 #3
            fast=fast.next.next #46

        slow.next = slow.next.next
        return head