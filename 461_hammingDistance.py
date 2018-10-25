'''
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 2^31.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
'''

def hammingDistance(x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    
    >>> hammingDistance(1, 4)
    2
    
    """
    
    x = str(bin(x))[2:]
    y = str(bin(y))[2:]
    
    bins = [x, y]
    
    print(bins)
    
    max_length = max(len(x), len(y))
    
    for i in range(2):
        bins[i] = (max_length - len(bins[i])) * '0' + bins[i]
    
    print(bins)
    
    ham = 0
    
    for i in range(max_length):
        if bins[0][i] != bins[1][i]:
            ham += 1
    
    return ham