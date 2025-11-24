def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
def print_array(arr):
    for x in arr:
        print(x, end=" ")
    print()
arr = [5, 1, 4, 2, 8]
bubble_sort(arr)
print("Sorted array:")
print_array(arr)
