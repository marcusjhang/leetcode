class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            start, end = intervals[i]

            if start > newInterval[1]:
                res.append(newInterval)
                return res + intervals[i:]

            elif end < newInterval[0]:
                res.append(intervals[i])
            
            else:
                newInterval = [min(newInterval[0], start), max(newInterval[1], end)]
            
        res.append(newInterval)
        return res