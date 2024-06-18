#importing data and logos
import random
from art import logo
from art import vs
from game_data import data

def format_data(account):
    account_name= account["name"]
    account_descr= account["description"]
    account_country= account["country"]
    return f"{account_name}, a {account_descr} , from {account_country}"
#defining a and b

#choosing random items


def check_answer(guess, a_followers,b_followers):
    if a_followers>b_followers:
        return guess=="a"
    else:
        return guess=="b"

game_should_continue= True
print(logo)
score=0 
account_b=random.choice(data)
while game_should_continue:

    account_a= account_b
    account_b= random.choice(data)
   
    if account_a==account_b:
        account_b=random.choice(data)

    print(f"compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")


    a_follower_count= account_a["follower_count"]
    b_follower_count= account_b["follower_count"]

    

  
    guess= input("who has more followers? type 'A' or 'B' :").lower()
    is_correct= check_answer(guess, a_follower_count, b_follower_count)
   
    if is_correct:
        score+= 1
        print(f"You're right! Current score : {score}")
    else:
        game_should_continue= False
        print(f"Sorry , that is wrong. your final score : {score}")    