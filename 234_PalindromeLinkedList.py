class listNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def isPalindrome1(head):
    rev = None
    fast = head
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, head = head, rev, head.next
    tail = head.next if fast else head
    isPali = True
    while rev:
        isPali = isPali and rev.val == tail.val
        head, head.next, rev = rev, head, rev.next
        tail = tail.next
    return isPali


def isPalindrome2(head):

    if head is None: return True
    return False if find(head, head.next) is None else True

# this version restore the list to its original state by reversing the first half back
def isPalindrome3(head):
    rev = None
    fast = head
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, head = head, rev, head.next
    tail = head.next if fast else head
    isPali = True
    while rev:
        isPali = isPali and rev.val == tail.val
        head, head.next, rev = rev, head, rev.next
        tail = tail.next
    return isPali


def find(head, nxt):
    if nxt is None: return head

    if nxt.next is None:
        return head.next if head.val == nxt.val else None

    checkNode = find(head, nxt.next)

    if checkNode is None:
        return None

    return checkNode.next if checkNode.val == nxt.val else None


def main():
    o = listNode(3)
    for i in [2, 5, 2, 5, 2, 3]:
        a = listNode(i)
        a.next = o
        o = a
    isPalindrome = isPalindrome1
    print(isPalindrome(o))

if __name__ == '__main__':
    main()
