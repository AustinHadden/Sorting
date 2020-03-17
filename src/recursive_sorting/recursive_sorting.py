# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    merge_arrays = arrA + arrB

    for i in range(0, len(merged_arr)):
        min_id = 0
        for n in range(0, len(merge_arrays)):
            if merge_arrays[n] < merge_arrays[min_id]:
                min_id = n
        merged_arr[i] = merge_arrays.pop(min_id)
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) <= 1:
        return arr

    left_side = arr[len(arr) // 2 :]
    right_side = arr[: len(arr) // 2]

    left_side = merge_sort(left_side)
    right_side = merge_sort(right_side)

    arr = merge(left_side, right_side)

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
