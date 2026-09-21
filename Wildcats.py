team_name = "Wildcats"

wins = 12
losses = 4

games_played= wins + losses

win_percentage = wins/games_played

if win_percentage >= 70:
    print(team_name,"is likely to make the playoffs!")
else:
    print(team_name,"needs to win more games.")

print("Team:", team_name)

if wins > 10:
    print("Winning Season!")

def winning_record(win, loss):
    return win > loss

result = winning_record(wins,losses)

print("Winning Record?", result)

#print games played and win percentage

print("Games Played:",games_played)
print("Win Percentage", win_percentage*100,"%")