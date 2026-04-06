# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur, pre = head, None

        while cur :
            newNode = ListNode(cur.val,pre)
            pre = newNode
            cur = cur.next
        return pre



    def printListNode(self,head: Optional[ListNode]) :
        while head :
            print(head.val)
            head = head.next
    