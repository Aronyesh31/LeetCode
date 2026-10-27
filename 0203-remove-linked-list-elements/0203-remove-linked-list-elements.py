class Solution:
    def removeElements(self, head, val: int):
        dummy = cur = ListNode(0, head)
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next
