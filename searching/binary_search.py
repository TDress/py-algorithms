import lib.assertion


def binary_search(l, target, start, end): 
    if start > end:
        return -1

    mid = (end + start) // 2

    if l[mid] == target:
        return mid
    elif l[mid] > target:
        return binary_search(l, target, start, mid - 1)
    else: 
        return binary_search(l, target, mid + 1, end)


def main(): 
    lib.assertion.equals(-1, binary_search([1], 5, 0, 0))
    lib.assertion.equals(0, binary_search([5], 5, 0, 0))
    lib.assertion.equals(1, binary_search([3,5], 5, 0, 1))
    lib.assertion.equals(-1, binary_search([3,5], 0, 0, 1))
    lib.assertion.equals(-1, binary_search([2,3,8,9], 0, 0, 3))
    lib.assertion.equals(-1, binary_search([1,2,3,8,9], 0, 0, 4))
    lib.assertion.equals(5, binary_search([1,2,3,5,7,8,9], 8, 0, 6))
    lib.assertion.equals(1, binary_search([1,2,3,5,7,8,9], 2, 0, 6))


if __name__ == '__main__':
    main()
