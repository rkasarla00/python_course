my_list = ['a', 'b', 'c', 'd']

#Adding another letter at the end
my_list.append('e')

#

print(my_list)
#Getting index value
print(my_list[-2])
#slicing
print(my_list[1:4])
#Flips the order
print(my_list[::-1])


languages = ['Python', 'Swift', 'C++', 'C', 'Java', 'Rust', 'R']

# deleting the second item
del languages[1]
print(languages)
languages.remove('C')
print(languages)


words1 = ["hello", "world"]
words2 = ["goodbye", "mars"]

all_words = words1 + words2
print(all_words)


transactions = [10.1, 22.0, 32.2, 17.8, 55.0]
min_number = min(transactions)
max_number = max(transactions)
total_number = sum(transactions)

print(f"The small number is {min_number}")
print(f"The max number is {max_number}")
print(f"The total sum of transactions is {total_number}")

print()
print()

fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
  print(fruit)

fruit_to_find = 'banana'
if fruit_to_find in fruits:
  print(True)

print()
print()

date = "2022-03-18"
parts = date.split("-")
print(parts)
#splitting and assiging each part a variable name
year, month, day = date.split("-")
print(year) 
print(month)
print(day)