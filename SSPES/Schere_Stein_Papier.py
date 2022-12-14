import json
import random
import numpy as np
import requests
import matplotlib.pyplot as plt
from datetime import datetime

#Rules:
        #Schere schneidet Papier         
        #Papier bedeckt Stein                
        #Stein zerquetscht Echse
        #Echse vergiftet Spock
        #Spock zertrümmert Schere
        #Schere köpft Echse
        #Echse frisst Papier
        #Papier widerlegt Spock
        #Spock verdampft Stein
        #Stein schleift Schere

def comp_fig():
    figs = { 0 : "Stein", 1 : "Papier", 2 : "Schere", 3 : "Echse", 4 : "Spock"}
    f = random.choice(list(figs.values()))
    return f

def comp_fig_impossible(p_fig):
    figs = { 0 : "Stein", 1 : "Papier", 2 : "Schere", 3 : "Echse", 4 : "Spock"}
    r = random.randint(0,1)
    f = 0
    if p_fig == figs[0]:
        f = figs[1] if r == 0 else figs[4]
    if p_fig == figs[1]:
        f = figs[2] if r == 0 else figs[3]
    if p_fig == figs[2]:
        f = figs[0] if r == 0 else figs[4]
    if p_fig == figs[3]:
        f = figs[2] if r == 0 else figs[0]
    if p_fig == figs[4]:
        f = figs[3] if r == 0 else figs[1]
    return f

def comp_fig_hard(p):
    figs = { 0 : "Stein", 1 : "Papier", 2 : "Schere", 3 : "Echse", 4 : "Spock"}
    l = []
    x = 0
    with open('SSPES/sspes.json', 'r') as file:
        data = json.load(file)
        sch = data["players"][str(p)]['player']['schere']
        st = data["players"][str(p)]['player']['stein']
        pap = data["players"][str(p)]['player']['papier']
        ec = data["players"][str(p)]['player']['echse']
        sp = data["players"][str(p)]['player']['spock']
        
        su = sch + st + pap + ec + sp
        
        sch_p = int(round(sch / su,2) * 10000)
        st_p = int(round(st / su, 2) * 10000)
        pap_p = int(round(pap / su,2) * 10000)
        ec_p = int(round(ec / su, 2) * 10000)
        sp_p = int(round(sp / su, 2) * 10000)
        
        for i in range(sch_p):
            x = random.randint(0,1)
            l.append(figs[4]) if x == 1 else l.append(figs[0])

        for i in range(st_p):
            x = random.randint(0,1)
            l.append(figs[1]) if x == 1 else l.append(figs[4])

        for i in range(pap_p):
            x = random.randint(0,1)
            l.append(figs[2]) if x == 1 else l.append(figs[3])

        for i in range(ec_p):
            x = random.randint(0,1)
            l.append(figs[0]) if x == 1 else l.append(figs[2])

        for i in range(sp_p):
            x = random.randint(0,1)
            l.append(figs[1]) if x == 1 else l.append(figs[3])
            
        f = random.randint(0,len(l))
        
    return l[f]

def player_fig():
    figs = { 0 : "Stein", 1 : "Papier", 2 : "Schere", 3 : "Echse", 4 : "Spock"}
    i = input("Stein, Papier, Schere, Echse, Spock?")
    print("\n")
    valid = False
    while not valid:
        if i.lower() == "stein":
            valid = True
            return figs[0]
        elif i.lower() == "papier":
            valid = True
            return figs[1]
        elif i.lower() == "schere":
            valid = True
            return figs[2]
        elif i.lower() == "echse":
            valid = True
            return figs[3]
        elif i.lower() == "spock":
            valid = True
            return figs[4]
        else:
            print("input error")
            i = input("Stein, Papier, Schere, Echse, Spock?")

