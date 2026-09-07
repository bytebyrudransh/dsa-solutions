class Solution {
public:
    int distinctSubseqII(string s) {
        int n=s.length();
        vector<int> dp(n,0);
        vector<int> last(26,-1);
        const int mod= 1e9+7;

        dp[0]=2;
        last[s[0]-'a']=0;

        for(int i=1;i<n;i++){
            dp[i]=2*dp[i-1];
            dp[i]%=mod; 
            if(last[s[i]-'a']==0){
                dp[i]--;
                dp[i]%=mod;
            }       
         else if(last[s[i]-'a']>0){
            dp[i]-=dp[last[s[i]-'a']-1];
            dp[i]%=mod;
        }
        last[s[i]-'a']=i;


    }
    dp[n-1]--;
    dp[n-1]%=mod;

    if(dp[n-1]<0) dp[n-1]+=mod;
    return dp[n-1];
    }

};