with open("story.txt", "r") as file:
    story = file.read()

words = set()
start_of_word = -1
target_start = "<"
target_end = ">"

for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i
    
    # if we found the ending angle bracket and we found the starting engle bracket, then we can take that entire word
    # and add that to our words list
    if char == target_end and start_of_word != -1:
        word = story[start_of_word: i + 1]
        words.add(word)
        # reset start_of_word for our next word
        start_of_word = -1

answers = {} # an empty dictionary

for word in words:
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])

print(story)