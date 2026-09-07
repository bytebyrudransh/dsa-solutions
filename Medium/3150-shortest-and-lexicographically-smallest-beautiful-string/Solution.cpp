class Solution {
public:

    string res(deque<char> dq) {
        string res = "";

        for (char c : dq) {
            res += c;
        }

        return res;
    }

    string shortestBeautifulSubstring(string s, int k) {

        deque<char> dq;

        
        int count = 0;

        string ans = s;

        for (int i = 0; i < s.size(); i++) {

            if (s[i] == '1') {
                count++;
            }

            dq.push_back(s[i]);

            while (count > k) {

                int val = dq.front();
                dq.pop_front();

                if (val == '1') {
                    count--;
                }
            }

            while (!dq.empty() && dq.front() != '1') {
                dq.pop_front();
            }

            if (count == k) {

                string cur = res(dq);

                if (cur.size() < ans.size() ||
                    (cur.size() == ans.size() && cur < ans)) {
                    ans = cur;
                }
            }
        }

        return ans == s && count < k ? "" : ans;
    }
};