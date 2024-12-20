# Analysis-and-Design-of-Algorithms-
The following programing assignment measures the ability to analyze and  implement Heap-Sort algorithm.

Part (b): Analyze in detail your written algorithms
1. Time Complexity Analysis:
Building the max heap:

The heapify function is called for each node. For a tree with n elements, the heapify operation has a time complexity of O(log n) because, in the worst case, it needs to traverse the height of the tree.
Since we call heapify for each non-leaf node, the overall time complexity to build the max heap is O(n).
Sorting the array:

After building the heap, we repeatedly swap the root element with the last element of the heap and reduce the heap size. Each swap involves reheapifying the heap.
The number of heapify calls is n - 1, and each call takes O(log n) time.
Therefore, the time complexity for the sorting phase is O(n log n).
Overall Time Complexity:

The time complexity for Heap-Sort is dominated by the sorting phase and is O(n log n).
2. Space Complexity:
python
Copy code
- Heap-Sort is an in-place sorting algorithm, meaning it does not require any extra space apart from the input array.
- The space complexity is **O(1)**, making it very space-efficient.
3. Stability:
vbnet
Copy code
- Heap-Sort is **not stable**. Stability means that elements with equal values retain their relative order after sorting. However, in Heap-Sort, the relative order of equal elements might change due to the heap structure and the way elements are swapped.
