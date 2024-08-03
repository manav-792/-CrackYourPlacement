class Solution:
    def subarraySum(self, nums, k):
        map={0:1}
        cnt=0
        sum=0
        for i in nums:
            sum+=i
            diff=sum-k
            if diff in map:cnt+=map[diff]
            if sum in map:map[sum]+=1
            else:map[sum]=1
        return cnt
        