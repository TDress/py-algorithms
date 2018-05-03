from lib import assertion
from statistics import median
from collections import deque

# USING A LIST, USING "MEDIAN-OF-THREE" HEURISTIC INSTEAD OF RANDOMIZATION
def partition(l, start, end):
    # select pivot
    mid = (end - start) // 2
    pivot_value = median([l[start], l[mid], l[end]])
    if pivot_value == l[start]:
        pivot_index = start
    else:
        pivot_index = mid if l[mid] == pivot_value else end

    # move pivot to end of list and scan towards the middle
    l[pivot_index], l[end] = l[end], l[pivot_index]
    i, j = start, end
    while j > i:
        if l[end] < l[j - 1]:
            j -= 1
        else:
            l[j - 1], l[i] = l[i], l[j - 1]
            i += 1

    l[j], l[end] = l[end], l[j]
    return j
#    right, left = end - 1, start
#    while left < right:
#        if l[left] < l[end]:
#            left += 1
#        elif l[right] < l[end]:
#            l[left], l[right] = l[right], l[left]
#            left += 1
#        else:
#            right -= 1
#    l[left], l[end] = l[end], l[left]
#    return left

def quick_sort_in_place(l, start, end):
    if end - start < 1: return
    elif end - start < 2:
        if l[end] < l[start]:
            l[start], l[end] = l[end], l[start]
        return

    pivot_index = partition(l, start, end)
    quick_sort_in_place(l, start, pivot_index - 1)
    quick_sort_in_place(l, pivot_index + 1, end)



def quick_sort(l):
    quick_sort_in_place(l, 0, len(l) - 1)


def quick_sort_not_in_place(l):
    len_l = len(l)
    if len_l < 2:
        return l
    # set the pivot index
    if len_l > 2:
        start = l[0]
        mid = l[len_l // 2]
        end = l[-1]
        pivot_value = median([start, mid, end])
        pivot_index = len_l // 2
        if l[0] == pivot_value: pivot_index = 0
        elif l[-1] == pivot_value: pivot_index = len_l - 1
    else:
        pivot_value = l[1]
        pivot_index = 1

    left = []
    right = []
    middle = []
    for i in range(len_l):
        if l[i] < pivot_value:
            left.append(l[i])
        elif l[i] > pivot_value:
            right.append(l[i])
        else:
            middle.append(l[i])

    left = quick_sort(left)
    right = quick_sort(right)

    middle.extend(right)
    left.extend(middle)
    return left
        
# QUICKSORT WITH A DEQUE.  NO OPTIMIZATIONS.
def quicksort2(S):
    len_s = len(S)
    if len_s > 1:
        pivot = S.popleft()
        L = deque()
        E = deque([pivot])
        G = deque()

        while len(S) > 0:
            next = S.popleft()
            if next > pivot:
                G.append(next)
            elif next < pivot:
                L.append(next)
            else:
                E.append(next)

        quicksort2(L)
        quicksort2(G)

        for queue in [L, E, G]:
            while len(queue) > 0:
                S.append(queue.popleft())



def main():
    l1 = [3,2,5,4,1]
    l2 = [1,2,3]
    l3 = [3]
    l4 = [777,11,1,8,1234,56,2,4]
    l5 = [6,2]
    l6 = []

    q1 = deque(l1)
    q2 = deque(l2)
    q3 = deque(l3)
    q4 = deque(l4)
    q5 = deque(l5)
    q6 = deque(l6)

    print("testing quicksort with a list...")
    #assertion.equals([1,2,3,4,5], quick_sort(l1))
    #assertion.equals([1,2,3], quick_sort(l2))
    #assertion.equals([3], quick_sort(l3))
    #assertion.equals([1,2,4,8,11,56,777,1234], quick_sort(l4))
    #assertion.equals([2,6], quick_sort(l5))
    #assertion.equals([], quick_sort(l6))

    quick_sort(l1)
    quick_sort(l2)
    quick_sort(l3)
    quick_sort(l4)
    quick_sort(l5)
    quick_sort(l6)

    assertion.equals([1,2,3,4,5], l1)
    assertion.equals([1,2,3], l2)
    assertion.equals([3], l3)
    assertion.equals([1,2,4,8,11,56,777,1234], l4)
    assertion.equals([2,6], l5)
    assertion.equals([], l6)

    print("testing quicksort with a deque...")
    quicksort2(q1)
    quicksort2(q2)
    quicksort2(q3)
    quicksort2(q4)
    quicksort2(q5)
    quicksort2(q6)
    
    assertion.equals(deque([1,2,3,4,5]), q1)
    assertion.equals(deque([1,2,3]), q2)
    assertion.equals(deque([3]), q3)
    assertion.equals(deque([1,2,4,8,11,56,777,1234]), q4)
    assertion.equals(deque([2,6]), q5)
    assertion.equals(deque([]), q6)



if __name__ == '__main__':
    main()

        


