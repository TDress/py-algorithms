from lib import assertion
from collections import deque

# MERGE SORT WITH A PYTHON LIST
def merge(l1, l2, l):
    """Merge sorted lists l1 and l2 together so that the answer is sorted.
    Overwrite l with the answer-- everything is done in-place
    
    To say that everything is done in place is oversimplified.  We pass list
    slices to mergesort over and over recursively and every time merge is
    called it modifies a slice, EXCEPT for the last call with the original list. 
    So as we recurse down and then come back up the call stack with merge calls,
    we are modifying list slices and not the original list.  those slices are lost
    along the way but it doesn't matter because the final call to merge will have two 
    slices that are both sorted.
    """
    l1_i = l2_i = 0
    
    while l1_i + l2_i < len(l):
        if l1_i == len(l1) or (l2_i < len(l2) and l2[l2_i] < l1[l1_i]):
            l[l1_i + l2_i] = l2[l2_i]
            l2_i += 1
        else:
            l[l1_i + l2_i] = l1[l1_i]
            l1_i += 1
            
def merge_sort(l):
    len_l = len(l)
    if len_l > 1:
        mid = len_l // 2
        l1 = l[:mid]
        l2 = l[mid:]

        merge_sort(l1)
        merge_sort(l2)

        merge(l1, l2, l)



# MERGE SORT WITH A PYTHON DEQUE
def merge2(S1, S2, S):
    while not len(S1) == 0 or not len(S2) == 0:
        if len(S2) == 0 or (len(S1) > 0 and S1[0] <= S2[0]):
            S.append(S1.popleft())
        else:
            S.append(S2.popleft())

def merge_sort2(S):
    len_s = len(S)
    if len_s < 2:
        return
    q_left = deque()
    q_right = deque() 
    
    while len(q_left) < len_s // 2:
        q_left.append(S.popleft())
    while len(S) > 0:
        q_right.append(S.popleft())

    merge_sort2(q_left)
    merge_sort2(q_right)
    merge2(q_left, q_right, S)





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


    print("testing mergesort with a list!")
    merge_sort(l1)
    merge_sort(l2)
    merge_sort(l3)
    merge_sort(l4)
    merge_sort(l5)
    merge_sort(l6)

    assertion.equals([1,2,3,4,5], l1)
    assertion.equals([1,2,3], l2)
    assertion.equals([3], l3)
    assertion.equals([1,2,4,8,11,56,777,1234], l4)
    assertion.equals([2,6], l5)
    assertion.equals([], l6)


    print("testing mergesort with a deque!")
    merge_sort2(q1)
    merge_sort2(q2)
    merge_sort2(q3)
    merge_sort2(q4)
    merge_sort2(q5)
    merge_sort2(q6)

    assertion.equals(deque([1,2,3,4,5]), q1)
    assertion.equals(deque([1,2,3]), q2)
    assertion.equals(deque([3]), q3)
    assertion.equals(deque([1,2,4,8,11,56,777,1234]), q4)
    assertion.equals(deque([2,6]), q5)
    assertion.equals(deque([]), q6)



if __name__ == '__main__':
    main()
