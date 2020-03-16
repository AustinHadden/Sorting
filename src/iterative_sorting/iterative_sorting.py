# TO-DO: Complete the selection_sort() function below
def selection_sort( arr ):
    for x in range(len(arr)):
        min_id = x
        for y in range(x+1, len(arr)):
            if arr[min_id] > arr[y]:
                min_id = y

        arr[x], arr[min_id] = arr[min_id], arr[x]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    x = len(arr)

    for y in range(x):
        for z in range(0, x-y-1):
            if arr[z] > arr[z+1]:
                arr[z], arr[z+1] = arr[z+1], arr[z]

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr