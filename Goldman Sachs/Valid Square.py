class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        b=set([dist(p1,p2),dist(p3,p4),dist(p1,p3),dist(p1,p4),dist(p2,p4),dist(p2,p3)])
        if(p1==p2 or p1==p3 or p2==p4 or p2==p3 or p2==p4 or p3==p4):
            return False
        if len(b)==2:
            return True
        else:
            return False
    
