"""
LeetCode Problem: 721. Accounts Merge
Link: https://leetcode.com/problems/accounts-merge/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(AlogA)
Space Complexity: O(A)
"""

class DisjointSetUnion:
    def __init__(self):
        self.parent = {}
        self.rank = {}
        
    def initialize(self, x):
        self.parent[x] = x
        self.rank[x] = 0
    
    def find(self, k):
        if self.parent[k] != k:
            self.parent[k] = self.find(self.parent[k])

        return self.parent[k]
    
    def union(self, x, y):
        xRoot = self.find(x)
        yRoot = self.find(y)
        
        if xRoot == yRoot:
            return
        
        if self.rank[xRoot] > self.rank[yRoot]:
            self.parent[yRoot] = xRoot
        elif self.rank[xRoot] < self.rank[yRoot]:
            self.parent[xRoot] = yRoot
        else:
            self.parent[xRoot] = yRoot
            self.rank[yRoot] += 1
    
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = DisjointSetUnion()
        email2Idx = {}
        email2Name = {}
        i = 0
        
        for account in accounts:
            name = account[0]
            
            for email in account[1:]:
                email2Name[email] = name
                
                if email not in email2Idx:
                    email2Idx[email] = i
                    uf.initialize(i)
                    i += 1
                
                uf.union(email2Idx[account[1]], email2Idx[email])
                
        ans = defaultdict(list)
        
        for email in email2Name:
            idx = uf.find(email2Idx[email])
            ans[idx].append(email)
            
        return [[email2Name[v[0]]] + sorted(v) for v in ans.values()]