import random

random.seed(1234)

ROCK = 1
PAPER = 2
SCISSORS = 3

HASH_LINE = "#" * 25

ROCK_ART = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

PAPER_ART = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

SCISSORS_ART = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


def choice_to_name(choice: int) -> str:
    if choice == ROCK:
        return "rock"
    elif choice == PAPER:
        return "paper"
    elif choice == SCISSORS:
        return "scissors"
    else:
        return "unknown"


def choice_to_art(choice: int) -> str:
    if choice == ROCK:
        return ROCK_ART
    elif choice == PAPER:
        return PAPER_ART
    elif choice == SCISSORS:
        return SCISSORS_ART
    else:
        return ""


def print_menu():
    print("Options:")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")
    print("0 - Quit game")


def decide_result(player_choice: int, bot_choice: int, player_name: str, bot_name: str) -> str:
    player_name_txt = player_name
    bot_name_txt = bot_name

    if player_choice == bot_choice:
        # draw
        return f"Draw! Both players chose {choice_to_name(player_choice)}."

    # player wins cases
    if (
        (player_choice == ROCK and bot_choice == SCISSORS) or
        (player_choice == PAPER and bot_choice == ROCK) or
        (player_choice == SCISSORS and bot_choice == PAPER)
    ):
        # form reason text
        if player_choice == ROCK and bot_choice == SCISSORS:
            reason = "rock beats scissors"
        elif player_choice == PAPER and bot_choice == ROCK:
            reason = "paper beats rock"
        else:
            reason = "scissors beat paper"
        return f"{player_name_txt} {reason}."

    # bot wins cases
    if bot_choice == ROCK and player_choice == SCISSORS:
        reason = "rock beats scissors"
    elif bot_choice == PAPER and player_choice == ROCK:
        reason = "paper beats rock"
    else:
        reason = "scissors beat paper"
    return f"{bot_name_txt} {reason}."


def main():
    print("Program starting.")
    print("Welcome to the rock-paper-scissors game!")
    player_name = input("Insert player name: ")
    print(f"Welcome {player_name}!")
    bot_name = "RPS-3PO"
    print(f"Your opponent is {bot_name}.")
    print("Game starts...\n")

    player_wins = 0
    player_losses = 0
    player_draws = 0

    while True:
        print_menu()
        choice_str = input("Your choice: ")

        if choice_str == "0":
            break

        if choice_str not in ("1", "2", "3"):
            # invalid, show menu again
            continue

        player_choice = int(choice_str)
        bot_choice = random.randint(1, 3)

        print("Rock! Paper! Scissors! Shoot!\n")

        print(HASH_LINE)
        print(f"{player_name} chose {choice_to_name(player_choice)}.")
        print(choice_to_art(player_choice))
        print(HASH_LINE)
        print(f"{bot_name} chose {choice_to_name(bot_choice)}.")
        print(choice_to_art(bot_choice))
        print(HASH_LINE)
        print()

        result_text = decide_result(player_choice, bot_choice, player_name, bot_name)
        print(result_text)
        print()

        # update counters
        if "Draw!" in result_text:
            player_draws += 1
        elif result_text.startswith(player_name):
            player_wins += 1
        else:
            player_losses += 1

    print()
    print("Results:")
    print(f"{player_name} - wins ({player_wins}), losses ({player_losses}), draws ({player_draws})")
    print(f"{bot_name} - wins ({player_losses}), losses ({player_wins}), draws ({player_draws})")
    print()
    print("Program ending.")


if __name__ == "__main__":
    main()
