'''
1) Create a function called dollarizer that takes a word replaces every s with a $ sign and outputs it
2) Create function called eurizer that takes a word that also replaces every e with euro sign
3) Now, combine the dollarizer and eurizer function into one, more general function called replacer that takes a word and 2 characters as input and replaces every occurrence of character 1 with character 2
4) Create a function wonky_text that replaces every s with the $ sign, every e with the euro sign and every l with the £
Hint: utilize the functions you have created above to avoid repeating yourself 
5) Create a function named celsius_to_fahrenheit that takes a temperature in Celsius and returns its equivalent in Fahrenheit. Use the formula:  F = C * 9/5 + 32.
6) Create a function named age_in_days that takes an age in years (assume whole years only) and returns the age in days (ignore leap years). Assume each year has 365 days.
7) Create a function named simple_interest that calculates simple interest. It should take three arguments: principal amount, rate of interest, and time in years. Use the formula: ( SI = P * R * T ). Return the calculated simple interest.
8) Write a function named plan_finances that takes a principal amount, rate of interest, time in years, and a desired final amount after simple interest. The function should return whether the final amount after simple interest is achieved from the principal within the given time and rate.
'''
def dollarizer(x):
    return x.replace('s', '$')

def eurizer(x):
    return x.replace("e", "€")

def replacer(x, char1, char2):
    return x.replace(char1, char2)

def wonky_text(x):
    phase_1 =  dollarizer(x)
    phase_2 = eurizer(phase_1)
    return phase_2.replace('1', '£')

def celsius_to_fahrenheit(celcius):
    return celcius * (9/5) + 32

def age_in_days(age):
    return age * 365

def simple_interest(p, r, t):
       return p * r * t

def plan_finances(p, r, t, final):
    step_1 = simple_interest(p,r,t)
    if (final == step_1):
        return True
    elif (final > step_1):
        return True
    else:
        return False



print(dollarizer("testcase"))
print(eurizer("testcase"))
print(replacer("testcase", 't', '#'))
print(wonky_text("1est1ase"))
print(f"25 degree F is {celsius_to_fahrenheit(25)} C")
print(f"The total age in days for a 25 year old is {age_in_days(25)} days")
print(f"Simple Interest: {simple_interest(100, .75, 5)} ")
print(f"Plan Finances: {plan_finances(100, .75, 5, 500)}")
