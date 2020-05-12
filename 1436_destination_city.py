class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        destination = set()
        start = set()
        for path in paths:
            # save every path
            destination.add(path[1])
            start.add(path[0])
        for point in destination:
            # check if a point is also a start, if it isn't that's the answer.
            if point not in start:
                return point
        
