class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        sort the intitial candidates list
        if total > target or i >= len(candidates):
            cannot make a solution
        if total == target:
            check if the combo is not alread in res:
                add total
        
        dfs(i + 1, combo, total + nums[i])
        pop
        dfs(i + 1, combo, total)

        candidates=[1,2,3,4,5]
        target=7
        '''
        res = []
        candidates.sort()

        def dfs(i, combo, total):
            if total == target:
                res.append(combo.copy())
                return
            if total > target or i == len(candidates):
                return
            
            combo.append(candidates[i]) #
            dfs(i + 1, combo, total + candidates[i])

            combo.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1

            dfs(i + 1, combo, total)

        dfs(0, [], 0)
        return res
