class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        if len(rectangles) == 0 or len(rectangles[0]) == 0:
            return False
        x1 = float("inf")
        y1 = float("inf")
        x2 = 0
        y2 = 0
        a = set()
        area = 0
        for rect in rectangles:
            x1 = min(rect[0], x1)
            y1 = min(rect[1], y1)
            x2 = max(rect[2], x2)
            y2 = max(rect[3], y2)
            area += (rect[3] - rect[1]) * (rect[2] - rect[0])
            a.remove((rect[0],rect[3])) if (rect[0],rect[3]) in a else a.add((rect[0],rect[3]))
            a.remove((rect[0],rect[1])) if (rect[0],rect[1]) in a else a.add((rect[0],rect[1]))
            a.remove((rect[2],rect[3])) if (rect[2],rect[3]) in a else a.add((rect[2],rect[3]))
            a.remove((rect[2],rect[1])) if (rect[2],rect[1]) in a else a.add((rect[2],rect[1]))
        if (x1, y2) not in a or (x2, y1) not in a or (x1, y1) not in a or (x2, y2) not in a or len(a) != 4:
            return False
        return area == (y2 - y1) * (x2 - x1)
