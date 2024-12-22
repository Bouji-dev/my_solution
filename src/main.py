import random

class RockPaperScissors:
    def __init__(self, name):
        self.choices = ['rock', 'paper', 'scissors']
        self.player_name = name


    def get_player_choice(self):
        user_choice = input(f"Enter your choice {self.choices} :")
        if user_choice.lower() in self.choices:
            return user_choice.lower()

        print(f"Invalid choice. you must select from {self.choices}.")    
        return self.get_player_choice()
    
    def get_computer_choice(self):
        return random.choice(self.choices)

    def decide_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a Tie!"
        win_combinations = [('rock, scissors'), ('paper', 'rock'), ('scissors', 'paper')]
        for win_comb in win_combinations:
            if (user_choice == win_comb[0]) & (computer_choice == win_comb[1]):
                return "Congeratulations! You won!"
            
        return "Oh no! The computer won!"
        
    def play(self):
        user_choice = self.get_player_choice()
        computer_choice = self.get_computer_choice()    
        winner_msg = self.decide_winner(user_choice, computer_choice)
        print(f"computer choice is {computer_choice}")
        print(winner_msg)


if __name__ == '__main__':
    game = RockPaperScissors('Ehsan')

    
while True:
    game.play()

    continue_game = input('Do you want to play again? (Enter any to play again or Enter q/Q to exit.)')    
    if continue_game.lower() == 'q':
        break