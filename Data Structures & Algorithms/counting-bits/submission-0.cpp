class Solution {
public:
    vector<int> countBits(int n) {

        vector<int> ans(n + 1);

        for (int i = 0; i <= n; i++) {
            int j = i;
            int cnt = 0;

            while (j) {
                j &= j - 1;
                cnt += 1;
            }

            ans[i] = cnt;

        }

        return ans;



        
    }
};
