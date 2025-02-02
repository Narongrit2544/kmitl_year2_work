import random
import time
from os import system, name


def clear():
    """This function will be used to clear the screen"""
    if name == 'nt':  # Windows
        system('cls')
    else:  # Unix/Linux/macOS
        system('clear')

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

class Cash:
    def __init__(self, credit=200, bet=2):
        self.credit = credit
        self.bet = bet
        self.bets = [2, 5, 10, 20]
        self.bet_stack = Stack()

    def change_bet(self):
        self.bets.append(self.bets.pop(0))
        self.bet = self.bets[0]
        self.bet_stack.push(self.bet)

    def undo_bet(self):
        last_bet = self.bet_stack.pop()
        if last_bet is not None:
            self.bet = last_bet

    def charge(self):
        if self.bet <= self.credit:
            self.credit -= self.bet
            return False
        else:
            print('\n\t     Not enough credit to place a bet press "a" to add money!')
            time.sleep(2)
            return True

class SlotMachine:
    def __init__(self, slot_one, slot_two, slot_three):
        self.reels = [slot_one, slot_two, slot_three]
        self.loss_count = 0  # Add a counter for losses

    def spin(self):
        if  self.loss_count >= random.randint(3,10):
            # If there have been 3 in 10 losses, force a win by choosing the same symbol for all reels
            symbol = random.choices(self.reels[0], k=1)[0]
            return [symbol, symbol, symbol]
        else:
            # Otherwise, spin normally
            return [random.choices(reel, k=1)[0] for reel in self.reels]

    def play(self, cash):
        clear()
        result = self.spin()
        print("Result: ", [res[0] for res in result])
        if len(set([res[0] for res in result])) == 1:
            symbol = result[0][0]
            multiplier = result[0][1]
            win_amount = cash.bet * multiplier  # Calculate win amount based on bet and multiplier
            print(f"Congratulations! You won ${win_amount}!")
            cash.credit += win_amount
            self.loss_count = 0  # Reset the loss counter after a win
        else:
            print("Sorry, you lost. Try again!")
            self.loss_count += 1  # Increment the loss counter after a loss



            
# Define the symbols and multipliers
strawberry = ("🍓", 2)
banana = ("🍌", 10)
plum = ("🍑", 3)
raspberry = ("🍇", 5)
orange = ("🍊", 8)
seven = ("💎", 15)

# Define the probabilities for each symbol
probabilities = [10, 6, 5, 3, 2, 1]
symbols = [strawberry, plum, raspberry, orange, banana, seven]
slot_one = random.choices(symbols, weights=probabilities, k=100)

probabilities = [10, 6, 5, 3, 2, 1]
symbols = [strawberry, plum, raspberry, orange, banana, seven]
slot_two = random.choices(symbols, weights=probabilities, k=100)

probabilities = [10, 6, 5, 3, 2, 1]
symbols = [strawberry, plum, raspberry, orange, banana, seven]
slot_three = random.choices(symbols, weights=probabilities, k=100)

# Create a slot machine and cash with these symbols
slot_machine = SlotMachine(slot_one, slot_two, slot_three)
cash = Cash()

def welcome():
    welcome = ['\n\n\t #######    #######    #######',
               '\t########   ########   ########',
               '\t     ##         ##         ##',
               '\t    ##         ##         ##',
               '\t   ##         ##         ##',
               '\t  ##         ##         ##',
               '\t  ##         ##         ##',
               '\n\n'
               '\t##### ##    ####### ###### ',
               '\t##    ##    ##   ##   ##   ',
               '\t##### ##    ##   ##   ##   ',
               '\t   ## ##    ##   ##   ##   ',
               '\t##### ##### #######   ##   ']
    
    for c in welcome:
        print(c)
        time.sleep(0.1)
    time.sleep(1)
    clear()

# Play the game
if __name__ == '__main__':
    clear()
    welcome()
    
    while True:
        print(f"\nCurrent Bet: {cash.bet}, Current Credit: {cash.credit}")
        again = input("\nPress 'q' to quit or 'b' to change bet or 'a' to add money or any other key to spin: ")
        if again == 'q':
            break
        elif again == 'b':
            cash.change_bet()
        elif again == 'a':
            amount = int(input("Enter the amount of money you want to add: "))
            cash.credit += amount
            print(f"You added ${amount}. Your new credit is ${cash.credit}.")
        else:
            if not cash.charge():
                slot_machine.play(cash)
                
    time.sleep(1)
    clear()
