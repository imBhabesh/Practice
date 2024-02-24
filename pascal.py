class Solution:
    def makerows(self,row):
        finalrow=[1]
        res=1
        for col in range(1,row):
            res=res*(row-col)
            res=res//col
            finalrow.append(res)
        return finalrow    


    def generate(self, numRows: int) -> List[List[int]]:
        ans=[]
        for row in range(1,numRows+1):
            ans.append(self.makerows(row))
        return ans    
