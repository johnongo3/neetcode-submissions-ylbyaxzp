# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        i = 0
        total = 0
        while l1 and l2:
            iSum = l1.val * (10 ** i) + l2.val * (10 ** i)
            l1 = l1.next
            l2 = l2.next
            i += 1
            total += iSum

        while l1:
            iSum = l1.val * (10 ** i)
            total += iSum
            l1 = l1.next
            i += 1
        
        while l2:
            iSum = l2.val * (10 ** i)
            total += iSum
            l2 = l2.next
            i += 1

        reversed_str = reversed(str(total))

        dummy = ListNode()
        curr = dummy

        for digit in reversed_str:
            curr.next = ListNode(int(digit))
            curr = curr.next

        return dummy.next
