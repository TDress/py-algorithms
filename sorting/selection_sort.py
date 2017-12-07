import lib.assertion 
import sys

def selection_sort(number_list): 
    sorted = number_list[:]
    size = len(number_list)
    if size < 1:
        raise RuntimeError('Argument must be non-empty')

    index = 0
    while index < size - 1:
        index_of_smallest = index
        for i in range(index + 1, size): 
            if sorted[i] < sorted[index_of_smallest]:
                index_of_smallest = i
            
        if index != index_of_smallest:
            # swap items
            sorted[index], sorted[index_of_smallest] = (
                sorted[index_of_smallest], sorted[index]
            )
        index += 1

    return sorted

def selection_sort_recursive(number_list): 
    size = len(number_list)
    if size < 2:
        return number_list

    i_smallest = 0
    for j in range(i_smallest + 1, size): 
        if number_list[j] < number_list[i_smallest]:
            i_smallest = j

    new_list = number_list[:i_smallest] + number_list[i_smallest + 1:]
    return [number_list[i_smallest]] + selection_sort_recursive(new_list)



def main(recursive=False): 
    sort_function = selection_sort if not recursive else selection_sort_recursive
    lib.assertion.equals([8], sort_function([8]))
    lib.assertion.equals([1,2,3,4,5,6,7,8,9], sort_function([7,1,5,2,8,9,3,4,6]))
    lib.assertion.equals([1,2,3,4,5,6,7,8,9], sort_function([1,7,5,2,8,9,3,4,6]))
    lib.assertion.equals([1,2,3,4,5,6,7,8,9], sort_function([9,8,7,6,5,4,3,2,1]))

if __name__ == '__main__': 
    main('--recursive' in sys.argv)

