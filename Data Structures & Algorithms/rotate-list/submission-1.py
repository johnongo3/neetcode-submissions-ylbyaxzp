# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        # get the length, and tail node
        length, tail = 1, head
        while tail.next:
            tail = tail.next
            length += 1
        
        # get k modded
        k = k % length
        if k == 0:
            return head
        # traverse up to pivot, and perform the rotate
        curr = head
        for i in range(length - k - 1):
            curr = curr.next
        
        new_head = curr.next
        # set to tail
        curr.next = None
        tail.next = head
        return new_head