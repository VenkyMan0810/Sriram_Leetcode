class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2): return False

        s1count, s2count = [0] * 26, [0] * 26

        for i in s1:
            s1count[ord(i) - ord('a')] += 1

        for i in range(len(s2)):
            s2count[ord(s2[i]) - ord('a')] += 1

            if i >= len(s1):
                s2count[ord(s2[i - len(s1)]) - ord('a')] -= 1

            if s2count == s1count: 
                return True
        
        return False