def move_forward():
    print("moving forward")

def turn(direction):
    print(f"turning {direction}")

def start_engine():
    print("starting engine")

def stop_engine():
    print("stopping engine")

def follow_roundabout(exit_number):
    print(f"taking exit number {exit_number} from the roundabout")


start_engine()
destination = input("Where would you like to go? ")

if (destination == "library"):
    move_forward()
    turn("left")
    print("Arrived at library!")
elif (destination == "tech park"):
    move_forward()
    turn("right")
    print("Arrived at tech park!")
elif (destination in ["hospital", "mall", "airport", "university", "stadium"]):
    move_forward()
    print("Entering roundabout")
    if (destination == "hospital"):
        follow_roundabout(1)
        print("Arrived at hospital")
    elif (destination == "mall"):
        follow_roundabout(2)
        move_forward()
        turn("right")
        print("Arrived at mall")
    elif (destination == "airport"):
        follow_roundabout(3)
        print("Arrived at airport")
    elif (destination == "university"):
        follow_roundabout(4)
        turn("left")
        print("Arrived at university")
    else:
        follow_roundabout(4)
        turn("right")
        print("Arrived at stadium")
else:
    print("Destination is not found")

stop_engine()

