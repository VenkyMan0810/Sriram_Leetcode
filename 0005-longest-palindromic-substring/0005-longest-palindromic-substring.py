class Solution:
    def longestPalindrome(self, s: str) -> str:
        # if len(s) == 0:
        #     return ""
        
        # def expand(s,l,r):
        #     while l >= 0 and r < len(s) and s[l] == s[r]:
        #         l -= 1
        #         r += 1
        #     return r-l-1

        # st = 0
        # end = 0
        # for i in range(len(s)):
        #     odd = expand(s,i,i)
        #     even = expand(s,i,i+1)
        #     max_len = max(odd,even)
        #     if max_len > end -st:
        #         st = i- (max_len-1)//2
        #         end = i + max_len//2
        # return s[st:end+1]

        residx, resLen = 0,0
        n = len(s)

        dp = [[False] * n for i in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if resLen < (j - i + 1):
                        residx = i
                        resLen = j - i + 1

        return s[residx: residx + resLen]