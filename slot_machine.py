import random


MAX_LINES = 3 # all caps means const value
MAX_BET = 100
MIN_BET = 1

ROWS = 3 # number of faces on each reel
COLS = 3 # number of reels

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        # this is a for-else statement. If the for loop runs to completion without breaking, the else statement is then triggered
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break # if the next symbol doesnt match the previous, break out of the if statement
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line +1)
        
    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items(): # .items gives you the key and the value associated with the dictionary, rather than looping through the dictionary
        for _ in range(symbol_count): # _ is an anon variable and is not kept in memory
            all_symbols.append(symbol)

    columns = [] # this well be a nested list -- we're storing the columns not the rows
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:] # ':' is a slice operator and makes a copy
        for _ in range(rows):
            value = random.choice(current_symbols) # once a symbol is selected, we need to remove it from the list, which is why column is a copy of all_symbols
            current_symbols.remove(value) # removes the first instance of the chosen value, such that it can#t be chosen again
            column.append(value) # add thr chosen valeu to our column

        columns.append(column)

    return columns

def print_slot_machine(columns):
    '''
    We have 
    [A, B, C]
    [A, A, A]
    etc
    But these are our columns, not our rows, so we need to transpose these
    '''
    for row in range(len(columns[0])):
        for i, column in enumerate(columns): # loopinig through all the items in columns
            if i != len(columns) -1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        
        print() #brings us to the next line


def deposit():
    while True: # we're waiting until the user enters a valid amount
        amount = input("What would you like to deposit? £")
        if amount.isdigit(): # check this is a valid positive number
            amount = int(amount) # converts into a number from the input string
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a whole number")
    
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit(): # check this is a valid positive number
            lines = int(lines) # converts into a number from the input string
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a whole number")
    
    return lines

def get_bet():
    while True: 
        amount = input("What would you like to bet on each line? £")
        if amount.isdigit(): 
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between £{MIN_BET} - £{MAX_BET}")
        else:
            print("Please enter a whole number")
    
    return amount

def spin(balance):
    lines = get_number_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You don't have enough to bet that amount. Your current balance is: £{balance}")
        else:
            break
        
    print(f"You are betting £{bet} on {lines} lines. Total bet is equal to £{total_bet}")
    print("Balance is: £" + str(balance), "and the number of lines is:", lines)

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won £{winnings}.")
    print(f"You won on lines:", *winning_lines) # * is the splat operator and returns every line of an array
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is £{balance}")
        answer = input("Press enter to play (q to quit).").lower()
        if answer == "q":
            break
        balance += spin(balance)
    
    print(f"You left with £{balance}")

main()

