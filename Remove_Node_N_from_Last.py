
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def removeNthFromEnd(self, head: [ListNode], n: int) -> [ListNode]:

        dummy = ListNode()
        first = ListNode()
        # Second = ListNode()
        dummy.next = head
        first = dummy
        # second = dummy.next()
        length = 0
        while (first.next):
            first = first.next
            length += 1

        first = dummy

        for i in range(length - n):
            first = first.next

        first.next = first.next.next

        return dummy.next


class Solution2:
    def removeNthFromEnd(self, head: [ListNode], n: int) -> [ListNode]:
        dummy = ListNode()
        dummy.next = head
        first = dummy
        second = dummy

        for i in range(n):
            second = second.next

        while (second.next):
            first = first.next
            second = second.next

        first.next = first.next.next

        return dummy.next
