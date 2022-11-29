import json
import random

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

def player_fig():
    figs = { 0 : "Stein", 1 : "Papier", 2 : "Schere", 3 : "Echse", 4 : "Spock"}
    i = input("Stein, Papier, Schere, Echse, Spock?")
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

def logic(p_fig, c_fig):
    figs = { 0 : "Stein", 1 : "Papier", 2 : "Schere", 3 : "Echse", 4 : "Spock"}
    with open('sspes.json', 'r+') as f:
        data = json.load(f)
        data["player"][str(p_fig).lower()] = data["player"][str(p_fig).lower()] + 1
        data["comp"][str(c_fig).lower()] = data["comp"][str(c_fig).lower()] + 1
        if p_fig == c_fig:
            data["draw"] = data["draw"] + 1
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
            return "draw"
        elif p_fig == figs[0] and (c_fig == figs[2] or c_fig == figs[3]):
            data["player"]["won"] = data["player"]["won"] + 1
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
            return "player won with: " + p_fig + " against: " + c_fig
        elif p_fig == figs[1] and (c_fig == figs[0] or c_fig == figs[4]):
            data["player"]["won"] = data["player"]["won"] + 1
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
            return "player won with: " + p_fig + " against: " + c_fig
        elif p_fig == figs[2] and (c_fig == figs[1] or c_fig == figs[3]):
            data["player"]["won"] = data["player"]["won"] + 1
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
            return "player won with: " + p_fig + " against: " + c_fig
        elif p_fig == figs[3] and (c_fig == figs[4] or c_fig == figs[1]):
            data["player"]["won"] = data["player"]["won"] + 1
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
            return "player won with: " + p_fig + " against: " + c_fig
        elif p_fig == figs[4] and (c_fig == figs[2] or c_fig == figs[0]):
            data["player"]["won"] = data["player"]["won"] + 1
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
            return "player won with: " + p_fig + " against: " + c_fig
        else:
            data["comp"]["won"] = data["comp"]["won"] + 1
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
            return "player lost with:" + p_fig + " against: " + c_fig

def main():
    while 1:
        print(logic(player_fig(),comp_fig()))

if __name__ == '__main__':
    main()