import random


def game(user_choice):
    list1=["stone","paper","scissors"]
    user_count=0
    comp_count=0
    computer_choice=random.choice(list1)
    print("\n Your choice:",user_choice,"\nComputer's choice:",computer_choice)
    if (user_choice == computer_choice):
        print("Both players selected",user_choice,". It's a tie!")
    elif user_choice == "rock":
        if (computer_choice == "scissors"):
            print("Rock smashes scissors! You win!")
            user_count+=1
        else:
            print("Paper covers rock! You lose.")
            comp_count+=1
    elif (user_choice == "paper"):
        if computer_choice == "rock":
            print("Paper covers rock! You win!")
            user_count+=1
        else:
            print("Scissors cuts paper! You lose.")
            comp_count+=1
    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("Scissors cuts paper! You win!")
            user_count+=1
        else:
            print("Rock smashes scissors! You lose.")
            comp_count+=1
    
    return comp_count,user_count
def play(count):
    c_count=0
    u_count=0
    while(count>0):
        user_choice = input("Enter a choice (rock, paper, scissors): ")
        if user_choice=="rock" or user_choice=="paper" or user_choice=="scissors":
            comp_count,user_count=game(user_choice)
            c_count=c_count+comp_count
            u_count=u_count+user_count
        else:
            print("Choose from the available options.\n")
        count=count-1
    return c_count,u_count

class rock_paper_scissors:

    count=int(input("How many times do you want to play:")) 
    comp_count,user_count=play(count)

    if comp_count>user_count:
	    print("COMPUTER WINS!!!\n Comp_Score:",comp_count,"\n Your_Score",user_count)
    elif comp_count==user_count:
        print("IT'S A TIE!!!\n Comp_Score:",comp_count,"\n Your_Score",user_count)
    else:
	    print("YOU WIN!!!\n Comp_Score:",comp_count,"\n Your_Score",user_count)