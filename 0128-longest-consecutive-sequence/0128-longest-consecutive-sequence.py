class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        counter = 0
        num_set = set(nums)
        for num in num_set:
            if (num - 1) not in num_set:
                current_num = num
                curr_streak = 1

                while (current_num + 1) in num_set:
                    current_num +=1
                    curr_streak +=1

                counter = max(counter, curr_streak)

        return counter