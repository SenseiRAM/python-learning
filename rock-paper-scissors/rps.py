import random
import time
import sys
import logbook

app_log = logbook.Logger('App')

class Roll:
    def __init__(self, name, defeats, defeated_by):
        self.name = name
        self.defeats = defeats
        self.defeated_by = defeated_by

    def can_defeat(self, roll):
        if roll.name == self.defeats:
            return "win"
        elif roll.name == self.name:
            return "tie"


class Player:
    def __init__(self, name):
        self.name = name

def init_logging(filename: str = None):
    level = logbook.TRACE

    if not filename:
        logbook.StreamHandler(sys.stdout, level=level).push_application()
    else:
        logbook.TimedRotatingFileHandler(filename, level=level).push_application()

    msg = 'Logging initialized, level: {}, mode: {}'.format(
        level,
        "stdout mode" if not filename else 'file mode: ' + filename
    )
    logger = logbook.Logger('Startup')
    logger.notice(msg)


def print_header():
    print("-----------------------------")
    print("        Welcome to           ")
    print(" ROCK, PAPER, SCISSORS!!!!!! ")


def build_rolls():
    rock = Roll("Rock", "Scissors", "Paper")
    paper = Roll("Paper", "Rock", "Scissors")
    scissors = Roll("Scissors", "Paper", "Rock")

    return [rock, paper, scissors]


def get_player_name():
    return input("What is your name, player? ")


def get_player_roll(rolls, player):
    roll = None
    while roll not in ["r", "p", "s"]:
        roll = input(f'\nDo you choose [R]ock, [P]aper, or [S]cissors, {player.name}? ').lower()
        print("")
    if roll == "r":
        return rolls[0]
    elif roll == "p":
        return rolls[1]
    else:
        return rolls[2]

def dramatic_wait(secs):

    time.sleep(secs)

def main():
    print_header()

    rolls = build_rolls()
    msg = 'Rolls built'
    app_log.notice(msg)

    name = get_player_name()
    msg = f'Player enters name as {name}'
    app_log.notice(msg)

    player1 = Player(name)
    player2 = Player("Computer")

    game_loop(player1, player2, rolls)


def game_loop(player1, player2, rolls):
    count = 0
    player_score = 0
    cpu_score = 0
    answer = None

    while count < 3:
        p2_roll = random.choice(rolls)
        p1_roll = get_player_roll(rolls, player1)

        outcome = p1_roll.can_defeat(p2_roll)

        print(f"{player1.name} throws {p1_roll.name}!")
        dramatic_wait(1)
        print(f"{player2.name} throws {p2_roll.name}!")
        dramatic_wait(1)
        # display winner for this round

        if outcome == "tie":
            print("It's a tie!")
            dramatic_wait(1)

        elif outcome == "win":
            print(f"{p1_roll.name} beats {p2_roll.name}!")
            dramatic_wait(1)
            print(f"{player1.name} wins!!!")
            dramatic_wait(1)
            player_score += 1

        else:
            print(f"{p2_roll.name} beats {p1_roll.name}!")
            dramatic_wait(1)
            print(f"{player2.name} wins :(")
            dramatic_wait(1)
            cpu_score += 1

        count += 1

    # Compute who won
    if player_score > cpu_score:
        print(f'\nCongratulations, {player1.name}, you have {player_score} points and you win!')
    elif player_score == cpu_score:
        print(f'\n{player1.name} and {player2.name} have the same score, it\'s a tie!')
    else:
        print(f"\nSorry {player1.name}, but {player2.name} has {cpu_score} points and you lose.")

    while answer not in ['y','n']:
        answer = input('Would you like to play again? [y]es or [n]o?').lower()
        if answer == 'y':
            game_loop(player1, player2, rolls)
        elif answer == 'n':
            print("Good game! See you next time!")
            break

if __name__ == "__main__":
    init_logging('rps.log')
    main()
