#排七

#創建蓋牌順位及出牌順位
fold_order = []
play_order = []

def suit(n):
    li = []
    for s in ['Spades', 'Hearts', 'Diamonds', 'Clubs']:
        li.append(f'{s} {n}')
    return li

for i in range(7):    
    if i == 0:
        play_order.extend(suit(7))
    else:
        fold_order.extend(suit(14-i))
        fold_order.extend(suit(i))
        play_order.extend(suit(7+i))
        play_order.extend(suit(7-i))

#讀入玩家數及手牌數
player,card_num = map(int,input().split(' '))

#讀入玩家手牌資訊
all_hand = []
for n in range(player):
    card = input().split(' ')
    hand = []
    for m in range(card_num):
        hand.append(f'{card[2*m]} {card[2*m+1]}')
    all_hand.append(hand)

can_play = ['Spades 7','Hearts 7','Diamonds 7','Clubs 7']


while all_hand[-1] != []:
    for p in range(player):
        need_fold = True
        for card in can_play:
            if card in all_hand[p]:
                
