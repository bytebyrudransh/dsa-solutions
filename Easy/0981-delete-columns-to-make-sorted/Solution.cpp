class Solution {
public:
    int minDeletionSize(vector<string>& strs) {
        int m = strs.size();
        int n = strs.empty() ? 0 : strs[0].size();
        int deletions = 0;

        for (int col = 0; col < n; ++col) {
            for (int row = 1; row < m; ++row) {
                if (strs[row][col] < strs[row - 1][col]) {
                    ++deletions;
                    break;
                }
            }
        }

        return deletions;
    }
};