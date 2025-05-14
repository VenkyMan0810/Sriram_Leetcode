class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        counter = 0
        num_set = set(nums)
        for num in num_set:
            if (num - 1) not in num_set:
                curr_streak = 1

                while (num + curr_streak) in num_set:
                    curr_streak +=1

                counter = max(counter, curr_streak)

        return counter