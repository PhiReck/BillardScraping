from urllib.request import urlopen
import re
from bs4 import BeautifulSoup


def extractTextFromResultsPage(url) :
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    removedLines = "".join([s for s in soup.get_text().strip().splitlines(True) if s.strip()])
    removedWhiteSpaces = removedLines.replace("\t", "").replace(" ","")

    # print(soup.get_text())
    # print(removedWhiteSpaces)
    # print("\n\n ----------------------------------------------------------------- \n\n")
    # # print(html)
    return removedWhiteSpaces

def extract14_1Match1(fullResults) :
    # print(fullResults)
    start_index = fullResults.find("\n14.1") + len("\n14.1")+1
    # print(start_index)
    end_index = fullResults.find("8-Ball")
    # print(end_index)
    return fullResults[start_index:end_index]
    # print(interestingSection1)
    # print("\n\n ----------------------------------------------------------------- \n\n")

def extract14_1Match2(fullResults) :
    # print(fullResults)
    #arbitrary with knowledge of typical fullResults:
    start_of_second_round_index = fullResults.find("10-Ball")
    part2Results = fullResults[start_of_second_round_index:]
    # print(part2Results)
    start_index = part2Results.find("14.1") + len("14.1")+1
    # print(start_index)
    end_index = part2Results.find("8-Ball")
    # print(end_index)
    # print(part2Results[start_index:end_index])
    return part2Results[start_index:end_index]
    # print(interestingSection1)
    # print("\n\n ----------------------------------------------------------------- \n\n")

def fillPlayerDict(partResults):
    lines = partResults.splitlines()
    player1 = {}
    player2 = {}
    # if lines[0] == "Mayer,Alexander" or lines[1] == "Mayer,Alexander":
    #     print(lines)

    if len(lines) == 10:
        player1["Name"] = lines[0].replace(",", " ")
        player2["Name"] = lines[1].replace(",", " ")
        player1["Bälle"] = int(lines[2].split(":")[0])
        player2["Bälle"] = int(lines[2].split(":")[1])
        player1["Aufn."] = int(lines[4].split(":")[0])
        player2["Aufn."] = int(lines[4].split(":")[1])
        player1["HS"] = int(lines[6].split(":")[0])
        player2["HS"] = int(lines[6].split(":")[1])
        player1["Won"] = int(lines[9].split(":")[0])
        player2["Won"] = int(lines[9].split(":")[1])
        player1["Lost"] = int(lines[9].split(":")[1])
        player2["Lost"] = int(lines[9].split(":")[0])
        return player1, player2
    else:
        print("format error in match: ", lines[0].replace(",", " "), " vs. ", lines[1].replace(",", " "))
        player1["Name"] = "error: invalid format"
        player2["Name"] = "error: invalid format"
        player1["Bälle"] = 0
        player2["Bälle"] = 0
        player1["Aufn."] = 0
        player2["Aufn."] = 0
        player1["HS"] = 0
        player2["HS"] = 0
        player1["Won"] = 1# to track how many errors occurred
        player2["Won"] = 0
        player1["Lost"] = 0
        player2["Lost"] = 1# to track how many errors occurred
        return player1, player2


# interestingSection = extractTextFromResultsPage("https://bbv-billard.liga.nu/cgi-bin/WebObjects/nuLigaBILLARDDE.woa/wa/groupMeetingReport?meeting=7106649&championship=BBV+Pool+23%2F24&group=449")
# part1Results = extract14_1Match1(interestingSection)
# part2Results = extract14_1Match2(interestingSection)
# player1, player2 = fillPlayerDict(part1Results)
# player3, player4 = fillPlayerDict(part2Results)

# print(player1)
# print(player2)
# print(player3)
# print(player4)


# secondPartOfRemovedWhiteSpaces = removedWhiteSpaces[end_index:]
# start_index2 = secondPartOfRemovedWhiteSpaces.find("14.1")
# print(start_index2)
# end_index2 = secondPartOfRemovedWhiteSpaces.find("8-Ball")
# print(end_index2)
# interestingSection2 = secondPartOfRemovedWhiteSpaces[start_index2:end_index2]
# print(interestingSection2)