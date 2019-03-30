
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode):
    res = ListNode(0)
    r = res
    carry = 0
    while(l1 or l2):
        num1 = l1.val if l1 else 0
        num2 = l2.val if l2 else 0
        sum = carry + num1 + num2
        carry = sum // 10
        r.next = ListNode(sum % 10)
        r = r.next
        if (l1 != None): l1 = l1.next
        if (l2 != None): l2 = l2.next
    if (carry > 0):
        r.next = ListNode(1)
    return res

node1 = ListNode(2)
node2 = ListNode(5)
node3 = ListNode(4)
node4 = ListNode(6)
node5 = ListNode(3)
node6 = ListNode(8)

node1.next = node3
node2.next = node4
node3.next = node5
node4.next = node6

res = addTwoNumbers(node1, node2)
print(res.val)
node = res.next
print(node.val)
node_1 = node.next
print(node_1.val)
