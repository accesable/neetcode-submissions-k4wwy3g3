# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None :
            return head
        
        cur = head
        pre = None
        while cur != None:
            nextNode = cur.next
            cur.next = pre
            pre = cur
            cur =nextNode
        return pre

        