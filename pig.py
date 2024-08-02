import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True:
    players = input("Enter the number of players (2-4): ")
    # error hanndling for user input
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players")
    else:
        print("Invalid, try again")

# this is changable
max_score = 50
players_scores = [0 for i in range(players)]

# this while loop runs until a player reaches or surpasses the max score set above
# note that the for loop within means that once this is achieved, the outstanding players still get to complete their turns (otherwise this is
# unfair to the players going second, third, etc
while max(players_scores) < max_score:

    for player_index in range(players):
        print("\nPlayer", player_index + 1, "'s turn has just started. Player", player_index + 1, "has", players_scores[player_index], "in the bank\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll? (y) ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Your turn ends.")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:", value)
            
            print("You have:", current_score, "unbanked.")

        players_scores[player_index] += current_score
        print("Your total score is:", players_scores[player_index])

# when the while loop ends, we have at least one player reaching the score limit
max_score = max(players_scores)
winning_index = players_scores.index(max_score)
print("Player number", winning_index +1, "in the winner with the score of", max_score)