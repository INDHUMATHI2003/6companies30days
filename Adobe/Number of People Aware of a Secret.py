class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        persons=[0]*(n+1)
        persons[1]=1
        numberOfPeopleSharingSecret=0
        for i in range(2,n+1):
            if(i-delay>=0):
                 numberOfPeopleSharingSecret=( numberOfPeopleSharingSecret + persons[i-delay])
            if(i-forget>=0):
                 numberOfPeopleSharingSecret=( numberOfPeopleSharingSecret - persons[i-forget])
            persons[i]= numberOfPeopleSharingSecret
        ans=0
        for i in range(n-forget+1,n+1):
            ans=(ans+persons[i])%(10**9+7)
        return ans
