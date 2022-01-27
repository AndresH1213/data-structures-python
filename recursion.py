from linked_list import LinkedList
from linked_list_merge_sort import merge_sort

def findBinary(num, result):
    """Recieves a number and returns the binary representations in a string"""
    if num == 0:
        return result
    
    result = str(num % 2) + result

    return findBinary(num // 2, result)

print(findBinary(233, ""))

def sumNumbers(num):
    
    if num <= 1:
        return num
    
    return num + sumNumbers(num - 1)

print(sumNumbers(10))

def reverseLinkedList(node):
    """Takes the head node of a linked list and reverse the linked list"""
    if node == None or node.next_node == None:
        return node
    
    #Store the current head to the LinkedList to pass it through the recursion calls
    p = reverseLinkedList(node.next_node)

    # Point the next node to the current node (reverse the pointer)
    node.next_node.next_node = node
    node.next_node = None

    # p is never changes in the recursion calls, so the first element that is store in p is
    # the element that is returned in the case base the tail that is de new head
    return p

def mergeLists(l1, l2):
    """Takes two sorted list and merge them"""
    if l1 == None: return l2
    if l2 == None: return l1

    if l1.data <= l2.data:
        l1.next_node = mergeLists(l1.next_node, l2)
        return l1
    else:
        l2.next_node = mergeLists(l1, l2.next_node)
        return l2


linked1 = LinkedList()
linked1.add(5)
linked1.add(4)
linked1.add(3)
linked1.add(2)
linked1.add(1)

# # print(linked.head)
# headnode = reverseLinkedList(linked1.head)
# newLinked = LinkedList(headnode)
# print(newLinked)


linked2 = LinkedList()
linked2.add(10)
linked2.add(9)
linked2.add(8)
linked2.add(5)
linked2.add(1)

merged = mergeLists(linked1.head, linked2.head)
merge_result = LinkedList(merged)
print(merge_result)