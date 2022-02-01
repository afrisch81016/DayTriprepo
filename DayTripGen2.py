import random

planning_phase = 0

destinations = ["Los Angeles","Orlando","Wisconsin Dells","Las Vegas","New York"]
transportation = ["train","plane","rental car","motorcycle","bicycle"]
entertainment = ["Disney World","Disney Land","Kalahari Resort","M.G.M. Grand","Statue of Liberty"]
restaurants = ["Famous Daves","Belle's Castle","Mickey's Pub","Alinia","Gordon Ramsey's Palace"]

destination_pick = (None)
transportation_pick = (None)
entertainment_pick = (None)
restaurant_pick = (None)

def get_trip_choices(generated_list):
    trip_choice = random.choice(generated_list)
    return trip_choice

def interact_with_user(phase):
    match phase:
        case 0:
            print(f"Hello, and thank you for choosing Random Day Trip simulator! We have many options to choose from. Would you like to get started? For input, please select y for yes and n for no")
            user_makes_choice(input(),phase)
        case 1:
            destination_pick=get_trip_choices(destinations)
            print(f"Your random destination is {destination_pick}, do you like this destination choice?")
            user_makes_choice(input(),phase)
        case 2:
            transportation_pick=get_trip_choices(transportation)
            print(f"Your random transportation is {transportation_pick}, would you like this transportation choice?")
            user_makes_choice(input(),phase)
        case 3:
            entertainment_pick=get_trip_choices(entertainment)
            print(f"So lets get to something fun to do. Your random entertainment would be {entertainment_pick}. Would you like this choice?")
            user_makes_choice(input(),phase)
        case 4:
            restaurant_pick=get_trip_choices(restaurants)
            print(f"Ok, it's time for the best part, FOOD! your random restaurant choice is {restaurant_pick}. How does that sound?")
            user_makes_choice(input(),phase)
             
            
            
def user_makes_choice(choice, phase):
    match phase:
        case 0:
            match choice:
                case 'y':
                    planning_phase=1
                case 'n':
                    planning_phase=99 #end of interactions
        case 1:
            match choice:
                case 'y':
                    planning_phase=2
                case 'n':
                    planning_phase=1 
        case 2:
            match choice:
                case 'y':
                    planning_phase=3
                case 'n':
                    planning_phase=2
        case 3:
            match choice:
                case 'y':
                    planning_phase=4
                case 'n':
                    planning_phase=3
        case 4:
            match choice:
                case 'y':
                    planning_phase=5
                case 'n':
                    planning_phase=4
                    
    interact_with_user(planning_phase)


interact_with_user(planning_phase)



