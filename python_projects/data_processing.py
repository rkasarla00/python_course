#Prompt the user to enter a sentence and then print the sentence in uppercase letters.
sentence_upper = input("Write a sentence that you would like: ").upper()
print(sentence_upper)
#Prompt the user to enter a paragraph and then count the number of words in the paragraph.
count_words = input("Write a paragraph of your choice: ").split()
print(f"This paragraph has {len(count_words)} words")
#Prompt the user for a string, and check if all the characters in the string are digits. Output true or false
char_in_string = input("Enter any string you would like: ")
char_in_string_2 = all(chr.isdigit() for chr in char_in_string)
print(char_in_string_2)
#Prompt the user for a string, and replace all occurrences of the letter "a" with the letter "o".
og_string = input("Enter any string of your choice: ")
replace_string = og_string.replace("a", "o")
print(f"The new string with the characters 'a' replaced w/ 'o' is: {replace_string}")
#Prompt the user to enter their full name and then print their initials. Assume that the user will enter their full name with a space between each name.
name = input("Enter your full, first and last name: ").upper()
names = name.split()
print(f"Your initials are: {names[0][0]}.{names[1][0]}")
#Prompt the user for a string, then print its length.
z = input("Enter any string you like: ")
print(len(z))