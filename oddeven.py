def oddEvenSort(arr):
    n = len(arr)
    isSorted = False
    while not isSorted:
        isSorted = True
        for i in range(1, n - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                isSorted = False
        for i in range(0, n - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                isSorted = False

# User input
arr = list(map(int, input("Enter the elements of the array (separated by space): ").split()))

# Call the function
oddEvenSort(arr)

# Output the sorted array
print("Sorted array:", end=" ")
for num in arr:
    print(num, end=" ")
