class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start, path, total):
            # ✅ Base Case 1: Found valid combination
            if total == target:
                res.append(path[:])  # Copy of path to avoid reference issues
                return
            # ❌ Base Case 2: Invalid path, stop
            if total > target:
                return

            # \U0001f501 Explore candidates starting from `start` index
            for i in range(start, len(candidates)):
                path.append(candidates[i])               # Choose
                backtrack(i, path, total + candidates[i]) # Explore (re-use allowed)
                path.pop()                               # Un-choose (backtrack)

        backtrack(0, [], 0)
        return res