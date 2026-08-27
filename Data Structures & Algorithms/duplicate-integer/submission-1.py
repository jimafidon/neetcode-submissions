class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #run through a loop in nums
        #add values inside the set 
        #check if a value is in the set, return tru
        my_set = set()
        for num in nums:
            if num in my_set:
                return True
            else:
                my_set.add(num)
        return False

        