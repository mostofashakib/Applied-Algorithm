/*
LeetCode Problem: 359. Logger Rate Limiter
Link: https://leetcode.com/problems/logger-rate-limiter/
Written by: Mostofa Adib Shakib
Language: C++

Time Complexity: O(1)
Space Complexity: O(n)
*/

class Logger {
public:
    /** Initialize your data structure here. */
    map<string, int> hashMap;
    Logger() {
        hashMap.clear();
    }
    
    /** Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity. */
    bool shouldPrintMessage(int timestamp, string message) {
        if (hashMap.find(message) == hashMap.end()) {
            hashMap[message] = timestamp;
            return true;
        }
        if ( timestamp >= hashMap[message] + 10) {
            hashMap[message] = timestamp;
            return true;
        }
        return false;
    }
};

/**
 * Your Logger object will be instantiated and called as such:
 * Logger* obj = new Logger();
 * bool param_1 = obj->shouldPrintMessage(timestamp,message);
 */