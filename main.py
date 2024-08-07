import os, sys
sys.path.append(os.path.dirname(__file__))

from scrapeSingleMatchResult import *
from  extractMatchURLsFromLeague import *

def printPlayerTable(players):
    print('Name, HS, MinAufn, Won:Lost')
    for name, attributes in players.items():
        print(f'{name}, {attributes["HS"]}, {attributes["Min. Aufn."]}, {attributes["Won"]}:{attributes["Lost"]}')

def appendPlayer(leaguePlayers, matchPlayer):
    if matchPlayer["Name"] in leaguePlayers.keys():
        updateLeaguePlayer(matchPlayer, leaguePlayers[matchPlayer["Name"]])
    else:
        leaguePlayers[matchPlayer["Name"]] = {
            "HS" : matchPlayer["HS"],
            "Min. Aufn." : 100,
            "Won" : matchPlayer["Won"],
            "Lost" : matchPlayer["Lost"]}
        if leaguePlayers[matchPlayer["Name"]]["Won"] == 1:
            leaguePlayers[matchPlayer["Name"]]["Min. Aufn."] = matchPlayer["Aufn."]

def updateLeaguePlayer(matchPlayer, leaguePlayer):
    leaguePlayer["HS"] = max([leaguePlayer["HS"], matchPlayer["HS"]])
    if matchPlayer["Won"] == 1 :
        leaguePlayer["Min. Aufn."] = min([leaguePlayer["Min. Aufn."], matchPlayer["Aufn."]])
        leaguePlayer["Won"] += 1
    else:
        leaguePlayer["Lost"] += 1


print("------Annahme dieses Programms: in jeder Liga gibt es genau 1 Person mit dem gleichen Namen.\n")

gesamtSpielplanURL = "https://bbv-billard.liga.nu/cgi-bin/WebObjects/nuLigaBILLARDDE.woa/wa/groupPage?displayTyp=vorrunde&displayDetail=meetings&championship=BBV+Pool+23%2F24&group=433"

matchURLs = extractMatchURLsFromSpielPlan(gesamtSpielplanURL)

print("#matches: ", len(matchURLs))

players={}

for matchURL in matchURLs:
    interestingSection = extractTextFromResultsPage(matchURL)
    part1Results = extract14_1Match1(interestingSection)
    part2Results = extract14_1Match2(interestingSection)
    player1, player2 = fillPlayerDict(part1Results)
    player3, player4 = fillPlayerDict(part2Results)

    appendPlayer(players, player1)
    appendPlayer(players, player2)
    appendPlayer(players, player3)
    appendPlayer(players, player4)

printPlayerTable(players)
print("\nNumber format errors occurred: ", players["error: invalid format"]["Lost"])