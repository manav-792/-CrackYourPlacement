class Solution:
    def findDuplicates(self, nums):
        out = []
        seen = set()
        for n in nums:
            if n in seen:
                out.append(n)
            seen.add(n)
        return out