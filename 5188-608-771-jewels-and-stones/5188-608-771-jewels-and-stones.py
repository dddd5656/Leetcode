class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        x = 0    
        for i in range(len(stones)):
            if stones[i] in jewels:
                x+=1
        return x        
        