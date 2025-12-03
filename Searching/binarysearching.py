my_list = [1, 3, 5, 7, 9, 11, 13]
bs_t = 9
def bi_search (arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) 
        if arr [mid] == target:
            return mid
        elif arr [mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
print(bi_search(my_list, bs_t))