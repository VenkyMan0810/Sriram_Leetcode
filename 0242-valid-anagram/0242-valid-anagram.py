class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        temp = {}
        for i in s:
            if i in temp:
                temp[i] += 1
            else: 
                temp[i] = 1

        for j in t:
            if j not in temp:
                return False
            temp[j] -= 1
            if temp[j] < 0:
                return False

        return True