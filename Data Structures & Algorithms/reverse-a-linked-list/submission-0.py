# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
dummy -> head -> node -> node -> node -> null
curr.prev <- curr


'''

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        currPrev = None
        curr = head
        
        while curr:
            temp = curr.next
            curr.next = currPrev
            currPrev = curr
            curr = temp
        return currPrev

            
