from typing import List

def reverseString(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.

    >>> s = list('hello')
    >>> reverseString(s)
    >>> s
    ['o', 'l', 'l', 'e', 'h']
    """
    if len(s) < 2:
        pass

    for i in range((len(s) // 2)):
        s[i], s[-(i+1)] = s[-(i+1)], s[i]
