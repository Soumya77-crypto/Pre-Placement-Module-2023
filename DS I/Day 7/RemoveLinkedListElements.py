# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        x=ListNode(0)
        x.next=head
        p=x
        while p.next:
            if(p.next.val==val):
                p.next=p.next.next
            else:
                p=p.next
        return x.next
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
