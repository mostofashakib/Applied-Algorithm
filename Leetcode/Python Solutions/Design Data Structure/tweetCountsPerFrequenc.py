"""
LeetCode Problem: 1348. Tweet Counts Per Frequency
Link: https://leetcode.com/problems/tweet-counts-per-frequency/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(N)
Space Complexity: O(N)
"""

class TweetCounts:

    def __init__(self):
        self.tweetMap = defaultdict(list)
        
    def getInterval(self, freq):
        if freq == "minute":
            return 60
        elif freq == "hour":
            return 3600
        elif freq == "day":
            return 86400

    def recordTweet(self, tweetName: str, time: int) -> None:
        if tweetName not in self.tweetMap:
            self.tweetMap[tweetName].append(time)
        else:
            idx = bisect.bisect(self.tweetMap[tweetName], time)
            self.tweetMap[tweetName].insert(idx, time)
        
    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        if tweetName not in self.tweetMap:
            return []
        
        interval = self.getInterval(freq)
        
        size = ((endTime - startTime)//interval) + 1
        
        buckets = [0] * size
        
        i = bisect.bisect_left(self.tweetMap[tweetName], startTime)
        j = bisect.bisect_right(self.tweetMap[tweetName], endTime)
        
        times = self.tweetMap[tweetName][i:j]
        
        for t in times:
            k = (t-startTime)//interval
            buckets[k] += 1
        
        return buckets