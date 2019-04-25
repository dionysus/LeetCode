# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1, l2):
    """
    >>> node01A = ListNode(9)
    >>> node01B = ListNode(9)
    >>> node01A.next = node01B
    >>> node02A = ListNode(9)
    >>> new_list = addTwoNumbers(node02A, node01A)
    >>> node01A.val
    8
    >>> node01A.next.val
    0
    >>> node01A.next.next.val
    1
    """
    if not l1 and not l2:
        return None

    else:

        v01 = 0
        v02 = 0

        if l1 and not l2:
            v01 = l1.val
        elif l2 and not l1:
            v02 = l2.val
            l1, l2 = l2, None
        else:
            v01 = l1.val
            v02 = l2.val

        v = v01 + v02
        if v >= 10:
            l1.val = v - 10
            if l1.next is None:
                l1.next = ListNode(1)
            else:
                l1.next.val += 1

        else:
            l1.val = v

        if not l1 and not l2:
            l1.next = None
        elif l1 and not l2:
            l1.next = self.addTwoNumbers(l1.next, None)
            return l1
        elif l2 and not l1:
            l2.next = self.addTwoNumbers(l2.next, None)
            return l2
        else:
            l1.next = self.addTwoNumbers(l1.next, l2.next)
            return l1
