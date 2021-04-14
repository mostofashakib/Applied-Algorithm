"""
LeetCode Problem: 1235. Maximum Profit in Job Scheduling
Link: https://leetcode.com/problems/maximum-profit-in-job-scheduling/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(NlogK)
Space Complexity: O(N)

Explanation:

Sort the jobs by start time, (NOT end time).
    
Iterate through the jobs, use a heap to maintain all the job schedules, which are represented by
(end, totalProfit) entries. At each iteration, pop out all the job schedules that are compatible with
the next job, and keep the 'ans' updated to the max totalProfit we can achieve from all schedules.
At the end of each iteration, we add the job and its profit as our latest schedule.

A key is that, as we process the next job, 'ans' will keep track of the max profit from
the past schedules that are compatible with the next job, because the next job has a
greater-or-equal start time, as we sorted the jobs that way.

We end the iteration with a list of schedules that are mutually incompatible, and we find
the best profit out of them.
"""

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[0])
        
        hp = []
        total = 0

        for s,e,p in jobs:
            while hp and hp[0][0] <= s:
                popd = heappop(hp)
                total = max(total, popd[1])

            heappush(hp, (e, p + total))

        while hp:
            popd = heappop(hp)
            total = max(total, popd[1])

        return total