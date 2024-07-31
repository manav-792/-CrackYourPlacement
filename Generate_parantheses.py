class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        l=[]
        root='('
        def addB(root,k,i,j):
            if 2*n==k:
                l.append(root)
                return
            if i<n:
                addB(root+'(',k+1,i+1,j) 
            if j<=i:
                addB(root+')',k+1,i,j+1)
        addB(root,1,1,1)
        return l
