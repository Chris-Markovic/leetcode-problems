#My solution O(n)


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(next = head)
        prev = dummy
        while head and head.next:
            currNode = head
            nextNode = head.next
            afterNode = head.next.next #afterNode is the node after the swapper pair, keeps track of the next node to move to
            head = nextNode
            head.next = currNode
            head.next.next = afterNode
            head = head.next.next
            prev.next = nextNode #prev tracks the node before the swapped pair, so the pairs connect together
            prev = currNode

        return dummy.next