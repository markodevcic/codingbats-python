# Given an array of ints, return True if 6
# appears as either the first or last element
# in the array. The array will be length 1 or more.
#
#
# first_last6([1, 2, 6]) → True
# first_last6([6, 1, 2, 3]) → True
# first_last6([13, 6, 1, 2, 3]) → False

def first_last6(arr):

    return arr[0] == 6 or arr[-1] == 6

    # for i in arr:
    #     if arr[0] == 6 or arr[-1] == 6:
    #         return True
    # return False


print(first_last6([6,3,5]))