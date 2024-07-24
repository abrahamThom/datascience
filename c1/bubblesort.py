def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Get input from user
input_str = input("Enter elements of the array separated by spaces: ")

# Convert input string to list of integers
arr = list(map(int, input_str.split()))

# Call bubble_sort function
bubble_sort(arr)

# Print sorted array
print("Sorted array:", arr)
