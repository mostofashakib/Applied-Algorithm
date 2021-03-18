"""
LeetCode Problem 1396. Design Underground System
Link: https://leetcode.com/problems/design-underground-system/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(1)
Space Complexity: O(n)
"""

class UndergroundSystem:

    def __init__(self):
        # in_d stores information when id comes check in. key : str, id;  val: tuple, (t, stationName)
        # out_d stores information when id go check out: key: tuple, (startStation, endStation) val: list, [sum_time, count]
        
        self.in_d = {}
        self.out_d = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.in_d[id] = (t, stationName)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.in_d:
            in_t, in_station = self.in_d[id][0], self.in_d[id][1]
            key = (in_station, stationName)
            
            if key not in self.out_d:
                self.out_d[key] = [t - in_t, 1]
            else:
                self.out_d[key][0] += (t - in_t)
                self.out_d[key][1] += 1
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        # average time is sum_time / count for a certain key: (startStation, endStation) in self.out_d
        key = (startStation, endStation)
        res = self.out_d[key][0] / self.out_d[key][1]
        return res

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)