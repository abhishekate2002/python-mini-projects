print("Welcome to Pizza shop")  
size = input("What is your size? S, M, or L")  
chicken = input("Want chicken on your pizza?")  
extra_anything = input("Would you like extra anything?")  
prize = 12  
if size == "S":  
    print("Your pizza prize is 12$")  
    prize = 12  
elif size == "M":  
    print("Your pizza prize is 15$")  
    prize = 15  
else:  
    print("Your pizza prize is 17$")  
    prize = 17  
if chicken:  
    print("Your chicken pizza prize is 13$")  
if extra_anything:  
    print(f"Your pizza with {size} and extra {extra_anything} is for {prize + 1}")
