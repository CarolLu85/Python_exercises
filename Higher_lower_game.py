import random
from art_higher_lower import logo
from data_higher_lower import data
from art_higher_lower import vs
# print(len(data))
# print(data[0]["name"])
# a = fetch_data()
# print(f"Compare A: {a}")
index_a = 0
index_b = 0
player_a = "A"
player_b = "B"
score = 0
def fetch_data():
    number = 0
    number = random.randint(0,len(data)-1)
    return number
    # return f"{data[index]['name']}, {data[index]['description']}, from {data[index]['country']}"
    
def comparison():
    if data[index_a]["follower_count"] > data[index_b]["follower_count"]:
        return "A"
    elif data[index_a]["follower_count"] > data[index_b]["follower_count"]:
        return "B"

def check_answer():
    global player_a
    global player_b
    global index_a
    global index_b 
    right_answer = comparison()
    points = 0
    while True:
        guess = input("Who gets more followers? A or B\n").lower()
        if guess == right_answer:
            points = points + 1
            print(f"You're right! Current score: {points}")
            player_a = player_b
            play_b =""
            index_b = 0
        else:
            print(f"Sorry, you lose. Your final score is {points}")
            return


def play_game():
    global player_a
    global player_b
    global index_a
    global index_b 
    print(logo)
    index_a = fetch_data()
    player_a = "Compare A: " + f"{data[index_a]['name']}, {data[index_a]['description']}, from {data[index_a]['country']}"
    print(player_a)
    print(vs)
    index_b = fetch_data()
    player_b = "Compare B: " + f"{data[index_b]['name']}, {data[index_b]['description']}, from {data[index_b]['country']}"
    print(player_b)
    score = check_answer()

