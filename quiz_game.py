print("Welcome to the counties quiz!")

playing = input("Do you want to play? ")
score = 0

if playing.lower() != "yes":
    quit()

print("Okay, let's play :)")

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

print("Well done! You got" + str(score) + "questions correct.")
print("You scored " + str((score/3)*100) + "%")