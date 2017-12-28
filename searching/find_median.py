from random import randint
import lib.assertion

def find_median(nums, median_index=None):
    if (len(nums) < 1): 
        raise RuntimeError('List argument must be non-empty.')
    if median_index == None: 
        median_index = len(nums) // 2


    #pick a partition index at random
    partition_index = randint(0, len(nums) - 1)
    partition_value = nums[partition_index]
    nums_left = []
    nums_right = []
    nums_middle = [partition_value]

    for i in range(0, len(nums)):
        if i == partition_index:
            continue
        elif nums[i] < partition_value:
            nums_left.append(nums[i])
        elif nums[i] > partition_value:
            nums_right.append(nums[i])
        else:
            nums_middle.append(nums[i])
    
    mid_and_left_length = len(nums_left) + len(nums_middle) 
    if median_index < mid_and_left_length - 1:
        return find_median(nums_left, median_index)
    elif median_index > mid_and_left_length - 1:
        return find_median(nums_right, median_index - mid_and_left_length)
    else:
        return partition_value


def main():
    lib.assertion.equals(7, find_median([8,7,10,3,1,2]))
    lib.assertion.equals(6, find_median([7,9,3,4,1,6,8]))
    lib.assertion.equals(6, find_median([1,6,8]))
    lib.assertion.equals(6, find_median([6]))
    lib.assertion.equals(9, find_median([1,78,9,4,18,3,2,8,99,55,33,21,6]))

if __name__ == '__main__':
    main()
