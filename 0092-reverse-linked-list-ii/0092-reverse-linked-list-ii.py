class Solution:
    def reverseBetween(self, head, left: int, right: int):
        dummy = prev = ListNode(0, head)
        for _ in range(left - 1):
            prev = prev.next
        cur = prev.next
        for _ in range(right - left):
            nxt = cur.next
            cur.next = nxt.next
            nxt.next = prev.next
            prev.next = nxt
        return dummy.next
