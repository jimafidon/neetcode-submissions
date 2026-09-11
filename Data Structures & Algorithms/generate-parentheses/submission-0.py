class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        Input: n = 3
        Output: ["((()))","(()())","(())()","()(())","()()()"]

        since n = 1 = '()'
        n = 3 must have equal parts open parenthesis and closing parenthesis

        doing so, we can determine that a valid parenthesis input must have atleast n number of 
        parenthesis

        we can have a function to test all possible options - backtracking


Input: n = 3

Output: ["((()))","(()())","(())()","()(())","()()()"]
        '''

        res = []
        stack = []

        def dfs(openP, closedP):
            if openP == closedP == n:
                res.append("".join(stack.copy()))

            if openP < n: 
                stack.append('(')
                dfs(openP + 1, closedP)
                stack.pop()

            if closedP < openP:
                stack.append(')')
                dfs(openP, closedP + 1)
                stack.pop()
        
        dfs(0, 0)
        return res


