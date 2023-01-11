class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        min=float('inf')
        map={}
        for i,val in enumerate(cards):
            if val in map:
                b=i-map[val]+1
                if b<min:
                    min=b
            map[val]=i
        if min==float('inf'):
            return -1
        return min

            
