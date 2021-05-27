# tee ratkaisusi tänne
import json
class Stat:
    def __init__(self):
        self.stat = {}

    def load_file(self, name):
        with open(name) as file:
            data = file.read()
        self.stat = json.loads(data)
        print("luettiin",  len(self.stat), "pelaajan tiedot")             

    def get_player(self, name):
        for player in self.stat:
            if player['name'] == name:
                total = player['goals'] + player['assists']
                return f"{player['name']:<20}{player['team']:>4}{player['goals']:>4} +{player['assists']:>3} ={total:>4}"    

    def teams(self):  
        return sorted(list(set([player['team'] for player in self.stat])))

    def countries(self):   
        return sorted(list(set([player['nationality'] for player in self.stat])))

    def roster(self, team):   
        roster = [player for player in self.stat if player['team'] == team ]
        for player in sorted(roster, key=lambda player: (-(player['goals']+ player['assists']))):
            print(self.get_player(player['name']))

    def nationalities(self, country):   
        player_n = [player for player in self.stat if player['nationality'] == country ]
        for player in sorted(player_n, key=lambda player: (-(player['goals']+ player['assists']))):
            print(self.get_player(player['name']))
            
    def most_points(self, how_many):  
        s = sorted(self.stat, key=lambda player: (-(player['goals'] + player['assists']),  -player['goals'] ))
        for player in s[:how_many]:
            print(self.get_player(player['name']))

    def most_goals(self, how_many): 
        s = sorted(self.stat, key=lambda player: (-player['goals'] ,  player['games'] ))
        for pelaaja in s[:how_many]:
            print(self.get_player(pelaaja['name']))

class Sovellus:

    def valikko():
        t = Stat()
        file = input("file: ")   
        t.load_file(file)     
        komennot = """
    komennot:
    0 lopeta
    1 hae pelaaja
    2 joukkueet
    3 maat
    4 joukkueen pelaajat
    5 maan pelaajat
    6 eniten pisteitä
    7 eniten maaleja
    """

        while True:            
            print(komennot)
            komento= input("komento: ")
            if komento == "0":
                break
            if komento == "1":
                name = input("name: ") 
                print(t.get_player(name))
            elif komento == "2":
                for j in t.teams():
                    print(j)
            elif komento == "3":
                for m in t.countries():
                    print(m)
            elif komento == "4":
                team = input("joukkue: ")
                t.roster(team)  
            elif komento == "5":
                country = input("joukkue: ")
                t.nationalities(country)  
            elif komento == "6":  
                how_many = int(input("kuinka monta: "))
                t.most_points(how_many)
            elif komento == "7":  
                how_many = int(input("kuinka monta: "))
                t.most_goals(how_many)

s = Sovellus 
s.valikko()