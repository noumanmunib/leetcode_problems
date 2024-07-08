def reverseList(head):
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev

        # Time -> O(n)
        # Space -> O(1)