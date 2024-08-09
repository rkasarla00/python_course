print("Welcome to the magic potion shop!")
print("These are a list potions you can create: ")

potions = {
    'Invisibility Potion': ['Moonstone', 'Dragon scale', 'Fairy dust'],
    'Flying Potion': ["Phoenix feather", "Troll tooth", "Mermaid scale"],
    'Healing Potion': ["Unicorn horn", "Elf hair", "Golden apple"] 
    }
for potion in potions:
    print(potion)

user_potion = input("Which potion would you like to create? ")

print(f"The ingredients for {user_potion} are: ")
print(potions[user_potion])
print("")

print("Lets start by buying the ingredients")
x = 0
while x <= 2:
    y = input(f"Would you like to purchase {potions[user_potion][x]}? Enter 'y'/'n' ")
    if (y == 'y'):
        print(f"Congrats! You purchased {potions[user_potion][x]}")
        x += 1
    else:
        print("You stopped shopping...")
        break
if x == 3:
    print("Congrats! You purchased all ingredients to make your potion!")