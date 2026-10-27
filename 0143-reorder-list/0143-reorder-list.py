class Solution:
    def reorderList(self, head) -> None:
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        prev, cur = None, slow.next
        slow.next = None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        a, b = head, prev
        while b:
            a.next, a = b, a.next
            b.next, b = a, b.next
