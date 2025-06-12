class Solution {
    public int maxAdjacentDistance(int[] nums) {
        int n = nums.length;
        int maxDiff = 0;
        
        // linear neighbors
        for (int i = 0; i < n - 1; i++) {
            int diff = Math.abs(nums[i] - nums[i + 1]);
            if (diff > maxDiff) maxDiff = diff;
        }
        
        // circular neighbor: last vs first
        int wrapDiff = Math.abs(nums[n - 1] - nums[0]);
        return Math.max(maxDiff, wrapDiff);
    }
}