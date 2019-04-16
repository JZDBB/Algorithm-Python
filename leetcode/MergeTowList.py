
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class List:
    def __init__(self, L):
        Node_List = []
        for item in L:
            Node_List.append(ListNode(item))

        for i in range(len(Node_List) - 1):
            Node_List[i].next = Node_List[i + 1]


def mergeTwoLists(self, l1, l2):
    re = ListNode(0)
    r = re
    while (l1 or l2):
        if not l1:
            val = l2.val
            l2 = l2.next
        elif not l2:
            val = l1.val
            l1 = l1.next
        else:
            if l1.val <= l2.val:
                val = l1.val
                l1 = l1.next
            else:
                val = l2.val
                l2 = l2.next
        r.next = ListNode(val)
        r = r.next
    return re.next







