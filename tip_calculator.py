print("Welcome to  payment calculator")  
totalAmount = int(input("How much do you want to pay?"))  
print("How much tip you want to pay? 10, 15, or 20")  
tip = int(input("Enter the tip you want to pay: "))  
tip2 = (totalAmount * tip) / 100  
finalTip = totalAmount + tip2  
print(f"Tip amount: {tip2}")  
print("Your final total amount is ", finalTip)  
numberOfPeople = int(input("Enter the number of people you want to split: "))  
print(f"Total bill: {finalTip} and after splitting in {numberOfPeople}, \n per person bill will be {finalTip/numberOfPeople}")
