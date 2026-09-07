class Solution {
public:
    long long maximumScore(vector<int>& nums) {
        int n = nums.size();
        vector<int> suffixMin(n);
        
        // Build suffix minimum array from right to left
        suffixMin[n - 1] = nums[n - 1];
        for (int i = n - 2; i >= 0; --i) {
            suffixMin[i] = min(nums[i], suffixMin[i + 1]);
        }
        
        long long max_val = -4e18; 
        long long currentPrefixSum = 0;
        
        // Split index i goes from 0 to n-2
        for (int i = 0; i < n - 1; ++i) {
            currentPrefixSum += nums[i];
            long long currentScore = currentPrefixSum - suffixMin[i + 1];
            if (currentScore > max_val) {
                max_val = currentScore;
            }
        }
        
        return max_val;
    }
};