def validate_email(email):
    if "@" in email and "." in email:
        return True
    else:
        raise ValueError("Invalid Email Address")
    
email = input("Enter your email: ")

validate_email(email)
print("")