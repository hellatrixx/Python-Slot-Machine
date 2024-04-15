import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3

symbol_freq = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_values = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def calc_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_check = column[line]
            if symbol != symbol_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    
    return winnings, winning_lines



def get_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_freq in symbols.items():
        for _ in range(symbol_freq):
            all_symbols.append(symbol)

    columns = []
    current_symbols = all_symbols[:]
    for _ in range(cols):
        column = []
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)
    
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else: 
                print(column[row], end="")
        
        print()


def deposit():
    while True:
        amount = input("Enter the amount you wish to deposit: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                print(f"Deposited {amount}.")
                break
            else:
                print("Invalid number.")
        else:
            print("Invalid input. Please enter a valid number.")
    return amount

def number_of_lines():
    while True:
        lines = input(f"Enter the number of lines you want to bet on (1 - {MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= 3:
                print(f"You have chosen to bet on {lines} lines.")
                break
            else:
                print("Please enter a valid number.")
        else:
            print("Please enter a number.")
    return lines

def get_bet():
    while True:
        bet = input(f"Enter the amount you wish to bet (Max: {MAX_BET}, Min: {MIN_BET}): ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                print(f"You have chosen to bet {bet}.")
                break
            else:
                print("Invalid bet.")
        else:
            print("Please enter a number.")
    return bet

def game():
    lines = number_of_lines()
    bet = get_bet()
    bet_per_line = bet / lines
    print(f"You are betting {bet} on {lines} lines.\n" f"Bet per line: {bet_per_line}.")
    slots = get_spin(ROWS, COLS, symbol_freq)
    print_slot_machine(slots)
    winnings, winning_lines = calc_winnings(slots, lines, bet, symbol_values)
    print(f"You won {winnings}.")
    print("You won on lines:", *winning_lines)
    return winnings - bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is {balance}")
        spin = input("Press enter to play. (q to quit).")
        if spin == "q":
            break
        balance += game()

    print(f"You left with {balance}")


main()

    