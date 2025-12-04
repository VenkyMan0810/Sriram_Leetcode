class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        n = len(nums)
        c = [ [] for i in range(n+1) ]

        for (num, frq) in freq.items():
            c[frq].append(num)

        res = []


        for frq in range(n, 0, -1):
            for num in c[frq]:
                res.append(num)
                if len(res) == k:
                    return res

        

        