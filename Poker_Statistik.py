import collections
from itertools import product
from random import shuffle


def sort_cards(cards):
    txt = " ".join(cards)
    numbers =  [int(s) for s in txt.split() if s.isdigit()]  
    for iter_num in range(len(numbers)-1,0,-1):
      for idx in range(iter_num):
         if numbers[idx]>numbers[idx+1]:
            temp = numbers[idx]
            numbers[idx] = numbers[idx+1]
            numbers[idx+1] = temp    
    return numbers
   

def draw_cards(anz):
    colors = ["Clover ","Diamond ","Heart ","Spade "] 
    values = ["2 ","3 ","4 ","5 ","4 ","6 ","7 ","8 ","9 ","10 ","11 ","12 ","13 ", "14 "]
    cards = list(r + s for r, s in product(values, colors))
    shuffle(cards)
    hand = cards[:anz]
    print(cards)
    return hand


def highest(): #höchste Karte
    return True

def pair(numbers): #zwei gleiche Zahlen
    if 2 in set([numbers.count(n) for n in numbers]):
        return True
    else:
        return False

def two_pair(numbers): #2 x 2 gleiche Zahlen
    if len([k for k, v in collections.Counter(numbers).items() for _i in range(v // 2)]) == 2:
        return True
    return False

def triple(numbers): #drei gleiche Zahlen
    if 3 in set([numbers.count(n) for n in numbers]):
        return True
    return False

def straight(numbers): #Straße A,2,3,4,5,6,7,8,9,10,B,D,K,A
    s = 1
    a = [14,2,3,4,5]
    for i in range(len(numbers)-1):
        if numbers[i] == numbers[i+1] - 1:
            s = s+1
    if s >= 5:
        return True
    if all(value in numbers for value in a):
        return True
    return False

def flush(hand): #5 gleiche Farben/Symbole
    d = 0
    s = 0
    c = 0
    h = 0
    for i in range(len(hand)):
        if 'Diamond' in hand[i]:
            d = d + 1
        if 'Spade' in hand[i]:
            s = s + 1
        if 'Clover' in hand[i]:
            c = c + 1
        if 'Heart' in hand[i]:
            h = h + 1
    if d >= 5:
        return 'Diamond'
    if s >= 5:
        return 'Spade'
    if c >= 5:
        return 'Clover'
    if h >= 5:
        return 'Heart'
    return False
        
def full_house(numbers): #Drilling + Paar
    if pair(numbers) and triple(numbers):
        return True
    return False

def poker(numbers): #vier gleiche Zahlen
    if 4 in set([numbers.count(n) for n in numbers]):
        return True
    return False

def straight_flush(hand): #Straße in gleicher Farbe/Symbol
    if flush(hand) != False:
        matching = [s for s in hand if flush(hand) in s]
        if straight(sort_cards(matching)):
            return True
    return False

def royal_flush(hand): #Höchste Straße in gleicher Farbe/Symbol: 10,B,D,K,A
    r = [10,11,12,13,14]
    if flush(hand) != False:
        matching = [s for s in hand if flush(hand) in s]
        matching_n = sort_cards(matching)
        if all(value in matching_n for value in r):
            return True
    return False

def count_best(hand, numbers):
    if royal_flush(hand):
        return 'royal_flush'
    if straight_flush(hand):
        return 'straight_flush'
    if poker(numbers):
        return 'poker'
    if full_house(numbers):
        return 'full_house'
    if flush(hand) != False:
        return 'flush'
    if straight(numbers):
        return 'straight'
    if triple(numbers):
        return 'triple'
    if two_pair(numbers):
        return 'two_pair'
    if pair(numbers):
        return 'pair'
    else:
         return 'highest'



def statistics(anz_cards,anz):
    stat = {'royal_flush': 0, 'straight_flush': 0, 'poker': 0, 'full_house': 0, 'flush': 0,\
         'straight': 0, 'triple': 0, 'two_pair': 0, 'pair': 0, 'highest': 0}
    percent_stat = {'royal_flush': 0, 'straight_flush': 0, 'poker': 0, 'full_house': 0, 'flush': 0,\
         'straight': 0, 'triple': 0, 'two_pair': 0, 'pair': 0, 'highest': 0}

    for i in range(anz):
        hand = draw_cards(anz_cards)
        numbers = sort_cards(hand)
        stat[count_best(hand,numbers)] = stat[count_best(hand,numbers)] + 1
    percent_stat['royal_flush'] = "%.4f" % ((stat['royal_flush'] / anz) * 100)
    percent_stat['straight_flush'] = "%.4f" % ((stat['straight_flush'] / anz) * 100)
    percent_stat['poker'] = "%.2f" % ((stat['poker'] / anz) * 100)
    percent_stat['full_house'] = "%.2f" % ((stat['full_house'] / anz) * 100)
    percent_stat['flush'] = "%.2f" % ((stat['flush'] / anz) * 100)
    percent_stat['straight'] = "%.2f" % ((stat['straight'] / anz) * 100)
    percent_stat['triple'] = "%.2f" % ((stat['triple'] / anz) * 100)
    percent_stat['two_pair'] = "%.2f" % ((stat['two_pair'] / anz) * 100)
    percent_stat['pair'] = "%.2f" % ((stat['pair'] / anz) * 100)
    percent_stat['highest'] = "%.2f" % ((stat['highest'] / anz) * 100)

    l1 = [stat['royal_flush'],stat['straight_flush'],stat['poker'],stat['full_house'],stat['flush'],stat['straight'],stat['triple'],stat['two_pair'],stat['pair'], stat['highest']]
    s = sum(l1)
    l = [float(percent_stat['royal_flush']),float(percent_stat['straight_flush']),float(percent_stat['poker']), float(percent_stat['full_house']), \
        float(percent_stat['flush']), float(percent_stat['straight']), float(percent_stat['triple']), float(percent_stat['two_pair']), float(percent_stat['pair']), float(percent_stat['highest'])]

    print('Number of Cards:\t',anz_cards)
    print('Number of Trials:\t',anz)
    print('Royal Flush:\t', stat['royal_flush'], '\t\t|\t\t', percent_stat['royal_flush'],'%')
    print('Straight Flush:\t', stat['straight_flush'], '\t\t|\t\t', percent_stat['straight_flush'],'%')
    print('Poker:\t', stat['poker'], '\t\t|\t\t', percent_stat['poker'],'%')
    print('Full House:\t', stat['full_house'], '\t\t|\t\t', percent_stat['full_house'],'%')
    print('Flush:\t', stat['flush'], '\t\t|\t\t', percent_stat['flush'],'%')
    print('Straight:\t', stat['straight'], '\t\t|\t\t', percent_stat['straight'],'%')
    print('Triple:\t', stat['triple'], '\t\t|\t\t', percent_stat['triple'],'%')
    print('Two Pair:\t', stat['two_pair'], '\t\t|\t\t', percent_stat['two_pair'],'%')
    print('Pair:\t', stat['pair'], '\t\t|\t\t', percent_stat['pair'],'%')
    print('Highest Card:\t', stat['highest'], '\t\t|\t\t', percent_stat['highest'],'%')
    print('Sum:\t', s, '\t\t|\t\t', "%.2f" % sum(l),'%')

    #return stat, percent_stat


if __name__ == "__main__":
    statistics(7,100000)
