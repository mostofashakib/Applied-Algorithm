"""
LeetCode Problem: 811. Subdomain Visit Count
Link: https://leetcode.com/problems/subdomain-visit-count/
Language: Python
Written by: Mostofa Adib Shakib

Time Complexity: O(n*m)
Space Complexity: O(n)
"""

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        hashmap = {}
        answer = []
        
        for i in cpdomains:
            string = i.split()                              # splits a string based off spaces
            number = int(string[0])                         # extracts the running number
            website = string[1].split(".")                  # splits a string based off period
            
            for j in range(len(website)):
                invidual_domain = ".".join(website[j:])     # join words together to make a string
                if invidual_domain not in hashmap:
                    hashmap[invidual_domain] = number
                else:
                    hashmap[invidual_domain] += number
        
        for key, value in hashmap.items():
            string = ""
            string += str(value) + " "
            string += key
            answer.append(string)
        
        return answer