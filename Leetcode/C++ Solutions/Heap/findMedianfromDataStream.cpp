/*
LeetCode Problem: 295. Find Median from Data Stream
Link: https://leetcode.com/problems/find-median-from-data-stream/
Language: C++
Written by: Mostofa Adib Shakib

Time Complexity: O(log n)
Space Complexity: O(n)
*/

class MedianFinder {
    priority_queue <int> lowerHalf;                                     // Max Heap
    priority_queue <int, vector<int>, greater<int> > upperHalf;         // Min Heap
    
public:
    
    // A helper function that adds a given value to the correct heap
    void addToTheHeap(int num) {
        if ( lowerHalf.size() == 0 || num < lowerHalf.top() ) {
            lowerHalf.push(num);
        }
        else {
            upperHalf.push(num);
        }
    }
    
    // A helper function which ensures that the size difference between the two heaps is at most 1
    void reBalanceTheHeap(int num) {
        if ( lowerHalf.size() > upperHalf.size() + 1 ) {
            upperHalf.push(lowerHalf.top());
            lowerHalf.pop();
        }
        
        else if ( upperHalf.size() > lowerHalf.size() + 1 ) {
            lowerHalf.push(upperHalf.top());
            upperHalf.pop();
        }
    }
    
    void addNum(int num) {
        addToTheHeap(num);
        reBalanceTheHeap(num);
    }
    
    double findMedian() {
        
        if ( lowerHalf.size() == upperHalf.size() ) {
            return (float) ( (float) ( lowerHalf.top() + upperHalf.top() ) / 2.0 );
        }

        // Checks to see if the heap is of odd length
        if ( lowerHalf.size() > upperHalf.size() ) {
            return lowerHalf.top();
        }
        else {
            return upperHalf.top();
        } 
    }
};


/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */