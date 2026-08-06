import random
import bisect

class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.prefix = []
        total = 0
        for x1, y1, x2, y2 in rects:
            points = (x2 - x1 + 1) * (y2 - y1 + 1)
            total += points
            self.prefix.append(total)

    def pick(self) -> List[int]:
        target = random.randint(1, self.prefix[-1])
        idx = bisect.bisect_left(self.prefix, target)
        
        x1, y1, x2, y2 = self.rects[idx]
        points_in_rect = (x2 - x1 + 1) * (y2 - y1 + 1)
        
        offset = target - (self.prefix[idx] - points_in_rect) - 1
        cols = x2 - x1 + 1
        
        return [x1 + (offset % cols), y1 + (offset // cols)]