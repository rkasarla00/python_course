

def move_forward():
    print("Moving Forward")

def turn(direction):
    print(f"Turning {direction}")

def start_engine():
    print("**Starting engine**")

def stop_engine():
    print("**Stopping engine**")

destination = input("Where do you want to go? ")

start_engine()
move_forward()
if destination == "school":
    turn("right")
    print("We arrived at school!")
elif destination == "grocery store" or destination == "dentist":
    turn("left")
    move_forward()
    if (destination == "grocery store"):
        turn("right")
        print("We have arrived at the grocery store!")
    else:
        turn("left")
        print("We have arrived at the dentist!")
elif destination == "restraunt":
    move_forward()
    print("We have arrived at the restraunt!")
else:
    print("Invalid Destination...")

