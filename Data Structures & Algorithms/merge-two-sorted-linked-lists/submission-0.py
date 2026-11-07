# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
compare the two values from each of the lists for whichever is less than. if none then they are both equal

Time Complexity: O(n) - build
space O( n ) 
'''
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        curr = dummy

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        
        # if one of the lists are not done yet
        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2
        return dummy.next