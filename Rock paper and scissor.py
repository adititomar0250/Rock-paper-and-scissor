import random
choices=["rock","paper","scissors"]

user_choice=input("Enter rock,paper or scissors: ")
computer=random.choice(choices)

print("Computer:",computer)

if user_choice==computer:
    print("Its a tie!")
elif user_choice=="rock" and computer=="scissors":
    print("You win")
elif user_choice=="paper" and computer=="rock":
    print("You win")
elif user_choice=="scissors" and computer=="paper":
    print("You win")

elif computer=="rock" and user_choice=="scissors":
    print("Computer wins")
elif computer=="paper" and user_choice=="rock":
    print("Computer wins")
elif computer=="scissors" and user_choice=="paper":
    print("Computer wins")

print("----Game Over----")



