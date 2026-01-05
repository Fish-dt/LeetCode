class Solution {
public:
    long long maxMatrixSum(vector<vector<int>>& matrix) {
        long long sum = 0;
        int negCount = 0;
        int mn = INT_MAX;

        for (auto &row : matrix) {
            for (int x : row) {
                if (x < 0) negCount++;
                sum += abs(x);
                mn = min(mn, abs(x));
            }
        }

        if (negCount % 2 == 0) return sum;
        return sum - 2LL * mn;
    }
};