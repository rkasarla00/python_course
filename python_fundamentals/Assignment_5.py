'''
Exercise 1: List Manipulation

Create a list called fruits containing the following fruits: apple, banana, cherry, date.
Add "elderberry" to the end of the list.
Remove "banana" from the list.
Sort the list in alphabetical order.
Print the list.
'''
fruits = ['apple', 'banana', 'cherry', 'date']
fruits.append('elderberry')
fruits.remove('banana')
fruits.sort()
print(fruits)

'''
Exercise 2: Dictionary Basics

Create a dictionary called student with the following key-value pairs:
name: John Doe
age: 25
major: Computer Science
Change the value of 'major' to "Electrical Engineering".
Add a new key-value pair: 'year' with a value of 'Senior'.
Print out the keys in the dictionary.
Print out the values in the dictionary.
'''
student = {'name': 'John Doe',
'age': 25,
'major': 'Computer Science'}

student['major'] = 'Electrical Engineering'
student['year'] = 'Senior'
for i in student:
    print (f"KEY : {i}")

for i in student:
    print(f"VALUE : {student[i]}")


'''
Exercise 3: List of Dictionaries

Create a list of dictionaries, where each dictionary represents a book and has the following keys: title, author, and year.
Add at least 3 books to your list.
Print the title of the second book in the list.
Print the year the third book was published.
Iterate over the list and print out each book's title and author.
'''
books = {'1' : {'title' : "Harry Potter", 'author' : 'J.K Rowling', 'year' : 1997},
         '2' : {'title' : "Percy Jackson", 'author' : 'Rick Riordan', 'year' : 2005},
         '3' : {'title' : "Hunger Games", 'author' : 'Suzanne Collins', 'year' : 2008}}

print(books['2']['title'])
print(books['3']['year'])

for i in books:
    print(books[i]['title'])
    print(books[i]['author'])


'''
Exercise 4: Dictionary containing a List

Create a dictionary called courses where the keys are the names of courses (e.g., "math", "history", "chemistry") and the values are lists of student names enrolled in each course. Initialize every course with a list of some random names of your choosing (ie, a list of strings). Then complete the following using methods/functions:
Add 5 students to "math".
Remove the third student from "history".
Print out the students in "chemistry".
Add a new course "physics" with a list of 4 students.
'''

courses = {'math' : ['R.K', 'S.K', 'P.K'],
           'history' : ['P.K', 'S.K', 'R.K'],
           'chemistry' : ['S.K', 'P.K', 'R.K']}

courses['math'] = ['S.M', 'V.K', 'I.P', 'L.B', 'R.M']
del courses['history'][2]
print(courses['history'])
print(courses['chemistry'])
courses['physics'] = ['S.M', 'V.K', 'I.P', 'L.B']
print(courses['physics'])