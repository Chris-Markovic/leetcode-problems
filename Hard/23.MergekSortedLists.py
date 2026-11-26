#My solution O(m * n) where m is the number of lists and n is the number of nodes

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        dummy = ListNode()
        mergedList = dummy
        while True:
            curr_min = 100000
            min_id = None
            for i, head in enumerate(lists):
                if head != None:
                    if head.val < curr_min:
                        min_id = i 
                        curr_min = head.val
            if min_id == None:
                break
            mergedList.next = lists[min_id]
            lists[min_id] = lists[min_id].next
            mergedList = mergedList.next

        return dummy.next
                