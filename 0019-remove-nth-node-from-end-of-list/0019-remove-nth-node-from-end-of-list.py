class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy=ListNode(0, head)
        left=dummy
        right=head
        while n>0 and right:
            right=right.next
            n-=1
        while right:
            right=right.next
            left=left.next
        left.next=left.next.next
        return dummy.next
        