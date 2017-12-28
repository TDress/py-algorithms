from lib import assertion

def merge(l1, l2, l):
    """Merge sorted lists l1 and l2 together so that the answer is sorted.
    Overwrite l with the answer-- everything is done in-place"""
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

def main():
    l1 = [3,2,5,4,1]
    l2 = [1,2,3]
    l3 = [3]
    l4 = [777,11,1,8,1234,56,2,4]
    l5 = [6,2]
    l6 = []

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

if __name__ == '__main__':
    main()
