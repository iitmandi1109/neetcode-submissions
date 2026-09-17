# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node1=list1
        node2=list2
        new=ListNode()
        head=new
        while(node1 and node2):
            if (node1.val==node2.val):
                new1=ListNode(node1.val)
                new.next=new1
                new=new1
                new2=ListNode(node2.val)
                new.next=new2
                new=new2
                node1=node1.next
                node2=node2.next

            elif (node1.val>node2.val):
                new1=ListNode(node2.val)
                new.next=new1
                new=new1
                node2=node2.next
            
            else:
                new1=ListNode(node1.val)
                new.next=new1
                new=new1
                node1=node1.next

        if node1==None:
            new.next=node2
        if node2==None:
            new.next=node1
        return head.next


        