# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        remove_set = set(nums)

        dummy = ListNode(0)
        dummy.next = head

        current = dummy
        while current.next:
            if current.next.val in remove_set:
                current.next = current.next.next  
            else:
                current = current.next 

        return dummy.next
        