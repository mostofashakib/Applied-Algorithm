"""
Basic bit operators:
Bit Operators       Name
~                   Logical NOT
|                   Logical OR
&                   Logical AND
<<                  Logical LEFT SHIFT
>>                  Logical RIGHT SHIFT
^                   Logical XOR

Left Shift:
Multiplies the number by 2.

Right Shift:
Divides the number by 2.

OR truth table:

A  B  Result
0  0   0
0  1   1
1  0   1
1  1   1

And truth table:

A  B  Result
0  0   0
0  1   0
1  0   0
1  1   1

XOR truth table:

A  B  Result
0  0   0
0  1   1
1  0   1
1  1   0
"""

# Set bit

def set_bit(x, position):
    mask = 1 << position
    return x | mask

#  Clear bit

def clear_bit(x, position):
    mask = 1 << position
    return x & ~mask

# Flip bit

def flip_bit(x, position):
    mask = 1 << position
    return x ^ mask

# Is_Bit_set

def is_bet_set(x, position):
    shifted = x >> position
    return shifted & 1

# Modify bit

def modify_bit(x, position, state):
    mask = 1 << position                                   # creates a mask in order to clear the bit
    return (x & ~mask) | (state << position & mask)        # change the mask of the bit to b and then modifies the bit

# check if even. If true then the number is even, if false then the number is odd.

def is_even(x):
    return x & 1 == 0

# Check if powers of two. If true then the number is a power of two, if false then the number is not a power of two.

def powersOfTwo(x):
    return False if x == 0 else (x & x-1) == 0

# Write a function to count the number of bits that are different between two numbers.

def count_bits(A, B):
    count = 0

    for i in range(32):       # 32 bit binary representation
        if ( (A >> i) & 1 ) ==  ( (B >> i) & 1 ):   # if the bits are different at a certain position.
            count += 1
    return count              # returns the total number of mismatching bits.