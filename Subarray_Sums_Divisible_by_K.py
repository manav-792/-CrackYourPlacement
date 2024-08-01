class Solution:
    def subarraysDivByK(self, nums, k):
        map={0:1}
        sum=0
        cnt=0
        for i in nums:
            sum+=i
            if (r:=(sum%k)) in map:
                cnt+=map[r]
                map[r]+=1
            else:
                map[r]=1
        return cnt

        