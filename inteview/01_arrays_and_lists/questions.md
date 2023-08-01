## Arrays and Lists Interview Questions

1. **Find Maximum Element**
   - **Question:** Write a function to find the maximum element in an array/list.
   - **Function Signature:**
   ```python
   def find_maximum(arr: List[int]) -> int:
   ```
   - **Example:**
   ```python
   input_arr = [3, 7, 1, 9, 4]
   print(find_maximum(input_arr))
   ```
   - **Expected Output:**
   ```
   9
   ```

2. **Find Second Largest Element**
   - **Question:** Implement a function to find the second largest element in an array/list.
   - **Function Signature:**
   ```python
   def find_second_largest(arr: List[int]) -> int:
   ```
   - **Example:**
   ```python
   input_arr = [3, 7, 1, 9, 4]
   print(find_second_largest(input_arr))
   ```
   - **Expected Output:**
   ```
   7
   ```

3. **Remove Duplicates**
   - **Question:** Write a function to remove duplicates from an array/list and return the unique elements.
   - **Function Signature:**
   ```python
   def remove_duplicates(arr: List[int]) -> List[int]:
   ```
   - **Example:**
   ```python
   input_arr = [1, 2, 2, 3, 4, 4, 5]
   print(remove_duplicates(input_arr))
   ```
   - **Expected Output:**
   ```
   [1, 2, 3, 4, 5]
   ```

4. **Rotate Array by K Positions**
   - **Question:** Design a function to rotate an array/list by a given number of positions to the right.
   - **Function Signature:**
   ```python
   def rotate_array(arr: List[int], k: int) -> List[int]:
   ```
   - **Example:**
   ```python
   input_arr = [1, 2, 3, 4, 5]
   k = 2
   print(rotate_array(input_arr, k))
   ```
   - **Expected Output:**
   ```
   [4, 5, 1, 2, 3]
   ```

5. **Merge Two Sorted Arrays**
   - **Question:** Create a function to merge two sorted arrays/lists into a single sorted array/list.
   - **Function Signature:**
   ```python
   def merge_sorted_arrays(arr1: List[int], arr2: List[int]) -> List[int]:
   ```
   - **Example:**
   ```python
   input_arr1 = [1, 3, 5]
   input_arr2 = [2, 4, 6]
   print(merge_sorted_arrays(input_arr1, input_arr2))
   ```
   - **Expected Output:**
   ```
   [1, 2, 3, 4, 5, 6]
   ```

6. **Find Missing Number**
   - **Question:** Given an array/list of integers from 1 to n with one missing number, write a function to find the missing number.
   - **Function Signature:**
   ```python
   def find_missing_number(arr: List[int]) -> int:
   ```
   - **Example:**
   ```python
   input_arr = [1, 3, 4, 2, 6, 7, 8]
   print(find_missing_number(input_arr))
   ```
   - **Expected Output:**
   ```
   5
   ```

7. **Find Intersection of Two Arrays**
   - **Question:** Implement a function to find the intersection of two arrays/lists and return the common elements.
   - **Function Signature:**
   ```python
   def find_intersection(arr1: List[int], arr2: List[int]) -> List[int]:
   ```
   - **Example:**
   ```python
   input_arr1 = [1, 2, 3, 4, 5]
   input_arr2 = [3, 4, 5, 6, 7]
   print(find_intersection(input_arr1, input_arr2))
   ```
   - **Expected Output:**
   ```
   [3, 4, 5]
   ```

8. **Implement Stack using List**
   - **Question:** Create a stack data structure using a list and implement push, pop, and peek (top) operations.
   - **Function Signature for Stack:**
   ```python
   class Stack:
       def __init__(self):
           pass

       def push(self, value: int) -> None:
           pass

       def pop(self) -> int:
           pass

       def peek(self) -> int:
           pass
   ```

9. **Implement Queue using List**
   - **Question:** Create a queue data structure using a list and implement enqueue, dequeue, and peek operations.
   - **Function Signature for Queue:**
   ```python
   class Queue:
       def __init__(self):
           pass

       def enqueue(self, value: int) -> None:
           pass

       def dequeue(self) -> int:
           pass

       def peek(self) -> int:
           pass
   ```

10. **Search in Rotated Sorted Array**
    - **Question:** Given a rotated sorted array, write a function to search for a target element. Return the index if found; otherwise, return -1.
    - **Function Signature:**
    ```python
    def search_rotated_array(arr: List[int], target: int) -> int:
    ```
    - **Example:**
    ```python
    input_arr = [4, 5, 6, 7, 0, 1, 2]
    target_value = 0
    print(search_rotated_array(input_arr, target_value))
    ```
    - **Expected Output:**
    ```
    4
    ```