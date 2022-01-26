
def heapify(l, i):
    left_child = 2 * i + 1
    right_child = 2 * i + 2
    # If the node has two child
    if right_child <= len(l) - 1:
        if l[left_child] <= l[right_child]:
            min = left_child
        else:
            min = right_child
        
        if l[i] > l[min]:
            
            l[i], l[min] = l[min], l[i]

            heapify(l, min)
    
    # Si el nodo tiene un hijo
    elif left_child <= len(l) - 1:
        if l[i] > l[left_child]:
            aux = l[i]
            l[i] = l[left_child]
            l[left_child] = aux
    
    return l

def heapsort(l):
    l2 = []

    for i in range(len(l)// 2 - 1, -1, -1):
        l = heapify(l, i)

    for i in range(0, len(l)):
        # Swap first element (lower) and last one then delete the last (lower)
        l2.append(l[0])

        l[0], l[-1] = l[-1], l[0]
        
        l = l[:-1]

        l = heapify(l, 0)
    
    return l2


array = [1,34,5656,45234,21,456]
print(array)
print(heapsort(array))