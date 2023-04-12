class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map=dict()
        visited=[]
        for i,j in zip(s,t):
            if i not in map:
                map[i]=j
                if j in visited:
                    return False
                visited.append(j)
            elif map[i]!=j :
                return False
        return True
s,t="egg","add"
obj=Solution()
print(obj.isIsomorphic(s,t))