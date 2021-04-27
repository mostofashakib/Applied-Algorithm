"""
LeetCode Problem: 635. Design Log Storage System
Link: https://leetcode.com/problems/design-log-storage-system/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(N)
Space Complexity: O(N)
"""

class LogSystem:

    def __init__(self):
        self.array = []

    def put(self, id: int, timestamp: str) -> None:
        self.array.append((id, timestamp))
        
    def populateResult(self, start, end, granularityIdx):
        result = []
        
        startDate = self.convert(start, granularityIdx)
        endDate = self.convert(end, granularityIdx)
                
        for (timeId, timestamp) in self.array:
            splitDate = self.convert(timestamp, granularityIdx)
            
            if startDate <= splitDate <= endDate:
                result.append(timeId)
                
        return result
    
    def convert(self, timestamp, granularity):
        return "".join(timestamp.split(":")[:granularity+1])
    
    def getGranularityIndex(self, granularity):
        if granularity == "Year":
            return 0
        elif granularity == "Month":
            return 1
        elif granularity == "Day":
            return 2
        elif granularity == "Hour":
            return 3
        elif granularity == "Minute":
            return 4
        else:
            return 5

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        granularityIdx = self.getGranularityIndex(granularity)
        result = self.populateResult(start, end, granularityIdx)
        return result

# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)