tranasactions_aed = [25.67, 56.78, 100.45, 45.86, 154.23, 17.03, 19.00]

transactions_usd = []

for item in tranasactions_aed:
    item_usd = item * .27
    print(f"Converting value: {item}")
    transactions_usd.append(item_usd)


print(transactions_usd)


lst = [2, 4, 5, 6, 7, 20, 25]

for number in lst:
    if number % 2 == 0:
        print(f"{number} is divisible by 2")
    else:
        print(f"{number} is not divisible by 2")


student_data = [
    {'name' : 'Alice', 'grades' : [90, 87, 76], 'age' : 20},
    {'name' : 'Greg', 'grades' : [98, 95, 67], 'age' : 21},
    {'name' : 'Bryce', 'grades' : [88, 92, 95], 'age' : 19}
]

for student in student_data:
    total_grade = sum(student['grades'])
    number_of_grades = len(student['grades'])
    average_grade = total_grade / number_of_grades
    max_grade = max(student['grades'])

    #Message about the student
    message = f"{student['name']} is {student['age']} years old. "
    message += f"They have an average score of {average_grade:.2f}, and the max grade was {max_grade}. "
    message += "Here are their total grades: \n"

    #Adding a nested loop over grades to iterate and create detailed message
    for idx, grade in enumerate(student['grades']):
        message += f"\t - Test {idx + 1} : {grade}\n"
    
    #Check if student is graduating with honors
    if average_grade > 90:
        message += f"{student['name']} is graduating with honors!"
    else:
        message += f"{student['name']} is graduating." 
    

    print(message)