# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left==right or not head:
            return head
        before=None
        t=head
        pos=1
        while t and pos<left: #tracking position before
            before=t
            t=t.next
            pos+=1
        curr=t #position (from where lists would be reversed)sucessfully found
        prev=None
        times=right-left+1
        while times>0: #reversing the LL
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
            times-=1
        t.next=curr
        if before:
            before.next=prev
            return head
        return prev

