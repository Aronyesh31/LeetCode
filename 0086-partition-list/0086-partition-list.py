class Solution:
    def partition(self, head, x: int):
        small = s_tail = ListNode()
        large = l_tail = ListNode()
        while head:
            if head.val < x:
                s_tail.next = s_tail = head
            else:
                l_tail.next = l_tail = head
            head = head.next
        l_tail.next = None
        s_tail.next = large.next
        return small.next
