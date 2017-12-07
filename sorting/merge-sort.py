

def merge(num_list_1, num_list_2):
    if len(num_list_1) == 0:
        return num_list_2
    elif len(num_list_2) == 0:
        return num_list_1
    



def merge_sort(numbers):
    list_length = len(numbers)
    if list_length == 0:
        raise RuntimeError('A non-empty list must be provided')
    elif list_length == 1 and type list_length != int:
        raise TypeError('All values in the list must be integers!')
    elif list_length == 1:
        return numbers

    right_start = list_length // 2
    right = numbers[right_start:]
    left = numbers[:right_start]

    return merge(merge_sort(left), merge_sort(right))

