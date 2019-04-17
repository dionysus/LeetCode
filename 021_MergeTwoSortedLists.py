# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    """
    """

    if l1 is None and l2 is not None:
        return l2

    if l1 is not None and l2 is None:
        return l1

    if l1 is None and l2 is None:
        return None

    curr1 = l1
    curr2 = l2
    curr0 = None
    curr0_start = None

    while curr1 is not None and curr2 is not None:
        if curr1.val <= curr2.val:
            if curr0 is None:
                curr0 = curr1
                curr0_start = curr0
            else:
                curr0.next = curr1
                curr0 = curr0.next
            curr1 = curr1.next
        else:
            if curr0 is None:
                curr0 = curr2
                curr0_start = curr0
            else:
                curr0.next = curr2
                curr0 = curr0.next
            curr2 = curr2.next

    if curr1 is None:
        curr0.next = curr2
    elif curr2 is None:
        curr0.next = curr1

    return curr0_start
