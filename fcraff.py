import time
import random

team1name = input("Name of Team 1: ")
team2name = input("Name of Team 2: ")
amount = int(input("Amount of players: "))
team1players = []
team2players = []
print("Build " + team1name)
for i in range(amount):
    player = input("Name of player: ")
    team1players.append(player)
print("Build " + team2name)
for i in range(amount):
    player = input("Name of player: ")
    team2players.append(player)
print("Team 1")
print(team1players)
print("Team 2")
print(team2players)
print("KICK OFF!")
score1 = 0
score2 = 0
for i in range(1, 96):
    time.sleep(1)
    score_chance = random.randint(1, 101)
    if(score_chance > 90):
        team_scored = random.randint(1, 3)
        if(team_scored == 1):
            player_scored = random.randint(0, amount - 1)
            score1 += 1
            print(str(i) + " " + team1players[player_scored] + " scored " + str(score1) + " : " + str(score2))
            continue
        else:
            player_scored = random.randint(0, amount - 1)
            score2 += 1
            print(str(i) + " " + team2players[player_scored ] + " scored " + str(score1) + " : " + str(score2))
            continue
    missed_penalty = random.randint(1, 100)
    if missed_penalty > 98:
        team_missed = random.randint(1, 3)
        if team_missed == 1:
            player_missed = random.randint(0, amount - 1)
            print(str(i) + " " + team1players[player_missed] + " missed a penalty")
            continue
        else:
            player_missed = random.randint(0, amount - 1)
            print(str(i) + " " + team2players[player_missed] + " missed a penalty")
            continue
    print(i)


