import random
user_action=input("enter a choice(rock,paper scissor):")
possible_actions=("rock","paper","scissor")
computer_action=random.choice(possible_actions)
print("you chose(user_action),computer chose(computer_action)")

if user_action==computer_action:
    print("draw")
elif user_action=="rock":
    if computer_action=="scissor":
        print("rock smashes scissors! you win!")
    else:
        print("paper covers rock! you lose.")
elif user_action=="paper":
    if computer_action=="rock":
        print("paper covers rock! you win!")
    else:
        print("scissors cuts paper! you lose.")
elif user_action=="scissors":
    if computer_action=="paper":
        print("scissors cuts paper! you win!")
    else:
        print("rock smashes scissors! you lose.")