import questions as qs
import random

# print(qs.list_of_questions[3])
# TODO first we need a way to randomly pic two questions from list.

def pick_random_question():
    question = random.choice(qs.list_of_questions)

    return question


def the_highest_in_both(q1,q2):
    best_answer = max(q1["answer"],q2["answer"])
    return best_answer

did_user_lost = False
number_of_guess = 0
q1 = pick_random_question()
print("Welcome to Higher and Lower game.Just select Aor B for highest you think")
while not did_user_lost:
    
    q2 = pick_random_question()

    if(q1 == q2):
        q2 = pick_random_question()
    print("Question 1: ")
    print(q1["question"])
    print("Question 2")
    print(q2["question"])
    
    a = q1["answer"]
    b = q2["answer"]
    best = the_highest_in_both(q1,q2)
    guess = input("Select your answer. A or B ? ").upper()

    if guess == "A" and a == best:
        print("Wow, you guessed it right.")
        number_of_guess += 1
        print("\n"*20)
        print("Your score is: ", number_of_guess)
        q1 = q2
    elif guess == "B" and b == best:
        print("Wow, you guessed it right.")
        number_of_guess += 1
        print("\n"*20)
        print("Your score is: ", number_of_guess)
        q1 = q2
    else:
        print("Ah, shit You gussed it wrong.")
        print("Your total score is, " ,number_of_guess)
        did_user_lost = True


    # print("")
    # print(the_highest_in_both(q1,q2))


