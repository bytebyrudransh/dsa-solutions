from math import gcd
class Solution:
    def maxValidSplits(self, nums: list[int]) -> int:
        n=len(nums)
        pre=[0]*n
        suf=[0]*n
        pre[0]=nums[0]
        for i in range(1,n):
            pre[i]=gcd(pre[i-1],nums[i])
        suf[n-1]=nums[n-1]
        for i in range(n-2,-1,-1):
            suf[i]=gcd(suf[i+1],nums[i])
        lg=[0]*(n+1)
        for i in range(2,n+1):
            lg[i]=lg[i//2]+1
        st=[nums[:]]
        j=1
        while (1<<j)<=n:
            p=1<<(j-1)
            a=[]
            for i in range(n-(1<<j)+1):
                a.append(gcd(st[j-1][i],st[j-1][i+p]))
            st.append(a)
            j+=1
        def get(l,r):
            if l>r:
                return 0
            j=lg[r-l+1]
            p=1<<j
            return gcd(st[j][l],st[j][r-p+1])
        g=pre[n-1]
        l=0
        while pre[l]!=g:
            l+=1
        r=n-1
        while suf[r]!=g:
            r-=1
        ans=max(0,r-l)
        for i in range(n):
            m=n-1
            if m<2:
                continue
            g=gcd(pre[i-1] if i>0 else 0, suf[i+1] if i+1<n else 0)
            l1=0
            h1=m-1
            while l1<h1:
                j=(l1+h1)//2
                if j<i:
                    x=pre[j]
                else:
                    x=gcd(pre[i-1] if i>0 else 0, get(i+1,j+1))
                if x==g:
                    h1=j
                else:
                    l1=j+1
            l=l1
            l1=0
            h1=m-1
            while l1<h1:
                j=(l1+h1+1)//2
                if j<i:
                    x=gcd(get(j,i-1),suf[i+1] if i+1<n else 0)
                else:
                    x=suf[j+1]
                if x==g:
                    l1=j
                else:
                    h1=j-1
            r=l1
            ans=max(ans,r-l)
        return ans