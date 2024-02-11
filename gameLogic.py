import random
import os
import platform

player_score = 0
player_rankings = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
remaining_items = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
cost_guard_rankings = [
    [1, "Shaving mirror", "Of all the items, the mirror is absolutely critical. It is the most powerful tool you have for communicating your presence. In sunlight, a simple mirror can generate five to seven million candlepower of light. The reflected sunbeam can even be seen beyond the horizon."],
    [2, "A 10-liter can of oil/gasoline mixture", "The second most critical item for signaling. The mixture will float on water and can be ignited using the matches."],
    [3, "A 25-liter container of water", "Vital to restore fluids lost through perspiration. 25 liters will supply water rations for your group for several days."],
    [4, "A case of army rations", "This is your basic food intake"],
    [5, "20 square feet of Opaque plastic sheeting", "Can be used to collect rainwater and shelter from the wind and waves."],
    [6, "2 boxes of chocolate bars", "Your reserve food supply"],
    [7, "An ocean fishing kit with pole.", "Ranked lower than the chocolate as there is no guarantee you will catch any fish. The pole might be used as a tent pole."],
    [8, "15ft nylon rope", "Could be used to lash people or equipment together to prevent being washed overboard. There are a variety of other uses, but none high on the list for survival."],
    [9, "A floating seat cushion", "Useful as a life preserver if someone fell overboard."],
    [10, "A can of shark repellent", "To repel sharks, of course!"],
    [11, "One bottle of 160% proof rum", "Contains 80 percent alcohol, which means it can be used as an antiseptic for any injuries, otherwise of little value. Very dangerous if drunk, as it would cause the body to dehydrate, the opposite of what you need to survive."],
    [12, "A small transistor radio", "You would be out of range of any radio station."],
    [13, "Maps of the Atlantic Ocean", "Worthless without navigation equipment."],
    [14, "A quantity of mosquito netting", "There are NO mosquitoes in the middle of the Atlantic Ocean and the netting is useless for anything else."],
    [15, "A sextant", "Useless without the relevant tables and a chronometer."]
    ]

def clear_screen():
    # Check if the operating system is Windows
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def run_game():
    clear_screen()
    print("Welcome to the Cost Guard Game!")
    print("You are stranded in the middle of the Atlantic Ocean after a shipwreck.")
    print("You are in a lifeboat with 11 other people.")
    print("You have a limited amount of supplies and must rank them in order of importance.")
    print("You will be scored based on how close your ranking is to the official coast guard ranking.")
    print("The lower your score, the better.")
    print("Good luck!")
    input("Press enter to continue...")
    while "0" not in player_rankings:
        rank_items(cost_guard_rankings, player_rankings)
    #score_user_rankings()

    

def list_object_ranks():
    clear_screen()
    for item in cost_guard_rankings:
        print("Ranking: " + str(item[0]) + "\nItem: " + item[1] + "\nReasoning: " + item[2])
        print("----------------------------------------")

def score_user_rankings():
    global player_score
    for item in player_rankings:
        player_score += abs(int(item)-cost_guard_rankings[player_rankings.index(item)][0])
    print("Your score is: " + str(player_score))

def display_current_items():
    print("Remaining Items: ")
    random.shuffle(remaining_items)  # Shuffle the list of remaining items
    for item in remaining_items:
        print(cost_guard_rankings[item-1][1])

def rank_items(cost_guard_rankings, player_rankings):
    clear_screen()
    print("--Select the item you would like to rank--")
    display_current_items()
    item_input = input("Please enter the name of the item: ")  # Capture user input for item name

    # Check if the entered item name matches any items in the cost_guard_rankings
    item_found = False
    item_index = 0
    for ranking_item in cost_guard_rankings:
        if item_input.lower() == ranking_item[1].lower():  # Case-insensitive comparison
            item_found = True
            break
        item_index += 1

    if item_found:
        clear_screen()
        print("You have selected: " + item_input)
        print("Please enter the ranking you would like to assign to this item.")
        print("1 is the highest ranking, 15 is the lowest.")
        try:
            ranking = int(input())
            if ranking in range(1, 16) and ranking not in player_rankings:
                player_rankings[item_index] = ranking
            else:
                print("Invalid ranking. Please enter a number between 1 and 15.")
                return rank_items(cost_guard_rankings, player_rankings)
        except ValueError:
            print("Please enter a valid number for the ranking.")
            return rank_items(cost_guard_rankings, player_rankings)
    else:
        print("Invalid item. Please select an item from the list.")
        return rank_items(cost_guard_rankings, player_rankings)

    return player_rankings
run_game()