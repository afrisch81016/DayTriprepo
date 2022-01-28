
import random




# random.choice (destinations)

def get_random(my_list):
    random_choice = random.choice(my_list)
    return random_choice


def run_day_trip():
    destinations =["venice","greece","paris","tokyo","hawaii","new york"]
    restaurants = ["olive garden","sushi gardens","omlette du fromage","grass skirts cafe","alinia"]
    transpotation = ["plane","car","train","bus","bike","motorcycle","boat"]
    entertainment = ["broadway","canals","musicals","gambling","museum","aquarium","hiking"]
    user_is_happy = False
    dest = get_random(destinations)
    rest = get_random(restaurants)
    trans = get_random(transpotation)
    ente = get_random(entertainment)
    while user_is_happy == False:
        print(f"your random destination is {dest}, the restaurant is {rest}, the way you would get their is {trans}, and the fun activity would be {ente}")
        are_you_happy = input("Are you happy with your random trip selection? Press 1 to change destination. Press 2 to change restaurants. Press 3 to change transportation. Press 4 to change entertainment. Otherwise, enter 5 to confirm your choices")
        if are_you_happy == '1':
            user_is_happy = False
            dest = get_random(destinations)
        elif are_you_happy == "2":
            user_is_happy = False
            rest = get_random(restaurants)
        elif are_you_happy == "3":
            user_is_happy = False
            trans = get_random(transpotation)
        elif are_you_happy == "4":
            user_is_happy = False
            ente = get_random(entertainment)
        elif are_you_happy == "5":
            user_is_happy = True
            print(f"your random destination is {dest}, the restaurant is {rest}, the way you would get their is {trans}, and the fun activity would be {ente}")
            confirm = input("would you like to confirm your trip?")
            if confirm == "yes":           
                print("I hope you have a great time on your random trip selection!")
            else:
                user_is_happy = False

run_day_trip()