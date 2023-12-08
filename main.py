class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        indexS, indexT = 0, 0
        if(len(s)>len(t)):
            return False

        while(indexS < len(s) and indexT < len(t)):
            if s[indexS] == t[indexT]:
                indexS +=1
            indexT +=1

        return indexS == len(s)
       