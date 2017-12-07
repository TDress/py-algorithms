from lib import assertion

def insertion_sort(l):
    for i in range(1, len(l)):
        current = l[i]
        j = i
        while j > 0 and current < l[j - 1]:
            l[j] = l[j - 1]
            j -= 1
        
        l[j] = current

    return l

def main():
    assertion.equals([1,2,3,4,5], insertion_sort([2,5,3,4,1]))
    assertion.equals([1,2,3,4,5], insertion_sort([5,4,3,2,1]))
    assertion.equals([1], insertion_sort([1]))
    assertion.equals([1,5], insertion_sort([5,1]))


if __name__ == '__main__':
    main()




























# why are we using this  value 'current' instead of just truly swapping with a multiple 
# assignment like :
#   for j in range(i, 0, -1):   
#       if l[j] < l[j -1]:
#           l[j - 1], l[j] = l[j], l[j - 1]

# The answer is that we don't actually need to do a true swap
# because the current value only needs to be assigned once 
# (when the jth value is finally <= to current)

# worst case running time (list is in reverse order) is O(n**2)
# but in the best case (l is nearly sorted) we have O(n) because
# there are very few iterations of the inner loop. average case is
# quadratic.  
# insertion sort is very fast for small arrays but impractically slow for large ones
# use it when:  data is nearly sorted or problem size is small (because it has low overhead)
