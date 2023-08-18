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

6. **Inheritance and Polymorphism: Animal Hierarchy**
   - **Question:** Design a hierarchy of classes for different types of animals, with a base class `Animal` and derived classes like `Dog`, `Cat`, and `Bird`. Implement methods and properties specific to each animal, and demonstrate polymorphism.
   - **Class Signature:**
   ```python
   class Animal:
       def __init__(self, name: str):
           pass

   class Dog(Animal):
       def __init__(self, name: str):
           pass

       def make_sound(self) -> str:
           pass

   class Cat(Animal):
       def __init__(self, name: str):
           pass

       def make_sound(self) -> str:
           pass

   class Bird(Animal):
       def __init__(self, name: str):
           pass

       def make_sound(self) -> str:
           pass
   ```
   - **Example:**
   ```python
   dog = Dog("Buddy")
   cat = Cat("Whiskers")
   bird = Bird("Tweety")

   animals = [dog, cat, bird]
   for animal in animals:
       print(animal.name, ":", animal.make_sound())
   ```
   - **Expected Output:**
   ```
   Buddy : Woof!
   Whiskers : Meow!
   Tweety : Chirp!
   ```

7. **Encapsulation: Bank Account with Access Control**
   - **Question:** Implement a class for a bank account with private attributes for balance. Provide methods to access and modify the balance while ensuring proper encapsulation. How would you handle negative balances?
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

8. **Abstraction: Shape Area Calculation**
   - **Question:** Create an abstract base class `Shape` with abstract methods `area()` and `perimeter()`. Implement derived classes like `Circle`, `Rectangle`, and `Triangle` that inherit from `Shape` and provide specific implementations for the methods.
   - **Class Signature:**
   ```python
   from abc import ABC, abstractmethod

   class Shape(ABC):
       @abstractmethod
       def area(self) -> float:
           pass

       @abstractmethod
       def perimeter(self) -> float:
           pass

   class Circle(Shape):
       def __init__(self, radius: float) -> None:
           pass

       def area(self) -> float:
           pass

       def perimeter(self) -> float:
           pass

   class Rectangle(Shape):
       def __init__(self, width: float, height: float) -> None:
           pass

       def area(self) -> float:
           pass

       def perimeter(self) -> float:
           pass

   class Triangle(Shape):
       def __init__(self, base: float, height: float) -> None:
           pass

       def area(self) -> float:
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
   [Implement Correct Area Calculation]
   [Implement Correct Perimeter Calculation]
   [Implement Correct Area Calculation]
   ```

9. **Interfaces and Multiple Inheritance: Music Player**
   - **Question:** Design classes for a simple music player system. Implement an interface `Playable` for playable items like songs and playlists. Create classes for `Song`, `Playlist`, and `Album`, ensuring proper encapsulation and demonstrating multiple inheritance.
   - **Class Signature:**
   ```python
   class Playable:
       @abstractmethod
       def play(self) -> None:
           pass

   class Song(Playable):
       def __init__(self, title: str, artist: str):
           pass

       def play(self) -> None:
           pass

   class Playlist(Playable):
       def __init__(self, name: str):
           pass

       def add_item(self, item: Playable) -> None:
           pass

       def play(self) -> None:
           pass

   class Album(Playable):
       def __init__(self, title: str, artist: str):
           pass

       def add_song(self, song: Song) -> None:
           pass

       def play(self) -> None:
           pass
   ```
   - **Example:**
   ```python
   song1 = Song("Song 1", "Artist A")
   song2 = Song("Song 2", "Artist B")
   playlist = Playlist("My Playlist")
   album = Album("Album X", "Artist Y")

   playlist.add_item(song1)
   playlist.add_item(song2)
   album.add_song(song1)

   items = [song1, song2, playlist, album]
   for item in items:
       item.play()
   ```
   - **Expected Output:**
   ```
   [Play Song: Song 1 by Artist A]
   [Play Song: Song 2 by Artist B]
   [Play Playlist: My Playlist]
   [Play Album: Album X by Artist Y]
   ```

10. **Composition: Computer System**
   - **Question:** Design a class for a `Computer` that consists of various components like CPU, RAM, and Storage. Implement the composition relationship between the `Computer` class and the component classes.
   - **Class Signature:**
   ```python
   class CPU:
       def __init__(self, model: str):
           pass

   class RAM:
       def __init__(self, capacity_gb: int):
           pass

   class Storage:
       def __init__(self, capacity_gb: int):
           pass

   class Computer:
       def __init__(self, cpu: CPU, ram: RAM, storage: Storage):
           pass
   ```
   - **Example:**
   ```python
   cpu = CPU("Intel i7")
   ram = RAM(16)
   storage = Storage(512)
   computer = Computer(cpu, ram, storage)
   ```
   - **Expected Output:**
   ```
   [Proper Initialization of Computer with Components]
   ```
