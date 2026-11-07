# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
Brute force:
iterate through a linked list and if it never points to null then its a cycle

problem: could create infinite loop if its never null


need a check if pointer points to a previous index its a circular.

maybe we can keep a tuple list that keeps track of index and node/pointer
'''

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        # index = 0
        # my_tuple = (index, curr)
        # check_list = [my_tuple]
        check_list = set()

        while curr:
            if curr in check_list:
                return True
            check_list.add(curr)                
            curr = curr.next
        return False

        