## Object-Oriented Programming (OOP) Questions

1. **Create a Class for Rectangle**
   - **Question:** Design a class representing a rectangle with methods to calculate its area and perimeter.
   - **Class Signature:**
   ```python
   class Rectangle:
       def __init__(self, width: float, height: float):
           pass

       def area(self) -> float:
           pass

       def perimeter(self) -> float:
           pass
   ```
   - **Example:**
   ```python
   rectangle = Rectangle(4, 5)
   print(rectangle.area())
   print(rectangle.perimeter())
   ```
   - **Expected Output:**
   ```
   20.0
   18.0
   ```

2. **Create a Class for Bank Account**
   - **Question:** Implement a class representing a bank account with methods to deposit, withdraw, and check the balance.
   - **Class Signature:**
   ```python
   class BankAccount:
       def __init__(self, initial_balance: float):
           pass

       def deposit(self, amount: float) -> None:
           pass

       def withdraw(self, amount: float) -> None:
           pass

       def check_balance(self) -> float:
           pass
   ```
   - **Example:**
   ```python
   account = BankAccount(1000)
   account.deposit(500)
   account.withdraw(200)
   print(account.check_balance())
   ```
   - **Expected Output:**
   ```
   1300.0
   ```

3. **Create a Class for Book**
   - **Question:** Design a class representing a book with properties like title, author, and methods to display book information.
   - **Class Signature:**
   ```python
   class Book:
       def __init__(self, title: str, author: str):
           pass

       def display_info(self) -> None:
           pass
   ```
   - **Example:**
   ```python
   book1 = Book("Python Programming", "John Doe")
   book2 = Book("Data Science Handbook", "Jane Smith")
   book1.display_info()
   book2.display_info()
   ```
   - **Expected Output:**
   ```
   Title: Python Programming, Author: John Doe
   Title: Data Science Handbook, Author: Jane Smith
   ```

4. **Inheritance - Shape Hierarchy**
   - **Question:** Create a hierarchy of classes for shapes, with a base class Shape and derived classes like Circle, Rectangle, and Triangle. Implement methods to calculate area and perimeter for each shape.
   - **Class Signature:**
   ```python
   class Shape:
       def area(self) -> float:
           pass

       def perimeter(self) -> float:
           pass

   class Circle(Shape):
       def __init__(self, radius: float):
           pass

   class Rectangle(Shape):
       def __init__(self, width: float, height: float):
           pass

   class Triangle(Shape):
       def __init__(self, base: float, height: float):
           pass
   ```
   - **Example:**
   ```python
   circle = Circle(5)
   rectangle = Rectangle(4, 6)
   triangle = Triangle(3, 4)
   print(circle.area())
   print(rectangle.perimeter())
   print(triangle.area())
   ```
   - **Expected Output:**
   ```
   78.54
   20.0
   6.0

5. **Encapsulation - Private Variables**
   - **Question:** Implement a class with private variables to store sensitive information like a password. Provide methods to set and get the password securely.
   - **Class Signature:**
   ```python
   class UserAccount:
       def __init__(self, username: str):
           pass

       def set_password(self, password: str) -> None:
           pass

       def get_password(self) -> str:
           pass
   ```
   - **Example:**
   ```python
   user = UserAccount("john_doe")
   user.set_password("password123")
   print(user.get_password())
   ```
   - **Expected Output:**
   ```
   **********
   ```
