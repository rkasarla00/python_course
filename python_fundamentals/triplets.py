name1 = input("Enter the first name: ")
name1_formatted = name1.strip().capitalize()
name2 = input("Enter the second name: ")
name2_formatted = name2.strip().capitalize()
name3 = input("Enter the third name: ")
name3_formatted = name3.strip().capitalize()

print(f"The three names are: {name1_formatted}, {name2_formatted}, and {name3_formatted}")

#New Task
x = input("Enter a number to be multiplied by 10: ").replace(",", "")

print(int(x) * 10)