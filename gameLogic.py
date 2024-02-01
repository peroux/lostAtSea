import random
import os
import platform

playerScore = 0
playerRankings = []
remainingItems = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
costGuardRankings = [
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

def clearScreen():
    # Check if the operating system is Windows
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def runGame():
    clearScreen()
    print("Welcome to the Cost Guard Game!")
    print("You are stranded in the middle of the Atlantic Ocean after a shipwreck.")
    print("You are in a lifeboat with 11 other people.")
    print("You have a limited amount of supplies and must rank them in order of importance.")
    print("You will be scored based on how close your ranking is to the official coast guard ranking.")
    print("The lower your score, the better.")
    print("Good luck!")
    input("Press enter to continue...")
    rankItems()
    

def listObjectRanks():
    clearScreen()
    for item in costGuardRankings:
        print("Ranking: " + str(item[0]) + "\nItem: " + item[1] + "\nReasoning: " + item[2])
        print("----------------------------------------")

def scoreUserRankings():
    for item in playerRankings:
        playerScore += abs(int(item)-costGuardRankings[playerRankings.index(item)][0])
    print("Your score is: " + str(playerScore))

def displayCurrentItems():
    print("Remaining Items: ")
    random.shuffle(remainingItems)  # Shuffle the list of remaining items
    for item in remainingItems:
        print(costGuardRankings[item-1][1])

def rankItems():
    clearScreen()
    print("--Select the item you would like to rank--")
    displayCurrentItems()
    item = input()
    if item in costGuardRankings[][1]:
        clearScreen()
        print("You have selected: " + item)
        print("Please enter the ranking you would like to assign to this item.")
        print("1 is the highest ranking, 15 is the lowest.")
        ranking = input()
        if ranking in range(1,16) and ranking not in playerRankings:
            playerRankings.append(ranking)
        else:
            print("Invalid ranking. Please enter a number between 1 and 15.")
            rankItems()
    else:
        print("Invalid item. Please select an item from the list.")
        clearScreen()
        rankItems()
    playerRankings.append(input("Rank " + str(i+1) + ": "))

runGame()