#My solution O(m+n) - m and n are the lengths of the two linked lists


class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        currentNode = l1.next
        n1 = 0
        multiplier = 1
        n1 += l1.val * multiplier
        multiplier *= 10
        while currentNode:
            n1 += currentNode.val * multiplier
            multiplier *= 10
            currentNode = currentNode.next

        currentNode = l2.next
        n2 = 0
        multiplier = 1
        n2 += l2.val * multiplier
        multiplier *= 10
        while currentNode:
            n2 += currentNode.val * multiplier
            multiplier *= 10
            currentNode = currentNode.next
        
        finalNumber = n1 + n2
        l3 = list(map(int, str(finalNumber)))
        l3 = l3[::-1]

        dummy = ListNode()
        current = dummy
        for number in l3:
            current.next = ListNode(number)
            current = current.next
        return dummy.next