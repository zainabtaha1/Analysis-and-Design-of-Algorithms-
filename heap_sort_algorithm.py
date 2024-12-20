# -*- coding: utf-8 -*-
"""Heap Sort Algorithm.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12ytDUgAcGUwoQk5n8PNN3BjuiqkKj66Z

# **Part (a): Write all required algorithms needed to sort a sequence of numbers using Heapsort Algorithms**

# **1. Heapify Algorithm (for building a heap and restoring heap property)**
"""

def heapify(arr, n, i):
    largest = i  # Initialize root
    left = 2 * i + 1
    right = 2 * i + 2

    # If left child is larger than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # If right child is larger than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap and heapify the affected sub-tree
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

"""# **2. Build Max-Heap Algorithm**"""

def build_max_heap(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

"""# **3. Heap-Sort Algorithm**"""

def heap_sort(arr):
    n = len(arr)

    build_max_heap(arr)

    # One by one extract elements from heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

"""# **Part (c): Implement your written algorithms in Part (a)**"""

def heapify(arr, n, i):
    largest = i  # Initialize root
    left = 2 * i + 1
    right = 2 * i + 2

    # If left child is larger than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # If right child is larger than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap and heapify the affected sub-tree
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def build_max_heap(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)


def heap_sort(arr):
    n = len(arr)

    build_max_heap(arr)

    # One by one extract elements from heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


# Example usage:
arr = [12, 11, 13, 5, 6, 7]
print("Original array:", arr)
heap_sort(arr)
print("Sorted array:", arr)