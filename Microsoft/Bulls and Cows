class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret=[int(x) for x in str(secret)]
        guess=[int(y) for y in str(guess)]
        bulls=0
        freq=[0]*10
        for i in range(len(secret)):
            if(secret[i]==guess[i]):
                bulls+=1
            else:
                freq[secret[i]]+=1
        cow=0
        for i in range(len(guess)):
            if secret[i]!=guess[i] and freq[guess[i]]>0:
                cow+=1
                freq[guess[i]]-=1
        return str(bulls)+"A"+str(cow)+"B"
