"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)

        for i in range(len(intervals) - 1):
            meeting_A = intervals[i].end
            meeting_B = intervals[i + 1].start

            if meeting_B < meeting_A:
                return False
            else:
                continue
        return True
