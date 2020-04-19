T = int(input())
for x in range(1, T + 1):
    N, M, Q = map(int, input().split())
    P = map(int, input().split())
    R = map(int, input().split())
    pages = [True] * (N + 1)
    for P_i in P:
        pages[P_i] = False
    readers = {}
    y = 0
    
    print("Case #{}: {}".format(x, y), flush = True)



Python 3 (commands)

python3 solution.py < input_file.txt > output_file.txt
 python3 solution.py < input_file.txt > output_file.txt
 
Python 3 (solution.py)

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Kickstart problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  n, m = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
  print("Case #{}: {} {}".format(i, n + m, n * m))
  # check out .format's specification for more formatting options