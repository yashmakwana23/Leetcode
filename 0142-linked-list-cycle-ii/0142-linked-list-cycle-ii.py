# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return None

        hasha={}
        z=0
        prev=ListNode(0,head)
        pointer=head
        while pointer:
            if pointer not in hasha:
                hasha[pointer]=prev
                z+=1
                prev=pointer
                pointer=pointer.next
            else:
                if hasha.get(pointer)!=prev:
                    return pointer
                
        return None