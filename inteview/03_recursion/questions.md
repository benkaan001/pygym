## Recursion Questions

1. **Factorial Calculation**
   - Question: Write a recursive function to calculate the factorial of a given positive integer `n`.
   - Function Signature: `def factorial(n: int) -> int:`
   - Sample Input: `factorial(5)`
   - Expected Output: `120`

2. **Fibonacci Sequence**
   - Question: Write a recursive function to calculate the `n`th number in the Fibonacci sequence, where `F(0) = 0`, `F(1) = 1`, and `F(n) = F(n-1) + F(n-2)` for `n > 1`.
   - Function Signature: `def fibonacci(n: int) -> int:`
   - Sample Input: `fibonacci(6)`
   - Expected Output: `8`

3. **Power Calculation**
   - Question: Write a recursive function to calculate the result of raising a base `x` to a non-negative integer exponent `n`.
   - Function Signature: `def power(x: float, n: int) -> float:`
   - Sample Input: `power(2, 3)`
   - Expected Output: `8`

4. **Sum of Digits**
   - Question: Write a recursive function to calculate the sum of digits in a positive integer `n`.
   - Function Signature: `def sum_of_digits(n: int) -> int:`
   - Sample Input: `sum_of_digits(12345)`
   - Expected Output: `15`

5. **Palindrome Check**
   - Question: Write a recursive function to check if a given string is a palindrome (reads the same forwards and backwards).
   - Function Signature: `def is_palindrome(s: str) -> bool:`
   - Sample Input: `is_palindrome("racecar")`
   - Expected Output: `True`

6. **Binary Search in Sorted List**
   - Question: Write a recursive function to perform binary search on a sorted list and return the index of the target element if found, or -1 if not found.
   - Function Signature: `def binary_search(arr: List[int], target: int, low: int, high: int) -> int:`
   - Sample Input: `binary_search([2, 4, 6, 8, 10], 6, 0, 4)`
   - Expected Output: `2`

7. **String Permutations**
   - Question: Write a recursive function to generate all possible permutations of a given string.
   - Function Signature: `def string_permutations(s: str) -> List[str]:`
   - Sample Input: `string_permutations("abc")`
   - Expected Output: `['abc', 'acb', 'bac', 'bca', 'cab', 'cba']`
