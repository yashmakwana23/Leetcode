# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head==None:
            return head

        tempNode= ListNode(51,head)
        currpointer=tempNode.next
        prevpointer=tempNode
        while (currpointer != None):
            if currpointer.val == val:
                prevpointer.next=currpointer.next
                currpointer=currpointer.next
            else:
                currpointer=currpointer.next
                prevpointer=prevpointer.next
        return tempNode.next

