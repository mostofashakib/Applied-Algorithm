"""
LeetCode Problem: 1163. Last Substring in Lexicographical Order
Link: https://leetcode.com/problems/last-substring-in-lexicographical-order/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n)
Space Complexity: O(n)

Explanation

The solution is based on the thought that the last substring in lexicographical order has to start with the largest possible character.
Moreover, assuming the largest possible character is "z", "zz" + any substring starting with non-z (e.g., "zza") is always larger than
"z" + largest possible substring starting with non-z (e.g., "zyyyy"). Then, an important implication is that if there is a substring "zzzzz",
using one of them as the starting character, we only need to consider the first "z", because any substring starting with other "z" would be
smaller lexicographically (e.g., "zzzzza" > "zzzza").

Now we are ready to proceed to the next step, which is to browse through the whole string and find the largest possible character,
as well as the longest contiguous subtrings composed of that character only. The indexes of the starting characters of them can then be
saved in a HashSet. If there is only one such index, congratulation as you have already found the solution!

However, we do have to consider the cases where there are multiple such indexes. What is next then? Well, we just keep comparing the next
characters following them until we have only one winner left. If the next character under comparison happened to have the index saved in the original
HashSet (i.e. used as the starting character of a substring), the substring starting with this "next character"
could not be the optimal solution. This is very intuitive and please refer to mapleisle's post for explanations.

Finally, we got the solutions! Let me summarize the key steps below:

Find the largest character, and longest contiguous substrings of that character. Save starting indexes in a HashSet.
Iteratively compare the next following character until only one winner left.
Remove indexes being the next following character of other subtrings under comparison.

Alternative Readings: 
    https://leetcode.com/problems/last-substring-in-lexicographical-order/discuss/363662/Short-python-code-O(n)-time-and-O(1)-space-with-proof-and-visualization
    https://leetcode.com/problems/last-substring-in-lexicographical-order/discuss/361121/Python-O(n)-with-explanation

"""

class Solution:
    def lastSubstring(self, s: str) -> str:
        n, i, MAX, best, pool = len(s), 0, max(s), 0, set()
        
        # Find all the longest contiguous subtrings of largest charaters only
        # Save their starting indexes in "pool" and lengths using "best".

        while i < n: 
            j = i + 1
            if s[i] == MAX:
                while j < n and s[j] == MAX:
                    j += 1
                if j - i > best:
                    pool, best = {i}, j - i
                elif j - i == best:
                    pool.add(i)
            i = j
        
        # Compare following chacaters until only one winner left.
        # We can start the search using "best" because any character before "best" is the same.
        # "visited" is used for early termination purposes only. Not required.

        step, visited = best, pool.copy()
        
        while len(pool) > 1:
            temp, cur = set(), max(s[p + step] if p + step < n else "" for p in pool)
            for p in pool:
                if p + step == n or s[p + step] != cur:
                    temp.add(p)
                elif p + step in visited:
                    temp.add(p + step)
            pool -= temp
            step += 1

        return s[list(pool)[0]:]