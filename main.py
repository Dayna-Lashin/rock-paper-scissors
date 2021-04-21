import random

  def play():
    #user_score = 0
    #computer_score = 0

    user = input("\nPick 'r' for rock, 'p' for paper, or s for scissors: ").lower()
    print(f"\nYour choice: {user}")
    computer = random.choice(['r', 'p', 's'])
    print(f"Computer choice: {computer}\n")

    def user_wins():
      print("You win!\n")
      #print(f"\nYour Score: {user_score} \nComputer: {computer_score}\n")

    def computer_wins():
      print("Computer wins!\n")
      #print(f"\nYour Score: {user_score} \nComputer: {computer_score}\n")

    def draw():
      print("It's a tie\n")

    if (user == 'r' and computer == 's') or (user == 'p' and computer == 'r') \
      or (user == 's' and computer == 'p'):
      user_wins()

    if (user == 'r' and computer == 'p') or (user == 'p' and computer == 's')  \
      or (user == 's' and computer == 'r'):
      computer_wins()

    elif user == computer:
      draw()

  play()

  ## need to make it loop and keep score