def logic(p_fig, c_fig, p):
    figs = { 0 : "Stein", 1 : "Papier", 2 : "Schere", 3 : "Echse", 4 : "Spock"}
    with open('SSPES/sspes.json', 'r+') as f:
        data = json.load(f)
        if p in data["players"]:
            data["players"][str(p)]["player"][str(p_fig).lower()] = data["players"][str(p)]["player"][str(p_fig).lower()] + 1
            data["players"][str(p)]["comp"][str(c_fig).lower()] = data["players"][str(p)]["comp"][str(c_fig).lower()] + 1
        else:
            y = {p: { "player" : { "won" : 0, "schere" : 0, "stein" : 0, "papier" : 0, "echse" : 0, "spock" : 0},"comp" : { "won" : 0, "schere" : 0, "stein" : 0, "papier" : 0, "echse" : 0, "spock" : 0},"draw":0}}
            data["players"].update(y)
            data["players"][str(p)]["player"][str(p_fig).lower()] = data["players"][str(p)]["player"][str(p_fig).lower()] + 1
            data["players"][str(p)]["comp"][str(c_fig).lower()] = data["players"][str(p)]["comp"][str(c_fig).lower()] + 1
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
        if p_fig == c_fig:
            data["players"][str(p)]["draw"] = data["players"][str(p)]["draw"] + 1
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
            return "draw"
        elif p_fig == figs[0] and (c_fig == figs[2] or c_fig == figs[3]):
            data["players"][str(p)]["player"]["won"] = data["players"][str(p)]["player"]["won"] + 1
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
            return "player won with: " + p_fig + " against: " + c_fig
        elif p_fig == figs[1] and (c_fig == figs[0] or c_fig == figs[4]):
            data["players"][str(p)]["player"]["won"] = data["players"][str(p)]["player"]["won"] + 1
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
            return "player won with: " + p_fig + " against: " + c_fig
        elif p_fig == figs[2] and (c_fig == figs[1] or c_fig == figs[3]):
            data["players"][str(p)]["player"]["won"] = data["players"][str(p)]["player"]["won"] + 1
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
            return "player won with: " + p_fig + " against: " + c_fig
        elif p_fig == figs[3] and (c_fig == figs[4] or c_fig == figs[1]):
            data["players"][str(p)]["player"]["won"] = data["players"][str(p)]["player"]["won"] + 1
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
            return "player won with: " + p_fig + " against: " + c_fig
        elif p_fig == figs[4] and (c_fig == figs[2] or c_fig == figs[0]):
            data["players"][str(p)]["player"]["won"] = data["players"][str(p)]["player"]["won"] + 1
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
            return "player won with: " + p_fig + " against: " + c_fig
        else:
            data["players"][p]["comp"]["won"] = data["players"][p]["comp"]["won"] + 1
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
            return "player lost with:" + p_fig + " against: " + c_fig

def print_stats(p):
    url = 'http://127.0.0.1:5000/player/' + p
    resp = requests.get(url=url)
    d = resp.json()
    data = json.loads(d)
    
    print("Player won: " + str(data["player"]["won"]))
    print("Computer won: " + str(data["comp"]["won"]))
    print("for JSON-File visit:")
    print(url)
    
    su = data["player"]["schere"] + data["player"]["stein"] + data["player"]["papier"] + data["player"]["echse"] + data["player"]["spock"]
    labels = 'Schere', 'Stein', 'Papier', 'Echse', 'Spock'
    s1 = (data["player"]["schere"]/su)*100
    s2 = (data["player"]["stein"]/su)*100
    s3 = (data["player"]["papier"]/su)*100
    s4 = (data["player"]["echse"]/su)*100
    s5 = (data["player"]["spock"]/su)*100
    sizes = [s1,s2,s3,s4,s5]
    fig1, (ax1, ax2) = plt.subplots(2)
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')
    win = ('won', 'lost', 'draw')
    anzahl = [int(data["player"]["won"]), int(data["comp"]["won"]), int(data["draw"])]
    y_pos = np.arange(len(win))
    
    plt.bar(y_pos, anzahl, align='center')
    plt.xticks(y_pos, win)
    plt.tick_params(axis='x',which='both', bottom=False)
    z = str(datetime.today().strftime('%Y-%m-%d_%H-%M'))
    fig1 = plt.gcf()
    plt.show()
    plt.draw()
    fig1.savefig('SSPES/images/' + p + '_' + z + '.png', dpi=100)
    

def print_menu():
    print("-----------------------------")
    print("Select an option:")
    print("1. Play against comp (normal)")
    print("2. Play against comp (hard)")
    print("3. Play against comp (impossible)")
    print("4. Show statistics")
    print("5. exit")
    print("-----------------------------")
    print()


def main():
    running = True
    p = input("Who are you?").lower()
    while running:
        print_menu()
        option = input("Please make a choice >> ")
        if option == "1":
            print(logic(player_fig(), comp_fig(), p))
        elif option == "2":
            print("\n")
            print(logic(player_fig(), comp_fig_hard(p), p))
        elif option == "3":
            print("\n")
            x = player_fig()
            print(logic(x, comp_fig_impossible(x), p))
        elif option == "4":
            print()
            print_stats(p)
        elif option == "5":
            print()
            print("Goodbye!")
            running = False
        else:
            print("Invalid Option! Please try again!")

if __name__ == '__main__':
    main()
    