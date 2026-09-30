class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        nums = [1, 2, 3, 3]
        
        hashmap: [key: value]

        key = index
        value = num of times it appears

        (0: 1, 1: 1, 2: 2)

        iterate once through the array 

        iterate twice through key, value to see if anything is > 1 and return false

        O(N) - to create the hashmap, iterate through the items

        """
        
        # num_lst = dict(nums)
        num_lst = {}

        for num in nums:
            num_lst[num] = num_lst.get(num, 0) + 1
            
        for key, value in num_lst.items():
            if value > 1:
                return True
        return False
