class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        if sum of array > target:
            return

        if sum of array == target:
            append the copy into res.append(array.copy())
            return

        #include num
        array.append(num[i])
        dfs(i + 1)

        #backtrack
        array.pop()

        #dont include num
        dfs(i + 1)

        maybe a while loop that keeps hitting the 
        same number until it equals target or gets too large
        '''
        res = []
        def dfs(i, combo, total):
            ###(i, array, sum)

            if i >= len(nums) or total > target:             
                return
            if total == target:
                res.append(combo.copy())
                return
            
            combo.append(nums[i])
            dfs(i, combo, total + nums[i])

            combo.pop()

            dfs(i + 1, combo, total)
        
        dfs(0, [], 0)

        return res
            
            