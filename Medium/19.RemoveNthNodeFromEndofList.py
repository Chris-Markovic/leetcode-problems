#My solution O(n) where n = length of linked list, I used a two pinter technique to move one to the end and the other with a delay of n

"""
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
"""

class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummyNode = ListNode(0, next = head) #The dummy node is for cases where the first node is removed
        frontNode = dummyNode
        pointerNode = dummyNode
        i = 0 #Counts the iterations so pointerNode gets a delay of n+1, meaning it ends right before the node we want to remove
        while frontNode:
            frontNode = frontNode.next
            if i-1 >= n:
                pointerNode = pointerNode.next 
            i += 1
        pointerNode.next = pointerNode.next.next
        return dummyNode.next #We return head with dummyNode.next in case we remove the first node, bacuase head points to the deleted node
            
