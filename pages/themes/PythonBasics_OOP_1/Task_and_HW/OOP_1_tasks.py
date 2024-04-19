# ---------------------------------- Task 1 ---------------------------------- #
""" DESCRIPTION:
Create a class called 'Book' to represent a book. The class should have the following attributes and methods:

Attributes:
- 'title': a string representing the title of the book.
- 'author': a string representing the author of the book.
- 'pages': an integer representing the number of pages in the book.

Methods:
- 'get_book_info()': a method that returns a string with the book's title, author, and number of pages.

Create an instance of the 'Book' class with information about a book and demonstrate the usage of the 'get_book_info' method.
"""

# YOUR CODE HERE (Define the Book class)

# TEST
# book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 192)
# print(book1.get_book_info())

# EXPECTED OUTPUT
# Title: The Great Gatsby, Author: F. Scott Fitzgerald, Pages: 192


# ---------------------------------- Task 2 ---------------------------------- #
""" DESCRIPTION:
Create a class called 'Car' to represent a car. The class should have the following attributes and methods:

Attributes:
- 'make': a string representing the make of the car (e.g., Toyota, Honda).
- 'model': a string representing the model of the car (e.g., Camry, Civic).
- 'year': an integer representing the manufacturing year of the car.

Methods:
- 'start_engine()': a method that prints a message indicating that the car's engine has started.
- 'stop_engine()': a method that prints a message indicating that the car's engine has stopped.

Create an instance of the 'Car' class with information about a car and demonstrate the usage of the 'start_engine' and 'stop_engine' methods.

"""

# YOUR CODE HERE (Define the Car class)

# TEST
# car1 = Car("Toyota", "Camry", 2022)
# car1.start_engine()
# car1.stop_engine()

# EXPECTED OUTPUT:
# Engine started for Toyota Camry 2022
# Engine stopped for Toyota Camry 2022



# ---------------------------------- Task 3 ---------------------------------- #
""" DESCRIPTION:
Create a class called 'Student' to represent a student. The class should have the following attributes and methods:

Attributes:
- 'name': a string representing the student's name.
- 'student_id': an integer representing the student's ID.
- 'courses': a list representing the courses the student is enrolled in.

Methods:
- 'add_course(course_name)': a method that adds a course to the student's list of courses.
- 'remove_course(course_name)': a method that removes a course from the student's list of courses.
- 'list_courses()': a method that prints the list of courses the student is enrolled in.

Create an instance of the 'Student' class with your own information and demonstrate the usage of the methods.
"""

# YOUR CODE HERE (Define the Student class)


# TEST
# student1 = Student("Alice", 12345)
# student1.add_course("Math")
# student1.add_course("History")
# student1.list_courses()

#EXPECTED OUTPUT:
# Courses: Math,History



# ---------------------------------- Task 4 ---------------------------------- #
""" DESCRIPTION:
Given a library of books, define classes for both a library and a book.
The library should have a name and a list of books.
Each book should contain information about the title, author, publisher, year of publication, and ISBN number.
In the Library class add methods to add a book to the library, search for a book by a specified author,
display information about a book, and delete a book from the library.
"""

### YOUR CODE HERE (Define the Library and Book classes)


### TEST:
# library = Library("City Library")
# book1 = Book("Book One", "Author A", "Publisher X", 2020, "ISBN12345")
# book2 = Book("Book Two", "Author B", "Publisher Y", 2021, "ISBN67890")
# book2 = Book("Book Three", "Author A", "Publisher Z", 2021, "ISBN12390")

# library.add_book(book1)
# library.add_book(book2)

# library.display_book_info("ISBN12345")

# print(library.find_books_by_author("Author A"))

# library.remove_book("ISBN12345")
# library.display_book_info("ISBN12345")

### EXPECTED OUTPUT:
# Book One, Author A, Publisher X, 2020, ISBN: ISBN12345
# Book ISBN12345 not found.
# ['Book One', 'Book Three']
# Book ISBN12345 not found.