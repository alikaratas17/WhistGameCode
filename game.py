# WHIST
NUM_PLAYERS = int(input("How Many Players?\t"))
FONT_SIZE = 20
W=700
H=625
turns = []
turns = turns + [1 for i in range(NUM_PLAYERS)]
turns = turns + list(range(2,8))
turns = turns + [8 for i in range(NUM_PLAYERS)]
turns = turns + list(range(7,1,-1))
turns = turns + [1 for i in range(NUM_PLAYERS)]
#print(turns)


players = []
for i in range(NUM_PLAYERS):
    players.append(input("Name of Player #{}:\t".format(i+1)))

import pygame

def draw_grid(screen):
    screen.fill((0,0,0))

pygame.init()
screen = pygame.display.set_mode((W,H))
running = True
background_color = (255,255,255)
#draw_grid()
font = pygame.font.SysFont(None, FONT_SIZE)

txt = "ToBeRendered"
img = font.render(txt, True, (0,0,0))
text_coord_pairs = []
coord = (0,0)
dW = W / (NUM_PLAYERS+2)
number_positions = []
for player in players:
    coord = (coord[0]+dW,coord[1])
    text_coord_pairs.append((font.render(player, True, (0,0,0)),coord))
    number_positions.append(coord[0])
    number_positions.append(coord[0]+dW/2)
dH = H / (len(turns)+1)
coord = (0,0)

for turn in turns:
    coord = (coord[0],coord[1]+dH)
    text_coord_pairs.append((font.render(str(turn)+":", True, (0,0,0)),coord))
updates = True
current_turn = turns[0]
scores = [0 for i in players]
current_player = 0
bidding_turn = True
currentY = dH
bids = [-1 for i in range(NUM_PLAYERS)]
current_staring_player = 0
current_last_player = NUM_PLAYERS - 1
def calc_points(bid,result):
    if bid==result:
        return bid + 5
    elif bid > result:
        return  result - bid
    return bid - result
turn_number = 0
print("{} turn".format(current_turn))
print("{} starts\n-------------".format(players[current_staring_player]))
players_done = 0
while running:
    #if current_player == current_staring_player:
    #    print("It is {}'s turn".format(players[current_player]))
    if players_done == NUM_PLAYERS:
        if bidding_turn:
            bidding_turn = False
        else:
            #print(turns)
            if len(turns) == turn_number:
                break
            turn_number+=1
            current_turn = turns[turn_number]
            bidding_turn = True
            currentY+=dH
            bids = [-1 for i in range(NUM_PLAYERS)]
            current_staring_player +=1
            current_last_player +=1
            if current_staring_player == NUM_PLAYERS:
                current_staring_player = 0
            if current_last_player == NUM_PLAYERS:
                current_last_player = 0
            print("{} turn".format(current_turn))
            print("{} starts\n-------------".format(players[current_staring_player]))
        current_player = current_staring_player
        players_done = 0
    if updates:
        screen.fill(background_color)
        for x,y in text_coord_pairs:
            screen.blit(x, y)
        pygame.display.update()
        updates = False
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
        if event.type==pygame.KEYDOWN and event.unicode in "012345678":
            num = int(event.unicode)
            if num > current_turn:
                continue
            #print(event.unicode)
            if bidding_turn:
                if current_player == current_last_player and sum(bids)+1+num==turn:
                    print("Invalid BID")
                    continue
                text_coord_pairs.append((font.render(str(num), True, (0,125,125)),(number_positions[current_player*2],currentY)))
                bids[current_player] = num
            else:
                points = calc_points(bids[current_player],num)
                scores[current_player] += points
                text_coord_pairs.append((font.render(str(scores[current_player]), True, (0,125,125)),(number_positions[current_player*2+1],currentY)))
                if points<0:
                    text_coord_pairs[-NUM_PLAYERS-1] =(font.render(str(bids[current_player]), True, (255,0,0)),(number_positions[current_player*2],currentY))
            current_player +=1
            if current_player == NUM_PLAYERS:
                current_player = 0
            players_done +=1
            updates = True
while running:
    if updates:
        screen.fill(background_color)
        for x,y in text_coord_pairs:
            screen.blit(x, y)
        pygame.display.update()
        updates = False
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
