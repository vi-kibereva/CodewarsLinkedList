def loop_size(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            count = 1
            temp = slow.next
            while temp != slow:
                count += 1
                temp = temp.next
            return count
    return 0