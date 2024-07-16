def isPalindrome(head):
        if not head or not head.next: 
            return head
        
        fast = head
        slow = head

        # Find the middle value
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Reverse the node ahead of middle
        prev = None
        while slow: 
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        
        # Check palindrome
        left, right = head, prev

        while right: 
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True