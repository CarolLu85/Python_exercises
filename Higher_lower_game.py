import random
from art_higher_lower import logo
from data_higher_lower import data
from art_higher_lower import vs
import os
index_a = 0
index_b = 0
player_a = "A"
player_b = "B"
points = 0
def clear_console():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
      
def fetch_data():
    number = 0
    number = random.randint(0,len(data)-1)
    return number
    
def comparison(a,b):
    count_a = data[a]["follower_count"]
    count_b = data[b]["follower_count"]
    if count_a > count_b:
        return "A"
    elif count_a < count_b:
        return "B"

index_a = fetch_data()
while True:
    clear_console()
    print(logo)
    player_a = "Compare A: " + f"{data[index_a]['name']}, {data[index_a]['description']}, from {data[index_a]['country']}"
    print(player_a)
    print(data[index_a]["follower_count"])    
    print(vs)
    index_b = fetch_data()
    player_b = "Compare B: " + f"{data[index_b]['name']}, {data[index_b]['description']}, from {data[index_b]['country']}"
    print(player_b)
    print(data[index_b]["follower_count"])

    right_answer = comparison(index_a,index_b)
    print(right_answer)
    guess = input("Who gets more followers? A or B\n")
    if guess == right_answer:
        points = points + 1
        print(f"You're right! Current score: {points}")
        index_a = index_b
    else:
        print(f"Sorry, you lose. Your final score is {points}")
        end_of_game = True
        break



