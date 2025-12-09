import random  
  
symbols = ["!", "@", "#", "$", "%", "^", "&", "*"]  
sletters = ["A", "B", "C", "D", "E", "F", "G","H","I","J", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]  
# cletters = ["A", "B", "C", "D", "E", "F", "G","H","I","J"]  
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9","0"]  
  
print("Welcome to password generator!, we build strong passwords that peope trust.")  
numOfCharacter = int(input("How many characters would you like? "))  
numOfSymbol = int(input("How many symbols would you like? "))  
numOfNumber = int(input("How many numbers would you like? "))  
  
password = []  
  
for i in range(0,numOfCharacter):  
    password.append(random.choice(sletters))  
for i in range(0,numOfSymbol):  
    password.append(random.choice(symbols))  
for i in range(0,numOfNumber):  
    password.append(random.choice(numbers))  
  
  
print(password)  
random.shuffle(password)  
print(password)  
  
passw = ""  
for p in password:  
    passw += p  
  
print(passw)
