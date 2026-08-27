class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #sort the strings
        #check if they are equal to each other
        new_s = sorted(s)
        new_t = sorted(t)

        return new_s == new_t