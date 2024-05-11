# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            value = v1 + v2 + carry
            carry = value // 10
            value = value % 10

            cur.next = ListNode(value)
            cur = cur.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next

# Example usage
sol = Solution() 
l1 = ListNode(5)
l1.next = ListNode(6)
l1.next.next = ListNode(7)

l2 = ListNode(5)
l2.next = ListNode(5)

result = sol.addTwoNumbers(l1, l2)