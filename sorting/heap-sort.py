from lib import assertion

def left_child(n, i):
    """return the left child's index of element at index i in heap

    if not found, return None"""
    lc_index = i * 2 + 1
    if lc_index < n:
        return lc_index

    return None

def right_child(n, i):
    """return the right child's index of element at index i in heap

    if not found, return None"""
    rc_index = i * 2 + 2
    if rc_index < n:
        return rc_index

    return None


def heapify(l, n, i):
    """return the list in max-heap order

    l : List
        The list to heapify
    n : int
        The length of the list.  Needed because the function is recursive.
    i : int
        The index to perform down-heap bubbling on."""

    largest = i
    for child in [left_child(n, i), right_child(n, i)]:
        if child and l[child] > l[largest]:
            largest = child

    if largest != i:
        l[i], l[largest] = l[largest], l[i]
        heapify(l, n, largest)


def heap_sort(l):
    n = len(l)
    # heapify list
    for i in range(n-1, -1, -1):
        heapify(l, n, i)

    # swap the largest item with the next index of the sorted portion.
    sorted_i = n - 1
    while sorted_i != 0:
        l[0], l[sorted_i]= l[sorted_i], l[0]
        heapify(l, sorted_i, 0)
        sorted_i -= 1



def main():
    l1 = [3,2,5,4,1]
    l2 = [1,2,3]
    l3 = [3]
    l4 = [777,11,1,8,1234,56,2,4]

    heap_sort(l1)
    heap_sort(l2)
    heap_sort(l3)
    heap_sort(l4)

    assertion.equals([1,2,3,4,5], l1)
    assertion.equals([1,2,3], l2)
    assertion.equals([3], l3)
    assertion.equals([1,2,4,8,11,56,777,1234], l4)

if __name__ == '__main__':
    main()
