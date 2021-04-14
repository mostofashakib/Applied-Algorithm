"""
Language: Python
Written by: Mostofa Adib Shakib
Further Reading: https://www.geeksforgeeks.org/reservoir-sampling/
                 https://en.wikipedia.org/wiki/Reservoir_sampling
Video Explanation: https://www.youtube.com/watch?v=A1iwzSew5QY

Algorithm:

1) Create an array reservoir with size k and copy first k items from stream to it. 
2) Now one by one consider all items from (k+1)th item to nth item. 
  a) Generate a random number (j) from 0 to i where i is the index of the current item in stream.
  b) If j is in range 0 to k-1, replace reservoir[j] with stream[i]
"""

# A function to randomly select  items from stream[0..n-1].
def randomlySelectKItemsFromStream(stream, n, k):
        i=0;
        # index for elements
        # in stream[]
         
        # reservoir[] is the output
        # array. Initialize it with
        # first k elements from stream[]
        reservoir = [0]*k

        for i in range(k):
            reservoir[i] = stream[i]
         
        # Iterate from the (k+1)th
        # element to nth element
        while(i < n):
            # Pick a random index
            # from 0 to i.
            j = random.randrange(i+1)

            # If the randomly picked
            # index is smaller than k,
            # then replace the element
            # present at the index
            # with new element from stream
            if(j < k):
                reservoir[j] = stream[i]
            i+=1