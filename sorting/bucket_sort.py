from collections import deque
from lib import assertion

# remember that you can only use bucket sort for non comparison based sorting
# and when you can make assumptions about the range of the input keys.
# the performance deteriorates as the size of the range of keys grows
# too much bigger than the size of the input items
def bucket_sort(S, N):
    """Stable bucket sort implementation.

    input S is a deque of 2-typle key,value pairs.  We want keys and values to 
        demonstrate stability.
    input N is the range of key values.  bucket array will have bucket positions
        0 to N-1
    """
    bucket_array = [deque() for i in range(N)]
    while len(S) > 0:
        next = S.popleft()
        bucket_array[next[0]].append(next)

    for i in range(N):
        while len(bucket_array[i]) > 0:
            S.append(bucket_array[i].popleft())




def main():
    l1 = [(9, 4), (1, 8), (6, 3), (7, 0), (7, 5), (0, "hello"), (9, 1)]
    l2 = [(2, 3)]
    l3 = []
    l4 = [(8, 9), (0, 3)]
    l5 = [(3, 6), (3, 4)]

    S1 = deque(l1)
    S2 = deque(l2)
    S3 = deque(l3)
    S4 = deque(l4)
    S5 = deque(l5)

    bucket_sort(S1, 10)
    bucket_sort(S2, 10)
    bucket_sort(S3, 10)
    bucket_sort(S4, 10)
    bucket_sort(S5, 10)

    assertion.equals(deque([(0, "hello"), (1, 8), (6, 3), (7, 0), (7, 5), (9, 4), (9, 1)]), S1)
    assertion.equals(deque([(2, 3)]), S2)
    assertion.equals(deque([]), S3)
    assertion.equals(deque([(0, 3), (8, 9)]), S4)
    assertion.equals(deque([(3, 6), (3, 4)]), S5)




if __name__ == '__main__':
    main()
