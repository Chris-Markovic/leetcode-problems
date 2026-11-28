#My solution O(n), I use a probe to check if there are k more nodes, if not, the rest stays as it is
#Then I reverse the group by pointing each node to the previous one, and link the node before the group (groupPrev)
#to the new first node. The old first node becomes the last one, so it is groupPrev for the next group
#The space is O(1), as the task description asked for (follow-up)


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        dummy = ListNode(next = head)
        groupPrev = dummy
        while True:
            if not head:
                return dummy.next
            probeList = head
            prev = head
            #Probe
            for i in range(k-1):
                if probeList and probeList.next:
                    probeList = probeList.next
                else:
                    return dummy.next
                    
            last = probeList.next
            #Reversing 
            groupStart = head
            nextNode = head.next
            head.next = last
            head = nextNode
            for i in range(k-1):
                nextNode = head.next
                head.next = prev
                prev = head
                head = nextNode
            groupPrev.next = prev
            groupPrev = groupStart
        return dummy.next