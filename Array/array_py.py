# Array is a collection of items stored at contiguous memory locations. The idea is to store multiple items of the same type together. This makes it easier to calculate the position of each element by simply adding an offset to a base value, i.e., the memory location of the first element of the array (generally denoted by the name of the array).
# Array in Python can be represented by list data type.
# Creating an array
arr = [1, 2, 3, 4, 5]
print("Array:", arr)
# Accessing elements of an array
print("First element:", arr[0])
print("Third element:", arr[2])
# Modifying elements of an array
arr[1] = 20
print("Modified Array:", arr)
# Adding elements to an array
arr.append(6)
print("Array after adding an element:", arr)
# Removing elements from an array
arr.remove(3)
print("Array after removing an element:", arr)
# Slicing an array
print("Sliced Array:", arr[1:4])
# Reversing an array
print("Reversed Array:", arr[::-1])
# Length of an array
print("Length of the array:", len(arr))
# Iterating through an array
print("Iterating through the array:")
for i in arr:
    print(i)
# Checking if an element exists in an array
print("Is 20 in the array?", 20 in arr)
# Clearing an array
arr.clear()
print("Array after clearing:", arr)
# Copying an array
arr = [1, 2, 3, 4, 5]
arr_copy = arr.copy()
print("Original Array:", arr)
print("Copied Array:", arr_copy)
# Joining two arrays
arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
arr3 = arr1 + arr2
print("Joined Array:", arr3)
# Finding the index of an element in an array
print("Index of 4 in the array:", arr3.index(4))
# Counting the occurrences of an element in an array
print("Count of 2 in the array:", arr3.count(2))
# Sorting an array
arr3.sort()
print("Sorted Array:", arr3)
# Reversing an array using reverse() method
arr3.reverse()
print("Reversed Array using reverse() method:", arr3)
# Finding the maximum and minimum elements in an array
print("Maximum element in the array:", max(arr3))
print("Minimum element in the array:", min(arr3))
# Finding the sum of elements in an array
print("Sum of elements in the array:", sum(arr3))
# Finding the average of elements in an array
average = sum(arr3) / len(arr3)
print("Average of elements in the array:", average)
# Finding the product of elements in an array
product = 1
for num in arr3:
    product *= num
print("Product of elements in the array:", product)
# Finding the median of elements in an array
arr3.sort()
n = len(arr3)
if n % 2 == 0:
    median = (arr3[n // 2 - 1] + arr3[n // 2]) / 2
else:    
    median = arr3[n // 2]
print("Median of elements in the array:", median)
