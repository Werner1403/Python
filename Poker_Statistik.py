import random

def five_cards():
    cards = []
    f = [0,0,0,0,0]
    f_nr =[0,0,0,0,0]
    for i in range(52):
        cards.append(i+1)
    for j in range(5):
        c = cards[random.randint(0, 52)]
        if (c % 4 == 0):
            f[j] = "Spade"
            f_nr[j] = "1"
        if (c % 4 == 1):
            f[j] = "Heart"
            f_nr[j] = "2"
        if (c % 4 == 2):
            f[j] = "Clover"
            f_nr[j] = "3"
        if (c % 4 == 3):
            f[j] = "Diamond"
            f_nr[j] = "4"
        if(c % 13 == 0):
            f[j] = f[j] + " 2"
            f_nr[j] = 2
        if (c % 13 == 1):
            f[j] = f[j] + " 3"
            f_nr[j] = f_nr[j] + "03"
        if (c % 13 == 2):
            f[j] = f[j] + " 4"
            f_nr[j] = f_nr[j] + "04"
        if (c % 13 == 3):
            f[j] = f[j] + " 5"
            f_nr[j] = f_nr[j] + "05"
        if (c % 13 == 4):
            f[j] = f[j] + " 6"
            f_nr[j] = f_nr[j] + "06"
        if (c % 13 == 5):
            f[j] = f[j] + " 7"
            f_nr[j] = f_nr[j] + "07"
        if (c % 13 == 6):
            f[j] = f[j] + " 8"
            f_nr[j] = f_nr[j] + "08"
        if (c % 13 == 7):
            f[j] = f[j] + " 9"
            f_nr[j] = f_nr[j] + "09"
        if (c % 13 == 8):
            f[j] = f[j] + " 10"
            f_nr[j] = f_nr[j] + "10"
        if (c % 13 == 9):
            f[j] = f[j] + " B"
            f_nr[j] = f_nr[j] + "11"
        if (c % 13 == 10):
            f[j] = f[j] + " D"
            f_nr[j] = f_nr[j] + "12"
        if (c % 13 == 11):
            f[j] = f[j] + " K"
            f_nr[j] = f_nr[j] + "13"
        if (c % 13 == 12):
            f[j] = f[j] + " A"
            f_nr[j] = f_nr[j] + "14"
    return f, f_nr

def highest(): #höchste Karte
    pass

def pair(): #zwei gleiche Zahlen
    pass

def two_pair(): #2 x 2 gleiche Zahlen
    pass

def triple(): #drei gleiche Zahlen
    pass

def straight(): #Straße A,2,3,4,5,6,7,8,9,10,B,D,K,A
    pass

def flush(): #5 gleiche Farben/Symbole
    pass

def full_house(): #Drilling + Paar
    pass

def poker(): #vier gleiche Zahlen
    pass

def straight_flush(): #Straße in gleicher Farbe/Symbol
    pass

def royal_flush(): #Höchste Straße in gleicher Farbe/Symbol: 10,B,D,K,A
    pass

print(five_cards())
