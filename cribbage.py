import os
from deck import Deck

#create deck and make initial shuffle()
deck = Deck()
deck.shuffle()
#initialize globals
won = 0
lost = 0
cpu_score = 0
player_score = 0

def clear():#clearing the screen for a draw_screen()
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')
        
def game():
    clear()
    print("Welcome to Cribbage by arch-52factorial")
    print("The origional game code is licensed under the GPL v2")
    print("Some code however is and is modified from tutorials from the Raspberry Pi Foundation,")
    print("and the tutorial projects found at https://projects.raspberrypi.org/en/")
    print("Such code is licensed under the Creative Commons Attribution 4.0 International License,")
    print("a copy of which can be found at https://creativecommons.org/licenses/by-sa/4.0/")
    
    exit()
    
if __name__ == "__main__":
    game()
    
