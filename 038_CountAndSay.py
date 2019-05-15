def countAndSay(n: int) -> str:
    pass


def helper(n: str) -> str:
    """
    >>> helper('1')
    '11'
    >>> helper('11')
    '21'
    >>> helper('21')
    '1211'
    >>> helper('1211')
    '111221'
    """
    result = ""
    j = 0
    for i in range(len(n)):
        if n[i] == n[j]:
            if i == len(n) - 1:
                result += str(i - j + 1)
                result += n[j]

        elif n[i] != n[j]:
            result += str(i - j)
            result += n[j]
            j = i

    return result
