"""
LeetCode Problem: 1188. Design Bounded Blocking Queue
Link: https://leetcode.com/problems/design-bounded-blocking-queue/
Language: Python
Written by: Mostofa Adib Shakib

Semaphore is an abstract object that manages an internal counter which is decremented by each acquire() call
and incremented by each release() call. The counter can never go below zero; when acquire() finds that it is zero,
it blocks, waiting until some other thread calls release().

Acquire:
    1) If the internal counter is larger than zero on entry, decrement it by one and return "True" immediately.

    2) If the internal counter is zero on entry, block until awoken by a call to release(). Once awoken (and the counter is greater than 0),
    decrement the counter by 1 and return "True". Exactly one thread will be awoken by each call to release(). The order in which threads
    are awoken should not be relied on.

Release:
    Release a semaphore, incrementing the internal counter by n. When it was zero on entry and other threads are
    waiting for it to become larger than zero again, wake up n of those threads.
"""

import threading
from collections import deque

class BoundedBlockingQueue(object):
    def __init__(self, capacity: int):
        self.pushing = threading.Semaphore(capacity)
        self.pulling = threading.Semaphore(0)
        self.editing = threading.Lock()
        self.queue = deque()

    def enqueue(self, element: int) -> None:
        self.pushing.acquire()
        self.editing.acquire()
        
        self.queue.append(element)
        
        self.editing.release()
        self.pulling.release()

    def dequeue(self) -> int:
        self.pulling.acquire()
        self.editing.acquire()
        
        res = self.queue.popleft()
        
        self.editing.release()
        self.pushing.release()
        
        return res

    def size(self) -> int:
        return len(self.queue)