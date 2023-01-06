# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev= ListNode(0,head)
        slowpointer=head
        fasterpointer=head
        while fasterpointer and fasterpointer.next:
            fasterpointer=fasterpointer.next.next
            slowpointer=slowpointer.next
        
        return slowpointer