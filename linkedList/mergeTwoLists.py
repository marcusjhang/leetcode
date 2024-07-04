# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val < list2.val:
            curr = list1
            lil = list1.next
            big = list2
        else:
            curr = list2
            lil = list2.next
            big = list1
        
        curr.next = self.mergeTwoLists(lil, big)
        return curr
