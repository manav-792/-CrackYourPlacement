class Solution:
    def maxArea(self, height):
        m,l,r=0,0,len(height) - 1
        while l<r:
            m=max(m,(r-l)*min(height[l],height[r]))
            if height[l]<height[r]:l+=1
            else:r-=1     
        return m