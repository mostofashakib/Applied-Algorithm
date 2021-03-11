"""
LeetCode Problem: 1169. Invalid Transactions
Link: https://leetcode.com/problems/invalid-transactions/

Language: Python
Written by: Mostofa Adib Shakib
"""

# Sorting + HashMap
# Time Complexity: O(n^2)
# Space Complexity: O(n)

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        transactions = [t.split(",") for t in transactions]
        # sort by transaction time
        transactions = sorted(transactions, key=lambda x: int(x[1]))
        hashMap = defaultdict(list)
                
        for transaction in transactions:
            name = transaction[0]
            time = int(transaction[1])
            amount = int(transaction[2])
            place = transaction[3]
                        
            hashMap[name].append([time, place, amount, ','.join(transaction)])
        
        result = []
                
        for key, arr in hashMap.items():
            length = len(arr)
            visited = [True]*length
            i = 0
                                    
            while i < length:
                if arr[i][2] > 1000 and visited[i]:
                    result.append(arr[i][3])
                    visited[i] = False

                j = i + 1

                while j < length:                    

                    if arr[j][0] - arr[i][0] <= 60 and arr[j][1] != arr[i][1]:

                        if visited[i]:
                            result.append(arr[i][3])
                            visited[i] = False

                        if visited[j]:
                            result.append(arr[j][3])
                            visited[j] = False

                    j += 1

                i += 1

        return result


# Brute Force
# Time Complexity: O(n^2)
# Space Complexity: O(n)


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        visited = [False]*len(transactions)
        
        for i, transaction in enumerate(transactions): 
            name, time, amount, city = transaction.split(",")

            if int(amount) > 1000:
                visited[i] = True
                
            for j in range(i+1, len(transactions)): 
                otherName, otherTime, otherAmount, otherCity = transactions[j].split(",")
                
                if name == otherName and abs(int(time) - int(otherTime)) <= 60 and city != otherCity:
                    visited[i] = True
                    visited[j] = True
                    
        return [t for t, f in zip(transactions, visited) if f]