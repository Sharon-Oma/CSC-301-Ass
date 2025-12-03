my_list = [2, 5, 7, 10, 14, 20]
t = 10

def search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
print(search(my_list, t))