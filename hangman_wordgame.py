import random  
word_list = ["apple", "banana", "cherry" , "coach", "furniture", "iphone", "mouse"]  
  
# all variables declared here  
  
choose_random_word = random.choice(word_list)  
end_game = False  
  
placeholder = ""  
wordLength = len(choose_random_word)  
array_of_contain_words = []  
for char in range(wordLength):  
    placeholder += "_"  
  
print(choose_random_word)  
print(placeholder)  
  
lives = 6  
  
while not end_game:  
  
    guess = input("Enter your guess: ")  
    display = ""  
    for char in choose_random_word:  
        if char == guess:  
            display += char  
            array_of_contain_words.append(char)  
        elif char in array_of_contain_words:  
            display += char  
        else:  
            display += "_"  
  
    print(display)  
  
    if guess not in choose_random_word:  
        lives -= 1  
        if lives == 0:  
            end_game = True  
            print("You Lose!")  
  
    print(lives)  
    if "_" not in display:  
        end_game = True
