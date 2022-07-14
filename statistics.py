# This is for calculating winning prob. for 1 game
numbers = [str(x) for x in range(2,11)] + [c for c in "JQKA"]

starter = 'y' in input("ARE YOU STARTING (Y/N)\t").lower()
up_number = input("What is the card that is up?\t").upper()
while not up_number in numbers:
    up_number = input("Try again {} is not in the available list, choose from \n{}\n".format(up_number,numbers)).upper()
player_number = input("What is your card?\t").upper()
while not player_number in numbers:
    player_number = input("Try again {} is not in the available list, choose from \n{}\n".format(player_number,numbers)).upper()
dominant_suit = 'y' in input("Is your card's suit dominant?(Y/N)\t").lower()
print("Starter: {}\nUp card's number: {}\nYour card: {}\nDominant SUIT: {}\n".format(starter,up_number,player_number,dominant_suit))

num_cards = 52 - 2
def calc_prob(player_cnt, total_cards,worse_cards):
    prob = 1.0
    for i in range(player_cnt):
        prob *= worse_cards/total_cards
        worse_cards-=1
        total_cards-=1
    return prob
worse_cards = 0
if starter:
    worse_cards +=26 #adding the two other suits
    if dominant_suit:
        worse_cards+=13
        for x in numbers:
            if x ==player_number:
                break
            if x == up_number:
                continue
            worse_cards +=1
    else:
        for x in numbers:
            if x ==player_number:
                break
            worse_cards +=1
if dominant_suit and not starter:
    worse_cards +=39
    for x in numbers:
        if x ==player_number:
            break
        if x ==up_number:
            continue
        worse_cards+=1
def calc_prob_not_dominant_not_starter(player_cnt,player_num,total_cards):
    worse = 0
    for x in numbers:
        if player_num == x:
            break
        worse +=1
    prob = worse / total_cards
    worse -=1
    total_cards -=1
    worse +=26
    if player_cnt==2:
        return prob
    for i in range(player_cnt - 2):
        prob *= worse/total_cards
        worse-=1
        total_cards-=1
    return prob
if dominant_suit or starter:
    for i in range(2,7):
        print("For {} player game {}% wining probability".format(i,100*calc_prob(i,num_cards,worse_cards)))
else:
    for i in range(2,7):
        print("For {} player game {}% winning probability".format(i,100*calc_prob_not_dominant_not_starter(i,player_number,num_cards)))
      