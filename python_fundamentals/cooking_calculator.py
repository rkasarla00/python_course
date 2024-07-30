
turkey_cooking_time = 14
ham_cooking_time = 5

def cooking_end_time(start_time, duration):

    return (start_time + duration) % 24


print(f"Take the turkey out at {cooking_end_time(20, turkey_cooking_time)} o'clock")
print(f"Take the ham out at {cooking_end_time(15, ham_cooking_time)} o'clock")