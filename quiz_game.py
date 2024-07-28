# welcome message
print("Welcome to the counties quiz!") 

# ask if user wannts to play, if so, we initialise the score
playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay, let's play :)")
score = 0

# we now ask quiz questions, if the answer if correct, we increment the score
answer = input("Which county has a white horse on its flag? ") 
if answer.lower() == "kent":
    print('Correct.')
    score+=1
else:
    print("Good try.")

answer = input("Which county borders Wales and is home to Ludlow Castle? ") 
if answer.lower() == "shropshire":
    print('Correct.')
    score+=1
else:
    print("Good try.")

answer = input("What is the largest county is Wales? ") 
if answer.lower() == "powys":
    print('Correct.')
    score+=1
else:
    print("Good try.")

# at the end of the quiz, we give the final score as number of questions correct and a % calculation
print("Well done! You got" + str(score) + "questions correct.")
print("You scored " + str((score/3)*100) + "%")