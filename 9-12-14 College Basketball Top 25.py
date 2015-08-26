# David Rawlings
# 9-12-14
# After Class

import pprint
import random

simple = {'key': 'string'}
#print (simple['key'])

rooms = {
            'B': {'contents': ['a monster']}
        }

teams = {
            1: {'home': 'Duke', 'maskot': 'Blue Devils', 'rank': 1},
            2: {'home': 'Kentucky', 'maskot': 'Wildcats', 'rank': 2},
            3: {'home': 'North Carolina', 'maskot': 'Tar Heels', 'rank': 3},
            4: {'home': 'Kansas', 'maskot': 'Jayhawks', 'rank': 4},
            5: {'home': 'Louisville', 'maskot': 'Cardinals', 'rank': 5},
            6: {'home': 'Arizona', 'maskot': 'Wildcats', 'rank': 6},
            7: {'home': 'Michigan State', 'maskot': 'Spartans', 'rank': 7},
            8: {'home': 'Texas', 'maskot': 'Longhorns', 'rank': 8},
            9: {'home': 'Connecticut', 'maskot': 'Huskies', 'rank': 9},
            10: {'home': 'Villanova', 'maskot': 'Wildcats', 'rank': 10},
            11: {'home': 'LSU', 'maskot': 'Tigers', 'rank': 11},
            12: {'home': 'Georgetown', 'maskot': 'Hoyas', 'rank': 12},
            13: {'home': 'Illinois', 'maskot': 'Fighting Illini', 'rank': 13},
            14: {'home': 'Gonzaga', 'maskot': 'Bulldogs', 'rank': 14},
            15: {'home': 'USC', 'maskot': 'Trojans', 'rank': 15},
            16: {'home': 'Boston College', 'maskot': 'Eagles', 'rank': 16},
            17: {'home': 'Indiana', 'maskot': 'Hoosiers', 'rank': 17},
            18: {'home': 'Wake Forest', 'maskot': 'Demon Deacons', 'rank': 18},
            19: {'home': 'Texas A&M', 'maskot': 'Aggies', 'rank': 19},
            20: {'home': 'Pittsburg', 'maskot': 'Panthers', 'rank': 20},
            21: {'home': 'Oklahoma', 'maskot': 'Sooners', 'rank': 21},
            22: {'home': 'Michigan', 'maskot': 'Wolverines', 'rank': 22},
            23: {'home': 'Missouri', 'maskot': 'Tigers', 'rank': 23},
            24: {'home': 'Notre Dame', 'maskot': 'Fighting Irish', 'rank': 24},
            25: {'home': 'Kansas State', 'maskot': 'Wildcats', 'rank': 25}

        }

# pprint.pprint(teams, width = 50)

while True:
    
    command = input('What do you want to do (\'game\' or \'standings\'): ')

    if command == 'standings':
        #pprint.pprint(teams, width = 50)
        x = 1
        #while x < 26:
         #   print(teams[x]['rank'],teams[x]['home'],teams[x]['maskot'])
          #  x += 1
            
        
        while x < 26:
            print(teams[teams[x]['rank']]['rank'],teams[teams[x]['rank']]['home'],teams[teams[x]['rank']]['maskot'])
            x += 1
            
    
    if command == 'game':

        team1 = random.randint(1, 25)
        team2 = random.randint(1, 25)
        while team1 == team2:
            team2 = random.randint(1, 25)

        score1 = random.randint(40 + teams[team2]['rank'], 80 + teams[team2]['rank'])
        score2 = random.randint(40 + teams[team1]['rank'], 80 + teams[team1]['rank'])

        print(teams[team1]['rank'],teams[team1]['home'],teams[team1]['maskot'],score1)
        print(teams[team2]['rank'],teams[team2]['home'],teams[team2]['maskot'],score2)

        #switch ranks if there is an upset
        if teams[team1]['rank'] > teams[team2]['rank']:
            if score1 > score2:
                print('Upset!')
                x = teams[team1]['rank']
                teams[team1]['rank'] = teams[team2]['rank']
                teams[team2]['rank'] = x
        if teams[team1]['rank'] < teams[team2]['rank']:
            if score1 < score2:
                print('Upset!')
                x = teams[team1]['rank']
                teams[team1]['rank'] = teams[team2]['rank']
                teams[team2]['rank'] = x
