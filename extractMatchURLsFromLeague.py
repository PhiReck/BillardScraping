from urllib.request import urlopen
import re
from bs4 import BeautifulSoup


def extractMatchURLsFromSpielPlan(spielplan_url) :
    page = urlopen(spielplan_url)
    html_bytes = page.read()
    spielplan = html_bytes.decode("utf-8")
    # print(spielplan)

    matchURLs = []
    for matchURL in re.findall("a alt=\"Spielbericht\" title=\"Spielbericht\" href=\"(.*?)\"", spielplan):
        matchURLs.append(("https://bbv-billard.liga.nu/" + matchURL).replace("&amp;", "&"))

    # print(matchURLs)
    return matchURLs
    # soup = BeautifulSoup(html, "html.parser")
    # removedLines = "".join([s for s in soup.get_text().strip().splitlines(True) if s.strip()])
    # return removedLines

    # removedWhiteSpaces = removedLines.replace("\t", "").replace(" ","")

    # print(soup.get_text())
    # print(removedWhiteSpaces)
    # print("\n\n ----------------------------------------------------------------- \n\n")
    # # print(html)

    # return removedWhiteSpaces



# secondPartOfRemovedWhiteSpaces = removedWhiteSpaces[end_index:]
# start_index2 = secondPartOfRemovedWhiteSpaces.find("14.1")
# print(start_index2)
# end_index2 = secondPartOfRemovedWhiteSpaces.find("8-Ball")
# print(end_index2)
# interestingSection2 = secondPartOfRemovedWhiteSpaces[start_index2:end_index2]
# print(interestingSection2)