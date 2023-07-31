## String Manipulation Interview Questions

1. **Reverse a String**
   - **Question:** Given a string, write a function to reverse it.
   - **Function Signature:**
   ```python
   def reverse_string(s: str) -> str:
   ```
   - **Example:**
   ```python
   input_str = "hello"
   print(reverse_string(input_str))
   ```
   - **Expected Output:**
   ```
   "olleh"
   ```

2. **Check Palindrome**
   - **Question:** Write a function to determine if a given string is a palindrome (reads the same backward as forward).
   - **Function Signature:**
   ```python
   def is_palindrome(s: str) -> bool:
   ```
   - **Example:**
   ```python
   input_str = "level"
   print(is_palindrome(input_str))
   ```
   - **Expected Output:**
   ```
   True
   ```

3. **Count Character Occurrences**
   - **Question:** Implement a function that counts the occurrences of a specific character in a given string.
   - **Function Signature:**
   ```python
   def count_occurrences(s: str, char: str) -> int:
   ```
   - **Example:**
   ```python
   input_str = "hello"
   character = "l"
   print(count_occurrences(input_str, character))
   ```
   - **Expected Output:**
   ```
   2
   ```

4. **Check Anagrams**
   - **Question:** Create a function to check if two strings are anagrams (contain the same characters but in different orders).
   - **Function Signature:**
   ```python
   def are_anagrams(s1: str, s2: str) -> bool:
   ```
   - **Example:**
   ```python
   string1 = "listen"
   string2 = "silent"
   print(are_anagrams(string1, string2))
   ```
   - **Expected Output:**
   ```
   True
   ```

5. **String Compression**
   - **Question:** Design a function that compresses a string by replacing repeated characters with their count.
   - **Function Signature:**
   ```python
   def compress_string(s: str) -> str:
   ```
   - **Example:**
   ```python
   input_str = "aaabbbccc"
   print(compress_string(input_str))
   ```
   - **Expected Output:**
   ```
   "a3b3c3"
   ```

6. **Longest Substring Without Repeating Characters**
   - **Question:** Given a string, find the length of the longest substring without repeating characters.
   - **Function Signature:**
   ```python
   def length_of_longest_substring(s: str) -> int:
   ```
   - **Example:**
   ```python
   input_str = "abcabcbb"
   print(length_of_longest_substring(input_str))
   ```
   - **Expected Output:**
   ```
   3
   ```

7. **Valid Parentheses**
   - **Question:** Write a function to determine if a given string containing only parentheses is valid.
   - **Function Signature:**
   ```python
   def is_valid_parentheses(s: str) -> bool:
   ```
   - **Example:**
   ```python
   input_str = "()[]{}"
   print(is_valid_parentheses(input_str))
   ```
   - **Expected Output:**
   ```
   True
   ```

8. **String to Integer (atoi)**
   - **Question:** Implement the `atoi` function, which converts a string to an integer.
   - **Function Signature:**
   ```python
   def atoi(s: str) -> int:
   ```
   - **Example:**
   ```python
   input_str = "42"
   print(atoi(input_str))
   ```
   - **Expected Output:**
   ```
   42
   ```

9. **Remove Duplicates**
   - **Question:** Create a function that removes duplicate characters from a given string, keeping only the first occurrence of each character.
   - **Function Signature:**
   ```python
   def remove_duplicates(s: str) -> str:
   ```
   - **Example:**
   ```python
   input_str = "hello"
   print(remove_duplicates(input_str))
   ```
   - **Expected Output:**
   ```
   "helo"
   ```

10. **String Rotation**
    - **Question:** Given two strings, write a function to check if one string is a rotation of the other.
    - **Function Signature:**
    ```python
    def is_rotation(s1: str, s2: str) -> bool:
    ```
    - **Example:**
    ```python
    string1 = "waterbottle"
    string2 = "erbottlewat"
    print(is_rotation(string1, string2))
    ```
    - **Expected Output:**
    ```
    True
    ```


