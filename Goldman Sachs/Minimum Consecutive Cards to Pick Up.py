import sys
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        min=sys.maxsize
        map={}
        for i,val in enumerate(cards):
            if val in map:
                b=i-map[val]+1
                if b<min:
                    min=b
            map[val]=i
        if min==sys.maxsize:
            return -1
        return min
