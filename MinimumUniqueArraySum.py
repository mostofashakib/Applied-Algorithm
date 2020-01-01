"""

Problem description:
Given an array, increment any duplicate elements until all elements are unique. The sum of the elements must be the minimum possible.

Example 1:
[3,2,1,2,7]
minimum value = 3 + 2 + 1 + 4 + 7 = 17

Example 2:
[3,1,2,2]
minimum value = 3 + 1 + 2 = 6

Written by: Mostofa Adib Shakib
Language: Python

"""

def minimumArraySum(arr):
    sm = 0
    val =  0
    array = []
    array.append(arr[0])
    
    for i in range(1, len(arr)):
        val = arr[i]
        while val in array:
            val += 1
        array.append(val)
    
    for i in range(len(array)):
        sm += array[i]
    
    return sm